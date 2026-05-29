#!/usr/bin/env python3
"""從 VA 資料庫產生 CVE 知識庫頁面（不含 IP / Host 資訊）"""

import sqlite3
import os
import re
from datetime import datetime
from collections import defaultdict

DB_PATH    = os.path.join(os.path.dirname(__file__), "../VA/vuln.db")
DOCS_PATH  = os.path.join(os.path.dirname(__file__), "docs/cve")
PRIORITY_PAGE = os.path.join(os.path.dirname(__file__), "docs/priority.md")

SEVERITY_ICON = {
    "CRITICAL": '<span style="color:#ff003c">●</span> Critical',
    "HIGH":     '<span style="color:#ff6600">●</span> High',
    "MEDIUM":   '<span style="color:#ffd700">●</span> Medium',
    "LOW":      '<span style="color:#00ff88">●</span> Low',
    "INFO":     '<span style="color:#4a6a8a">●</span> Info',
}

def classify(plugin_name: str) -> str:
    name = plugin_name.lower()
    web_kw = [
        "http", "https", "ssl", "tls", "apache", "nginx", "tomcat",
        "iis", "php", "web", "hsts", "cipher", "certificate", "x.509",
        "sweet32", "openssl", "wordpress", "drupal"
    ]
    service_kw = [
        "ssh", "openssh", "smtp", "ftp", "dns", "snmp", "rdp",
        "exchange", "ldap", "kerberos", "mail", "ntp", "telnet",
        "vnc", "mta", "relay", "pop3", "imap"
    ]
    if any(k in name for k in web_kw):
        return "web"
    if any(k in name for k in service_kw):
        return "services"
    return "system"

def safe_filename(name: str) -> str:
    name = re.sub(r'[^\w\s-]', '', name)
    name = re.sub(r'[\s]+', '-', name.strip())
    return name[:80].lower()

def severity_order(s: str) -> int:
    return {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3, "INFO": 4}.get(s, 5)

def main():
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()

    cur.execute("""
        SELECT
            plugin_id,
            plugin_name,
            severity,
            MAX(cvss_v3)  AS cvss_v3,
            MAX(vpr)      AS vpr,
            MAX(epss)     AS epss,
            MAX(description) AS description,
            MAX(solution)    AS solution,
            GROUP_CONCAT(DISTINCT cve) AS cves,
            COUNT(DISTINCT ip)         AS host_count,
            MAX(scan_date)             AS last_seen
        FROM vuln
        WHERE severity != 'INFO'
        GROUP BY plugin_id
        ORDER BY cvss_v3 DESC, severity
    """)
    rows = cur.fetchall()
    con.close()

    categories = {"web": [], "system": [], "services": []}
    for row in rows:
        cat = classify(row[1])
        categories[cat].append(row)

    generated = 0
    cat_labels = {"web": "Web 類", "system": "系統類", "services": "服務類"}

    for cat, vulns in categories.items():
        cat_dir = os.path.join(DOCS_PATH, cat)
        os.makedirs(cat_dir, exist_ok=True)
        page_list = []

        for (plugin_id, plugin_name, severity, cvss_v3,
             vpr, epss, description, solution, cves,
             host_count, last_seen) in vulns:

            fname = f"{plugin_id}-{safe_filename(plugin_name)}.md"
            fpath = os.path.join(cat_dir, fname)

            cvss_str  = f"{cvss_v3:.1f}" if cvss_v3 else "N/A"
            vpr_str   = f"{vpr:.1f}"     if vpr     else "N/A"
            epss_str  = f"{float(epss)*100:.2f}%" if epss else "N/A"
            sev_badge = SEVERITY_ICON.get(severity, severity)

            cve_list = []
            if cves:
                for c in cves.split(","):
                    c = c.strip()
                    if c and c.upper().startswith("CVE-"):
                        cve_list.append(c.upper())
            cve_list = sorted(set(cve_list))

            desc_block = description.strip() if description and description.strip() else "_（尚無描述，待補充）_"
            sol_block  = solution.strip()    if solution    and solution.strip()    else "_（尚無修補建議，待補充）_"

            cve_section = ""
            if cve_list:
                cve_section = "\n".join(f"- `{c}`" for c in cve_list)
            else:
                cve_section = "_（無對應 CVE 編號）_"

            content = f"""# {plugin_name}

| 欄位 | 內容 |
|------|------|
| 嚴重度 | {sev_badge} |
| CVSS v3 | **{cvss_str}** |
| VPR | {vpr_str} |
| EPSS | {epss_str} |
| Plugin ID | `{plugin_id}` |

## CVE 編號

{cve_section}

## 弱點說明

{desc_block}

## 修補建議

{sol_block}
"""
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)

            page_list.append((severity, cvss_v3 or 0, plugin_name, fname))
            generated += 1

        # 分類索引頁
        page_list.sort(key=lambda x: (severity_order(x[0]), -x[1]))
        index_rows = "\n".join(
            f"| [{name}]({fname}) | {SEVERITY_ICON.get(sev, sev)} | "
            f"{f'{cvss:.1f}' if cvss else 'N/A'} |"
            for sev, cvss, name, fname in page_list
        )
        index_content = f"""# {cat_labels[cat]}弱點清單

共 **{len(page_list)}** 個弱點，依嚴重度排序。

| 弱點名稱 | 嚴重度 | CVSS v3 |
|---------|--------|---------|
{index_rows}
"""
        with open(os.path.join(cat_dir, "index.md"), "w", encoding="utf-8") as f:
            f.write(index_content)

    # ── 近期優先修補頁 ──
    con2 = sqlite3.connect(DB_PATH)
    cur2 = con2.cursor()
    cur2.execute("""
        SELECT plugin_id, plugin_name, severity, cvss_v3, vpr, epss
        FROM vuln
        WHERE vpr > 0 AND severity != 'INFO'
        GROUP BY plugin_id
        ORDER BY vpr DESC
    """)
    priority_rows = cur2.fetchall()
    con2.close()

    def vpr_label(v):
        if v >= 9.0: return ("立即處理", "#ff003c", "7 天內")
        if v >= 7.0: return ("優先排程", "#ff6600", "30 天內")
        return ("一般排程", "#ffd700", "90 天內")

    def epss_pct(e):
        return f"{float(e)*100:.1f}%" if e else "N/A"

    urgent   = [(r, *vpr_label(r[4])) for r in priority_rows if r[4] >= 9.0]
    high_pri = [(r, *vpr_label(r[4])) for r in priority_rows if 7.0 <= r[4] < 9.0]
    normal   = [(r, *vpr_label(r[4])) for r in priority_rows if r[4] < 7.0]

    def table_rows(items):
        rows = []
        for (pid, name, sev, cvss, vpr, epss), label, color, deadline in items:
            cat = classify(name)
            fname = f"cve/{cat}/{pid}-{safe_filename(name)}.md"
            sev_icon = SEVERITY_ICON.get(sev, sev)
            rows.append(
                f"| [{name}]({fname}) | {sev_icon} | "
                f"{cvss:.1f} | **{vpr:.1f}** | {epss_pct(epss)} | "
                f'<span style="color:{color}">{label}</span> |'
            )
        return "\n".join(rows) if rows else "_（目前無資料）_"

    updated_at = datetime.now().strftime("%Y-%m-%d %H:%M")
    priority_content = f"""# 近期優先修補清單

依 Tenable VPR（Vulnerability Priority Rating）分數排序，整合威脅情報與漏洞利用難度，比單純 CVSS 更貼近實際風險。

**資料更新時間：** `{updated_at}`

---

## 說明

| VPR 分數 | 建議行動 | 目標期限 |
|---------|---------|---------|
| <span style="color:#ff003c">●</span> 9.0 以上 | 立即處理 | 7 天內 |
| <span style="color:#ff6600">●</span> 7.0 – 8.9 | 優先排程 | 30 天內 |
| <span style="color:#ffd700">●</span> 4.0 – 6.9 | 一般排程 | 90 天內 |

!!! info "EPSS 說明"
    EPSS（Exploit Prediction Scoring System）代表該弱點在未來 30 天內被實際利用的機率，數值越高代表風險越迫切。

---

## 立即處理（VPR ≥ 9.0）

共 **{len(urgent)}** 個

| 弱點名稱 | 嚴重度 | CVSS v3 | VPR | EPSS | 建議 |
|---------|--------|---------|-----|------|------|
{table_rows(urgent)}

---

## 優先排程（VPR 7.0 – 8.9）

共 **{len(high_pri)}** 個

| 弱點名稱 | 嚴重度 | CVSS v3 | VPR | EPSS | 建議 |
|---------|--------|---------|-----|------|------|
{table_rows(high_pri)}

---

## 一般排程（VPR 4.0 – 6.9）

共 **{len(normal)}** 個

| 弱點名稱 | 嚴重度 | CVSS v3 | VPR | EPSS | 建議 |
|---------|--------|---------|-----|------|------|
{table_rows(normal)}
"""
    with open(PRIORITY_PAGE, "w", encoding="utf-8") as f:
        f.write(priority_content)
    print(f"  優先修補頁：立即 {len(urgent)} 個 / 優先 {len(high_pri)} 個 / 一般 {len(normal)} 個")

    print(f"完成：共產生 {generated} 個弱點頁面")
    print(f"  Web 類：{len(categories['web'])} 個")
    print(f"  系統類：{len(categories['system'])} 個")
    print(f"  服務類：{len(categories['services'])} 個")

if __name__ == "__main__":
    main()

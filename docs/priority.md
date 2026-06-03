# 近期優先修補清單

依 Tenable VPR（Vulnerability Priority Rating）分數排序，整合威脅情報與漏洞利用難度，比單純 CVSS 更貼近實際風險。

**資料更新時間：** `2026-06-03 20:24`

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

共 **1** 個

| 弱點名稱 | 嚴重度 | CVSS v3 | VPR | EPSS | 建議 |
|---------|--------|---------|-----|------|------|
| [OpenSSH < 9.8 RCE](cve/services/201194-openssh-98-rce.md) | <span style="color:#ff6600">●</span> High | 8.1 | **9.0** | 6383.0% | <span style="color:#ff003c">立即處理</span> |

---

## 優先排程（VPR 7.0 – 8.9）

共 **1** 個

| 弱點名稱 | 嚴重度 | CVSS v3 | VPR | EPSS | 建議 |
|---------|--------|---------|-----|------|------|
| [POP3 Service STLS Plaintext Command Injection](cve/web/52610-pop3-service-stls-plaintext-command-injection.md) | <span style="color:#ffd700">●</span> Medium | 0.0 | **7.3** | 3222.0% | <span style="color:#ff6600">優先排程</span> |

---

## 一般排程（VPR 4.0 – 6.9）

共 **15** 個

| 弱點名稱 | 嚴重度 | CVSS v3 | VPR | EPSS | 建議 |
|---------|--------|---------|-----|------|------|
| [Apache Tomcat 9.0.0.M1 < 9.0.118 multiple vulnerabilities](cve/web/314334-apache-tomcat-900m1-90118-multiple-vulnerabilities.md) | <span style="color:#ff003c">●</span> Critical | 9.8 | **6.7** | 4.0% | <span style="color:#ffd700">一般排程</span> |
| [OpenSSH < 10.3 Multiple Vulnerabilities](cve/services/306743-openssh-103-multiple-vulnerabilities.md) | <span style="color:#ff6600">●</span> High | 8.1 | **6.7** | 4.0% | <span style="color:#ffd700">一般排程</span> |
| [SSH Terrapin Prefix Truncation Weakness (CVE-2023-48795)](cve/services/187315-ssh-terrapin-prefix-truncation-weakness-cve-2023-48795.md) | <span style="color:#ffd700">●</span> Medium | 5.9 | **6.1** | 5421.0% | <span style="color:#ffd700">一般排程</span> |
| [OpenSSH < 9.6 Multiple Vulnerabilities](cve/services/187201-openssh-96-multiple-vulnerabilities.md) | <span style="color:#ffd700">●</span> Medium | 6.5 | **6.1** | 5421.0% | <span style="color:#ffd700">一般排程</span> |
| [MTA Open Mail Relaying Allowed](cve/services/10262-mta-open-mail-relaying-allowed.md) | <span style="color:#ff6600">●</span> High | 7.5 | **5.9** | 118.0% | <span style="color:#ffd700">一般排程</span> |
| [JQuery 1.2 < 3.5.0 Multiple XSS](cve/system/136929-jquery-12-350-multiple-xss.md) | <span style="color:#ffd700">●</span> Medium | 6.1 | **5.7** | 3466.0% | <span style="color:#ffd700">一般排程</span> |
| [SSL Medium Strength Cipher Suites Supported (SWEET32)](cve/web/42873-ssl-medium-strength-cipher-suites-supported-sweet32.md) | <span style="color:#ff6600">●</span> High | 7.5 | **5.1** | 4099.0% | <span style="color:#ffd700">一般排程</span> |
| [nginx 1.3.0 < 1.28.2 / 1.29.x < 1.29.5 SSL Upstream Injection](cve/web/304671-nginx-130-1282-129x-1295-ssl-upstream-injection.md) | <span style="color:#ffd700">●</span> Medium | 5.9 | **4.4** | 1.0% | <span style="color:#ffd700">一般排程</span> |
| [HTTP TRACE / TRACK Methods Allowed](cve/web/11213-http-trace-track-methods-allowed.md) | <span style="color:#ffd700">●</span> Medium | 5.3 | **4.0** | 6651.0% | <span style="color:#ffd700">一般排程</span> |
| [SSL Anonymous Cipher Suites Supported](cve/web/31705-ssl-anonymous-cipher-suites-supported.md) | <span style="color:#ffd700">●</span> Medium | 5.9 | **3.6** | 270.0% | <span style="color:#ffd700">一般排程</span> |
| [OpenSSH < 10.1 / 10.1p1 Multiple Vulnerabilities](cve/services/269984-openssh-101-101p1-multiple-vulnerabilities.md) | <span style="color:#00ff88">●</span> Low | 3.6 | **3.3** | 1.0% | <span style="color:#ffd700">一般排程</span> |
| [ICMP Timestamp Request Remote Date Disclosure](cve/system/10114-icmp-timestamp-request-remote-date-disclosure.md) | <span style="color:#00ff88">●</span> Low | 0.0 | **2.9** | 37.0% | <span style="color:#ffd700">一般排程</span> |
| [OpenSSH < 10.0 DisableForwarding](cve/services/234554-openssh-100-disableforwarding.md) | <span style="color:#00ff88">●</span> Low | 3.8 | **2.4** | 1.0% | <span style="color:#ffd700">一般排程</span> |
| [SSH Server CBC Mode Ciphers Enabled](cve/web/70658-ssh-server-cbc-mode-ciphers-enabled.md) | <span style="color:#00ff88">●</span> Low | 3.7 | **2.2** | 307.0% | <span style="color:#ffd700">一般排程</span> |
| [Apple Mac OS X Find-By-Content .DS_Store Web Directory Listing](cve/web/10756-apple-mac-os-x-find-by-content-ds_store-web-directory-listing.md) | <span style="color:#ffd700">●</span> Medium | 5.3 | **2.2** | 53.0% | <span style="color:#ffd700">一般排程</span> |

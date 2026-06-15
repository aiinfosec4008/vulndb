# 近期優先修補清單

依 Tenable VPR（Vulnerability Priority Rating）分數排序，整合威脅情報與漏洞利用難度，比單純 CVSS 更貼近實際風險。

**資料更新時間：** `2026-06-16 03:21`

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
| [OpenSSH < 9.8 RCE](cve/services/201194-openssh-98-rce.md) | <span style="color:#ff6600">●</span> High | 8.1 | **9.0** | 6579.0% | <span style="color:#ff003c">立即處理</span> |

---

## 優先排程（VPR 7.0 – 8.9）

共 **11** 個

| 弱點名稱 | 嚴重度 | CVSS v3 | VPR | EPSS | 建議 |
|---------|--------|---------|-----|------|------|
| [VMWare Aria Operations 8.x < 8.18.6 Multiple Vulnerabilities (VMSA-2026-0001)](cve/system/300235-vmware-aria-operations-8x-8186-multiple-vulnerabilities-vmsa-2026-0001.md) | <span style="color:#ff003c">●</span> Critical | 9.0 | **8.4** | 1076.0% | <span style="color:#ff6600">優先排程</span> |
| [VMware vCenter Server 7.0 < 7.0U3r / 8.0 < 8.0U2d Multiple Vulnerabilities (VMSA-2024-0012)](cve/system/200746-vmware-vcenter-server-70-70u3r-80-80u2d-multiple-vulnerabilities-vmsa-2024-0012.md) | <span style="color:#ff003c">●</span> Critical | 9.8 | **8.4** | 8205.0% | <span style="color:#ff6600">優先排程</span> |
| [VMware vRealize Log Insight 8.x < 8.10.2 Mutliple Vulnerabilities (VMSA-2023-0001)](cve/system/170661-vmware-vrealize-log-insight-8x-8102-mutliple-vulnerabilities-vmsa-2023-0001.md) | <span style="color:#ff003c">●</span> Critical | 9.8 | **8.4** | 9018.0% | <span style="color:#ff6600">優先排程</span> |
| [VMware ESXi 7.x < 7.0 Update 3w / 8.x < 8.0 Update 2e / 8.0 Update 3 < 8.0 Update 3f (VMSA-2025-0013)](cve/system/242168-vmware-esxi-7x-70-update-3w-8x-80-update-2e-80-update-3-80-update-3f-vmsa-2025-0.md) | <span style="color:#ff003c">●</span> Critical | 9.3 | **8.1** | 2.0% | <span style="color:#ff6600">優先排程</span> |
| [VMware ESXi 7.0 / 8.0 Multiple Vulnerabilities (VMSA-2025-0004)](cve/system/237304-vmware-esxi-70-80-multiple-vulnerabilities-vmsa-2025-0004.md) | <span style="color:#ff003c">●</span> Critical | 9.3 | **8.1** | 4680.0% | <span style="color:#ff6600">優先排程</span> |
| [SSL RC4 Cipher Suites Supported (Bar Mitzvah)](cve/web/65821-ssl-rc4-cipher-suites-supported-bar-mitzvah.md) | <span style="color:#ffd700">●</span> Medium | 5.9 | **8.1** | 9316.0% | <span style="color:#ff6600">優先排程</span> |
| [VMware Aria Operations 8.x < 8.18.5 Multiple Vulnerabilities (VMSA-2025-0015)](cve/system/266419-vmware-aria-operations-8x-8185-multiple-vulnerabilities-vmsa-2025-0015.md) | <span style="color:#ff6600">●</span> High | 7.8 | **7.4** | 3.0% | <span style="color:#ff6600">優先排程</span> |
| [VMware vCenter Server 7.x < 7.0 U3t / 8.x < 8.0.3 U3d Multiple Vulnerabilities (VMSA-2024-0019)](cve/system/207464-vmware-vcenter-server-7x-70-u3t-8x-803-u3d-multiple-vulnerabilities-vmsa-2024-00.md) | <span style="color:#ff003c">●</span> Critical | 9.8 | **7.4** | 7787.0% | <span style="color:#ff6600">優先排程</span> |
| [VMware Aria Operations for Logs < 8.18.3 Multiple Vulnerabilities (VMSA-2025-0003)](cve/system/215005-vmware-aria-operations-for-logs-8183-multiple-vulnerabilities-vmsa-2025-0003.md) | <span style="color:#ff003c">●</span> Critical | 9.0 | **7.3** | 10.0% | <span style="color:#ff6600">優先排程</span> |
| [VMware ESXi 7.0 / 8.0 Multiple Vulnerabilities (VMSA-2024-0006)](cve/system/191711-vmware-esxi-70-80-multiple-vulnerabilities-vmsa-2024-0006.md) | <span style="color:#ff6600">●</span> High | 8.2 | **7.3** | 23.0% | <span style="color:#ff6600">優先排程</span> |
| [POP3 Service STLS Plaintext Command Injection](cve/web/52610-pop3-service-stls-plaintext-command-injection.md) | <span style="color:#ffd700">●</span> Medium | 0.0 | **7.3** | 3777.0% | <span style="color:#ff6600">優先排程</span> |

---

## 一般排程（VPR 4.0 – 6.9）

共 **41** 個

| 弱點名稱 | 嚴重度 | CVSS v3 | VPR | EPSS | 建議 |
|---------|--------|---------|-----|------|------|
| [Open WebUI < 0.9.5 Multiple Vulnerabilities](cve/web/314912-open-webui-095-multiple-vulnerabilities.md) | <span style="color:#ff6600">●</span> High | 8.5 | **6.7** | 4.0% | <span style="color:#ffd700">一般排程</span> |
| [Apache Tomcat 9.0.0.M1 < 9.0.118 multiple vulnerabilities](cve/web/314334-apache-tomcat-900m1-90118-multiple-vulnerabilities.md) | <span style="color:#ff003c">●</span> Critical | 9.8 | **6.7** | 4.0% | <span style="color:#ffd700">一般排程</span> |
| [OpenSSH < 10.3 Multiple Vulnerabilities](cve/services/306743-openssh-103-multiple-vulnerabilities.md) | <span style="color:#ff6600">●</span> High | 8.1 | **6.7** | 4.0% | <span style="color:#ffd700">一般排程</span> |
| [VMware vCenter Server 7.0.x < 7.0 U3v / 8.0.x < 8.0 U3e Authenticated Command Execution (CVE-2025-41225) (VMSA-2025-0010)](cve/system/237247-vmware-vcenter-server-70x-70-u3v-80x-80-u3e-authenticated-command-execution-cve-.md) | <span style="color:#ff6600">●</span> High | 8.8 | **6.7** | 2.0% | <span style="color:#ffd700">一般排程</span> |
| [VMware ESXi 7.0 / 8.0 Multiple Vulenerabilities (VMSA-2025-0010)](cve/system/237246-vmware-esxi-70-80-multiple-vulenerabilities-vmsa-2025-0010.md) | <span style="color:#ffd700">●</span> Medium | 6.8 | **6.7** | 3.0% | <span style="color:#ffd700">一般排程</span> |
| [VMWare Aria Operations < 8.16 PrivEsc (VMSA-2024-0004)](cve/system/190887-vmware-aria-operations-816-privesc-vmsa-2024-0004.md) | <span style="color:#ffd700">●</span> Medium | 6.7 | **6.7** | 7.0% | <span style="color:#ffd700">一般排程</span> |
| [OpenSSH < 8.0](cve/services/159491-openssh-80.md) | <span style="color:#ffd700">●</span> Medium | 6.8 | **6.7** | 5757.0% | <span style="color:#ffd700">一般排程</span> |
| [ESXi 6.5 / 6.7 / 7.0 Multiple Vulnerabilities (VMSA-2022-0030)](cve/system/168828-esxi-65-67-70-multiple-vulnerabilities-vmsa-2022-0030.md) | <span style="color:#ff6600">●</span> High | 8.8 | **6.5** | 36.0% | <span style="color:#ffd700">一般排程</span> |
| [Apache Tomcat 9.0.92 < 9.0.117 multiple vulnerabilities](cve/web/307003-apache-tomcat-9092-90117-multiple-vulnerabilities.md) | <span style="color:#ff6600">●</span> High | 7.5 | **6.1** | 4.0% | <span style="color:#ffd700">一般排程</span> |
| [SSH Terrapin Prefix Truncation Weakness (CVE-2023-48795)](cve/services/187315-ssh-terrapin-prefix-truncation-weakness-cve-2023-48795.md) | <span style="color:#ffd700">●</span> Medium | 5.9 | **6.1** | 5166.0% | <span style="color:#ffd700">一般排程</span> |
| [OpenSSH < 9.6 Multiple Vulnerabilities](cve/services/187201-openssh-96-multiple-vulnerabilities.md) | <span style="color:#ffd700">●</span> Medium | 6.5 | **6.1** | 5300.0% | <span style="color:#ffd700">一般排程</span> |
| [Apache Tomcat 9.0.113 < 9.0.116 multiple vulnerabilities](cve/web/307004-apache-tomcat-90113-90116-multiple-vulnerabilities.md) | <span style="color:#ff003c">●</span> Critical | 9.1 | **6.0** | 4.0% | <span style="color:#ffd700">一般排程</span> |
| [SNMP Agent Default Community Name (public)](cve/services/41028-snmp-agent-default-community-name-public.md) | <span style="color:#ff6600">●</span> High | 0.0 | **6.0** | 8959.0% | <span style="color:#ffd700">一般排程</span> |
| [VMware Aria Operations 8.x < 8.18 HF 5 Privilege Escalation (VMSA-2025-0006)](cve/system/233816-vmware-aria-operations-8x-818-hf-5-privilege-escalation-vmsa-2025-0006.md) | <span style="color:#ff6600">●</span> High | 7.8 | **5.9** | 1.0% | <span style="color:#ffd700">一般排程</span> |
| [VMware Aria Operations Multiple Vulnerabilities (VMSA-2024-0022)](cve/system/212134-vmware-aria-operations-multiple-vulnerabilities-vmsa-2024-0022.md) | <span style="color:#ff6600">●</span> High | 7.8 | **5.9** | 13.0% | <span style="color:#ffd700">一般排程</span> |
| [VMware Aria Operations < 8.6 Hot Fix 11 / 8.10 Hot Fix 9 / 8.12 Hot Fix 5 Privilege Escalation (VMSA-2023-0020)](cve/system/182186-vmware-aria-operations-86-hot-fix-11-810-hot-fix-9-812-hot-fix-5-privilege-escal.md) | <span style="color:#ffd700">●</span> Medium | 6.7 | **5.9** | 5.0% | <span style="color:#ffd700">一般排程</span> |
| [MTA Open Mail Relaying Allowed](cve/services/10262-mta-open-mail-relaying-allowed.md) | <span style="color:#ff6600">●</span> High | 7.5 | **5.9** | 7086.0% | <span style="color:#ffd700">一般排程</span> |
| [JQuery 1.2 < 3.5.0 Multiple XSS](cve/system/136929-jquery-12-350-multiple-xss.md) | <span style="color:#ffd700">●</span> Medium | 6.1 | **5.7** | 3466.0% | <span style="color:#ffd700">一般排程</span> |
| [VMware vCenter Server 7.0.x < 7.0 U3w / 8.0.x < 8.0 U3g SMTP Header Injection (VMSA-2025-0016)](cve/services/266405-vmware-vcenter-server-70x-70-u3w-80x-80-u3g-smtp-header-injection-vmsa-2025-0016.md) | <span style="color:#ff6600">●</span> High | 8.5 | **5.1** | 5.0% | <span style="color:#ffd700">一般排程</span> |
| [SSL Medium Strength Cipher Suites Supported (SWEET32)](cve/web/42873-ssl-medium-strength-cipher-suites-supported-sweet32.md) | <span style="color:#ff6600">●</span> High | 7.5 | **5.1** | 4099.0% | <span style="color:#ffd700">一般排程</span> |
| [OpenSSH < 7.8](cve/services/159490-openssh-78.md) | <span style="color:#ffd700">●</span> Medium | 5.3 | **4.9** | 9036.0% | <span style="color:#ffd700">一般排程</span> |
| [nginx 1.3.0 < 1.28.2 / 1.29.x < 1.29.5 SSL Upstream Injection](cve/web/304671-nginx-130-1282-129x-1295-ssl-upstream-injection.md) | <span style="color:#ffd700">●</span> Medium | 5.9 | **4.4** | 1.0% | <span style="color:#ffd700">一般排程</span> |
| [VMware ESXi 7.0 / 8.0 Out-of-Bounds read (CVE-2024-37086)](cve/system/201125-vmware-esxi-70-80-out-of-bounds-read-cve-2024-37086.md) | <span style="color:#ffd700">●</span> Medium | 6.8 | **4.2** | 5.0% | <span style="color:#ffd700">一般排程</span> |
| [SSL Certificate Signed Using Weak Hashing Algorithm](cve/web/35291-ssl-certificate-signed-using-weak-hashing-algorithm.md) | <span style="color:#ffd700">●</span> Medium | 0.0 | **4.2** | 815.0% | <span style="color:#ffd700">一般排程</span> |
| [DNS Server Recursive Query Cache Poisoning Weakness](cve/services/10539-dns-server-recursive-query-cache-poisoning-weakness.md) | <span style="color:#ffd700">●</span> Medium | 0.0 | **4.2** | 132.0% | <span style="color:#ffd700">一般排程</span> |
| [HTTP TRACE / TRACK Methods Allowed](cve/web/11213-http-trace-track-methods-allowed.md) | <span style="color:#ffd700">●</span> Medium | 5.3 | **4.0** | 7987.0% | <span style="color:#ffd700">一般排程</span> |
| [VMware vCenter Server 7.0.x < 7.0 U3v / 8.0.x < 8.0 U3g DoS (VMSA-2025-0014)](cve/system/245963-vmware-vcenter-server-70x-70-u3v-80x-80-u3g-dos-vmsa-2025-0014.md) | <span style="color:#ffd700">●</span> Medium | 4.4 | **3.6** | 4.0% | <span style="color:#ffd700">一般排程</span> |
| [VMware Aria Operations Information Disclosure (VMSA-2025-0003)](cve/system/215067-vmware-aria-operations-information-disclosure-vmsa-2025-0003.md) | <span style="color:#ffd700">●</span> Medium | 6.5 | **3.6** | 5.0% | <span style="color:#ffd700">一般排程</span> |
| [VMware vRealize Operations 8.x < 8.10 Arbitrary File Read (VMSA-2022-0026)](cve/system/170605-vmware-vrealize-operations-8x-810-arbitrary-file-read-vmsa-2022-0026.md) | <span style="color:#ffd700">●</span> Medium | 4.9 | **3.6** | 17.0% | <span style="color:#ffd700">一般排程</span> |
| [DNS Server Spoofed Request Amplification DDoS](cve/services/35450-dns-server-spoofed-request-amplification-ddos.md) | <span style="color:#ff6600">●</span> High | 7.5 | **3.6** | 3071.0% | <span style="color:#ffd700">一般排程</span> |
| [SSL Anonymous Cipher Suites Supported](cve/web/31705-ssl-anonymous-cipher-suites-supported.md) | <span style="color:#ffd700">●</span> Medium | 5.9 | **3.6** | 270.0% | <span style="color:#ffd700">一般排程</span> |
| [OpenSSH < 10.1 / 10.1p1 Multiple Vulnerabilities](cve/services/269984-openssh-101-101p1-multiple-vulnerabilities.md) | <span style="color:#00ff88">●</span> Low | 3.6 | **3.3** | 1.0% | <span style="color:#ffd700">一般排程</span> |
| [VMware vRealize Log Insight 8.x < 8.8.2 XSS (VMSA-2022-0019)](cve/system/163099-vmware-vrealize-log-insight-8x-882-xss-vmsa-2022-0019.md) | <span style="color:#ffd700">●</span> Medium | 5.4 | **3.0** | 89.0% | <span style="color:#ffd700">一般排程</span> |
| [VMware vRealize Log Insight 4.x < 8.1.0 XSS Vulnerability (VMSA-2020-0007)](cve/system/135923-vmware-vrealize-log-insight-4x-810-xss-vulnerability-vmsa-2020-0007.md) | <span style="color:#ffd700">●</span> Medium | 6.1 | **3.0** | 50.0% | <span style="color:#ffd700">一般排程</span> |
| [ICMP Timestamp Request Remote Date Disclosure](cve/system/10114-icmp-timestamp-request-remote-date-disclosure.md) | <span style="color:#00ff88">●</span> Low | 0.0 | **2.9** | 37.0% | <span style="color:#ffd700">一般排程</span> |
| [Remote Desktop Protocol Server Man-in-the-Middle Weakness](cve/system/18405-remote-desktop-protocol-server-man-in-the-middle-weakness.md) | <span style="color:#ffd700">●</span> Medium | 6.5 | **2.5** | 427.0% | <span style="color:#ffd700">一般排程</span> |
| [OpenSSH < 10.0 DisableForwarding](cve/services/234554-openssh-100-disableforwarding.md) | <span style="color:#00ff88">●</span> Low | 3.8 | **2.4** | 1.0% | <span style="color:#ffd700">一般排程</span> |
| [OpenSSH < 7.6](cve/services/103781-openssh-76.md) | <span style="color:#ffd700">●</span> Medium | 5.3 | **2.2** | 284.0% | <span style="color:#ffd700">一般排程</span> |
| [SSH Server CBC Mode Ciphers Enabled](cve/web/70658-ssh-server-cbc-mode-ciphers-enabled.md) | <span style="color:#00ff88">●</span> Low | 3.7 | **2.2** | 307.0% | <span style="color:#ffd700">一般排程</span> |
| [Apple Mac OS X Find-By-Content .DS_Store Web Directory Listing](cve/web/10756-apple-mac-os-x-find-by-content-ds_store-web-directory-listing.md) | <span style="color:#ffd700">●</span> Medium | 5.3 | **2.2** | 53.0% | <span style="color:#ffd700">一般排程</span> |
| [VMware vCenter Server 7.0 < 7.0U3q / 8.0 < 8.0U3 DoS (CVE-2024-37087)](cve/system/201124-vmware-vcenter-server-70-70u3q-80-80u3-dos-cve-2024-37087.md) | <span style="color:#ffd700">●</span> Medium | 5.3 | **1.4** | 15.0% | <span style="color:#ffd700">一般排程</span> |

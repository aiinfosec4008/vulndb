# 中央研究院資安弱點知識庫

歡迎使用中央研究院資安科弱點管理知識庫。本知識庫供各所 IT 管理員查閱弱點資訊、修補建議與資安規範。

---

## 快速導覽

<div class="grid cards" markdown>

- :material-bug: **弱點百科 (CVE)**

    ---

    已知弱點的說明、危險程度與修補建議，依 Web、系統、服務分類。

    [:octicons-arrow-right-24: 查閱弱點](cve/index.md)

- :material-sword: **攻擊手法 (TTPs)**

    ---

    常見攻擊手法說明（釣魚、橫向移動、勒索軟體）與對應防禦措施。

    [:octicons-arrow-right-24: 了解攻擊手法](ttps/index.md)

- :material-shield-check: **資安政策與規範**

    ---

    院內資安規定、設定稽核清單與合規要求。

    [:octicons-arrow-right-24: 查閱規範](policy/index.md)

</div>

---

## 風險等級說明

<table>
<colgroup>
  <col style="width: 18%">
  <col style="width: 14%">
  <col>
</colgroup>
<thead><tr><th>等級</th><th>CVSS 分數</th><th>說明</th></tr></thead>
<tbody>
<tr><td>:material-circle:{ style="color: #d32f2f" } 重大 (Critical)</td><td>9.0 – 10.0</td><td>可被遠端利用，無需認證，影響範圍廣</td></tr>
<tr><td>:material-circle:{ style="color: #f57c00" } 高 (High)</td><td>7.0 – 8.9</td><td>可被利用，有明確 PoC 或已被在野利用</td></tr>
<tr><td>:material-circle:{ style="color: #fbc02d" } 中 (Medium)</td><td>4.0 – 6.9</td><td>需特定條件才能利用</td></tr>
<tr><td>:material-circle:{ style="color: #388e3c" } 低 (Low)</td><td>0.1 – 3.9</td><td>利用條件嚴苛或影響有限</td></tr>
</tbody>
</table>

---

!!! info "知識庫更新說明"
    本知識庫由資安科定期更新，CVE 頁面部分由 VA 掃描結果自動產生。如有疑問請聯絡資安科技術組。

---
name: paper-citation-check
description: "引用专项检查 — BibTeX 完整性 + 香火引用检测 + 遗漏关键引用推荐"
version: 1.0.0
author: TheeTarnished
license: MIT
---
# 引用检查 · Citation Check
.bib 完整性 + 引用质量 + 遗漏推荐。
## 检查项
- 所有 \cite 在 .bib 有对应条目
- .bib 中无未引用条目
- 香火引用检测 (cite but no discuss)
- 近3年引用占比
- 自引率
- 遗漏关键引用推荐 (从 Semantic Scholar)
## 输出
```json
{"total":35,"cited_in_text":35,"orphan_in_bib":2,
 "token_cites":5,"recent_ratio":0.31,"self_cite_ratio":0.08,
 "missing_recommendations":["paper_x (2023, 500+ cites)"]}
```
## 使用
```
检查引用: path/to/paper.tex path/to/refs.bib
```

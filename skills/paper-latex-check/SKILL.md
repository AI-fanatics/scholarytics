---
name: paper-latex-check
description: "LaTeX 专项检查 — 编译、引用、图表、页面全量审计，输出精确修复代码"
version: 1.0.0
author: TheeTarnished
license: MIT
---
# LaTeX 检查 · LaTeX Check
pdflatex 三遍编译 + 全部 warning/error 审计 + 精确修复建议。
## 检查项
- pdflatex ×3 编译
- Overfull/Underfull hbox
- 未定义引用 (??)
- 未定义 citation [?]
- 图表分辨率
- 字体缺失
- 页数超标
## 输出
每个问题附带精确的 LaTeX 修复代码。
## 使用
```
检查 LaTeX: path/to/paper.tex
```

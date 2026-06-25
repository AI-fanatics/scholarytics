---
name: paper-quick-scan
description: "论文快速扫描 — 5分钟生成论文核心画像: 贡献类型、方法快照、实验亮点、风险标记"
version: 1.0.0
author: TheeTarnished
license: MIT
---
# 快速扫描 · Quick Scan
5 分钟生成论文一页纸画像。适合投稿前自查或批量筛选。
## 输出
```json
{
  "title": "...",
  "contribution_type": "method|theory|application|benchmark",
  "method_snapshot": "one-paragraph summary",
  "key_result": "the single most important number",
  "red_flags": ["no ablation", "missing baseline"],
  "green_flags": ["open source", "multi-seed"],
  "estimated_score": "22-26/30",
  "recommend_action": "submit|revise|reject"
}
```
## 使用
```
快速扫描: path/to/paper.pdf
```

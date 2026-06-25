---
name: paper-venue-matcher
description: "会议/期刊匹配器 — 基于论文质量评分推荐合适的投稿目标 (CCF + SCI)"
version: 1.0.0
author: TheeTarnished
license: MIT
---
# 会议/期刊匹配器 · Venue Matcher
根据论文质量评分、创新性、实验完整度推荐投稿目标。
## 推荐逻辑
| 评分 | CCF 推荐 | SCI 推荐 |
|:--:|------|------|
| 26-30 | A类: NeurIPS/ICML/CVPR/ACL | 1区 Top |
| 22-25 | B类: ACML/ECCV/EMNLP | 2区 |
| 18-21 | C类: 专题 workshop | 3区 |
| <18 | 建议先完善实验再投 | 不建议投稿 |
## 输出
```json
{
  "paper_score": 24,
  "ccf_recommendations": [
    {"venue":"ACML","tier":"B","match_reason":"short paper, experimental"},
    {"venue":"ECCV","tier":"B","match_reason":"vision domain"}
  ],
  "sci_recommendations": [
    {"journal":"Pattern Recognition","if":8.5,"quartile":"Q1"}
  ]
}
```
## 使用
```
匹配会议: path/to/review_report.json
```

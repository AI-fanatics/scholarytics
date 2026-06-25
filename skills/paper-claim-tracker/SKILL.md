---
name: paper-claim-tracker
description: "论文声称追踪器 — 提取所有声称 → 映射到证据位置 → 标记未验证声称"
version: 1.0.0
author: TheeTarnished
license: MIT
---
# 声称追踪器 · Claim Tracker
从 Introduction 提取所有 claim → 定位证据 → 标记状态。
## 工作流
1. 提取 Introduction/Abstract 中所有声称 (claimed contributions)
2. 定位 Experiment/Results 中的对应证据 (table/figure/line)
3. 标记每个声称的状态: ✅verified / ⚠️partial / ❌unverified
4. 检测 Conclusion 中的新声称 (Introduction 未提及)
## 输出
```json
{"claims":[
  {"id":1,"text":"We propose method X","location":"§1 L45",
   "evidence":"Table 3, ablation row 4","status":"✅verified"},
  {"id":3,"text":"X outperforms all baselines","location":"§1 L52",
   "evidence":"Table 2 shows X<Y on metric Z","status":"⚠️partial"}
],"new_in_conclusion":1,"verified_ratio":0.67}
```
## 使用
```
追踪声称: path/to/paper.tex
```

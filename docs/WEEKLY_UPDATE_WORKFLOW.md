# 每周更新工作流

## 目标

每周输出一份可推送到 GitHub 的更新，而不是只有零散日常入库。

## 周更节奏

### 周内

持续做日常案例扫描，把确认后的案例写入：

- `knowledge_base/cases/`
- `knowledge_base/abilities/seed_abilities.json`

### 周末

运行周报脚本，生成 `reports/weekly/YYYY-WW.md`。

建议周报包含四块：

1. 本周新增案例
2. 本周新增能力
3. 本周重复出现的方法模式
4. 证据边界

## 更新原则

- 质量优先，不为了凑数补造案例
- 公开证据优先，不用私密来源
- 能力新增必须比“工具介绍”更稳定
- changelog 可入库，但应单独标明它是参数证据，不是成片案例

## GitHub 提交建议

### 正常周更

一次 commit 足够，建议格式：

```text
weekly: update AI video cases and abilities for 2026-W32
```

### 结构升级

当知识 schema、技能定义、脚本逻辑变更时，再单独提交：

```text
feat: refine ability schema and weekly digest generator
```

## 人工复核项

推送周报前至少看这四件事：

1. 原始链接是否仍然存在
2. 新增能力是否真的由案例支撑
3. changelog 类型内容是否被误写成“案例成片”
4. 证据边界是否写清楚

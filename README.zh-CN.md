# AI 视频大师Agent

[English README](./README.md) | [English Docs](./docs/en/) | [中文文档](./docs/zh-CN/)

`ai-video-master-agent` 是一个面向 AI 视频生产的开源“知识层 + 控制层”仓库。

它的目标不是堆积 Prompt，而是把公开案例、方法规则、能力沉淀、周报机制和执行层接口整理成一个可持续维护的 GitHub 项目。

## 为什么要做这个仓库

很多 AI 视频项目最终会变成两种坏形态：

1. 只有零散 Prompt，没有长期知识层。
2. 研究、案例、执行状态、媒体输出全混在一起，无法维护。

这个仓库就是为了解决这两个问题。

它把职责拆开：

- `knowledge_base/`：沉淀可复用能力和公开案例证据
- `skills/`：定义 Agent 的筛选、路由和升级规则
- `reports/weekly/`：输出适合公开周更的内容
- `automation/`：记录自动化维护约定
- `scripts/`：让校验和周报生成可重复执行

## 仓库边界

### 这个仓库包含什么

- 公开可验证的 AI 视频案例
- 可复用的能力定义
- Agent 路由规则
- 周报生成脚本
- Notion 同步合同
- 多语言说明文档

### 这个仓库不包含什么

- 直接生图
- 直接生视频
- 私密 Token 或账号信息
- 未公开媒体素材
- 没有真实调用却声称“已生成”的结果

## 仓库结构

```text
ai-video-master-agent/
  .github/
  automation/
  config/
  data/
  docs/
    en/
    zh-CN/
  knowledge_base/
    abilities/
    cases/
    schemas/
  reports/
    weekly/
  scripts/
  skills/
  CHANGELOG.md
  CONTRIBUTING.md
  CODE_OF_CONDUCT.md
  LICENSE
  README.md
  README.zh-CN.md
  SECURITY.md
```

## 四个核心模块

### 1. Skills

`skills/` 定义 AI 视频大师Agent 应该如何思考：

- 什么时候复用已有能力
- 什么时候只记为案例
- 什么时候值得升级成长期能力
- 什么时候应该交给执行层继续处理

当前内置两个核心技能：

- `ai-video-master-director`
- `ai-video-radar-librarian`

### 2. Knowledge Base

`knowledge_base/` 是本仓库的本地真相源。

当前包含：

- `abilities/seed_abilities.json`
- `cases/*.json`
- 对应 schema

这个结构天然适合 Git 管理，也方便后续同步到 Notion，但 Notion 不再被当作唯一真相源。

### 3. Weekly Reports

`reports/weekly/` 用来保存适合公开发布的周报。

一个好的周报应该说明：

- 本周新增案例
- 本周新增能力
- 重复出现的方法模式
- 证据边界

### 4. Execution Interface

这个仓库是“知识/控制层”。

[`ai-video-supervisor`](../ai-video-supervisor/README.md) 仍然是“执行层”。

推荐协作方式：

1. `ai-video-master-agent` 收集和固化规则
2. `ai-video-supervisor` 把规则用于 shot package、prompt、review、handoff
3. 真实验证后的经验再回流到本仓库，升级为能力和文档

## 当前内置 seed

目前已经包含：

- 10 条公开案例
- 10 条能力
- 2 个核心技能
- 周报生成脚本
- 知识库校验脚本
- 多语言文档结构
- GitHub 社区规范文件

## 快速开始

```bash
cd /Users/jiapeng/Projects/AIGC/ai-video-master-agent
python3 scripts/validate_knowledge_base.py
python3 scripts/generate_weekly_digest.py --date 2026-08-09
```

示例输出：

- [`reports/weekly/2026-W32.md`](./reports/weekly/2026-W32.md)

## 文档入口

- [架构说明](./docs/zh-CN/architecture.md)
- [周更工作流](./docs/zh-CN/weekly-update-workflow.md)
- [Notion 同步合同](./docs/zh-CN/notion-sync-contract.md)
- [参考项目](./docs/zh-CN/reference-projects.md)
- [路线图](./docs/zh-CN/roadmap.md)

英文镜像：

- [Architecture](./docs/en/architecture.md)
- [Weekly Update Workflow](./docs/en/weekly-update-workflow.md)
- [Notion Sync Contract](./docs/en/notion-sync-contract.md)
- [Reference Projects](./docs/en/reference-projects.md)
- [Roadmap](./docs/en/roadmap.md)

## 开源协议

本项目采用 [MIT License](./LICENSE)。

目标是让这个仓库：

- 易于 fork
- 易于审查
- 易于持续周更
- 易于和私有生产素材分离

## 持续更新机制

这个仓库的持续更新方式包括：

- 日常案例增量入库
- 每周自动或手动生成周报
- 当模式稳定后升级能力
- 持续完善文档
- 用 GitHub Actions 做校验和定时周报

## 发布建议

如果单独发布到 GitHub，优先公开：

- `README*`
- `docs/`
- `skills/`
- `knowledge_base/`
- `reports/weekly/`
- `scripts/`
- `.github/` 社区与自动化文件

不要公开：

- 私有草稿
- 本地凭证
- 私有素材
- 内部 Token
- 未验证的生产输出

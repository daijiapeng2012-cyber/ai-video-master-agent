# ComfyUI Agent 编排

可以，而且很值得做。但真正应该自动化的目标不是“让 Agent 盲点 ComfyUI 界面”，而是：

1. 先由 Agent 生成结构化执行计划
2. 计划选择合适的工作流家族
3. 再由一个很薄的执行适配层把计划映射进 ComfyUI 图
4. review 和 retry 保持显式

## 为什么 ComfyUI 会显得复杂

ComfyUI 强，正是因为它把图级控制暴露出来了。但这也意味着：

- 节点太多
- 运行时组合太多
- 社区工作流里有很多隐含假设
- 容易从“看起来炫”滑向“根本不可复用”

Agent 最该帮忙的，不是替你乱点界面，而是做界面上层的决策：

- 选哪类工作流
- 绑定哪些参考
- 选什么模型路由
- 用什么重试策略
- 生成一个小而清楚的执行合同

## 推荐架构

### 第 1 层：知识与路由

由 `ai-video-master-agent` 负责：

- 能力选择
- 基于案例的推理
- 按阶段规划
- 证据边界

### 第 2 层：计划生成

生成一个紧凑计划，字段例如：

- 任务目标
- 工作流家族
- 输入参考
- 时长 / 画幅 / 输出目标
- 模型路由
- 控制资产
- review gate
- fallback 策略

### 第 3 层：ComfyUI 适配层

一个薄执行层负责：

- 选定已有 workflow template
- 注入 prompt、reference、checkpoint、LoRA 和参数
- 启动图
- 记录输出路径和运行状态

### 第 4 层：Review 回路

review 不要塞进节点图里，应放在图外：

- 验证文件是否真的存在
- 记录 review 结果
- 决定 retry / revise / approve

## 最值得先自动化的部分

优先自动化：

1. 工作流家族选择
2. prompt 与 reference 绑定
3. seed / checkpoint / LoRA 预设路由
4. 导出执行计划
5. 稳定的 retry 策略

不要一开始就自动化：

- 从零自由生成整张节点图
- 把盲点 UI 当主要方案
- 上来就做超大一体化图且没有中间检查

## 工作流家族

更实用的做法是让 Agent 在“工作流家族”之间选择，而不是每次都发明新图。

例如：

- `text_to_video_base`
- `image_to_video_reference`
- `character_consistency_ref`
- `dialogue_performance_branch`
- `clean_plate_fix`
- `relight_pass`

## 仓库已支持

这个仓库现在已经补了：

- ComfyUI handoff 导出器
- Agent 生成 ComfyUI 执行计划的 schema
- 生成 starter plan JSON 的脚本

它们就是知识层和执行层之间的桥。

# clear-output · 理解与表达设计

一个中文优先、语言无关的解释设计 Skill：让复杂内容更容易理解、核验和行动，而不是只做摘要或美化。它保留数据、条件、反证和来源，并按任务选择文字、表格、图、交互或视频的最小充分组合。

## 使用

无需额外依赖、API Key 或付费 Skill。需要生成 PPT、Word、图表或交互时，使用宿主已具备的工具；本 Skill 本身不提供这些工具。

在支持 Agent Skills 的宿主中，把本目录作为一个完整 Skill 导入。Codex 可按当前官方文档将目录放入项目 `.agents/skills/clear-output/` 或用户级 `~/.agents/skills/clear-output/`。不同宿主和版本的发现路径可能不同，以其文档为准；不要覆盖现有技能或配置。参考 [官方 Skill 指南](https://learn.chatgpt.com/docs/build-skills)。

显式调用示例：

```text
请使用 $clear-output，把以下报告解释给没有技术背景的投资委员会。
保留所有影响决策的数据、假设、反证和限制；交付一页结论及可追溯附录。
```

默认允许宿主自动选择；安装并不保证每次都触发，也不会自动同步所有 Agent。如希望每次复杂任务使用，可在每个 Agent 的既有指令中追加而非覆盖：

```text
复杂解释、比较和长文改写任务优先应用可用的 clear-output Skill。
不得改变用户指定格式；简单问题直接回答，不增加不必要图表或篇幅。
```

## 文件

- `SKILL.md`：触发条件、优先级、解释工作流和四项验收。
- `references/fidelity-check.md`：保真台账、数字与冲突、分层及核验。
- `references/modality-routing.md`：载体选择、图表、交互、文件兼容性。
- `tests/cases.json`：可重复的行为验收案例。
- `tests/validate.py`：离线结构和测试数据检查；不是模型能力评测。

运行基础检查：`python3 tests/validate.py`。进行行为评测时，给独立 Agent 加载 Skill 并逐条提供 `prompt`，按 `checks` 评判，不预先提供标准答案。记录模型、日期、输出和失败项目；不要把静态检查当作理解效果已经验证。

## 思路来源与边界

实现主要来自用户提供的七步“理解与表达设计”流程。表达载体选择受到 [Andrej Karpathy 2026 年 10 月 2 日的 X 帖子](https://x.com/karpathy/status/2105819303471976479)启发：降低人理解模型输出的成本，按需要采用更清楚的语言、图像、交互和解释视频。这是工作流改编，并非 Karpathy 官方 Skill、授权背书或经过证明的统一理论；未复制其完整原帖。

可进一步参考：[Plain Language](https://digital.gov/guides/plain-language/)、[复述测试](https://digital.gov/guides/plain-language/test/paraphrase-testing)、[W3C 复杂图像](https://www.w3.org/WAI/tutorials/images/complex/)、[颜色使用](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html)、[ONS 坐标轴指南](https://service-manual.ons.gov.uk/data-visualisation/guidance/axes-and-gridlines)、[ASD-STE100 FAQ](https://www.asd-ste100.org/STE_faq.html)。借鉴不等于声称达到这些标准的合规认证。

这是指令型 Skill，不保证模型零遗漏或审美自动提升。应结合真实任务、读者反馈和技术验收迭代；不会自动读取账户、执行发布或安装其他软件。

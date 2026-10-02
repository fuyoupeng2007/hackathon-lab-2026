# 黑客松作品交付与提交指南

交付日期：2026-10-02。账户：fuyoupeng2007。按你确认的方案完成两个独立成品、五份比赛专用材料和三代迭代证据，由你最终投稿。

总仓库：[https://github.com/fuyoupeng2007/hackathon-lab-2026](https://github.com/fuyoupeng2007/hackathon-lab-2026)。在线入口：[https://fuyoupeng2007.github.io/hackathon-lab-2026/](https://fuyoupeng2007.github.io/hackathon-lab-2026/)。本地总目录：`D:\chatgpt\hackathon-lab-2026`。

## 五场比赛与适配条件

推荐以不需硬件、无需强制付费 API、可个人完成、允许或未明令排除 AI 辅助、与现有功能匹配为筛选依据。你的年龄和学生身份尚未验证；本表是条件推荐，不能视为参赛资格证明。四场可以优先核对，ML Empowerment 是需先澄清规则的候选。

| 比赛与官方规则 | 对应作品 | 截止时间 北京时间 | 资格口径 | 当前适配状态 |
| --- | --- | --- | --- | --- |
| [Build With AI: Basics](https://learn-ai-basics.devpost.com/rules) | BriefCheck | 2026-10-27 05:00 | 达到居住地法定成年年龄；地区及关联方限制见规则 | 优先；需本人确认资格和个人参与要求 |
| [LovHack Season 3](https://lovhack-season-3.devpost.com/rules) | BriefCheck | 2026-10-05 11:45 | 13 至 24 岁的学生；个人或最多 4 人 | 近期优先；资格待本人确认 |
| [WarriorHacks 2.0](https://warriorhacks-2-0.devpost.com/rules) | AccessProof | 2026-10-14 12:45 | 全球高中生和本科生；允许个人，推荐最多 4 人 | 主题匹配；需另填 Track Selection Form |
| [HACK47: OFFGRID](https://hack47-offgrid.devpost.com/rules) | BriefCheck | 2026-10-15 12:00 | 页面标签为成年学生；正文欢迎各类全球创作者；存在口径差异 | 适合作品方向；时间与资格口径需复核 |
| [ML Empowerment Build Challenge 3.0](https://ml-build-challenge-3.devpost.com/rules) | AccessProof | 保守按 2026-10-06 12:00；页面另写 10-10 14:45 | 13 岁以上；高中和大学学生，允许 1 至 5 人 | 条件候选；截止日期与 AI 项目口径待复核 |

LovHack 最早截止，优先检查；随后是 ML 的保守截止、WarriorHacks、OFFGRID 和 Basics。ML 的两个时间分别来自规则正文和页面页头，不能替主办方裁定。OFFGRID 正文写正式时间另行公布，资格又比页面标签宽泛。两项都需提交前查看更新。

Basics 需公开 YouTube/Vimeo 视频、英文材料、开源仓库和 Learn Skill Pack 的 scope/prd/spec。它还强调参与者自己的想法与学习过程，本项目保留自主构建与访谈步骤偏离的披露，需要你本人阅读、理解和如实填写自己的部分。[官方规则](https://learn-ai-basics.devpost.com/rules)

WarriorHacks 已公布社区问题主题，还要求另填 Track Selection Form；对应目录已附官方表单链接。[官方更新](https://warriorhacks-2-0.devpost.com/updates)

## 成品与目录

`projects/briefcheck`：中英双语需求验收工具。输入需求，核对原文，编辑交付标准和答复，比较修订，切换本机项目，导出 Markdown、JSON 和独立客户预览。最多 20 个本机项目，原文 20,000 字，JSON 导入上限 1 MB。

`projects/accessproof`：中英双语 HTML 无障碍源码预检。输入源码，查看问题元素、原因和修复模式，记录人工决定，比较改动，导出记录。原文上限 100,000 字，JSON 上限 1 MB。它不宣称 WCAG 合规。

`competitions/01...05...`：每场均有中文使用清单、英文投稿文字、资格条件、演示链接和代码入口。两款软件没有改名冒充五款软件；跨比赛复用必须按各场规则披露。

`media`：真实操作录屏、英文说明字幕和截图。BriefCheck 为 128.00 秒，AccessProof 为 103.64 秒；均为 1600 x 900、25 fps、H.264、无配音。格式检查各 8 项通过、0 项失败，两个提示是无音轨与无内嵌可选字幕轨；视频已有烧录字幕，另提供 SRT。GitHub 视频文件可下载，但不是 Basics 要求的公开 YouTube/Vimeo URL。

`evidence`：源码历史 Git bundle、自动测试和对照结果。`docs`：这份可编辑文档、可打印网页版、PDF、GitHub 整理记录。`scripts`：材料生成和校验工具。

## 三代迭代和测量

| 作品 | V1 | V2 | V3及打磨 | 最终验证 |
| --- | --- | --- | --- | --- |
| BriefCheck | 单草稿、首匹配字段；固定用例 6/12 | 冲突原句、可选范围、手动交付、答复计数；12/12 | 项目库、源文重算导入、保留编辑并重置确认、差异与客户 HTML；12/12 | 18 项单元测试通过；浏览器导入导出与移动布局通过 |
| AccessProof | 简单标签和位置编号；固定用例 5/12 | 标签解析、隐藏祖先、按钮名称、重复 ID、iframe、标题层级；12/12 | 稳定证据编号、复核失效与保留、导入重算和差异；固定集 12/12，扩展 18/18 | axe 对照后调整占位符分类，扩展 19/19 |

这是 V1、V2、V3 三代成品以及一次对照后的补丁。新增测试和固定测试分开统计。小型手写测试集不能推出真实用户准确率，未虚构用户反馈、市场数据或比赛成绩。原始提交、版本标签和完整可恢复历史见 [版本来源](PROVENANCE.md)。

## 同类软件差距和改进依据

| 对照对象 | 已核实的强项 | 本作品差距 | 已落地的改进 |
| --- | --- | --- | --- |
| Bonsai、Plutio、Proposify | 文档描述了结构化提案、可复用服务、项目流程、客户预览等能力 | BriefCheck 无签名、付款、CRM 或多人协作；规则不能理解全部语义 | 增加可编辑范围、本机项目库、修订比较和独立客户预览 |
| axe-core | 实際浏览器无障碍规则引擎，覆盖更广 | AccessProof 只检查源码子集，无计算样式、完整名称算法或运行时分析 | 在十个限定测试页面真实对照；占位符字段从障碍改成持久标签复核提示 |
| Pa11y、WAVE | 文档提供重复测试、CI 或运行页面/人工复核支持 | 没有实时 URL 扫描、CI、键盘自动化或屏幕阅读器研究 | 增加复核记录保留/失效、前后比较和人工检查提示 |

BriefCheck 的商业产品比较基于官方文档，没有登录付费账户试用。[Bonsai](https://help.hellobonsai.com/en/articles/5616844-all-about-proposals)、[Plutio](https://help.plutio.com/help/proposals-overview)、[Proposify](https://support.proposify.com/hc/en-us/articles/4845167361051-Page-Breakdown-Client-Preview)

AccessProof 的 axe-core 4.13.0 是实际运行比较；限定七个重叠规则、十个合成页面，障碍分类一致性由 9/10 到 10/10。这不代表总体覆盖与 axe 等同。Pa11y 与 WAVE 只查官方文档。[axe-core](https://github.com/dequelabs/axe-core)、[Pa11y](https://pa11y.org/)、[WAVE](https://wave.webaim.org/)

## 尚存不足

BriefCheck 的复杂句和文本日期仍可能误判，改过源文后被移除的自动交付项可能重新出现。本机存储没有跨设备同步，未测大型项目库的键入延迟，也未进行真实客户访谈。勾选确认不等于电子签名。

AccessProof 无法判断计算对比度、CSS 类隐藏、动态交互、Shadow DOM 和完整可访问名称；重复的相同元素可能移动复核身份。问题消失仅说明本次源码规则未再发现，不等于页面已经无障碍。实际键盘和屏幕阅读器测试仍需补充。

## GitHub 账户整理

新增 [总参赛仓库](https://github.com/fuyoupeng2007/hackathon-lab-2026) 和 [个人主页作品入口](https://github.com/fuyoupeng2007)。总仓库收录子目录源码、比赛材料、演示与完整历史；独立 BriefCheck、AccessProof 仓库保留原始版本。为本次作品设置明确简介、首页和主题标签，通过 Release 提供整包下载。现有其他公开作品在主页按工具、研究、游戏与学习记录分类链接；原仓库的名称和可见性保留，私有仓库不收录到公开目录。

## 你醒来后的提交步骤

1. 打开总入口试用两款作品，检查自己的年龄、学生身份和居住地是否符合各场条件。
2. 优先打开 LovHack 的目录，使用英文稿、源码、截图和视频；其他比赛按各自检查清单完成。不要批量将同一个已完成投稿版本冒充新作品。
3. Basics 的视频需你上传公开 YouTube 或 Vimeo 后粘贴链接。本人姓名、邮箱、团队角色和个人学习反思由你如实填写。
4. WarriorHacks 先填 Track Selection Form；ML 先核对较早截止与 AI 口径。若要求运行时模型，当前两款规则工具不满足。
5. 在 Devpost 最终提交后保存回执；本次交付未生成比赛投稿回执、奖项或参赛成绩。

## 筛掉的比赛与原因

- [Next Byte V4](https://next-byte-hacks-v4.devpost.com/rules)：9 月 30 日截止，已过期。
- [FirstCommit](https://firstcommit.devpost.com/rules)：限制 AI 占主要开发部分，不适合本次高度自主生成流程。
- [Amazon](https://amazonappdev2026.devpost.com/) 与 [Nebius x NVIDIA](https://nebiusglobalaihackathon.devpost.com/rules)：强制指定平台或实际云模型/API；现有作品没有这些集成。
- [ImpactHack](https://impacthack26.devpost.com/rules)、[CSC](https://csc-back-to-school.devpost.com/rules)：高中生限制，不能默认本科生符合。
- [Hyperbloom](https://hyperbloom-october.devpost.com/rules)：规则主要为空标题，无法核实必要条款。
- [Galuxium](https://galuxium-nexus-v2-29411.devpost.com/)：更偏生产级商业 SaaS，当前离线 POC 与架构/营收要求差距较大。
- [STEMergent](https://stemergent-hacks.devpost.com/rules)、[Cosmo](https://cosmohacks.devpost.com/rules)：活动尚未开始，不把本次成品假称为未来窗口的新工作。

所有日期和规则判断以 2026-10-02 阅读的官方页面为依据，可能更新。适配判断是基于现有作品与已知条件的推断，最终资格由主办方决定。

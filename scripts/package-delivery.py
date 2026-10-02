"""Build local competition documents and a printable delivery report. No credentials."""
from pathlib import Path
import json, html, shutil

ROOT=Path(__file__).resolve().parents[1]
OWNER='fuyoupeng2007'
REPO=f'https://github.com/{OWNER}/hackathon-lab-2026'
SITE=f'https://{OWNER}.github.io/hackathon-lab-2026/'
def write(path,text):
    target=ROOT/path
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text('\n'.join(line.rstrip() for line in text.strip().splitlines())+'\n',encoding='utf-8')

events=[
 {'id':'01-build-with-ai-basics','name':'Build With AI: Basics','url':'https://learn-ai-basics.devpost.com/','app':'briefcheck','deadline':'2026-10-27 05:00','eligibility':'达到居住地法定成年年龄；地区及关联方限制见规则','status':'优先；需本人确认资格和个人参与要求','reason':'允许 AI 编程，目标是有规划文档的完整 POC；现有证据链与三代迭代契合。','checks':['确认年龄、居住地和关联方资格','本人阅读并认领产品决策，填写真实学习反思或调查；保留 PROCESS.md 的流程偏离披露','将 BriefCheck-demo.mp4 上传公开 YouTube 或 Vimeo，填写真实视频 URL','提供公开代码、MIT License、devpost/scope.md、prd.md、spec.md；使用英文提交材料'],'theme':'An intentional proof of concept: make an informal freelance brief traceable, editable and portable.','focus':'The core loop is complete without API credentials: brief, source evidence, editable acceptance, clarification, revision and export. The repository includes curriculum-shaped planning documents and a transparent process disclosure.'},
 {'id':'02-lovhack-season-3','name':'LovHack Season 3','url':'https://lovhack-season-3.devpost.com/','app':'briefcheck','deadline':'2026-10-05 11:45','eligibility':'13 至 24 岁的学生；个人或最多 4 人','status':'近期优先；资格待本人确认','reason':'开放主题，明确允许 AI 辅助；产品主要在 9 月 26 日至 10 月 4 日窗口内构建。','checks':['确认学生身份、年龄及地区资格','确认主要构建时间符合 9 月 26 日至 10 月 4 日；披露已有代码及其他比赛投稿','不要把此前已经完成并投稿的成品原样重复提交','核对 Devpost 表单中的最终必填项；准备代码、在线演示、截图、英文描述和 AI 使用披露'],'theme':'Help student freelancers agree on what “done” means before they commit to a project.','focus':'The product serves a narrow audience: students taking their first small client job. Optional work stays optional, competing source facts remain unresolved, and acceptance is edited before the user confirms it.'},
 {'id':'03-warriorhacks-2','name':'WarriorHacks 2.0','url':'https://warriorhacks-2-0.devpost.com/','app':'accessproof','deadline':'2026-10-14 12:45','eligibility':'全球高中生和本科生；允许个人，推荐最多 4 人','status':'主题匹配；需另填 Track Selection Form','reason':'已公布主题为解决社区等现实问题；社区活动报名页面的无障碍预检具有明确使用场景。','checks':['确认在读高中或本科资格','阅读规则所链接的 Code of Conduct；其中未在本次报告中完整验证的附加条款需本人确认','提交必需 Track Selection Form，选择 Hackathon，填本人真实姓名与邮箱','按表单要求上传作品；说明 AI 辅助和构建时间；不声称真实社区用户验证已完成'],'theme':'Reduce preventable accessibility gaps in community workshop registration pages.','focus':'A community event can exclude people through unnamed controls or missing image descriptions. AccessProof gives volunteer maintainers element evidence and repair patterns, while directing them to rendered-page and human checks.'},
 {'id':'04-hack47-offgrid','name':'HACK47: OFFGRID','url':'https://hack47-offgrid.devpost.com/','app':'briefcheck','deadline':'2026-10-15 12:00','eligibility':'页面标签为成年学生；正文欢迎各类全球创作者；存在口径差异','status':'适合作品方向；时间与资格口径需复核','reason':'无需指定平台或技术栈，允许 AI 编程，强调有明确用户和可继续发展的功能原型。','checks':['复核成年/学生页面标签与更宽泛规则正文；本报告不替组织者裁定','页面写 9 月 15 日至 10 月 15 日，规则正文说正式时间另行公布，提交前核对更新','如实写明 10 月 1 日起的新代码、10 月 2 日两轮扩展和比赛材料；不倒填创建目的','核对 created for OFFGRID 与跨比赛复用要求：若同一版本已在他处完成投稿，先披露并确认需补的新工作'],'theme':'Keep the agreement useful after the meeting ends, without forcing a client into another account.','focus':'BriefCheck offers local project storage, a revision comparison and a single-file client preview. These choices focus on continuation and handover instead of an isolated one-shot generator.'},
 {'id':'05-ml-empowerment-3','name':'ML Empowerment Build Challenge 3.0','url':'https://ml-build-challenge-3.devpost.com/','app':'accessproof','deadline':'保守按 2026-10-06 12:00；页面另写 10-10 14:45','eligibility':'13 岁以上；高中和大学学生，允许 1 至 5 人','status':'条件候选；截止日期与 AI 项目口径待复核','reason':'规则包含技术执行与社会影响，通用 Web 项目符合概述要求；AI 方向有解释风险。','checks':['规则正文写 10 月 5 日 21:00 PDT，页头写 10 月 9 日 23:45 PDT；在较早时间前行动并核对更新','概述要求 using AI，详细要求允许通用 Web/生产力作品；确认 AI-assisted development 是否符合，而非假称运行了模型','如要求实际运行时 AI，此成品不满足该附加要求，改用文档中的其他候选','提交至少一项展示功能或设计的文件，并如实填写学生资格与成员角色'],'theme':'An AI-assisted development project that helps volunteers review accessibility with explicit evidence.','focus':'The application runs deterministic source rules, not a machine-learning model. AI was used in development and evaluation. This distinction must remain visible in the entry; suitability is conditional on the organizer’s interpretation.'}
]
write('competitions/competitions.json',json.dumps(events,ensure_ascii=False,indent=2))

apps={
'briefcheck':{'name':'BriefCheck','tagline':'Agree on the brief. Then deliver.','features':[
'Extract five tracked source fields without inventing missing values; retain competing statements as conflicts.',
'Separate optional outputs, edit deliverable names and criteria, and record clarification separately from source facts.',
'Keep up to 20 local projects; export/import one project as JSON with source reanalysis.',
'Regenerate with retained matching edits and reset confirmation after a source change; inspect one previous revision.',
'Export Markdown and a standalone escaped client HTML preview; use English or Chinese.'],
'demo':['Select English, load the Website sample and build the checklist.','Inspect the missing budget and optional brand video; edit a criterion and confirm it.','Record a budget answer. Add a different source budget and deadline, then regenerate and inspect differences.','Create a second sample project, switch projects, and export/import JSON.','Download the client preview and open it independently.'],
'limits':'This is a transparent rule-based negotiation aid. Complex clauses may be misclassified; textual date differences may trigger conflicts. It has no electronic signatures, payments, cloud collaboration or contractual guarantees. Source edits can restore removed generated items. No real customer study or statistically representative accuracy estimate was conducted.',
'measure':'The same 12 synthetic behavioral cases improved from 6/12 in V1 to 12/12 in V2 and V3. The final unit suite passes 18/18. These are controlled regression results, not a field accuracy rate.'},
'accessproof':{'name':'AccessProof','tagline':'Make access part of done.','features':[
'Parse pasted HTML in an inert template without mounting submitted scripts, images or iframes.',
'Check a small source subset: language, title, image alternatives, names, duplicate IDs, iframe titles, headings and landmarks.',
'Show element evidence, a location path, impact and an adaptable repair pattern.',
'Retain reviews for unchanged evidence, reset changed evidence, and compare added/disappeared findings.',
'Save a local draft, import/export JSON with reanalysis, export Markdown and print; English and Chinese UI.'],
'demo':['Load the broken community workshop page and scan: four potential barriers and two review prompts.','Inspect missing image alt and the separate placeholder-only label review prompt.','Write an evidence note and mark the image finding reviewed.','Add an untitled iframe and scan again: inspect one new finding and retained review.','Export Markdown/JSON, import the report, and inspect the manual keyboard, contrast and screen-reader checklist.'],
'limits':'This source preflight is not a WCAG conformance check. It does not evaluate computed styles or contrast, live interaction, shadow DOM or full accessible-name behavior. Inline-only visibility and static-name logic are limited. Identical duplicate elements can shift review identity. Rendered-page tools and human checks remain necessary. No community-user study was conducted.',
'measure':'The frozen 12-case set improved from 5/12 in V1 to 12/12 in V2 and V3. V3 extended checks passed 18/18, and the competitor-guided polish passed 19/19. A real axe-core 4.13.0 comparison on ten synthetic fixtures agreed on barrier classification in 9/10 before polish and 10/10 after; only seven overlapping rules were considered.'}}

disclosure='AI coding assistance was used extensively for scoping proposals, implementation, debugging, tests, interface copy, competitor research and documentation. The application itself uses deterministic browser-side rules and does not call an AI service. All samples and screenshots use fictional data. Product decisions were proposed by an agent under the account owner’s authorization. No user interview, personal learning experience, customer validation, community deployment or participant survey is invented. The owner must personally understand and present the entry and confirm eligibility before submission.'
for e in events:
    a=apps[e['app']]; folder='competitions/'+e['id']; n=a['name']
    write(folder+'/README.md',f"""# {e['name']} 参赛包

本次建议作品：**{n}**。材料已经生成；未代表你注册或正式提交。当前状态：**{e['status']}**。

比赛：[概述]({e['url']}) · [规则]({e['url']}rules)  
北京时间截止：{e['deadline']}。资料核查日期：2026-10-02。资格：{e['eligibility']}。

选择理由：{e['reason']}

## 直接可用的材料

- [英文投稿文字](submission.en.md)，英文部分可贴到 Devpost 对应字段；姓名、邮箱、学习经历和真实视频 URL 由本人填写。
- [在线作品]({SITE}projects/{e['app']}/) · [完整源码]({REPO}/tree/main/projects/{e['app']})。
- [演示视频](../../media/{n}-demo.mp4) · [截图](../../media/{e['app']}-desktop.png)。
- [独立作品仓库](https://github.com/{OWNER}/{e['app']})，保留原始三代提交历史与版本标签。
- [使用与测试说明](../../projects/{e['app']}/README.md) · [三代迭代](../../projects/{e['app']}/devpost/ITERATIONS.md)。

## 投稿前本人完成的事项

"""+'\n'.join('- [ ] '+x for x in e['checks'])+f"""

五份材料对应两个独立成品，代码复用已明确披露。它们是候选投稿包；跨比赛复用是否许可，由各场规则与组织者决定。不要把同一成品改名后声称是另一款新项目。

{('[Track Selection Form](https://docs.google.com/forms/d/e/1FAIpQLScYxGmIowiwkZsbmJwWhoc5kPi2_gbJAgeGBAuoMiNPPD_kbA/viewform?usp=dialog) · [主题和要求更新](https://warriorhacks-2-0.devpost.com/updates)' if e['app']=='accessproof' and e['id'].startswith('03') else '')}
""")
    write(folder+'/submission.en.md',f"""# {n} for {e['name']}

## Project name

{n}

## Elevator pitch

{e['theme']}

## Problem and target users

{e['focus']}

## What it does

"""+'\n'.join('- '+x for x in a['features'])+f"""

## How it was built

Plain HTML, CSS and JavaScript with no runtime package dependency. The browser stores local work and generates portable files. Node.js is optional for the loopback development server. New application code was authored on 2026-10-01 and 2026-10-02; source history records the real progression. The agent compared official product documentation and used fixed synthetic tests to improve behavior over V1, V2 and V3. The core analysis remains deterministic and inspectable.

## Technical findings and iteration evidence

{a['measure']}

## What is complete and what remains

The source-to-review-to-export core loop works end to end. Browser tests covered export/import, local restoration, revised inputs, narrow viewports and inert user-supplied content. {a['limits']}

## AI and prior-work disclosure

{disclosure}

These five contest packages share two completed applications. Any previous publication or submission must be disclosed to organizers rather than presented as new work. The repository’s PROCESS.md explains curriculum use and where autonomous development departed from the guided learner interview sequence.

## Links and testing instructions

Live application: {SITE}projects/{e['app']}/  
Source and instructions: {REPO}/tree/main/projects/{e['app']}  
Full original history: https://github.com/{OWNER}/{e['app']}  
Downloadable English-captioned demo: {SITE}media/{n}-demo.mp4

No login or credentials are required. Open the demo, then:

"""+'\n'.join(f'{i+1}. {step}' for i,step in enumerate(a['demo']))+"""

## Entrant fields to complete personally

Use your actual team names, roles, age/student/residence eligibility, personal learning reflection if required, and a real public YouTube/Vimeo URL when required. This file does not fabricate those fields. Verify this event’s package checklist before submitting.
""")

rows='\n'.join(f"| [{e['name']}]({e['url']}rules) | {apps[e['app']]['name']} | {e['deadline']} | {e['eligibility']} | {e['status']} |" for e in events)
report=f"""# 黑客松作品交付与提交指南

交付日期：2026-10-02。账户：{OWNER}。按你确认的方案完成两个独立成品、五份比赛专用材料和三代迭代证据，由你最终投稿。

总仓库：[{REPO}]({REPO})。在线入口：[{SITE}]({SITE})。本地总目录：`D:\\chatgpt\\hackathon-lab-2026`。

## 五场比赛与适配条件

推荐以不需硬件、无需强制付费 API、可个人完成、允许或未明令排除 AI 辅助、与现有功能匹配为筛选依据。你的年龄和学生身份尚未验证；本表是条件推荐，不能视为参赛资格证明。四场可以优先核对，ML Empowerment 是需先澄清规则的候选。

| 比赛与官方规则 | 对应作品 | 截止时间 北京时间 | 资格口径 | 当前适配状态 |
| --- | --- | --- | --- | --- |
{rows}

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
"""
write('docs/FINAL-DELIVERY.md',report)

def md_html(text):
    import re
    def inline(s):
        s=html.escape(s)
        s=re.sub(r'`([^`]+)`',r'<code>\1</code>',s)
        s=re.sub(r'\[([^]]+)\]\(([^)]+)\)',r'<a href="\2">\1</a>',s)
        s=re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',s)
        return s
    out=[]; table=[]; items=[]; ordered=[]; para=[]
    def flush():
        if para: out.append('<p>'+inline(' '.join(para))+'</p>');para.clear()
        if items:out.append('<ul>'+''.join('<li>'+inline(x)+'</li>' for x in items)+'</ul>');items.clear()
        if ordered:out.append('<ol>'+''.join('<li>'+inline(x)+'</li>' for x in ordered)+'</ol>');ordered.clear()
        if table:
            rows=[x for x in table if not re.match(r'^\|\s*[-: ]+\|',x)]
            out.append('<table>'+''.join('<tr>'+''.join(('<th>' if i==0 else '<td>')+inline(c.strip())+('</th>' if i==0 else '</td>') for c in row.strip('|').split('|'))+'</tr>' for i,row in enumerate(rows))+'</table>');table.clear()
    for line in text.splitlines():
        if not line.strip():flush()
        elif line.startswith('|'):table.append(line)
        elif line.startswith('#'):flush(); level=len(line)-len(line.lstrip('#'));out.append(f'<h{level}>'+inline(line[level:].strip())+f'</h{level}>')
        elif line.startswith('- '):items.append(line[2:])
        elif re.match(r'^\d+\. ',line):ordered.append(re.sub(r'^\d+\. ','',line))
        else:para.append(line)
    flush();return '\n'.join(out)

css='''body{margin:0;background:#f7f6f1;color:#183c32;font:15px/1.75 "Microsoft YaHei",Arial,sans-serif}main{max-width:1080px;margin:40px auto;padding:48px;background:white}h1{font-size:32px;line-height:1.35;margin:0 0 24px}h2{font-size:22px;border-top:2px solid #dde8df;margin-top:34px;padding-top:15px;break-after:avoid}p,li{color:#293d37}a{color:#236147}table{border-collapse:collapse;width:100%;font-size:12px;line-height:1.6;margin:20px 0}th,td{text-align:left;vertical-align:top;border:1px solid #cddbd2;padding:9px}th{background:#e7efe9}tr{break-inside:avoid}code{font-size:12px;overflow-wrap:anywhere}img{max-width:100%}@media print{body{background:white;font-size:10.5px;line-height:1.55}main{margin:0;padding:0}h1{font-size:25px}h2{font-size:17px;margin-top:20px;padding-top:10px}table{font-size:9px}th,td{padding:6px}a{color:#183c32;overflow-wrap:anywhere}p,ul,ol{orphans:3;widows:3}}'''
body=md_html(report).replace('<h2>GitHub 账户整理</h2>','<h2 class="new-page">GitHub 账户整理</h2>')
css+='@media print{.new-page{break-before:page;border-top:0;padding-top:0;margin-top:0}}'
write('docs/FINAL-DELIVERY.html',f'<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>黑客松作品交付与提交指南</title><style>{css}</style></head><body><main>{body}</main></body></html>')

write('README.md',f'''# Hackathon Lab 2026

Two complete offline applications, three generations of iteration, and five tailored Devpost entry packages. 两款独立成品、三代迭代、五场条件推荐与专用参赛材料。

**[Open the portfolio]({SITE}) · [Read the Chinese delivery guide](docs/FINAL-DELIVERY.md) · [Download the PDF](docs/FINAL-DELIVERY.pdf)**

| Application | Purpose | Run | Evidence |
| --- | --- | --- | --- |
| [BriefCheck](projects/briefcheck) | Traceable client briefs, editable acceptance, local projects and portable handover | [Demo]({SITE}projects/briefcheck/) | 18 unit tests; fixed benchmark 6/12 → 12/12 |
| [AccessProof](projects/accessproof) | Static HTML accessibility preflight with element evidence and human review | [Demo]({SITE}projects/accessproof/) | 19 browser regressions; narrow actual axe comparison |

## Five competition packages

'''+ '\n'.join(f"- [{e['name']}](competitions/{e['id']}) — {apps[e['app']]['name']}; {e['status']}." for e in events)+f'''

Personal eligibility is unverified. ML dates/AI wording and OFFGRID wording need checking; these are candidate packages, not registrations or submitted entries. Runtime logic is deterministic; AI was used during development. Cross-event reuse is disclosed and must comply with each organizer's rules.

## Directory and local run

```text
projects/briefcheck/      complete source, tests and planning
projects/accessproof/     complete source and browser regressions
competitions/01...05.../  tailored English entry copy + Chinese checklist
media/                   English-captioned real demos + screenshots
docs/                    delivery guide, comparison and provenance
evidence/                original Git history bundles + test evidence
scripts/                 document builder and history verification
```

Open either project's index.html directly, or run `node server.cjs` from this root and visit `http://127.0.0.1:4399/`. No installation or API key is required. Run `npm test` in `projects/briefcheck`; open `projects/accessproof/tests.html` in Chromium. Use `node scripts/verify-briefcheck-history.cjs` to reproduce the three-generation fixed benchmark from the included history bundle.

Applications are MIT licensed. No personal profile, credential, .env or unrelated private repository is included. The [original standalone repositories](docs/PROVENANCE.md) preserve continuous commit history; this monorepo packages their verified sources and adds the submission materials. [AI and reuse disclosure](docs/AI-DISCLOSURE.md).
''')
write('docs/AI-DISCLOSURE.md','# AI and shared-work disclosure\n\n'+disclosure+'\n\nFive packages map to two applications. Publication is not registration or submission. Sharing source across events does not establish permission to reuse a completed entry; review each event’s new-work and prior-submission rules.\n\nFor Basics, the official Learn Skill Pack was consulted before implementation, at revision 6984209dd33f12ab8781d8caf0c16a5de2343657. The guided interview/sign-off process was overridden by the owner’s explicit request for autonomous development. The process deviation is preserved and no learner survey is fabricated.')
write('docs/PROVENANCE.md',f'''# Source and iteration provenance

Verified source snapshot copied using `git archive HEAD`, not a filesystem copy of credentials or private drafts.

| Application | Generation | Original commit | Frozen benchmark |
| --- | --- | --- | --- |
| BriefCheck | V1 | f0c13dca045272df7d696a6d48aa0bc0ea5ce35d | 6/12 |
| BriefCheck | V2 | 7a51bf1128903aec7ceec35aa23077437d1ce9b7 | 12/12 |
| BriefCheck | V3 | 10fd0e8f171c963fb46f719be65d8ecb7f9beb93 | 12/12 |
| AccessProof | V1 | 442d379 | 5/12 |
| AccessProof | V2 | 03c306d | 12/12 |
| AccessProof | V3 | fdd92ab | 12/12 + 18/18 expanded |
| AccessProof | V3.0.1 | 38da0376643774e76bfb0ebd5290929bfa0008e7 | 19/19 expanded; narrow axe comparison 10/10 |

Original repositories: [BriefCheck](https://github.com/{OWNER}/briefcheck), [AccessProof](https://github.com/{OWNER}/accessproof).

Recover complete history locally with `git clone evidence/briefcheck-history.bundle .work/briefcheck-history` or the corresponding accessproof bundle. Bundles contain only already-public, owned project history. In the restored BriefCheck repository, `node tests/benchmark.cjs <commit>` runs the current frozen harness against that historic core. The included script automates this without relying on the monorepo's unrelated commit layout.

The AccessProof browser runner is in `projects/accessproof/tests.html`. Historic 12-case and expanded results were measured in Chromium and are documented in its VERIFICATION.md and ITERATIONS.md. axe-core was test-only, not bundled at runtime. [Detailed comparison](../projects/accessproof/devpost/AXE-COMPARISON.md).
''')
for name in ['briefcheck','accessproof']:
    for pic,new in [('v3-desktop.png','desktop.png'),('v3-mobile.png','mobile.png')] if name=='briefcheck' else [('mobile.png','mobile.png')]:
        src=Path(r'D:\chatgpt\黑客松审批_2026-10-01')/name/'qa'/pic
        target=ROOT/'media'/f'{name}-{new}'
        if src.exists() and not target.exists():shutil.copy2(src,target)
print('Generated five competition packages and delivery guide.')

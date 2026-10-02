# Hackathon Lab 2026

Two complete offline applications, three generations of iteration, and five tailored Devpost entry packages. 两款独立成品、三代迭代、五场条件推荐与专用参赛材料。

**[Open the portfolio](https://fuyoupeng2007.github.io/hackathon-lab-2026/) · [Read the Chinese delivery guide](docs/FINAL-DELIVERY.md) · [Download the PDF](docs/FINAL-DELIVERY.pdf)**

| Application | Purpose | Run | Evidence |
| --- | --- | --- | --- |
| [BriefCheck](projects/briefcheck) | Traceable client briefs, editable acceptance, local projects and portable handover | [Demo](https://fuyoupeng2007.github.io/hackathon-lab-2026/projects/briefcheck/) | 18 unit tests; fixed benchmark 6/12 → 12/12 |
| [AccessProof](projects/accessproof) | Static HTML accessibility preflight with element evidence and human review | [Demo](https://fuyoupeng2007.github.io/hackathon-lab-2026/projects/accessproof/) | 19 browser regressions; narrow actual axe comparison |

## Five competition packages

- [Build With AI: Basics](competitions/01-build-with-ai-basics) — BriefCheck; 优先；需本人确认资格和个人参与要求.
- [LovHack Season 3](competitions/02-lovhack-season-3) — BriefCheck; 近期优先；资格待本人确认.
- [WarriorHacks 2.0](competitions/03-warriorhacks-2) — AccessProof; 主题匹配；需另填 Track Selection Form.
- [HACK47: OFFGRID](competitions/04-hack47-offgrid) — BriefCheck; 适合作品方向；时间与资格口径需复核.
- [ML Empowerment Build Challenge 3.0](competitions/05-ml-empowerment-3) — AccessProof; 条件候选；截止日期与 AI 项目口径待复核.

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

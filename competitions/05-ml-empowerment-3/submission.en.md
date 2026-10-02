# AccessProof for ML Empowerment Build Challenge 3.0

## Project name

AccessProof

## Elevator pitch

An AI-assisted development project that helps volunteers review accessibility with explicit evidence.

## Problem and target users

The application runs deterministic source rules, not a machine-learning model. AI was used in development and evaluation. This distinction must remain visible in the entry; suitability is conditional on the organizer’s interpretation.

## What it does

- Parse pasted HTML in an inert template without mounting submitted scripts, images or iframes.
- Check a small source subset: language, title, image alternatives, names, duplicate IDs, iframe titles, headings and landmarks.
- Show element evidence, a location path, impact and an adaptable repair pattern.
- Retain reviews for unchanged evidence, reset changed evidence, and compare added/disappeared findings.
- Save a local draft, import/export JSON with reanalysis, export Markdown and print; English and Chinese UI.

## How it was built

Plain HTML, CSS and JavaScript with no runtime package dependency. The browser stores local work and generates portable files. Node.js is optional for the loopback development server. New application code was authored on 2026-10-01 and 2026-10-02; source history records the real progression. The agent compared official product documentation and used fixed synthetic tests to improve behavior over V1, V2 and V3. The core analysis remains deterministic and inspectable.

## Technical findings and iteration evidence

The frozen 12-case set improved from 5/12 in V1 to 12/12 in V2 and V3. V3 extended checks passed 18/18, and the competitor-guided polish passed 19/19. A real axe-core 4.13.0 comparison on ten synthetic fixtures agreed on barrier classification in 9/10 before polish and 10/10 after; only seven overlapping rules were considered.

## What is complete and what remains

The source-to-review-to-export core loop works end to end. Browser tests covered export/import, local restoration, revised inputs, narrow viewports and inert user-supplied content. This source preflight is not a WCAG conformance check. It does not evaluate computed styles or contrast, live interaction, shadow DOM or full accessible-name behavior. Inline-only visibility and static-name logic are limited. Identical duplicate elements can shift review identity. Rendered-page tools and human checks remain necessary. No community-user study was conducted.

## AI and prior-work disclosure

AI coding assistance was used extensively for scoping proposals, implementation, debugging, tests, interface copy, competitor research and documentation. The application itself uses deterministic browser-side rules and does not call an AI service. All samples and screenshots use fictional data. Product decisions were proposed by an agent under the account owner’s authorization. No user interview, personal learning experience, customer validation, community deployment or participant survey is invented. The owner must personally understand and present the entry and confirm eligibility before submission.

These five contest packages share two completed applications. Any previous publication or submission must be disclosed to organizers rather than presented as new work. The repository’s PROCESS.md explains curriculum use and where autonomous development departed from the guided learner interview sequence.

## Links and testing instructions

Live application: https://fuyoupeng2007.github.io/hackathon-lab-2026/projects/accessproof/
Source and instructions: https://github.com/fuyoupeng2007/hackathon-lab-2026/tree/main/projects/accessproof
Full original history: https://github.com/fuyoupeng2007/accessproof
Downloadable English-captioned demo: https://fuyoupeng2007.github.io/hackathon-lab-2026/media/AccessProof-demo.mp4

No login or credentials are required. Open the demo, then:

1. Load the broken community workshop page and scan: four potential barriers and two review prompts.
2. Inspect missing image alt and the separate placeholder-only label review prompt.
3. Write an evidence note and mark the image finding reviewed.
4. Add an untitled iframe and scan again: inspect one new finding and retained review.
5. Export Markdown/JSON, import the report, and inspect the manual keyboard, contrast and screen-reader checklist.

## Entrant fields to complete personally

Use your actual team names, roles, age/student/residence eligibility, personal learning reflection if required, and a real public YouTube/Vimeo URL when required. This file does not fabricate those fields. Verify this event’s package checklist before submitting.

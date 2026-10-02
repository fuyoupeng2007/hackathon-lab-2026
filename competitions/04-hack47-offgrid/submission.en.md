# BriefCheck for HACK47: OFFGRID

## Project name

BriefCheck

## Elevator pitch

Keep the agreement useful after the meeting ends, without forcing a client into another account.

## Problem and target users

BriefCheck offers local project storage, a revision comparison and a single-file client preview. These choices focus on continuation and handover instead of an isolated one-shot generator.

## What it does

- Extract five tracked source fields without inventing missing values; retain competing statements as conflicts.
- Separate optional outputs, edit deliverable names and criteria, and record clarification separately from source facts.
- Keep up to 20 local projects; export/import one project as JSON with source reanalysis.
- Regenerate with retained matching edits and reset confirmation after a source change; inspect one previous revision.
- Export Markdown and a standalone escaped client HTML preview; use English or Chinese.

## How it was built

Plain HTML, CSS and JavaScript with no runtime package dependency. The browser stores local work and generates portable files. Node.js is optional for the loopback development server. New application code was authored on 2026-10-01 and 2026-10-02; source history records the real progression. The agent compared official product documentation and used fixed synthetic tests to improve behavior over V1, V2 and V3. The core analysis remains deterministic and inspectable.

## Technical findings and iteration evidence

The same 12 synthetic behavioral cases improved from 6/12 in V1 to 12/12 in V2 and V3. The final unit suite passes 18/18. These are controlled regression results, not a field accuracy rate.

## What is complete and what remains

The source-to-review-to-export core loop works end to end. Browser tests covered export/import, local restoration, revised inputs, narrow viewports and inert user-supplied content. This is a transparent rule-based negotiation aid. Complex clauses may be misclassified; textual date differences may trigger conflicts. It has no electronic signatures, payments, cloud collaboration or contractual guarantees. Source edits can restore removed generated items. No real customer study or statistically representative accuracy estimate was conducted.

## AI and prior-work disclosure

AI coding assistance was used extensively for scoping proposals, implementation, debugging, tests, interface copy, competitor research and documentation. The application itself uses deterministic browser-side rules and does not call an AI service. All samples and screenshots use fictional data. Product decisions were proposed by an agent under the account owner’s authorization. No user interview, personal learning experience, customer validation, community deployment or participant survey is invented. The owner must personally understand and present the entry and confirm eligibility before submission.

These five contest packages share two completed applications. Any previous publication or submission must be disclosed to organizers rather than presented as new work. The repository’s PROCESS.md explains curriculum use and where autonomous development departed from the guided learner interview sequence.

## Links and testing instructions

Live application: https://fuyoupeng2007.github.io/hackathon-lab-2026/projects/briefcheck/  
Source and instructions: https://github.com/fuyoupeng2007/hackathon-lab-2026/tree/main/projects/briefcheck  
Full original history: https://github.com/fuyoupeng2007/briefcheck  
Downloadable English-captioned demo: https://fuyoupeng2007.github.io/hackathon-lab-2026/media/BriefCheck-demo.mp4

No login or credentials are required. Open the demo, then:

1. Select English, load the Website sample and build the checklist.
2. Inspect the missing budget and optional brand video; edit a criterion and confirm it.
3. Record a budget answer. Add a different source budget and deadline, then regenerate and inspect differences.
4. Create a second sample project, switch projects, and export/import JSON.
5. Download the client preview and open it independently.

## Entrant fields to complete personally

Use your actual team names, roles, age/student/residence eligibility, personal learning reflection if required, and a real public YouTube/Vimeo URL when required. This file does not fabricate those fields. Verify this event’s package checklist before submitting.

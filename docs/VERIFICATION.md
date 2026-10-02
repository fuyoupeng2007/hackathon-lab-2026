# Delivery verification

2026-10-02. Public source copied from the recorded original commits, then packaged with contest documentation. No application behavior was changed during consolidation.

## Verified locally

- BriefCheck: 18/18 unit tests pass in the consolidated source. [Receipt](../evidence/briefcheck-unit-results.txt).
- BriefCheck: included original history bundle reproduces fixed V1/V2/V3 benchmark results 6/12, 12/12, 12/12. [Receipt](../evidence/briefcheck-history-results.txt).
- AccessProof: consolidated browser regression runner passes 19/19. [Receipt](../evidence/accessproof-regressions.json).
- Portfolio: filters show five total, three BriefCheck and two AccessProof entries. Both applications and the portfolio have document width 390 at viewport width 390. No page JavaScript error observed. [Receipt](../evidence/browser-checks.json).
- Existing original repositories document actual browser JSON/Markdown/HTML downloads, restoration, changed-source behavior and inert source checks. Their earlier fixed sets and new tests remain separate.
- Video: BriefCheck 128.00 seconds; AccessProof 103.64 seconds; each 1600 x 900, 25 fps, H.264. FFmpeg YouTube-format checks: 8 PASS, 2 WARN, 0 FAIL each. Warnings are silent audio and no embedded selectable subtitle stream. Both videos have burned English explanations and separate SRT files; this is not a YouTube upload receipt.
- Final contact sheets were visually inspected: captions readable, no blank recorder tail retained in BriefCheck; mobile segment intentionally occupies the narrow part of a widescreen recording.

## Verified public delivery

GitHub Pages built successfully. A real browser opened the public portfolio, filtered the AccessProof entries, generated the BriefCheck detailed sample, and scanned the AccessProof broken sample (4 barriers, 2 review prompts). No page JavaScript error observed.

The public PDF, both public MP4 files and the competition index all returned HTTP 200 with the expected content types. The PDF contains three pages; all pages were rendered to PNG and visually inspected for readable Chinese text, tables, links and page breaks. GitHub profile README existence was confirmed through the API. [Public browser receipt](../evidence/public-browser-checks.json).

The narrow axe-core comparison was repeated on consolidated source, again producing 10/10 matching barrier classifications; the receipt includes the actual ten source fixtures and selected rules. [Comparison receipt](../evidence/axe-comparison.json).

Individual contest registrations and submissions are intentionally left to the owner as requested; no Devpost submission receipt is claimed. The ML and OFFGRID ambiguities remain documented. GitHub release files are checked after creation against local sizes and SHA-256 digests.

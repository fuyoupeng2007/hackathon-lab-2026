# Source and iteration provenance

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

Original repositories: [BriefCheck](https://github.com/fuyoupeng2007/briefcheck), [AccessProof](https://github.com/fuyoupeng2007/accessproof).

Recover complete history locally with `git clone evidence/briefcheck-history.bundle .work/briefcheck-history` or the corresponding accessproof bundle. Bundles contain only already-public, owned project history. In the restored BriefCheck repository, `node tests/benchmark.cjs <commit>` runs the current frozen harness against that historic core. The included script automates this without relying on the monorepo's unrelated commit layout.

The AccessProof browser runner is in `projects/accessproof/tests.html`. Historic 12-case and expanded results were measured in Chromium and are documented in its VERIFICATION.md and ITERATIONS.md. axe-core was test-only, not bundled at runtime. [Detailed comparison](../projects/accessproof/devpost/AXE-COMPARISON.md).

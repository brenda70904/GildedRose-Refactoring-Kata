---
description: "Refactor safely in small behavior-preserving steps with mandatory regression checks"
name: "Safe Refactor"
argument-hint: "Target file or symbol and optional goal"
agent: "agent"
---
Refactor the requested code in the smallest safe step possible while preserving behavior.

Inputs:
- Use the chat argument as the target (file, class, function, or short goal).
- If no target is provided, infer the best refactor target from the current editor context.

Required workflow:
1. Read relevant files and tests before editing.
2. Make one small refactor step only (rename for clarity, extract tiny helper, remove duplication, simplify conditionals, or improve structure without changing public behavior).
3. Run the most relevant regression checks for the changed area.
4. If tests fail, fix only issues introduced by the refactor and re-run checks.
5. Report changes with file links and concise rationale.

Project-specific defaults for this workspace:
- Preserve public API names unless explicitly requested: Item, GildedRose, update_quality.
- Prefer behavior verification with approval/regression tests when touching item update logic.
- Useful checks:
  - python tests/test_gilded_rose_approvals.py
  - python -m unittest
  - pytest

Output format:
- Step summary: one sentence describing the exact refactor performed.
- Files changed: list with links and what changed in each file.
- Verification: commands run and pass/fail result.
- Next safest step: one optional follow-up refactor.

Constraints:
- Do not perform broad rewrites.
- Do not change behavior unless explicitly requested.
- Keep edits focused and easy to review.

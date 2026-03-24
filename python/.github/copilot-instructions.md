# Project Guidelines

## Code Style
- Keep changes small and focused; this kata values incremental refactoring.
- Preserve existing public names unless a task explicitly asks for API changes:
  - Item
  - GildedRose
  - update_quality
- Keep item behavior rules explicit and easy to test.

## Architecture
- Core domain logic is in gilded_rose.py.
- Item is the data holder with name, sell_in, and quality.
- GildedRose.update_quality is the single orchestration entry point for daily updates.
- Behavior is currently routed by exact item name matching:
  - Aged Brie
  - Backstage passes to a TAFKAL80ETC concert
  - Sulfuras, Hand of Ragnaros
  - all other names treated as normal items
- texttest_fixture.py is a regression fixture that prints multi-day item states.

## Build and Test
- Create and activate a virtual environment before running commands if needed.
- Install dependencies:
  - pip install -r requirements.txt
- Run tests from this folder:
  - python -m unittest
  - pytest
  - python tests/test_gilded_rose_approvals.py
- Run the text fixture snapshot manually:
  - python texttest_fixture.py 10

## Conventions
- Respect quality bounds for non-legendary items:
  - minimum 0
  - maximum 50
- Sulfuras is legendary and should not change in quality or sell_in in the current rules.
- Post-expiration behavior matters:
  - normal items degrade twice as fast after sell date
  - Aged Brie improves faster after sell date
  - Backstage passes drop to 0 after the concert
- The fixture includes Conjured Mana Cake; treat it as an intentional extension point and do not assume special behavior exists unless implemented by the task.
- tests/test_gilded_rose.py contains a placeholder failing test; do not treat it as a specification of intended behavior.

## References
- Local task and run guidance: README.md
- Cross-language kata context: ../README.md

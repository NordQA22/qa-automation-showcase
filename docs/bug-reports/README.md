# Bug Reports — SauceDemo

Manual exploratory testing was performed on [SauceDemo](https://www.saucedemo.com/) using the `problem_user` account. The bugs below were found and documented according to a standard bug report format.

## Summary

| ID | Title | Severity | Priority |
|----|-------|----------|----------|
| [BUG-001](BUG-001-sorting-not-working.md) | Sorting does not work for problem_user | Major | High |
| [BUG-002](BUG-002-add-to-cart-not-working-for-some-items.md) | "Add to cart" works only for 3 of 6 products | Major | High |
| [BUG-003](BUG-003-last-name-field-overwrites-first-name.md) | Last Name field overwrites First Name | Critical | High |
| [BUG-004](BUG-004-validation-shows-all-fields-required.md) | Validation shows "required" error for all fields | Critical | High |
| [BUG-005](BUG-005-wrong-product-images.md) | All products show the same image | Major | Medium |

## Environment

- **URL:** https://www.saucedemo.com/
- **User:** `problem_user` / `secret_sauce`
- **Browser:** Google Chrome (Windows 11)

## Severity Levels

- **Blocker** — system is unusable
- **Critical** — key feature is broken
- **Major** — important feature does not work correctly
- **Minor** — small issue, low impact
- **Trivial** — cosmetic issue

## Priority Levels

- **High** — must be fixed in the current sprint
- **Medium** — should be fixed soon
- **Low** — can be fixed later
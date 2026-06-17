# Lab 4 — Playwright UI Test Suite (Starter, Page Object Model)

The three Page Object classes are already created with **method stubs**.
Your job: **fill in the method bodies** and **write the tests** — you do not
design the class structure.

## Step 1 — Install (one time)
```bash
pip install -r requirements.txt
playwright install      # downloads the browsers — don't skip this
```

## Step 2 — Complete the method stubs in `pages/`
Each stub has a hint showing the selector to use:
- **LoginPage:** `login(user, pw)`, `get_error()`
- **ProductsPage:** `is_loaded()`, `add_to_cart(name)`, `cart_count()`
- **CartPage:** `open()`, `items()`, `go_to_checkout()`

## Step 3 — Write the 6 required tests in `tests/`
1. valid login → products page
2. wrong password → error shown
3. empty username → error shown
4. add 1 item → cart badge = 1
5. add 2 items → cart badge = 2
6. open cart → correct items listed

**Two rules:** use `page.get_by_role(...)` selectors, and **never** `time.sleep()`.

## Step 4 — Run
```bash
pytest            # headless
pytest --headed   # watch it in a real browser
```

## Step 5 — Submit
**Repo link + a screenshot of all tests passing (headless).**

## Target app
SauceDemo — https://www.saucedemo.com  (login: `standard_user` / `secret_sauce`)

### Troubleshooting
- *"Browser/executable not found"* → run `playwright install`.
- *flaky failures* → remove `time.sleep()`; use role/text selectors, not brittle CSS.

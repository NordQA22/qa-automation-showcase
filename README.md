# QA Automation Showcase

UI automation tests for [SauceDemo](https://www.saucedemo.com/) built with **Python**, **Playwright**, and **pytest**.

## 🛠️ Tech Stack

- Python 3.14
- Playwright 1.62
- pytest 9.1
- Page Object Model
- Locators separated from page logic

## 📁 Project Structure

```
qa-automation-showcase/
├── .github/
│   └── workflows/
│       └── tests.yml          # CI configuration
├── locators/
│   ├── __init__.py
│   ├── login_locators.py      # Login page locators
│   ├── inventory_locators.py  # Inventory page locators
│   ├── cart_locators.py       # Cart page locators
│   └── checkout_locators.py   # Checkout page locators
├── pages/
│   ├── login_page.py          # Login page object
│   ├── inventory_page.py      # Inventory page object
│   ├── cart_page.py           # Cart page object
│   └── checkout_page.py       # Checkout page object
├── tests/
│   ├── test_login.py          # Login tests
│   ├── test_cart.py           # Cart tests
│   └── test_checkout.py       # End-to-end checkout flow
├── .gitignore
├── requirements.txt
├── pytest.ini
└── README.md
```

## ✅ Test Coverage

- **Login:** successful login, locked-out user, wrong password
- **Cart:** add one item, add multiple items
- **Checkout:** full end-to-end flow (login → cart → checkout → order complete)

## 🏗️ Architecture

The project follows **Page Object Model** with a separate **Locators** layer:

- **`locators/`** — all CSS selectors in one place per page. If the UI changes, only locators need updating.
- **`pages/`** — page objects with actions and assertions. No raw selectors inside — only references to locators.
- **`tests/`** — clean, readable tests using page objects.

This separation makes the framework maintainable and easy to scale.

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/NordQA22/qa-automation-showcase.git
   cd qa-automation-showcase
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # Windows
   pip install -r requirements.txt
   playwright install
   ```

3. Run all tests:
   ```bash
   pytest tests/ -v
   ```

4. Run with visible browser:
   ```bash
   pytest tests/ -v --headed
   ```

5. Run only smoke tests:
   ```bash
   pytest tests/ -v -m smoke
   ```

## 📊 Test Report

Generate an HTML report:

```bash
pytest tests/ --html=report.html --self-contained-html
```

---

**Author:** Ivan Taran — QA Engineer
- Telegram: [@Ivan_T_QA](https://t.me/Ivan_T_QA)
- GitHub: [NordQA22](https://github.com/NordQA22)
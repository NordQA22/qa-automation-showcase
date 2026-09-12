# QA Automation Showcase

UI automation tests for [SauceDemo](https://www.saucedemo.com/) built with **Python**, **Playwright**, and **pytest**.

## 🛠️ Tech Stack

- Python 3.14
- Playwright 1.62
- pytest 9.1
- Page Object Model

## 📁 Project Structure

```
qa-automation-showcase/
├── .github/
│   └── workflows/
│       └── tests.yml          # CI configuration
├── tests/
│   ├── test_login.py          # Login tests
│   ├── test_cart.py           # Cart tests
│   └── test_checkout.py       # End-to-end checkout flow
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── .gitignore
├── requirements.txt
├── pytest.ini
└── README.md
```

## ✅ Test Coverage

- **Login:** successful login, locked-out user, wrong password
- **Cart:** add one item, add multiple items
- **Checkout:** full end-to-end flow (login → cart → checkout → order complete)

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

## 📊 Test Report

Generate an HTML report:

```bash
pytest tests/ --html=report.html --self-contained-html
```

---

**Author:** Ivan Taran — QA Engineer
- Telegram: [@Ivan_T_QA](https://t.me/Ivan_T_QA)
- GitHub: [NordQA22](https://github.com/NordQA22)
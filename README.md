# QA Automation Showcase

UI and API automation tests built with **Python**, **Playwright**, **pytest**, and **requests**.

## 🛠️ Tech Stack

- Python 3.14
- Playwright 1.62
- pytest 9.1
- requests 2.34
- Page Object Model
- Locators separated from page logic

## 📋 About the Test Targets

This project demonstrates UI and API testing techniques using two public practice resources:

- **SauceDemo** (UI) — an e-commerce demo site with login, cart, and checkout flows.
- **JSONPlaceholder** (API) — a free REST API for testing HTTP methods (GET, POST, PUT, DELETE).

Both are widely used for QA practice and require no registration or API keys.

## 📁 Project Structure

```
qa-automation-showcase/
├── .github/
│   └── workflows/
│       └── tests.yml              # CI configuration
├── api_clients/
│   ├── __init__.py
│   └── posts_client.py            # API client for JSONPlaceholder
├── locators/
│   ├── __init__.py
│   ├── login_locators.py
│   ├── inventory_locators.py
│   ├── cart_locators.py
│   └── checkout_locators.py
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/
│   ├── api/
│   │   ├── __init__.py
│   │   └── test_posts.py          # API tests (GET, POST, PUT, DELETE)
│   ├── test_login.py              # UI: login tests
│   ├── test_cart.py               # UI: cart tests
│   └── test_checkout.py           # UI: end-to-end checkout flow
├── .gitignore
├── requirements.txt
├── pytest.ini
└── README.md
```

## ✅ Test Coverage

### UI Tests (SauceDemo)
- **Login:** successful login, locked-out user, wrong password
- **Cart:** add one item, add multiple items
- **Checkout:** full end-to-end flow (login → cart → checkout → order complete)

### API Tests (JSONPlaceholder)
- **GET:** retrieve single post, retrieve all posts, status codes (200/404)
- **POST:** create a new post
- **PUT:** update an existing post
- **DELETE:** delete a post
- **Validation:** response structure, required fields, data types

## 🏗️ Architecture

The project follows **Page Object Model** (UI) and **API Client** (API) patterns with a separate **Locators** layer:

- **`locators/`** — all CSS selectors in one place per page. If the UI changes, only locators need updating.
- **`pages/`** — page objects with actions and assertions. No raw selectors inside — only references to locators.
- **`api_clients/`** — API client classes with methods for each HTTP endpoint.
- **`tests/`** — clean, readable tests using page objects and API clients.

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

4. Run only UI tests:
   ```bash
   pytest tests/ -v -m ui
   ```

5. Run only API tests:
   ```bash
   pytest tests/ -v -m api
   ```

6. Run with visible browser:
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
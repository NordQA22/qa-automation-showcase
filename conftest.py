import allure
import pytest

pytest_plugins = [
    "fixtures.auth",
]


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Добавляет скриншот в Allure при падении UI-теста."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            try:
                screenshot = page.screenshot()
                allure.attach(
                    screenshot,
                    name="screenshot-on-failure",
                    attachment_type=allure.attachment_type.PNG,
                )
            except Exception:
                pass

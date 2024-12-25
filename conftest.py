import pytest


#
#
# @pytest.fixture(scope="session")
# def user_credentials(request):
#     return request.param
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )


@pytest.fixture
def browser_instance(playwright, request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)
    page = browser.new_context().new_page()
    yield page  # pause
    browser.close()

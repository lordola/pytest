from playwright.sync_api import Playwright, expect

from utils.apiBase import APIUtils


def test_e2e_web_api(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_context().new_page()

    # Create order -> orderId
    api_utils = APIUtils()
    orderId = api_utils.create_order(playwright)

    # Login
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("kunlyy2k2@yahoo.com")
    page.get_by_placeholder("enter your passsword").fill("Uthman@01012021")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()

    # order History page -> order is present
    row = page.locator("tr").filter(has_text=orderId)
    row.get_by_role("button", name="view").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you")


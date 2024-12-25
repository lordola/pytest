from playwright.sync_api import Page, Playwright, expect

from utils.apiBase import APIUtils


# HOW TO MOCK Request


# -> make api call from browser
# moke request before it reach server

def intersect_request(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=676a713ae2b5443b1f006483")


def test_network1(page: Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intersect_request)
    page.get_by_placeholder("email@example.com").fill("kunlyy2k2@yahoo.com")
    page.get_by_placeholder("enter your passsword").fill("Uthman@01012021")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    message = page.locator(".blink_me").text_content()
    print(message)


def test_session_storage(playwright:Playwright):
    api_utils = APIUtils()
    token = api_utils.get_token(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # script to inject token in session local storage
    page.add_init_script(f"""localStorage.setItem('token','{token}')""")
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text('Your Orders')).to_be_visible()

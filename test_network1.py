from playwright.sync_api import Page, Playwright

# HOW TO MOCK RESPONSE
fakePayloadOrderResponse = {"data": [], "message": "No Orders"}


# -> make api call from browser
# -> api call contact server return back response to browser
# -> browser use response to generate html data
def intersect_response(route):
    route.fulfill(
        json=fakePayloadOrderResponse
    )


def test_network1(page: Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intersect_response)
    page.get_by_placeholder("email@example.com").fill("kunlyy2k2@yahoo.com")
    page.get_by_placeholder("enter your passsword").fill("Uthman@01012021")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    order_text = page.locator(".mt-4").text_content()
    print(order_text)

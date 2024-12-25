from playwright.sync_api import Page, expect

# css - .classname, #id, tagname
def test_UIValidationDynamicScript(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    iphone_product = page.locator("app-card").filter(has_text="iphone X")
    iphone_product.get_by_role("button").click()
    nokia_product = page.locator("app-card").filter(has_text="Nokia Edge")
    nokia_product.get_by_role("button").click()
    samsung_product = page.locator("app-card").filter(has_text="Samsung Note 8")
    samsung_product.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(3)
    expect(page.locator(".btn-danger")).to_have_count(3)
    expect(page.get_by_text("Checkout")).to_be_visible()


# strip() cut spaces at beginning n at end
def test_childWindowHandle(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as newPage_info:
        page.locator("body > div.float-right > a:nth-child(1)").click()
        childpage = newPage_info.value
        text = childpage.locator(".red").text_content()
        print(text.split(" ")[4])



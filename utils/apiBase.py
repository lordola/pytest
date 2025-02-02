from playwright.sync_api import Playwright

payload = {"orders": [{"country": "India", "productOrderedId": "6570d7839fd99c85e8e23047"}]}


class APIUtils:
    def get_token(self, playwright: Playwright):
        username = "kunlyy2k2@yahoo.com"
        password = "Uthman@01012021"
        api_request = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request.post("/api/ecom/auth/login",
                                    data={"userEmail": username, "userPassword": password}, )
        assert response.ok
        print(response.json())
        return response.json()["token"]

    def create_order(self, playwright: Playwright):
        token = self.get_token(playwright)
        api_request = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request.post("/api/ecom/order/create-order",
                                    data=payload,
                                    headers={"Authorization": token,
                                             "Content_Type": "application/json"})
        print(response.json()["orders"][0])
        return response.json()["orders"][0]

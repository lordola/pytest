from playwright.sync_api import Playwright

payload = {"orders": [{"country": "India", "productOrderedId": "6570d7839fd99c85e8e23047"}]}


class APIUtils:
    def get_token(self, playwright: Playwright,user_credentials):
        username = user_credentials["userEmail"]
        password = user_credentials["userPassword"]
        api_request = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request.post("/api/ecom/auth/login",
                                    data={"userEmail": username, "userPassword": password}, )
        assert response.ok
        print(response.json())
        return response.json()["token"]

    def create_order(self, playwright: Playwright, user_credentials):
        token = self.get_token(playwright, user_credentials)
        api_request = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request.post("/api/ecom/order/create-order",
                                    data=payload,
                                    headers={"Authorization": token,
                                             "Content_Type": "application/json"})
        print(response.json()["orders"][0])
        return response.json()["orders"][0]

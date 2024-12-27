import json

import pytest
from playwright.sync_api import Playwright
from pageObjects.login import Login
from utils.apiBaseFramework import APIUtils

with open("data/credentials.json") as file:
    test_data = json.load(file)
    user_credential_list = test_data["user_credentials"]


@pytest.mark.parametrize("user_credentials", user_credential_list)
def test_e2e_web_api(playwright: Playwright, browser_instance, user_credentials):
    username = user_credentials["userEmail"]
    password = user_credentials["userPassword"]

    # Create order -> orderId
    api_utils = APIUtils()
    order_id = api_utils.create_order(playwright, user_credentials)

    # Login
    login_page = Login(browser_instance)
    login_page.navigate()
    dashboard = login_page.login(username, password)

    # Dashboard page
    order_history = dashboard.select_order()
    order_details = order_history.order_history_page(order_id)

    # order History page -> order is present
    order_details.verify_order_details()

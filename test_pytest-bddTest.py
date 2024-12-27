import pytest
from pytest_bdd import given, when, then, parsers, scenarios

from pageObjects.login import Login
from utils.apiBaseFramework import APIUtils

scenarios('features/orderTransaction.feature')


@pytest.fixture
def shared_data():
    return {}


@given(parsers.parse('user place the item order with {username} and {password}'))
def place_item_order(playwright, username, password, shared_data):
    user_credentials = {"userEmail": username, "userPassword": password}
    api_utils = APIUtils()
    order_id = api_utils.create_order(playwright, user_credentials)
    shared_data['order_id'] = order_id


@given('the user is on landing page')
def landing_page(browser_instance, shared_data):
    login_page = Login(browser_instance)
    login_page.navigate()
    shared_data['login_page'] = login_page


@when(parsers.parse('user login to portal with {username} and {password}'))
def login_to_portal(username, password, shared_data):
    login_page = shared_data['login_page']
    dashboard = login_page.login(username, password)
    shared_data['dashboard_page'] = dashboard


@when('user navigate to orders page')
def navigate_to_orders_page(shared_data):
    dashboard = shared_data['dashboard_page']
    order_history = dashboard.select_order()
    shared_data['order_history_page'] = order_history


@when('user select the orderId')
def select_order_id(shared_data):
    order_history = shared_data['order_history_page']
    order_id = shared_data['order_id']
    order_details = order_history.order_history_page(order_id)
    shared_data['order_details_page'] = order_details


@then('order message is successfully displayed')
def order_message_is_successfully_displayed(shared_data):
    order_details = shared_data['order_details_page']
    order_details.verify_order_details()

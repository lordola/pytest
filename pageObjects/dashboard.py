from pageObjects.orderHistory import OrderHistoryPage


class Dashboard:
    def __init__(self, page):
        self.page = page

    def select_order(self):
        self.page.get_by_role("button", name="ORDERS").click()
        order_history = OrderHistoryPage(self.page)
        return order_history

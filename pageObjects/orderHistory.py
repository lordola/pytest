from pageObjects.orderDetails import OrderDetails


class OrderHistoryPage:
    def __init__(self, page):
        self.page = page

    def order_history_page(self, orderId):
        row = self.page.locator("tr").filter(has_text=orderId)
        row.get_by_role("button", name="view").click()
        orderDetails = OrderDetails(self.page)
        return orderDetails

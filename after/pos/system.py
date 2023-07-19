import random
import string

from pos.order import Order, OrderStatus
from pos.payment import PaymentProcessor


def generate_id(length: int = 6) -> str:
    """Helper function for generating an id."""
    return "".join(random.choices(string.ascii_uppercase, k=length))


class POSSystem:
    def __init__(self, payment_processor: PaymentProcessor):
        self.payment_processor = payment_processor
        self.orders: dict[str, Order] = {}

    def setup_payment_processor(self) -> None:
        self.payment_processor.connect_to_service()

    def register_order(self, order: Order):
        order.id = generate_id()
        self.orders[order.id] = order

    def find_order(self, order_id: str) -> Order:
        return self.orders[order_id]

    def process_order(self, order: Order) -> None:
        self.payment_processor.process_payment(
            price=order.total_price(), reference_id=order.id
        )
        order.set_status(OrderStatus.PAID)
        print("Shipping order to customer.")

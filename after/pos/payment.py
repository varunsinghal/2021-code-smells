from abc import ABC, abstractmethod

from pos.order import Order


class PaymentServiceConnectionError(Exception):
    """Custom error that is raised when we couldn't
    connect to the payment service."""


class PaymentProcessor(ABC):
    @abstractmethod
    def connect_to_service(self) -> None:
        pass

    @abstractmethod
    def process_payment(self, order: Order) -> None:
        pass


class StripePaymentProcessor(PaymentProcessor):
    def __init__(self, url: str):
        self.connected = False
        self.url = url

    def connect_to_service(self) -> None:
        print(
            "Connecting to payment processing service at "
            f"url {self.url}... done!"
        )
        self.connected = True

    def process_payment(self, order: Order) -> None:
        if not self.connected:
            raise PaymentServiceConnectionError()
        total_price = order.total_price()
        print(
            f"Processing payment of ${(total_price / 100):.2f}, "
            f"reference: {order.id}."
        )

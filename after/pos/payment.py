from abc import ABC, abstractmethod


class PaymentServiceConnectionError(Exception):
    """Custom error that is raised when we couldn't
    connect to the payment service."""


class PaymentProcessor(ABC):
    @abstractmethod
    def connect_to_service(self) -> None:
        pass

    @abstractmethod
    def process_payment(self, price: int, reference_id: int) -> None:
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

    def process_payment(self, price: int, reference_id: int) -> None:
        if not self.connected:
            raise PaymentServiceConnectionError()
        print(
            f"Processing payment of ${(price / 100):.2f}, "
            f"reference: {reference_id}."
        )

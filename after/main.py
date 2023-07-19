from pos.order import Customer, Order
from pos.payment import StripePaymentProcessor
from pos.system import POSSystem


def main() -> None:
    # create the POS system and setup the payment processor
    payment_processor = StripePaymentProcessor("https://api.stripe.com/v2")
    system = POSSystem(payment_processor)
    system.setup_payment_processor()

    # create the order
    customer = Customer(
        12345,
        "Arjan",
        "Sesame street 104",
        "1234",
        "Amsterdam",
        "hi@arjancodes.com",
    )
    order = Order(customer=customer)
    order.create_line_item("Keyboard", 1, 5000)
    order.create_line_item("SSD", 1, 15000)
    order.create_line_item("USB cable", 2, 500)

    # register and process the order
    system.register_order(order)
    system.process_order(order)


if __name__ == "__main__":
    main()

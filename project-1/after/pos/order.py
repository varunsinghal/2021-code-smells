from dataclasses import dataclass, field
from enum import Enum, auto
from typing import List

from pos.customer import Customer

ORDER_ID_LENGTH = 6


class OrderStatus(Enum):
    """Order status"""

    OPEN = auto()
    PAID = auto()
    CANCELLED = auto()
    DELIVERED = auto()
    RETURNED = auto()


@dataclass
class OrderItem:
    item: str
    quantity: int
    price: int


@dataclass
class Order:
    customer: Customer
    items: List[OrderItem] = field(default_factory=list)
    _status: OrderStatus = OrderStatus.OPEN
    id: str = ""

    def create_line_item(self, name: str, quantity: int, price: int) -> None:
        item = OrderItem(name, quantity, price)
        self.items.append(item)

    def set_status(self, status: OrderStatus):
        self._status = status

    def total_price(self) -> int:
        total = 0
        for item in self.items:
            total += item.quantity * item.price
        return total

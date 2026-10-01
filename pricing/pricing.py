"""Price calculation for bookstore orders."""

from dataclasses import dataclass


@dataclass
class LineItem:
    isbn: str
    unit_price: float
    quantity: int


def apply_discount(price: float, percent: float) -> float:
    """Return the price after a percentage discount."""
    if not 0 <= percent <= 100:
        raise ValueError("percent must be between 0 and 100")
    return round(price * (1 - percent / 100), 2)


class PriceCalculator:
    def __init__(self, tax_rate: float):
        self.tax_rate = tax_rate

    def subtotal(self, items: list[LineItem]) -> float:
        return round(sum(i.unit_price * i.quantity for i in items), 2)

    def total(self, items: list[LineItem], discount_percent: float = 0) -> float:
        discounted = apply_discount(self.subtotal(items), discount_percent)
        return round(discounted * (1 + self.tax_rate), 2)

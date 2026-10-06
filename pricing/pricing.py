"""Price calculation for bookstore orders."""

from dataclasses import dataclass


@dataclass
class LineItem:
    isbn: str
    unit_price: float
    quantity: int


TIER_BONUS = {"standard": 0, "member": 5, "partner": 10}


def apply_discount(price: float, percent: float, tier: str = "standard") -> float:
    """Return the price after a percentage discount plus the tier bonus."""
    total_percent = min(percent + TIER_BONUS[tier], 100)
    if not 0 <= total_percent <= 100:
        raise ValueError("percent must be between 0 and 100")
    return round(price * (1 - total_percent / 100), 2)


class PriceCalculator:
    def __init__(self, tax_rate: float):
        self.tax_rate = tax_rate

    def subtotal(self, items: list[LineItem]) -> float:
        return round(sum(i.unit_price * i.quantity for i in items), 2)

    def total(
        self, items: list[LineItem], discount_percent: float = 0, tier: str = "standard"
    ) -> float:
        discounted = apply_discount(self.subtotal(items), discount_percent, tier)
        return round(discounted * (1 + self.tax_rate), 2)

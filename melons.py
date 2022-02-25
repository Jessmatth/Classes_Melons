"""Classes for melon orders."""

class AbstractMelonOrder:
    """An abstract class that other melon orders inherit from."""
    def __init__(self, species, qty, shipped, order_type, tax):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5 
        total = (1 + self.tax) * self.qty * base_price

        if self.species  == "christmas melon":
            base_price = base_price*1.5

        if self.qty < 10 and self.order_type == "international":
            total += 3
        
        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    def __init__(self, species, qty):
        super().__init__(species, qty, False, 'domestic', .08)
       


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty, False, "international", 0.17)
        self.country_code = country_code
 
        

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

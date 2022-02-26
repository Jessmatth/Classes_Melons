"""Classes for melon orders."""
from calendar import weekday
from random import randrange 
from datetime import datetime

class AbstractMelonOrder:
    """An abstract class that other melon orders inherit from."""
    def __init__(self, species, qty, shipped, order_type, tax):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax
        

    def get_base_price(self):
        """Find a random integer between 5-9 and set it as the base price.""" 
        base_price = randrange(5, 9)
        now = datetime.now()
        if now.hour >= 8 and now.hour <= 11 and now.weekday() <= 5: 
            base_price += 4
            
        return base_price

    def get_total(self):
        """Calculate price, including tax."""
        base_price = self.get_base_price()
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

class GovernmentMelonOrder(AbstractMelonOrder):
    """A government melon order that requires inspection."""
    def __init__(self, species, qty, shipped, order_type, tax):
       super().__init__(species, qty, shipped, "government", 0.0)
       self.passed_inspection = False
    
    def marked_inspection(self, passed):
        """Indicates if the melon passed inspection."""
        self.passed_inspection = passed




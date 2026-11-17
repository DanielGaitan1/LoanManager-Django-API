from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

class Loan(models.Model):
    amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.01"))]
    )

    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Loan #{self.id} - ${self.amount}"
    


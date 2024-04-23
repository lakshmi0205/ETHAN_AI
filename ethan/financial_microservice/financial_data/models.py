from django.db import models

# In financial_app/models.py
# from django.db import models

class FinancialData(models.Model):
    ISIN = models.CharField(max_length=20)
    Symbol = models.CharField(max_length=10)
    Date = models.DateField()
    Asset_Class = models.CharField(max_length=50)
    Quantity = models.DecimalField(max_digits=15, decimal_places=2)
    # Market_Price = models.DecimalField(max_digits=10, decimal_places=2)
    Cost_Price = models.DecimalField(max_digits=10, decimal_places=2)
    MarketPrice = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.Symbol} - {self.Date}"


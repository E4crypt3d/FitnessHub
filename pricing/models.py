from django.db import models

# Create your models here.


class Pricing(models.Model):
    times = [
        ('Day', 'Day'),
        ('Week', 'Week'),
        ('Month', 'Month'),
        ('Year', 'Year'),
    ]
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField(default=0)
    discount_price = models.PositiveIntegerField(
        default=None, null=True, blank=True)
    details = models.TextField(max_length=1000)
    membership_time = models.CharField(max_length=12, choices=times)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def discount_percentage(self):
        if self.price > 0 and self.discount_price:
            discount_amount = self.discount_price - self.price
            discount_percentage = (discount_amount / self.discount_price) * 100
            return int(discount_percentage)
        return 0

from django.db import models


# class Crop(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#     hausa_name = models.CharField(max_length=100, blank=True)
#     unit = models.CharField(max_length=50, default="100 kg bag")
#     description = models.TextField(blank=True)

#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ["name"]

#     def __str__(self):
#         return self.name


#         class MarketPrice(models.Model):
#     crop = models.ForeignKey(
#         Crop,
#         on_delete=models.CASCADE,
#         related_name="market_prices"
#     )

#     state = models.CharField(max_length=100)
#     market = models.CharField(max_length=150)

#     price = models.DecimalField(max_digits=12, decimal_places=2)

#     currency = models.CharField(max_length=10, default="NGN")

#     recorded_at = models.DateTimeField(auto_now_add=True)

#     source = models.CharField(
#         max_length=100,
#         blank=True,
#         help_text="Example: FMARD, Local Survey, User Submission"
#     )

#     class Meta:
#         ordering = ["-recorded_at"]

#     def __str__(self):
#         return f"{self.crop.name} - {self.market} ({self.state}) - ₦{self.price}"

from django.db import models


class Car(models.Model):
    "Generated Model"
    f1 = models.BigIntegerField()
    f2 = models.BinaryField()
    f3 = models.BooleanField()
    f4 = models.CharField(max_length=256,)
    f5 = models.DateField(auto_now=False, auto_now_add=False,)
    f6 = models.DateTimeField(auto_now=False, auto_now_add=False,)
    f7 = models.DurationField()
    f9 = models.EmailField(max_length=254,)
    f10 = models.FloatField()
    f11 = models.IntegerField()
    f13 = models.PositiveIntegerField()
    f14 = models.PositiveSmallIntegerField()
    f16 = models.SmallIntegerField()
    f17 = models.TextField()
    f19 = models.URLField()
    f20 = models.UUIDField()
    f22 = models.ForeignKey(
        "home.HomePage", on_delete=models.CASCADE, related_name="car_f22",
    )
    f23 = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="car_f23",
    )
    f8 = models.DecimalField(max_digits=30, decimal_places=10, blank=True, null=True,)
    f18 = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True,)
    f21 = models.ForeignKey(
        "home.CustomText",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="car_f21",
    )
    f15 = models.SlugField(max_length=50, blank=True, null=True,)


# Create your models here.

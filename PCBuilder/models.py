from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=256, verbose_name="Category")

    def __str__(self):
        return self.name


class Price(models.Model):
    amount = models.IntegerField(verbose_name="Amount")

    def __str__(self):
        return str(self.amount)


class Part(models.Model):
    type = models.CharField(max_length=256, verbose_name="Type")
    company = models.CharField(max_length=256, verbose_name="Company")
    selection = models.TextField(verbose_name="Selection")
    price = models.IntegerField(verbose_name="Price")

    def __str__(self):
        return self.company + " " + self.selection


class FinalProduct(models.Model):
    category = models.CharField(max_length=256, verbose_name="Category", default="Gaming")
    cat_price = models.IntegerField(verbose_name="Price")
    # amount = models.ForeignKey(Price, on_delete=models.CASCADE)
    parts = models.ManyToManyField(Part)

    def __str__(self):
        return self.category + " " + str(self.cat_price)

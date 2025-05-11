from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


    @property
    def product_count(self):
        return self.product_set.count()


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField(default=0)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def rating(self):
        stars = [review.stars for review in self.reviews.all() if review.stars is not None]
        if not stars:
            return 0
        else:
            return round(sum(stars) / len(stars), 2)


STARS = (
    (i, '* ' * i) for i in range(1, 6)
)


class Review(models.Model):
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, related_name='reviews')
    stars = models.IntegerField(choices=STARS, default=0)

    def __str__(self):
        return f'{self.product} - {self.text}'
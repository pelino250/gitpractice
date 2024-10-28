from django.db import models

class Bike(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(default='default-slug')
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity_in_stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='bike_images', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = [
            ("can_manage_bike", "Can manage bike"),
        ]

    def __str__(self):
        return self.name

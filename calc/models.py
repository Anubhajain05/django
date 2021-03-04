from django.db import models
from datetime import datetime


class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField('date published', default=datetime.now)
    tutorial_slug = models.CharField(max_length=200, default=1)


    def __str__(self):
        return self.tutorial_title

class add_product(models.Model):

    product_name = models.CharField(max_length=250)
    product_category = models.ForeignKey(Tutorial, on_delete= models.CASCADE)
    product_price = models.FloatField()
    sale_price = models.FloatField()
    product_image = models.ImageField(upload_to = 'products/%Y/%d')
    details = models.TextField()

class TutorialCategory(models.Model):

    tutorial_category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200, default=1)

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.tutorial_category

class TutorialSeries(models.Model):
    tutorial_series = models.CharField(max_length=200)

    tutorial_category = models.ForeignKey(TutorialCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
    series_summary = models.CharField(max_length=200)

    class Meta:
        # otherwise we get "Tutorial Seriess in admin"
        verbose_name_plural = "Series"

    def __str__(self):
        return self.tutorial_series




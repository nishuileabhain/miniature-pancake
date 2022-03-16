from django.db import models

class Speechlength(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Speech(models.Model):
    title = models.CharField(max_length=100)
    Speechlength = models.ForeignKey('Speechlength', null=False, blank=False, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # image_url = models.URLField(max_length=1024, null=True, blank=True)
    # image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
from django.db import models
from django.urls import reverse


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    image = models.ImageField(upload_to='articles/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return f"/product/{self.id}"
        return reverse("blog:article_detail", kwargs={"id": self.id})
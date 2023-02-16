from django.db import models

# Create your models here.

class FlashNews(models.Model):
    flash_news  = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.flash_news
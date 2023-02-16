from django.shortcuts import render
from .models import FlashNews
# Create your views here.

flash_news = FlashNews.objects.all()

context = {
    'flash_news': flash_news
}

def index(request):
    return render(request, 'index.html', context)
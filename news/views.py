from django.shortcuts import render
from .models import New,Category,Comment

def home_page(request):
    latest_new=New.published.order_by('-id').first()
    latest_news=New.published.order_by('-id')[:5]
    sport_news=New.published.filter(category__name="Sport")
    texno_news=New.published.filter(category__name="Texnologiya")

    context={
        "latest_new":latest_new,
        "latest_news":latest_news,
        "sport_news":sport_news,
        "texno_news":texno_news,
    }
    return render(request,"index.html",context)



def contact_page(request):
    return render(request,"contact.html")

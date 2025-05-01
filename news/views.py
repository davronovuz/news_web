from django.shortcuts import render, redirect
from .models import New, Category, Comment, Contact
from .forms import CommentForm



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
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        subject=request.POST.get("subject")
        message=request.POST.get("message")
        contact=Contact(name=name,email=email,subject=subject,message=message)
        contact.save()
        return redirect("kontakt")
    return render(request,"contact.html")


def detail_page(request,slug):
    new=New.published.filter(slug=slug).first()
    all_comments=Comment.objects.filter(new=new,status=True).order_by("-created")
    new.count+=1
    new.save()

    if request.method=="POST":
        if not request.user.is_authenticated:
            return redirect("login")
        else:
            message=request.POST.get("message")
            if message:
                comment=Comment(user=request.user,comment=message,new=new)
                comment.save()
                return redirect("new_detail",slug=slug)
    context={
        "new":new,
        "all_comments":all_comments

    }
    return render(request,"single-page.html",context)



# Mahalliy xabar
def mahalliy_news_page(request):
    mahalliy_news=New.published.filter(category__name="Mahalliy")
    context={
        "news":mahalliy_news
    }
    return render(request,"mahalliy.html",context)
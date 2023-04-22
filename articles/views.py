from django.shortcuts import render
from . import models
from django.contrib.auth.decorators import login_required

def articles_list(request):
    articles = models.Articles.objects.all().order_by('date')
    return render(request , 'articles/articleslist.html' , {'articles': articles})

def articles_detail(request , slug):
    articles = models.Articles.objects.get(slug=slug)
    return render(request , 'articles/articledetail.html' , {'articles': articles})

@login_required(login_url="/accounts/login")
def create_article(request):
    return render(request , 'articles/createarticle.html')




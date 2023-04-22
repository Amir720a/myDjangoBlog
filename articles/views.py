from django.shortcuts import render,redirect
from . import models
from django.contrib.auth.decorators import login_required
from . import forms

def articles_list(request):
    articles = models.Articles.objects.all().order_by('date')
    return render(request , 'articles/articleslist.html' , {'articles': articles})

def articles_detail(request , slug):
    articles = models.Articles.objects.get(slug=slug)
    return render(request , 'articles/articledetail.html' , {'articles': articles})

@login_required(login_url="/accounts/login")
def create_article(request):
    if request.method == "POST":
        form = forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()

    return render(request , 'articles/createarticle.html' , {'form':form})




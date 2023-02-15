from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from . import forms
def article_list(request):
    articles = Article.objects.all().order_by("date")
    return render(request, "app/article_list.html", {'articles':articles})

def show_detail(request, slug):
    article_detail = Article.objects.get(slug=slug)
    a = render(request, "app/detail_view.html", {"article_details":article_detail})
    return a

@login_required(login_url="/accounts/login")
def create_article(request):
    form = forms.Create_article
    if request.method == "POST":
        form = forms.Create_article(request.POST, request.FILES)
        if form.is_valid():
            a = form.save(commit=False)
            a.author = request.user
            a.save()
        return redirect('/')
    
    return render(request, 'app/create.html', {'form':form})

@login_required(login_url="/accounts/login")
def update_article(request, id):
   arty = Article.objects.get(id=id)
   form = forms.Create_article(instance=arty) 
   if request.method == "POST":
        form = forms.Create_article(request.POST, request.FILES,instance=arty )
        if form.is_valid():
            form.save()
            return redirect('/')
   return render(request, 'app/create.html',{'form':form})
    
@login_required(login_url="/accounts/login")
def delete_article(request, id):
   arty = Article.objects.get(id=id)
   if request.method == "POST":
        arty.delete()
        return redirect('/')
   return render(request, 'app/delete.html',{'article':arty})
        
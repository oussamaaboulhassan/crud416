from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#UserCreationForm is responsible for the form of creating a now user 
from django.contrib.auth import login as lg 
from django.contrib.auth import logout as lo

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            lg(request, user)
            return redirect('articles:article_list') 
    else:   
        form = UserCreationForm
    return render(request, "accounts/signup.html", {'form':form})

def login(request):
    if request.method == 'POST':
        login = AuthenticationForm(data=request.POST)
        if login.is_valid():
            user = login.get_user()
            lg(request, user)
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            return redirect('articles:article_list') 
    else:
        login = AuthenticationForm()
    return render(request, 'accounts/login.html', {'login': login})    

def logout(request):
    lo(request)
    return redirect("articles:article_list")    
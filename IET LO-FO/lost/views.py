from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import kunal
from .forms import kunalform, registrationform
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout as user_logout, authenticate
from django.contrib import messages

# Views

def index(request):
    return render(request, 'index.html')

def kunallist(request):
    kunals = kunal.objects.all().order_by('-create')
    return render(request, 'list.html', {'kunals': kunals})

@login_required(login_url='/login/')  # Redirect to login if not logged in
def kunalcreate(request):
    if request.method == "POST":
        form = kunalform(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('list')
    else:
        form = kunalform()
    return render(request, 'form.html', {'form': form})

@login_required(login_url='/login/')  # Redirect to login if not logged in
def edit(request, tweet_id):
    tweet = get_object_or_404(kunal, pk=tweet_id, user=request.user)
    if request.method == "POST":
        form = kunalform(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('list')
    else:
        form = kunalform(instance=tweet)
    return render(request, 'form.html', {'form': form})

@login_required(login_url='/login/')  # Redirect to login if not logged in
def delete(request, tweet_id):
    tweet = get_object_or_404(kunal, pk=tweet_id, user=request.user)
    if request.method == "POST":
        tweet.delete()
        return redirect('list')
    return render(request, 'delete.html', {'tweet': tweet})

def register(request):
    if request.method == "POST":
        form = registrationform(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            
            # Display a success message with the username
            messages.success(request, f"{user.username.upper()}, you are registered and logged in !!!")
            
            return redirect('list')
    else:
        form = registrationform()
    
    return render(request, 'registration/register.html', {'form': form})
def logout(request):
    if request.user.is_anonymous:
        return redirect('list')
    username = request.user.username
    user_logout(request)
    messages.success(request, f"YOU ARE LOGGED OUT, {username.upper()} !!!")
    return redirect('list')

def loginuser(request):
    if request.method == "POST":
        username = request.POST.get("user")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"YOU ARE LOGGED IN AS {user.username.upper()} !!!")
            return redirect("/")
        else:
            return redirect("/login")
    return render(request, "registration/login.html")

def about(request):
    return render (request,"about.html")

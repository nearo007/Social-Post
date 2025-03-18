from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .models import Post
from django.utils import timezone

# Create your views here.
def index(request):
    posts = Post.objects.all()
    posts = list(reversed(posts))

    return render(request, 'index.html', {'posts': posts})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if username and email and password and password2:
            if User.objects.filter(username=username):
                messages.info(request, 'User already used!')
                return redirect('register')
            
            if User.objects.filter(email=email):
                messages.info(request, 'Email already used!')
                return redirect('register')
            
            if password != password2:
                messages.info(request, 'The passwords don\'t match!')
                return redirect('register')
            
            User.objects.create_user(username=username, email=email, password=password)
            messages.info(request, 'User was registred sucessfully!')
            return redirect('login')
        
        else:
            messages.info(request, 'Please fill all the spaces!')
            return redirect('register')
        
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if username and password:
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('index')
            
            else:
                messages.info(request, 'Invalid username or password!')
                return redirect('login')

        else:
            messages.info(request, 'Please fill all the spaces!')
            return redirect('login')
    
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')

@login_required(login_url='login')
def create_post(request):
    if request.method == 'POST':
        author = request.user
        title = request.POST.get('title').strip()
        content = request.POST.get('content').strip()
        date = timezone.now()

        if title and content:
            Post.objects.create(author=author, title=title, content=content, date=date)
            messages.info(request, 'Posted!')
            return redirect('index')

        else:
            messages.info(request, 'Please fill all the spaces!')
            return redirect('create_post')
    
    else:
        return render(request, 'create_post.html')

@login_required(login_url='login')
def user_profile(request):
    return render(request, 'user_profile.html')

@login_required(login_url='login')
def post_page(request, post_id):
    if request.method == 'GET':
        post = Post.objects.filter(id=post_id).first()
        return render(request, 'post_page.html', {'post': post})
    
    else:
        return render(request, 'index.html')
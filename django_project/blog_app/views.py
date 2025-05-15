from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .models import Post, UserProfile
from django.utils import timezone
from django.core.files import File
import os

# Create your views here.
def index(request):
    posts = Post.objects.all()
    posts = list(reversed(posts))

    user_profile = UserProfile.objects.filter(user=request.user.id)

    context = {'posts': posts, 'user_profile': user_profile}

    return render(request, 'index.html', context)

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
            
            user= User.objects.filter(username=username).first()
            profile_picture_path= os.path.join('static', 'assets', 'img', 'user_default_profile.png')
            profile_bio='Hello there! I\'m using this app!'

            with open(profile_picture_path, 'rb') as f:
                profile = UserProfile.objects.create(
                    user=user,
                    profile_bio=profile_bio,
                )
                profile.profile_picture.save('user_default_profile.png', File(f))
            
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
            return redirect('index')

        else:
            messages.info(request, 'Please fill all the spaces!')
            return redirect('create_post')
    
    else:
        return render(request, 'create_post.html')
    
@login_required(login_url='login')
def update_post(request, post_id):
    if request.method == 'POST':
        title = request.POST.get('title').strip()
        content = request.POST.get('content').strip()

        if title and content:
            post = Post.objects.filter(id=post_id).first()
            post.title = title
            post.content = content
            post.edited = True
            post.save()
            return redirect('index')

        else:
            messages.info(request, 'Please fill all the spaces!')
            return redirect('update_post', post_id=post_id)
    else:
        context = {'post_id': post_id, 'post': Post.objects.filter(id=post_id).first()}
        return render(request, 'update_post.html', context)
    
@login_required(login_url='login')
def delete_post(request, post_id):
    if request.method == 'GET':
        post = Post.objects.filter(id=post_id).first()
        if post.author.id == request.user.id:
            post.delete()
            return redirect('index')

        else:
            return redirect('index')
        
    else:
        return redirect('index')

@login_required(login_url='login')
def user_profile(request):
    posts = Post.objects.all().filter(author=request.user)
    post_count = posts.count()
    posts = list(reversed(posts))
    
    context = {'posts': posts, 'post_count': post_count}
    return render(request, 'user_profile.html', context)

@login_required(login_url='login')
def user_page(request, user_id):
    if request.method == 'GET':
        user_found = User.objects.filter(id=user_id).first()

        if user_found == request.user:
            return(redirect('user_profile'))

        posts = Post.objects.filter(author=user_found)
        post_count = posts.count()
        posts = list(reversed(posts))
        
        context = {'user_found': user_found, 'posts': posts, 'post_count': post_count}

        return render(request, 'user_page.html', context)
    
    else:
        return render(request, 'user_page.html', {'user_found': None})

@login_required(login_url='login')
def post_page(request, post_id):
    if request.method == 'GET':
        post = Post.objects.filter(id=post_id).first()
        return render(request, 'post_page.html', {'post': post})
    
    else:
        return render(request, 'index.html')
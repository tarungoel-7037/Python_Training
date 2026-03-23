from django.shortcuts import render,redirect , get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Post


# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']

        Post.objects.create(
            title=title,
            content=content,
            author=request.user
        )
        return redirect('home')

    return render(request, 'create_post.html')

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


@login_required
def update_post(request, id):
    post = Post.objects.get(id=id)

    if post.author != request.user:
        return redirect('home')

    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        return redirect('home')

    return render(request, 'update_post.html', {'post': post})


@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)

    if post.author != request.user:
        return redirect('home')

    if request.method == 'POST':
        post.delete()
        return redirect('home')

    return render(request, 'delete_post.html', {'post': post})
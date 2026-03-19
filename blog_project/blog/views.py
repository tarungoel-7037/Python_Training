from django.shortcuts import render,redirect
from .forms import PostForm
from .models import Post

def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
        else:
            print(form.errors())
    else:
        form = PostForm()
        return render(request,'blog/create_post.html',{'form' : form})
    

def post_list(request):
    posts = Post.objects.all()
    return render(request,'blog/post_list.html',{'posts':posts})


def update_post(request,id):
    post = Post.objects.get(id=id)
    
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/create_post.html', {'form': form})

def delete_post(request,id):
    post = Post.objects.get(id=id)
    
    if request.method == "POST":
        post.delete()
        return redirect('post_list')
    return render(request,"blog/delete_post.html",{'post':post})


from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import PostForm
from .models import Post

# Create your views here.
# def index(request):
#     posts = Post.objects.all()[:20]
#     return render(request,'posts.html',{'posts':posts }) 

def index(request):

    #if the method is post
    form = PostForm(request.POST, request.FILES)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
        #if the form is valid
            form.save()
           #if yes save it and redirect it to home
            return HttpResponseRedirect('/')

        #if no then show error
        else:
            return HttpResponseRedirect(form.errors.as_json())
    posts = Post.objects.all().order_by('-created_at')[:20]
    return render(request,'posts.html',{'posts':posts }) 



def delete(request,post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')
    output = 'Post id is'+ str(post_id)
    return HttpResponse(output)

# Create your views here.
def edit(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())

    return render(request, 'edit.html', {'post':post} )





def LikeView(request, post_id):
    post = Post.objects.get(id=post_id)
    new_value = post.likes +1
    post.likes = new_value
    post.save()
    return HttpResponseRedirect('/')


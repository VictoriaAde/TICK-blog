from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import BlogPost,Profile,Comment_post
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from .forms import ProfileForm, PostForm,CommentForm



def ProfileView(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/") 
    else:
        form = ProfileForm

    return render(request, 'profile.html', {'form':form})


class PostView(ListView):
    model= BlogPost
    form_class= PostForm
    prof=Profile.objects.filter()
    template_name='index.html'
    ordering=["-id"]
    
class PostDetail(DetailView):
    model=BlogPost
    template_name='detail.html'
    
class AddPost(CreateView):
    model=BlogPost
    form_class=PostForm
    template_name='add_post.html'
    #fields="__all__"
    success_url= reverse_lazy('main:home')
    
class UpdatePost(UpdateView):
    model=BlogPost
    template_name= 'updates.html'
    fields=('Title','Body')
    success_url= reverse_lazy('main:home')
    
class DeletePost(DeleteView):
    model=BlogPost
    template_name='delete.html'
    success_url= reverse_lazy('main:home')

class CommentPost(CreateView):
    model=Comment_post
    form_class=CommentForm
    template_name='add_comment.html'
    #fields="__all__"
    success_url= reverse_lazy('/')
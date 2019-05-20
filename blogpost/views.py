from django.shortcuts import render, get_object_or_404
from .models import post
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from .forms import NewBlogPostForm, LoginForm
from django.http import HttpResponseRedirect
# Create your views here.

def Index(request):
    all_posts = post.objects.order_by('-upload_date')
    auth = request.user.is_authenticated
    context = {
        'posts' : all_posts,
        'auth' : auth,
    }
    return render(request, 'blogpost/posts.html', context)

def PostView(request, p_id):
    p = get_object_or_404(post, pk=p_id)
    context = {
        'p' : p,
    }
    return render(request, 'blogpost/single.html', context)

class AddPost(CreateView):
    model = post
    #form_class = NewBlogPostForm
    fields = ['heading', 'upload_date', 'content']
    template_name = 'blogpost/add.html'

class ModifyPost(UpdateView):
    model = post
    fields = {'heading', 'upload_date', 'content'}
    template_name = 'blogpost/modify.html'

class DeletePost(DeleteView):
    model = post
    success_url = reverse_lazy("Index")
    template_name = 'blogpost/delete.html'

def LoginView(request):
    if request.method == 'POST':
        #form = LoginForm(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username = username, password = password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse_lazy("Index"))
            #Index(request)
        else:
            form = LoginForm()
            context = {
                "error_msg" : "Invalid credentials:" + str(user),
                'form': form,
            }
            return render(request, 'blogpost/login.html', context)
    form = LoginForm()
    return render(request, 'blogpost/login.html', {'form': form})

def LogoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy("Index"))
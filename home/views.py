from django.shortcuts import render, redirect
from django.db.models import Q
from blogs.models import Post
from newsletter.models import Subscribe
from .forms import ContactFormForm



def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(Q(title__icontains=query) | Q(overview__icontains=query)).distinct()

    context = {'queryset':queryset}
    return render(request, 'home/search_result.html', context)

def about(request):
    return render(request, 'home/about.html', {})

def contact(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    form = ContactFormForm()
    context = {'form':form}
    return render(request, 'home/contact.html', context)

def index(request):
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:3]

    if request.method == 'POST':
        email = request.POST['email']
        new_subscribe = Subscribe()
        new_subscribe.email = email
        new_subscribe.save()

    context = {'obj_list': featured, 'latest':latest}
    return render(request, 'home/index.html', context)

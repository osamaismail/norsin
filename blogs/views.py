from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from .models import Post
from .forms import PostForm
from accounts.models import Blogger


def get_author(user):
    qs = Blogger.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None




def get_category_count():
    queryset = Post.objects.values('categories__title').annotate(Count('categories__title'))
    return queryset



def blogs(request):
    category_count = get_category_count()
    most_recent = Post.objects.order_by('-timestamp')[:3]
    queryset = Post.objects.all().order_by('-timestamp')
    paginator = Paginator(queryset,4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)


    context = {'obj_all': paginated_queryset,
                'page_request_var':page_request_var,
                'most_recent': most_recent,
                'category_count':category_count
                }
    return render(request, 'blogs/blog.html', context)


def post(request, slug):
    # form = CommentForm(request.POST)
    # if request.method == 'POST':
    #     if form.is_valid():
    #         new_comment = form.save(commit=False)
    #         new_comment.post = post
    #         new_comment.save()
    #         return redirect(reverse('post_detial', kwargs={'id': post.pk}))

    # PostView.objects.get_or_create(user=request.user, post=post)
    post = get_object_or_404(Post, slug=slug)
    category_count = get_category_count()
    most_recent = Post.objects.order_by('-timestamp')[:3]

    context = {'post':post,
                # 'form': form,
                'most_recent': most_recent,
                'category_count':category_count}
    return render(request, 'blogs/post.html', context)

@login_required

def post_create(request):
    title = 'Create an'
    submit = 'Create'
    form = PostForm(request.POST or None, request.FILES or None)
    author = get_author(request.user)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()
            messages.success(request, 'Post has been created')
            return redirect('blogs')
    context = {'title': title,'submit': submit,'form': form}
    return render(request,'blogs/create_post.html', context)

def post_update(request, slug):
    title = 'Update the'
    submit = 'Update'
    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    author = get_author(request.user)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()
            messages.success(request, 'Post Updated')
            return redirect('blogs')
    context = {'title': title,'submit': submit, 'form': form}
    return render(request,'blogs/create_post.html', context)

def post_delete(request, slug):
    p = Post.objects.get(slug=slug)
    p.deleted = True
    p.save()
    messages.success(request, 'Post Deleted')
    return redirect('blogs')

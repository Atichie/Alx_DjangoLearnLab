from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.contrib.auth import views as auth_views
from django.urls import path
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixins
from .models import Post, Comment
from .forms import CommentForm
from django.urls import reverse_lazy
from django.db.models import Q
urlpatterns = [
        path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
        path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name= 'logout'),
]

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
        else:
            form = CustomUserCreationForm()
        return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'blog/profile.html')

def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'Post':
        form = CommentForm(request.Post)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post-detail', pk=post_id)
        else:
            form = CommentForm()
        return render(request, 'blog/comment_form.html', {'form': form})

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    template_name = 'blog/post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def get_success_url(self):
        post_id = self.object.post.id
        return reverse_lazy('post-detail', kwargs={'pk': post_id})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def search_posts(request):
        query = request.Get.get('q')
        results = Post.objects.filter(
                Q(title__icontains=query) | Q(content__icontains=query) | Q(tags_name_icontains=query
        ).distinct()
        return render(request, 'blog/search_results.html', {'results': results})

    def posts_by_tag(request, tag_name):
        posts = Post.objects.filter(tags_name=tag_name)
        return render(request, 'blog/posts_by_tag.html', {'posts': posts, 'tag_name':tag_name})



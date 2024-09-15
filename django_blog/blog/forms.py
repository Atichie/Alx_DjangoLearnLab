from django import forms
from .models import Post, Tag
from .models import Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            form = UserUpdateForm(instance=request.user)
        return render(request, 'blog/edit_profile.html', {'form': form})

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        TagWidget = {
                'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a comment...'}),
        }


class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False)

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import Article

@permissiom_required('app_name.can_edit', raise_exception=True)
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    return render(request, 'edit_article.html', {'article': article})


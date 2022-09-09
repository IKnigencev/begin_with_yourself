from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import User, IdeaModel
from .forms import CreateIdea
from .utils import generate_map


def main(request):
    """Главная страница."""

    return render(request, 'main/index.html')


@login_required
def map(request):
    """Страница с картой."""
    generate_map()

    return render(request, 'main/map.html')


@login_required
def profile(request, user_id):
    """Страница пользователя."""
    user = get_object_or_404(User, id=user_id)
    all_ideas = user.ideas.all()

    paginator = Paginator(all_ideas, 10)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }

    return render(request, 'main/profile.html', context)


def idea_detail(request, idea_id):
    idea = get_object_or_404(IdeaModel, pk=idea_id)

    context = {
        'idea': idea
    }
    return render(request, 'main/idea_detail.html', context)


@login_required
def create_idea(request):
    """Страница создания поста."""

    form = CreateIdea(request.POST or None)

    if form.is_valid():
        form = form.save(commit=False)
        form.author = request.user
        form.save()
        return redirect('main:profile', request.user.id)

    return render(request, 'main/create_idea.html', {'form': form})


@login_required
def idea_edit(request, idea_id):
    post = get_object_or_404(IdeaModel, id=idea_id)
    if request.user != post.author:
        return redirect('posts:post_detail', post_id=idea_id)

    form = CreateIdea(request.POST or None, instance=post)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('main:profile', user_id=request.user.id)

    is_edit = True
    return render(
        request,
        'main/create_idea.html',
        {'is_edit': is_edit, 'form': form})

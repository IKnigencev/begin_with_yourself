from django.shortcuts import render
from django.core.paginator import Paginator

from main.models import IdeaModel


def news(request):
    """Страница последних идей."""
    list_idea = IdeaModel.objects.select_related('author').all()

    paginator = Paginator(list_idea, 10)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj
    }
    return render(request, 'news/news.html', context)

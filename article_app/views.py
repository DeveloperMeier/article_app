from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from article_app.models import Comment

from . import controller as article_ctrl

# Makeshift Cache
first_article = {}
article_choices = []

# Create your views here.
def index(request):
    first_article = article_ctrl.get_first_article()
    article_choices = article_ctrl.get_random_three_articles()
    context = {'top_article': first_article, 'article_choices': article_choices}
    return render(request, 'home.html', context)


def article(request, article_id):
    context = {
        'article': article_ctrl.retrience_article_by_uuid(article_id),
        'stocks': article_ctrl.get_three_stocks(),
        'comments': [comment for comment in Comment.objects.all().filter(article_uuid=article_id)][::-1] # reverse it so it displays newest on top
    }
    return render(request, 'article.html', context)

def add_comment(request, article_id):
    comment_text = request.POST.get('data')
    if comment_text:
        q = Comment(comment_text=comment_text, article_uuid=article_id)
        q.save()
        return HttpResponse(comment_text)


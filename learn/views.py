from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Article


def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year':year, 'article_list':a_list}
    return render(request, 'learn/year-archive.html', context)




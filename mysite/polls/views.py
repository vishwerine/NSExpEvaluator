from django.shortcuts import render

from django.template import loader
from django.http import HttpResponse

from .models import Article

# Create your views here.

def index(request):
	return HttpResponse("hi this is a sample")

def index2(request):
	context = {}
	template = loader.get_template('index2.html')
	return HttpResponse(template.render(context,request))




def article(request):
    article_list = Article.objects.all()
    template = loader.get_template('index.html')
    context = {
        'article_list': article_list,
    }
    return HttpResponse(template.render(context, request))


def getarticle(request,article_id):
	
	
	if article_id != ' ':
		article = Article.objects.filter(id=article_id)[0]
		template = loader.get_template('detail.html')
		context = {
			'article':article,
		}
		return HttpResponse(template.render(context,request))



from django.shortcuts import get_object_or_404, render
from blog.models import Comment,Blog

def index(request):
	hi=3	
	con={'hi':hi}
	return render(request , 'blog/index.html',con)

def data(request):
	title=Blog.objects.order_by("date")
	con={'title':title}
	return render(request,'blog/title.html',con)

def tail(request,ob):
	body=Blog.objects.get(id=ob)
	con={'body':body}
	return render(request,'blog/body.html',con)




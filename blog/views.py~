from django.shortcuts import get_object_or_404, render
from blog.models import Comment,Blog
from django.http import HttpResponseRedirect
from django.http import HttpResponse

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

def form(request):
	if request.method=="POST":
		c=Comment()
		c.name=request.POST["name"]
		c.phone=request.POST["phone"]
		c.email=request.POST["email"]
		c.message=request.POST["message"]
		c.save()
		ht = "<html><body style = 'background-color: #2c3e50 ;color:white;font-size:64px ;text-align:center' >Thank you !!!  <a href='/'>Home</a></body></html>" 
    	return HttpResponse(ht)
	return HttpResponse("Error")






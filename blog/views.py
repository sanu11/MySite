from django.shortcuts import get_object_or_404, render

def index(request):
	hi=3	
	con={'hi': hi }
	return render(request , 'blog/index.html',con)

from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
# Create your views here.
from .forms import PostForm
from . models import Post

def posts_create(request):
	form = PostForm()
	context = {
	    "form" : form,

	}
	return render(request,"post_form.html",context)

def posts_detail(request,id=None):
	instance=get_object_or_404(Post,id=id)
	context = {
	"title":instance.title,
	"instance":instance,
	}
	return render(request,"post_detail.html",context)

def posts_list(request):
	queryset=Post.objects.all()
	context = { 
		"object_list":queryset,
	     "title": "List"
	}
	#return HttpResponse("<h1>List !</h1>")
	# if request.user.is_authenticated(): 
	# 	context = {
	# 			"title": "My user List"
	# 	}

	# else:
	#   context = { 
	#       "title": "List"
	# }


	return render(request,"index.html",context)
	

def posts_update(request):
	return HttpResponse("<h1>Update !</h1>")

def posts_delete(request):
	return HttpResponse("<h1>Delete !</h1>")
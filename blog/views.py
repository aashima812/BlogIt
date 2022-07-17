from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import post
from django.contrib.auth.models import User
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView, 
	UpdateView, 
	DeleteView 
	)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# posts=[
# 	{
# 		'author':'Aashima',
# 		'title':'blog 1',
# 		'content':'blablervijkdnc',
# 		'date_posted':'dec 8,2020'
# 	},
# 	{
# 		'author':'maahi',
# 		'title':'blog 2',
# 		'content':'blablervijkdnc',
# 		'date_posted':'dec 18,2020'
# 	}

# ]

#function view 
def home(request):
	context={
		'posts':post.objects.all()
	}
	return render(request,'blog/home.html',context)

#list view
# inherit from ListView that we imported
class PostListView(ListView):
#model var will tell what model to query to create list
	model= post
	template_name='blog/home.html'
	#var that will loop through each list item for viewing
	context_object_name='posts'
	#- sign means new to old
	ordering=['-date_posted']
	paginate_by=6

# taaki saari posts by that user can be displayed
class UserPostListView(ListView):
#model var will tell what model to query to create list
	model= post
	template_name='blog/user_posts.html'
	#var that will loop through each list item for viewing
	context_object_name='posts'
	#- sign means new to old
	# ordering=['-date_posted']
	#this will be overriden by filter so we add order by
	paginate_by=6

	# the user we will get from usl
	def get_queryset(self):
		#if obj exists then return otherwise 404 erroe
		user= get_object_or_404(User, username= self.kwargs.get('username'))
		return post.objects.filter(author=user).order_by('-date_posted')


#detail view
class PostDetailView(DetailView):
#model var will tell what model to query to create list
	model= post

#delete view
#mixins have o be to the left
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#model var will tell what model to query to create list
	model= post

	def test_func(self):
		post= self.get_object()
		if self.request.user==post.author :
			return True
		return False

	#for redirection
	success_url='/'
	
#update view
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#model var will tell what model to query to create list
	model= post
	fields= ['title','content']

	def form_valid(self,form):
		form.instance.author = self.request.user
		#before submitting the form put author id= current logged in user
		return super().form_valid(form)

	def test_func(self):
		post= self.get_object()
		if self.request.user==post.author :
			return True
		return False


#create view
class PostCreateView(LoginRequiredMixin,CreateView):
#model var will tell what model to query to create list
	model= post
	#fields of the form as this page will be form
	fields= ['title','content']
	#override form valid method

	def form_valid(self,form):
		form.instance.author = self.request.user
		#before submitting the form put author id= current logged in user
		return super().form_valid(form)
		# running form valid function

def about(request):
	return render(request, 'blog/about.html', {'title':'about'})
	# return HttpResponse('<h1> Blog About </h1>')


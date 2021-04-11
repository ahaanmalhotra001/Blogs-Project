from django.shortcuts import render, get_object_or_404
from .models import post
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
class PostListView (ListView):
	model= post				#the model on which we are iterating
	template_name = 'blog/home.html'	#where the app should lool for the template
	context_object_name = 'blogs'		#how we call the object in our html file
	ordering = ['-date_posted']         #how to order the posts
	paginate_by = 3

class UserPostListView (ListView):
	model= post				#the model on which we are iterating
	template_name = 'blog/user_post.html'	#where the app should lool for the template
	context_object_name = 'blogs'		#how we call the object in our html file
	paginate_by = 3

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))	#checking if user exists
		return post.objects.filter(author=user).order_by('-date_posted')		#filtering to get only those posts by current user
	
class PostDetailView (DetailView):
	model= post	

def about (request):
	return render(request, 'blog/about.html')

class PostCreateView(LoginRequiredMixin , CreateView):
	model = post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin , UserPassesTestMixin, UpdateView):
	model = post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin , UserPassesTestMixin, DeleteView):
	model = post
	success_url='/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
# this is so that anyone trying to open profile link has to first login



def register(request):
	if request.method == 'POST':
		form=UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created, {username}! You can now login')
			return redirect('login')
	else:
		form=UserRegisterForm()
	return render(request,'users/register.html',{'form' : form})

#decorator adds functionality to an existing func,it is inbuilt
@login_required
def profile(request):

	#check for validity if valid then save
	#when update
	if request.method == 'POST':
	#instance=request.user= current logged in user
		u_form=UserUpdateForm(request.POST,instance=request.user)
		p_form=ProfileUpdateForm(request.POST,
			request.FILES,
			instance=request.user.profile)
		#request.FILES->for image that will be recieved  y post

		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			#show msg and redirect to profile
			messages.success(request, f'Your profile has been updated')
			return redirect('profile')


	#actual data
	else:
		u_form=UserUpdateForm(instance=request.user)
		p_form=ProfileUpdateForm(instance=request.user.profile)


#keys are variables that we'll access within template
	context={
	'u_form':u_form,
	'p_form':p_form
	}
	return render(request, 'users/profile.html',context)

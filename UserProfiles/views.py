from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from PIL import Image

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        profile_form = ProfileUpdateForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            
            profile.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('profile')
    else:
        form = UserRegisterForm()
        profile_form = ProfileUpdateForm()
    
    context = {'form' : form, 'profile_form' : profile_form}
    return render(request, 'UserProfiles/register.html', context)



@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                request.FILES,
                                instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'UserProfiles/profile.html', context)
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def register(request):
    context = {'title': 'The Linux Blog - Register', 'register': 'active',}
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            
            email = form.cleaned_data.get('email')
            # send_mail(
            #     'Log In Confirmed',
            #     'Hey there you are successfully registerd with our website. Welcome',
            #     settings.EMAIL_HOST_USER,
            #     [email,],
            #     fail_silently=False,
            #     )

            username = form.cleaned_data.get('username')

            messages.success(request,f'Hey! You can login with your credentials.')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form},context)

@login_required
def profile(request):
    template_name = 'users/profile.html'

    context = {'title': 'The Linux Blog - Profile', 'profile': 'active',}

    return render(request, template_name, context)
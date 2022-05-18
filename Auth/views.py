from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMessage
from .Auth import *
from django.conf import settings
# Create your views here.
def Register(request):
        form = RegisterForm()
        if request.method == "POST":
                form = RegisterForm(request.POST)
                if form.is_valid():
                        new_user = form.save()
                        new_user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'])
                        login(request, new_user)
                        emailname = request.POST.get("username")
                        emailid = request.POST.get("email")
                        #print(emailname)
                        template = render_to_string('Auth/Email.html', {'name':emailname})
                        email = EmailMessage(
                                'MGCloud',
                                template,
                                settings.EMAIL_HOST_USER,
                                [emailid],
                                )
                        email.fail_silently=False
                        email.send()
                        if email.send():
                                print("Mail Sent")
                        return redirect('/')
                else:
                        errmsg = "Check Your Credentials"
        return render(request, 'Auth/Signup.html', {"Createform": form})
def SignIn(request):
        if request.method == "POST":
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                        login(request, user)
                        #messages.success(request, 'logged in as ' + username)
                        return redirect('/')
                else:
                        context = {'err': "Your Username or password is incorrect"}
                        return render(request, 'Auth/Signin.html', context)
        return render(request,'Auth/Signin.html')
def logoutuser(request):
        logout(request)
        return HttpResponseRedirect('/SignIn/')
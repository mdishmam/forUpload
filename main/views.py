from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from ckeditor.fields import RichTextFormField
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import UserDB
from django.contrib.auth.models import User
from pyfacebook import GraphAPI
from requests import get
#global veriables

# Create your views here.
def Homepage(response):
    if  response.method == 'POST':
        if 'login' in response.POST:
            return HttpResponseRedirect('/login')
        elif 'register' in response.POST:
            return HttpResponseRedirect('/register')
    else:
        return render(response, 'main/base.html', {})

def Register(response):
    if response.user.is_authenticated:
        return redirect('contentcreation')
    else:
        if response.method == 'POST':
            form = CreateUserForm(response.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(response, 'Account created for ' + username)
                return HttpResponseRedirect('/login')
        else:
            form = CreateUserForm()
        return render(response,'registration/register.html', {'form':form})

@csrf_exempt
def LoginPage(response):
    if response.user.is_authenticated:
        return redirect('contentcreation')

    else:
        if response.method == 'POST':
            username = response.POST.get('username')
            password = response.POST.get('password')
            user = authenticate(response, username = username, password = password)

            if user is not None:
                login(response, user)
                return redirect('contentcreation')
            else:
                messages.info(response,'Username or password incorrect.')
                return render(response, 'registration/Login.html', {})

        return render(response, 'registration/Login.html', {})

def LogoutUser(response):
    logout(response)
    return redirect('loginpage')

@csrf_exempt
@login_required(login_url='loginpage')
def WrittingSpace(response):
    #textEditor = RichTextFormField(blank = True, null = True)
    dsrbd = UserDB()
    dsrbd.user = response.user
    dsrbd.author = response.user
    #print(UserDB.objects.all())
    contentList = []
    for item in UserDB.objects.all():
        if str(item.user) == str(dsrbd.user):
            print('printing..')
            print(item.title)
            print('\tdone.')
            contentList.append(item.title)
    if response.method == 'POST':
        if 'save' in response.POST:
            title = response.POST['title']
            content = response.POST['Content']
            dsrbd.title = title
            dsrbd.content = content
            dsrbd.save()

            contentList.append(title)
            return render(response, 'main/ContentCreation2.html', {'contentlist':contentList, 'post':content})

        elif 'saved_item' in response.POST:
            print('Saved item clicked')
            title = response.POST['saved_item']
            post = UserDB.objects.filter(title=title).values('content')[0]['content']
            return render(response, 'main/ContentCreation2.html', {'contentlist':contentList,'edit_title':title, 'edit_post':post, 'post':post})
    return render(response, 'main/ContentCreation2.html', {'contentlist':contentList})

def testView(response):
    return render(response, 'main/ContentCreation2.html', {})


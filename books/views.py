from django.shortcuts import render
from books.models import book, laber, UserProfile
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

def home(request):
    book_list = []
    for id in range(1, 11):
        book_list.append(book.objects.get(book_id = id))
    return render(request,  'home.html', {'book_list': book_list, 'title': 'book_website',})

def about(request):
    return render(request, 'about.html', {})

def top25(request):
    book_list = []
    for id in range(12, 22):
        book_list.append(book.objects.get(book_id = id))
    return render(request, 'home.html', {'book_list': book_list, 'title': 'book_website',})

def detail(request, book_id):
    try:
        book_detail = book.objects.get(book_id = book_id)
    except book.DoesNotExist:
        raise Http404
    return render(request, 'detail.html', {'title': book_detail.title, 'book_detail': book_detail, 'book_labels': book_detail.label.split()},)

def laber_detail(request, laber_title):
    try:
        laber_de = laber.objects.get(title = laber_title)
    except laber.DoesNotExist:
        raise Http404
    return render(request, 'laber_detail.html')

def register(request):
    context_dict = {}
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            return HttpResponseRedirect('/register/success/')
        else:
            context_dict['user_form_errors'] = user_form.errors
            context_dict['profile_form_errors'] = profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    context_dict['user_form'] = user_form
    context_dict['profile_form'] = profile_form
    return render(request, 'register.html', context_dict)

def register_success(request):
    return render(request, 'register_success.html', {})

def user_login(request):
    context_dict = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                context_dict['disabled_message'] = "此账户已经失活"
        else:
            context_dict['error_message'] = "用户名和密码错误"
    return render(request, 'login.html', context_dict)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def set_account(request, username_slug):
    if request.method == 'POST':
        old_user = User.objects.get(username=username_slug)
        old_user_profile = UserProfile.objects.get(user=old_user)
        new_username = request.POST.get('new_username')
        if new_username:
            old_user.username = new_username
        new_password = request.POST.get('new_password')
        if new_password:
            old_user.set_password(new_password)
        new_email = request.POST.get('new_email')
        if new_email:
            old_user.email = new_email
        old_user_profile.user = old_user
        if 'new_picture' in request.FILES:
            old_user_profile.picture = request.FILES['new_picture']
        old_user.save()
        old_user_profile.save()
        logout(request)
        return HttpResponseRedirect('/account/success/')
    else:
        return render(request, 'account.html', {})

def set_account_success(request):
    return render(request, 'set_account_success.html', {})
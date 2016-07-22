from django.shortcuts import render
from books.models import book, laber
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
    return render(request, 'detail.html', {'title': book_detail.title, 'book_detail': book_detail},)

def laber_detail(request, laber_title):
    try:
        laber_de = laber.objects.get(title = laber_title)
    except laber.DoesNotExist:
        raise Http404
    return render(request, 'laber_detail.html')

def register(request):
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
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request,
                  'register.html',
                  {'user_form': user_form, 'profile_form': profile_form})

def register_success(request):
    return render(request, 'register_success.html', {})

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
        book_list = book.objects.order_by("-score").filter(label__contains = laber_title)
        laber_de = laber.objects.get(title = laber_title)
        size = len(book_list)
    except laber.DoesNotExist:
        raise Http404
    return render(request, 'laber_detail.html', {'book_list': book_list, 'size':size})

def search_book(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        book_list = []
        books = book.objects.all()
        for bk in books:
            if q in bk.author:
                book_list.append(bk)
            elif q in bk.title:
                book_list.append(bk)
            elif q in bk.Isbn:
                book_list.append(bk)
            elif q in bk.content_intro:
                book_list.append(bk)
            elif q in bk.directory:
                book_list.append(bk)
            elif q in bk.label:
                book_list.append(bk)
            elif q in bk.publisher:
                book_list.append(bk)
            elif q in bk.translator:
                book_list.append(bk)
        return render(request, 'search.html', {'book_list': book_list, 'query': q},)
    else:
        return render(request, 'search.html', {'error': True},)

def notes(request, note_book_title):
    return render(request, 'note.html', {'note_book_title':note_book_title},)

def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('book_page', ''):
            errors.append('Enter a book_page.')
        if request.POST.get('book_page') and type(eval(request.POST['book_page'].trim())) != int:
            errors.append('Enter a int number.')
        if not request.POST.get('book_chapter', ''):
            errors.append('Enter a book_chapter.')
        if request.POST.get('book_note', ''):
            errors.append('Enter book notes.')
        if not errors:
            return HttpResponseRedirect('/contact/thanks/')
    return render_to_response('note.html',
        {'errors': errors})

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

def comment(request, book_id):
    try:
        comment_detail = book.objects.get(book_id = book_id)
    except book.DoesNotExist:
        raise Http404
    return render(request, 'comment.html', {'comment_detail': comment_detail})    
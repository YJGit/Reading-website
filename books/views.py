from django.shortcuts import render
from books.models import book, laber, UserProfile, note, Comment
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .forms import UserForm, UserProfileForm, noteForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import datetime
import json

# Create your views here.

def home(request):
    book_list = []
    for id in range(1, 13):
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
    flag = 0
    if 'fname' in request.GET:
        flag = 1
        message1 = request.GET['fname']
    else:
        message1 = ['']
    if 'rev_rating' in request.GET:
        flag = 1
        message2 = request.GET['rev_rating']
    else:
        message2 = ['']
    if 'rev_text' in request.GET:
        flag = 1
        message3 = request.GET['rev_text']
    else:
        message3 = ['']
    if 'user' in request.GET:
        message4 = request.GET['user']
    else:
        message4 = ['']
    if 'bkname' in request.GET:
        message5 = request.GET['bkname']
    else:
        message5 = ['']
    try:
        book_detail = book.objects.get(book_id = book_id)
        nt = note.objects.filter(book_title=book_detail.title)
    except book.DoesNotExist:
        raise Http404

    length = len(nt)
    if length > 3:
        nt = nt[length - 3: ]
    if flag == 1:
        Comment.objects.create(comment_rate = message2, comment_title = message1, comment_content = message3, comment_user = message4, comment_book = message5)
    try:
        comment_list = Comment.objects.filter(comment_book = book_detail.title)
    except:
        comment_list = []
    size = len(comment_list)
    if size > 3:
        comment_list = comment_list[size - 3: ]
    if len(book_detail.score_star) > 4:
        score_star = book_detail.score_star.split()
        five_star = score_star[0]
        four_star = score_star[1]
        there_star = score_star[2]
        two_star = score_star[3]
        one_star = score_star[4]
    else:
        five_star = '0%'
        four_star = '0%'
        there_star = '0%'
        two_star = '0%'
        one_star = '0%'
    return render(request, 'detail.html', {'title': book_detail.title, 'book_detail': book_detail,
                                           'book_labels': book_detail.label.split(), 'notes': nt,
                                           'length': length, 'book_id': book_id, 'five_star': five_star,
                                           'four_star': four_star, 'there_star': there_star,
                                           'two_star': two_star, 'one_star': one_star,})

def laber_detail(request, laber_title):
    try:
        book_list = book.objects.order_by("-score").filter(label__contains = laber_title)
        laber_de = laber.objects.get(title = laber_title)
        size = len(book_list)
    except laber.DoesNotExist:
        raise Http404
    return render(request, 'laber_detail.html', {'book_list': book_list, 'size': size})

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

def laber_search(request, laber_title):
    book_list = []
    books = book.objects.order_by("-score").all()
    for bk in books:
        if laber_title in bk.label:
            book_list.append(bk)
    if len(book_list):
        return render(request, 'search.html', {'book_list': book_list, 'query': laber_title,},)
    else:
        return render(request, 'search.html', {'error': True},)
    
@login_required
def notes(request, note_book_id):
    bk = book.objects.get(book_id = note_book_id)
    params = request.POST if request.method == 'POST' else None
    form = noteForm(params)
    if form.is_valid():
        nt = form.save(commit=False)
        nt.book_title = bk.title
        nt.author = request.user
        nt.page = form.cleaned_data['page']
        nt.chapter = form.cleaned_data['chapter']
        nt.content = form.cleaned_data['content']
        nt.time = "" + datetime.datetime.now().strftime("%Y-%m-%d %H:%I:%S")
        nt.save()

        my_notes = note.objects.filter(book_title=bk.title)
        length = len(my_notes)
        if len(my_notes) > 3:
            my_notes = my_notes[len(my_notes) - 3:]
        return render(request, 'detail.html', {'notes': my_notes, 'title': bk.title,
                                               'book_detail': bk, 'book_labels': bk.label.split(),
                      'length': length, 'book_id': bk.book_id,})
    else:
        form = noteForm()

    return render(request, 'note.html', {'form': form, 'note_book_title': bk.title,})

def note_detail(request, note_book_id):
    bk = book.objects.get(book_id=note_book_id)
    my_notes = note.objects.filter(book_title=bk.title)
    return render(request, 'note_detail.html', {'notes': my_notes,})

def comment_detail(request, book_id):
    book_detail = book.objects.get(book_id = book_id)
    comment_list = Comment.objects.filter(comment_book = book_detail.title)
    return render(request, 'comment_detail.html', {'comment_list': comment_list,})

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

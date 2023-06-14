from django.shortcuts import render, redirect
from .models import Author, Post


def home(request):
    return render(request, 'home.html')


def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author/author_list.html', {'authors':authors})


def author_detail(request, my_id):
        authors = Author.objects.get(id=my_id)
        return render(request, 'author/author_detail.html', {'authors':authors})


def author_update(request, my_id):
    authors = Author.objects.get(id=my_id)
    if request.method == 'POST':
        my_name = request.POST['my_name']
        my_email = request.POST['my_email']
        my_password = request.POST['my_password']
        authors.name = my_name
        authors.email = my_email
        authors.password = my_password
        authors.save()
        return redirect('/') 
    else:
        return render(request, "author/author_update.html", {'authors' : authors})


def post_list(request):
    return render(request, 'post/post_list.html')  


def author_new(request):
    if request.method == 'POST':
        my_name = request.POST['my_name']
        my_email = request.POST['my_email']
        my_password = request.POST['my_password']
            # DB에 INSERT -> SAVE함수
            # DB에 테이블과 SYNC가 맞는 test 클래스에서 객체를 만들어 save
        a1 = Author()
        a1.name = my_name
        a1.email = my_email
        a1.password = my_password
        a1.save()
        return redirect('/') # localhost:8000/
    # return HttpResponse("ok")
    else:
        return render(request, "author/author_new.html") 


 
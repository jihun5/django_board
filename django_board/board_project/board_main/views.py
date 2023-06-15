from django.shortcuts import render, redirect
from .models import Author, Post
from django.http import HttpResponse, HttpResponseNotFound

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


def post_list(request):
    # order_by하고 -컬럼명 이렇게 주면 내림차순 정렬
    posts = Post.objects.filter().order_by('-created_at')
    return render(request, 'post/post_list.html', {'posts':posts}) 


def post_new(request):
    if request.method == 'POST':
        my_title = request.POST['my_title']
        my_contents = request.POST['my_contents']
        my_email = request.POST['my_email']
        p1 = Post()
        if my_email:
            try:
                a1 = Author.objects.get(email = my_email)
                # 장고에서 a1객체에서 id값만 빼서, DB에 저장할때는 author_id에 id값을 저장
                p1.author = a1 #(id: 1, name:"hong", email:"hong@naver,com")
            except Author.DoesNotExist:
                # HttpResopnse는 200정상화면이 나온다
                # HttpResopnseNotFound는 404상태가 나온다
                return HttpResponseNotFound("존재하지 않는 이메일입니다.")
        p1.title = my_titleㄴ
        p1.contents = my_contents
        p1.save()
        return redirect('/') 
    else:
        return render(request, "post/post_new.html") 



def post_detail(request, my_id):
    post = Post.objects.get(id=my_id)
    return render(request, 'post/post_detail.html', {'post':post})



def post_update(request, my_id):
    post = Post.objects.get(id=my_id)
    if request.method == 'POST':
        my_title = request.POST['my_title']
        my_contents = request.POST['my_contents']
        post.title = my_title
        post.contents = my_contents
        post.save()
        return redirect('/') 
    else:
        return render(request, "post/post_update.html", {'post' : post})



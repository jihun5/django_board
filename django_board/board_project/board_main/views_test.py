from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

# get 요청시 html파일 그대로 return
def test_html(request):
    return render(request, "test/test.html")

# get 요청시 html+date return
def test_html_data(request):
    my_name = "hongildong"
    return render(request, "test/test.html", {'name' : my_name})

# get 요청시 html+multy data return
def test_html_multi_data(request):
    data = {
        'name' : 'hongildong',
        'age' : 20
    }
    return render(request, "test/test.html", {'data' : data})

# get요청 시 data만 return
def test_json_data(request):
    data = {
        'name' : 'hongildong',
        'age' : 20
    }
    # render라는 의미는 웹개발에서 화면을 일반적으로 return해줄 때
    # 파이썬의 dict와 유사한 json의 혈태로 변환해서 rethurn  
    return JsonResponse(data)


# 사용자가 get요청으로 쿼리파라미터 방식으로 데이터를 넣어올 때
# 사용자가 get요청으로 데이터를 넣어오는 방식 2가지
# 1. 쿼리파라미터 방식 : localhost:8000/author?id=10&name=hongildong
# 2. pathvariable 방식(좀 더 rest api 규격에 맞는 방식, 좀 더 현대적인 방식) : localhost:8000/author/10
def test_html_parameter_data(request):
    id = request.GET.get('id')
    name = request.GET.get('name')
    print(id)
    print(name)
    return render(request, "test/test.html", {})



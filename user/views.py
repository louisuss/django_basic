from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import User
from .forms import LoginForm

# Create your views here.


def home(request):
    user_id = request.session.get('user')

    if user_id:
        user = User.objects.get(pk=user_id)
        return HttpResponse(user.username)
    return HttpResponse('Home!')


def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/')


def login(request):
<<<<<<< HEAD
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        res_data = {}

        if not (username and password):
            res_data['error'] = '모든 값을 입력해야합니다.'
        else:
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                # 비밀번호 일치
                # 세션 - 딕셔너리 변수 사용
                request.session['user'] = user.id
                # Redirect Code
                return redirect('/')
            else:
                res_data['error'] = '비밀번호가 다릅니다.'

        return render(request, 'login.html', res_data)
=======
    form = LoginForm()
    return render(request, 'login.html', {'form': form})
>>>>>>> develop


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        res_data = {}

        if not (username and password and re_password and email):
            res_data['error'] = '모든 값을 입력해야합니다.'
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            user = User(
                username=username,
                email=email,
                password=make_password(password)
            )

            user.save()

        return render(request, 'register.html', res_data)

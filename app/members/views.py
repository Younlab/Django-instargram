from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


#1 member.urls <- 'members/' 로 include 되도록 config.urls모듈에 추가
#2 path 구현 (URL: '/members/login/')
#3 path 와 이 view 연결
#4 일단 잘 나오는지 확인
#5 잘 나오면 form을 작성 (username, password를 받는 input 2개)
#6 form 작성 후에는 POST 방식 요청을 보내서 이 뷰에서 request.POST 에 요청이 잘 왔는지 확인
#7 일단은 받는 username, password 값을 HttpResponse에 보여주도록 한다.

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # 인증에 성공하면 posts:post-list로 이동
        # 실패하면 다시 members:login으로 이동

        # 받은 username
        user = authenticate(request, username=username, password=password)

        # 인증에 성공한 경우
        if user is not None:

            # 세션값을 만들어 DB에 저장하고, HTTP response의 Cookie에 해당값을 담아보내도록 하는
            # login() 함수를 실행한다.
            login(request, user)
            # 이후 post-list로 redirect
            return redirect('posts:post-list')
        # 인증에 실패한 경우 (username 또는 password가 틀린 경우
        else:
            # 다시 로그인 페이지로 redirect
            return redirect('members:login')
    # GET 요청일 경우
    else:
        # form 이 있는 template를 보여준다.
        return render(request, 'members/login.html')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('posts:post-list')
    else:
        return redirect('posts:post-list')
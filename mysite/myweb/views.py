from django.shortcuts import render

# Create your views here.

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout

@login_required
def secret_page(request):
    return render(request, 'secret_page.html')

# ログアウト用の関数を追加
def logout_view(request):
    logout(request)
    return redirect('login') # ログアウトしたらトップのログイン画面へ
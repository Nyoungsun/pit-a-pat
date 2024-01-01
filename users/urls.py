from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
from . import views

app_name = "users"
urlpatterns = [
    path('login_view', auth_views.LoginView.as_view(template_name='users/login.html'), name='login_view'),  # 로그인 페이지
    path('logout_view', auth_views.LogoutView.as_view(),name='logout_view'),  # 로그아웃 페이지
    path('signup_view', views.signup_view, name='signup_view'),  # 회원가입 페이지
    path('my_page', views.my_page, name='my_page'),  # 마이페이지
    path('update', views.update, name='update'),  # 회원정보수정페이지
    path('change_pwd', views.change_pwd, name='change_pwd'),  # 회원정보수정페이지
    path('withdraw_view', views.withdraw_view, name='withdraw_view'),  # 회원탈퇴페이지
    path('check_id', views.check_id, name="check_id"),  # 아이디 중복 체크
]

from django.urls import path
from apps.users import views

urlpatterns = [
    path("", views.UserListView.as_view(), name="user-list"),  # GET 회원 목록
    path("<int:pk>/", views.UserDetailView.as_view(), name="user-detail"),
    # GET 단일 회원
    path("signup/", views.UserSignupView.as_view(), name="user-signup"),
    # POST 회원가입
    path("login/", views.UserLoginView.as_view(), name="user-login"),
    # POST 로그인
]

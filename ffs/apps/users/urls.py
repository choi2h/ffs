from django.urls import path
from apps.users import views

urlpatterns = [
    # GET 회원 목록
    path("", views.UserListView.as_view(), name="user-list"),
    # GET 단일 회원
    path("<int:pk>/", views.UserDetailView.as_view(), name="user-detail"),
    # POST 회원가입
    path("signup/", views.UserSignupView.as_view(), name="user-signup"),
    # POST 로그인
    path("login/", views.UserLoginView.as_view(), name="user-login"),

    # POST 멤버십 추가
    path("membership/", views.MembershipRegisterView.as_view(), name="membership-register"),
]

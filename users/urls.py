from django.urls import path
from users.views import SignupView
from rest_framework_simplejwt.views import TokenBlacklistView, TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup_view"),
    # 로그인 - access, refresh 토큰 발급
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # 로그아웃 - JS localStorage.clear() or localStorage.removeItem("") 추가 처리 필요
    path("api/token/blacklist/", TokenBlacklistView.as_view(), name="token_blacklist"),
]

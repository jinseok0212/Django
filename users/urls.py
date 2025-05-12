from django.urls import path
from .views import UserRegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserInfoView

urlpatterns = [

    path('register/', UserRegisterView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name = 'token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name = 'token_refresh'),
    path('userinfo/', UserInfoView.as_view(), name = 'user_info'),
]



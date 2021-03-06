from zx_express_management.users.api.views import (
    CustomAuthToken,
    Logout_Delete_Token,
    SignupAccount,
)
from django.urls import path

urlpatterns = [
    path("", CustomAuthToken.as_view(), name="login_token"),
    path("logout/", Logout_Delete_Token.as_view(), name="logout"),
    path("adminsignup/", SignupAccount.as_view(), name="signup"),
]

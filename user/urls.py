from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView


from .views import RegistrationUser, AuthorizationUser, LogOut
from django.urls import path

urlpatterns = [
    path('registration/', RegistrationUser.as_view(), name='registration'),
    path('authorization/', AuthorizationUser.as_view(), name='authorization'),
    path('logout/', LogOut.as_view(), name='logout'),


    path('password-reset/', PasswordResetView.as_view(
        template_name='user/password_reset_form.html'),name='password_reset'),


    path('password-reset/done/',
         PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'), name='password_reset_done'),

    path('password-reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password-reset/complete/',
         PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),
         name='password_reset_complete'),

]

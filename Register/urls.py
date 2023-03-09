from django.urls import path

from Register.views import RegisterView

urlpatterns = [
    path('', RegisterView.as_view(), name='reg'),
]
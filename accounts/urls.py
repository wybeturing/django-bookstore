from django.urls import path
from django.views.generic.detail import SingleObjectMixin 
from .views import SignupPageView

urlpatterns = [
    path('signup/', SignupPageView.as_view(), name='signup'),
]

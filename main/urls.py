from django.urls import path, include

from .views import *

urlpatterns = [
    path('', HomesPageView.as_view(), name="home"),
    path('teachers/', TeachersPageView.as_view(), name="teachers"),
    path('blog/', BlogsPageView.as_view(), name="blog"),
    path('best-pupils/', PupilPageView.as_view(), name="best-pupils"),
    path('post/<int:a>/', PostDetail),
]
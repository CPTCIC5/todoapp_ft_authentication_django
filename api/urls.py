from django.urls import path
from . import views

urlpatterns=[
    path('indexapi/',views.IndexAPI.as_view(),name='indexapi'),
    path('<int:question_id>/detailview/',views.detail_view,name='detailview'),
    path('signup/',views.signup,name='signup')
]
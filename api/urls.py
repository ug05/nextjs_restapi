from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api.views import TaskViewSet, CreateUserView, TastListView, TastRetrieveView, PostListView, PostRetrieveView



router = routers.DefaultRouter()
router.register('tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    path('list-post/', PostListView.as_view(), name='list-post'),
    path('detail-post/<str:pk>/', PostRetrieveView.as_view(), name='detail-post'),
    path('list-task/', TastListView.as_view(), name='list-task'),
    path('detail-task/<str:pk>/', TastRetrieveView.as_view(), name='detail-task'),
    path('register/', CreateUserView.as_view(), name='register'),
    path('auth/', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]
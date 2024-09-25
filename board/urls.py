from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (
    PostList, PostDetail, PostCreate, PostUpdate, PostDelete, ResponsesList, response_handle, subscriptions)


urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('subscriptions/', subscriptions, name='subscriptions'),
    path('responses/', ResponsesList.as_view(), name='responses'),
    path('responses/handle', response_handle, name='response_handle'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
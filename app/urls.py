from django.urls import path, re_path
from .views import article_list, show_detail, create_article, update_article, delete_article
from django.conf.urls.static import static
from django.conf import settings

app_name = "articles"

urlpatterns = [
    path('', article_list, name="article_list"),
    path('create/', create_article , name='create'),
    path('<slug:slug>/', show_detail, name="details"),
    path('update/<int:id>/', update_article, name="update_article"),
    path('delete/<int:id>', delete_article, name="delete_article"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
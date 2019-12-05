from django.conf.urls.static import static
from django.urls import path
from .import views
from django.conf import settings

app_name = 'blog'
urlpatterns =[
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.EntryDetailView.as_view(), name='detail'),
    path('<int:entry_id>/comment', views.comment, name='comment'),
    path('subscribe/', views.MembershipFormView.as_view(), name='subscribe'),
    path('<int:year>/<int:month>/', views.EntryMonthArchiveView.as_view(
        month_format='%m'), name="archive_month_numeric"),
]

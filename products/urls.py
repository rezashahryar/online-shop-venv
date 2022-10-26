from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    # path('', views.ProductListView.as_view(), name='product_list'),
    path('', views.product_list_view, name='product_list'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('comment/<int:product_id>/', views.CommentCreateView.as_view(), name='comment_create'),
]

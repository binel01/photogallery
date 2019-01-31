from django.urls import path
from .views import ImageListView, ImageDetailView, ImageCreateView, \
	ImageUpdateView, ImageDeleteView

urlpatterns = [
	path('', ImageListView.as_view(), name='image-list'), # Will serve as homepage
	path('<int:pk>', ImageDetailView.as_view(), name='image-detail'),
	path('create', ImageCreateView.as_view(), name='image-create'),
    path('update/<int:pk>', ImageUpdateView.as_view(), name='image-update'),
	path('delete/<int:pk>', ImageDeleteView.as_view(), name='image-delete'),
]
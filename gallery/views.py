from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, \
	 UpdateView, DeleteView
from .models import Image

class ImageListView(ListView):
	model = Image
	template_name = 'gallery/image_list.html'
	
class ImageDetailView(DetailView):
	model = Image
	template_name = 'gallery/image_detail.html'

class ImageCreateView(CreateView):
	model = Image
	template_name = 'gallery/image_create.html'
	fields = '__all__'

class ImageUpdateView(UpdateView):
	model = Image
	template_name = 'gallery/image_update.html'
	fields = '__all__'

class ImageDeleteView(DeleteView):
	model = Image
	template_name = 'gallery/image_delete.html'
	success_url = reverse_lazy('image-list')

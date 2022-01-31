from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.index, name='shopindex'),
    path('About', views.About, name='about'),
    path('products/<int:myid>', views.products, name='product'),
    path('tracker', views.tracker, name='tracker'),
    path('contact', views.contact, name='contact'),
]

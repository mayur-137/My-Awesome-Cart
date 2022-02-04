from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.index, name='shopindex'),
    path('About', views.about, name='about'),
    path('products/<int:myId>', views.products, name='product'),
    path('tracker', views.tracker, name='tracker'),
    path('contact', views.contact, name='contact'),
    path('checkout', views.checkout, name='checkout'),
]

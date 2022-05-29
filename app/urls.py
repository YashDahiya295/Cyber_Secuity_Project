from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_page'),
    path('buy/', views.Buy_land.as_view(), name='buyland'),
    path('sell/', views.Sell_land.as_view(), name='Sell_land')
    # path('pdfdown/', views.PDF_of.as_view(), name='pdf_gen')
]

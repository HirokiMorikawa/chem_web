from django import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("chem_chat", views.chem_chat, name="chem_chat"),
    
]
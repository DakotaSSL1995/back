from django.urls import path
from .views import faq, capsula, faq_nueva, faq_modificar, adminfaq, faq_eliminar

urlpatterns = [
    path('', faq, name="faq"),
    path('capsula/', capsula, name="capsula"),
    path('faq-nueva/', faq_nueva, name="faq_nueva"),
    path('faq-modificar/<id>/', faq_modificar, name="faq_modificar"),
    path('adminfaq/', adminfaq, name="adminfaq"),
    path('faq-eliminar/<id>/', faq_eliminar, name="faq_eliminar"),
]

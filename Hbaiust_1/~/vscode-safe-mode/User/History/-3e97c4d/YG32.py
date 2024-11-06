from .views.fviews import cover_page
from django.urls import path

urlpatterns = [
    path('fbv/', cover_page, name='cover_page'),
    path('cbv/', cover_page.as_view(), name='student-list-cbv'),

]

from .views.fviews import cover_page
from django.urls import path

urlpatterns = [
    path('covers/', cover_page, name='cover_page'),
    path('cbv/', StudentListView.as_view(), name='student-list-cbv'),
    
]
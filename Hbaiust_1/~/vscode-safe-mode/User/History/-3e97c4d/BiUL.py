from .views.fviews import cover_page
from .views.cviews import class_cover
from django.urls import path

urlpatterns = [
    path('fbv/', cover_page, name='cover_page'),
    path('cbv/', class_cover.as_view(), name='student-list-cbv'),

]

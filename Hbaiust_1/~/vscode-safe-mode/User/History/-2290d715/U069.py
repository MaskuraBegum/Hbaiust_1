rom django.shortcuts import render,redirect, get_object_or_404
from app_cover.models import CoverPage
from django.views.generic import ListView

class StudentListView(ListView):
    model = CoverPage
    template_name = 'templates/cover_page.html'
    context_object_name = 'covers'
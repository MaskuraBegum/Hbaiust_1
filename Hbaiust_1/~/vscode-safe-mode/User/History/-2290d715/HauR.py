rom django.shortcuts import render,redirect, get_object_or_404
from app_cover.models import CoverPage

class StudentListView(ListView):
    model = Student
    template_name = 'students/student_list_cbv.html'
    context_object_name = 'students
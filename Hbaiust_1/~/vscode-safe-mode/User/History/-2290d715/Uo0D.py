class StudentListView(ListView):
    model = Student
    template_name = 'students/student_list_cbv.html'
    context_object_name = 'students
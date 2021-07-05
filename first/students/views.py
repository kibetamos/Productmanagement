from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import StudentForm


# Create your views here.

def student_create_view(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = StudentForm()
    context = {
        'form': form
    }
    return render(request, "students/student_create.html", context)


def student_list_view(request):
    query = Student.objects.all()
    context = {
        "object_list": query
    }
    return render(request, "students/student_list.html", context)


def student_detail_view(request, id):
    obj = get_object_or_404(Student, id=id)
    context = {
        "object": obj
    }
    return render(request, "students/student_detail.html", context)


def student_update_view(request, id):
    form = StudentForm(request.POST or none)
    if form.is_valid():
        form.save()
        form = studentform()
        content = {
            'form': form
        }
        return render(request, "students/student_update.html", context)


def student_list_view(request):
    queryset = Student.objects.all()  # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "students/student_list.html", context)

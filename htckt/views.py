from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Student


def student_list(request):
    student = Student.objects.order_by('reg_date')
    return render(request, 'htckt/student_list.html', {'student':student})

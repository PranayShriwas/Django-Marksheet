# markssheet/views.py
from django.shortcuts import render
from .models import Result

def marksheet(request):
    if request.method == 'POST':
        student_name = request.POST.get('student_name', '')
        subject_names = request.POST.getlist('subject_name')
        marks_obtained = request.POST.getlist('marks_obtained')

        for subject, marks in zip(subject_names, marks_obtained):
            Result.objects.create(
                student_id=student_name,
                subject_id=subject,
                marks_obtained=marks
            )

    students = Result.objects.values('student__name').distinct()
    subjects = Result.objects.values('subject__name').distinct()
    results = Result.objects.all()

    return render(request, 'index.html', {'students': students, 'subjects': subjects, 'results': results})

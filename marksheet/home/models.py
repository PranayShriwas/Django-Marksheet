# markssheet/models.py
from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=50)

class Student(models.Model):
    name = models.CharField(max_length=100)

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks_obtained = models.IntegerField()

    def __str__(self):
        return f"{self.student.name} - {self.subject.name}: {self.marks_obtained}"

from django.db import models
from users.models import Student, Teacher


# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    students = models.ManyToManyField(Student, related_name="team_students", null=True, blank=True)
    mentors = models.ManyToManyField(Teacher, related_name="team_mentors", null=True, blank=True)
    spl_code = models.CharField(max_length=8, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Project(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    team = models.ForeignKey(Team, related_name="project", on_delete=models.CASCADE, null=True, blank=True)
    spl_code = models.CharField(max_length=8, null=True, blank=True)

    def __str__(self):
        return str(self.title)


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assign = models.ManyToManyField(Student, related_name="task", null=True, blank=True)
    name = models.CharField(max_length=80)
    status = models.CharField(max_length=7)
    priority = models.CharField(max_length=7)

    def __str__(self):
        return str(self.name)


class Spl(models.Model):
    title = models.CharField(max_length=20, null=True,
                             blank=True)
    description = models.TextField(null=True,
                                   blank=True)
    join_code = models.CharField(max_length=8, null=True,
                                 blank=True)

    def __str__(self):
        return str(self.title)

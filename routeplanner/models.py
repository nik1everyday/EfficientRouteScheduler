from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_manager = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)


class Task(models.Model):
    HIGH = 'high'
    MEDIUM = 'medium'
    LOW = 'low'
    PRIORITY_CHOICES = [
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low'),
    ]

    ASSIGNED = 'assigned'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'
    FAILED = 'failed'
    STATUS_CHOICES = [
        (ASSIGNED, 'Assigned'),
        (IN_PROGRESS, 'In progress'),
        (COMPLETED, 'Completed'),
        (FAILED, 'Failed'),
    ]

    task_type = models.IntegerField()
    name = models.CharField(max_length=255)
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default=MEDIUM)
    expected_duration = models.DurationField()
    condition_1 = models.CharField(max_length=255, blank=True)
    condition_2 = models.CharField(max_length=255, blank=True)
    required_employee_level = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ASSIGNED)
    employee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='tasks')
    comments = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.get_priority_display()})"


class Employee(models.Model):
    SENIOR = 'senior'
    MIDDLE = 'middle'
    JUNIOR = 'junior'
    GRADE_CHOICES = [
        (SENIOR, 'Senior'),
        (MIDDLE, 'Middle'),
        (JUNIOR, 'Junior'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location_address = models.CharField(max_length=255)
    grade = models.CharField(max_length=6, choices=GRADE_CHOICES, default=JUNIOR)

    def __str__(self):
        return self.user.get_full_name() or self.user.username

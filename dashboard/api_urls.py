from django.urls import path
from .views import (
    overdue_tasks,
    created_vs_completed,
    completed_per_day,
    completed_per_week,
)

urlpatterns = [
    path('tasks/overdue/', overdue_tasks),
    path('tasks/created-vs-completed/', created_vs_completed),
    path('tasks/completed/day/', completed_per_day),
    path('tasks/completed/week/', completed_per_week),
]

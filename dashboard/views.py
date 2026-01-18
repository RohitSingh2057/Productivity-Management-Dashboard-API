from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils.timezone import now
from datetime import timedelta
from members.models import Task


def login_page(request):
    return render(request, "login.html")

def dashboard_page(request):
    return render(request, "dashboard/dashboard.html")

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def overdue_tasks(request):
    overdue = Task.objects.filter(
        user=request.user,
        status__in=['P', 'I'],
        deadline__lt=now()
    ).count()
    return Response({"overdue": overdue})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def created_vs_completed(request):
    created = Task.objects.filter(user=request.user).count()
    completed = Task.objects.filter(user=request.user, status='C').count()
    return Response({
        "created": created,
        "completed": completed
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def completed_per_day(request):
    data = []
    for i in range(6, -1, -1):
        day = now().date() - timedelta(days=i)
        count = Task.objects.filter(
            user=request.user,
            status='C',
            update_t__date=day
        ).count()
        data.append({"day": str(day), "total": count})
    return Response(data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def completed_per_week(request):
    data = []
    for i in range(7, -1, -1):
        start = now().date() - timedelta(weeks=i+1)
        end = now().date() - timedelta(weeks=i)
        count = Task.objects.filter(
            user=request.user,
            status='C',
            update_t__date__range=[start, end]
        ).count()
        data.append({"week": f"{start} → {end}", "total": count})
    return Response(data)



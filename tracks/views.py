from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from tracks.models import ApplicationRecord


def index(request):

    if not request.user.is_authenticated:
        return render(request, 'accounts/login.html')

    items = ApplicationRecord.objects.all()
    # myFilter = facultyFilter(request.GET, queryset=items)
    # items = myFilter.qs
    context = {
        'items': items,
        # 'header': 'faculty',
        # 'myFilter': myFilter,
    }
    return render(request, 'index.html', context)
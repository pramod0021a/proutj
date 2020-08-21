from django.shortcuts import render, get_object_or_404
from .models import Year, Magazine

# Create your views here.


def list_page(request):
    queryset = Year.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'archives/list.html', context)


def detail_page(request, mag_id):
    qs = get_object_or_404(Year, pk=mag_id)
    context = {
        'object': qs
    }
    return render(request, 'archives/detail.html', context)


def detail(request, mag_id):
    year = get_object_or_404(Year, pk=mag_id)
    return render(request, 'archives/mag-details.html', {'year': year})

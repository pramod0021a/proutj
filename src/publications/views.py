from django.shortcuts import render
from .models import Publication

# Create your views here.


def list_page(request):
    queryset = Publication.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'publications/list.html', context)

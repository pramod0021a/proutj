from django.shortcuts import render, get_object_or_404
from .models import Resource, Item

# Create your views here.


def list_page(request):
    queryset = Resource.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'resources/list.html', context)


def detail_page(request, item_id):
    qs = get_object_or_404(Resource, pk=item_id)
    context = {
        'object': qs
    }
    return render(request, 'resources/detail.html', context)

from django.shortcuts import render, get_object_or_404
from .models import Download, Item


# Create your views here.
def list_page(request):
    queryset = Download.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'downloads/list.html', context)


def detail_page(request, item_id):
    qs = get_object_or_404(Download, pk=item_id)
    context = {
        'object': qs
    }
    return render(request, 'downloads/detail.html', context)

from django.shortcuts import render
from edits.models import Edit, Contact
from django.http import Http404

# Create your views here.


def index(request):
    queryset = Edit.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'edits/index.html', context)


# def about_page(request):
#     return render(request, 'edits/about.html')


def details1(request, id_1):
    qs = Edit.objects.filter(id=id_1)

    context = {
        'object': qs
    }
    return render(request, 'edits/act1.html', context)


def details2(request, id_2):
    qs = Edit.objects.filter(id=id_2)

    context = {
        'object': qs
    }
    return render(request, 'edits/act2.html', context)


def details3(request, id_3):
    qs = Edit.objects.filter(id=id_3)

    context = {
        'object': qs
    }
    return render(request, 'edits/act3.html', context)


def details4(request, id_4):
    qs = Edit.objects.filter(id=id_4)

    context = {
        'object': qs
    }
    return render(request, 'edits/act4.html', context)


def details5(request, id_5):
    qs = Edit.objects.filter(id=id_5)

    context = {
        'object': qs
    }
    return render(request, 'edits/act5.html', context)


def details6(request, id_6):
    qs = Edit.objects.filter(id=id_6)

    context = {
        'object': qs
    }
    return render(request, 'edits/act6.html', context)


def editorial(request, id_edit):
    qs = Edit.objects.filter(id=id_edit)

    context = {
        'object': qs
    }
    return render(request, 'edits/editorial.html', context)


def coverstory(request, id_story):
    qs = Edit.objects.filter(id=id_story)

    context = {
        'object': qs
    }
    return render(request, 'edits/coverstory.html', context)


def contact_page(request):
    thank = False
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')
        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()
        thank = True
    return render(request, 'edits/contact.html', {'thank': thank})

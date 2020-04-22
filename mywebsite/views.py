from django.shortcuts import render

from contact.models import PostModel


def index(request):
    contact_data = PostModel.objects.all()
    context = {
        'Heading': 'Home Form',
        'Contact': contact_data,
    }
    if request.method == 'POST':
        context['nama'] = request.POST['nama']
        context['alamat'] = request.POST['alamat']

    return render(request, 'index.html', context)

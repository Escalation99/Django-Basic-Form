from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

from .forms import ContactForm
from .models import PostModel


def index(request):
    contact_form = ContactForm(request.POST or None)
    error = None

    if request.method == 'POST':

        if contact_form.is_valid():
            PostModel.objects.create(
                nama=contact_form.cleaned_data.get('nama'),
                gender=contact_form.cleaned_data.get('gender'),
                email=contact_form.cleaned_data.get('email'),
                alamat=contact_form.cleaned_data.get('alamat'),
                # agree=request.POST['agree'],
                # tanggal_lahir=request.POST['tanggal_lahir'],
            )
            return HttpResponseRedirect("/")
        else:
            error = contact_form.errors

    context = {
        'Heading': 'Contact Form',
        'contact_form': contact_form,
        'error': error,
    }
    return render(request, 'contact/index.html', context)

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, 'ashish23d@gmail.com', ['milansojitra1019@gmail.com'])
            except BadHeaderError:
                return HttpResponse('please check your data.')
            return HttpResponse('success')
    return render(request, "contact_us.html", {'form': form})
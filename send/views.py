from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.

def index(request):
    send_mail(
        'hello from karan',
        'message by django',
        'deykaran07@gmail.com',
        ['deykaran02@gmail.com'],
        fail_silently=False,
    )
    return render(request,'send/index.html')
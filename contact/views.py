from datetime import datetime

from django.shortcuts import render

def contact(request):
    return render(request, 'contact.html')

from django.shortcuts import render, get_object_or_404




def shopPage(request, *args, **kwargs):
    return render(request, template_name="pages/listing.html")

def demoPage(request, *args, **kwargs):
    return render(request, template_name='pages/demo.html')

def landing(request, *args, **kwargs):
    return render(request, template_name='pages/landing.html')
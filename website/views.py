from django.shortcuts import render

def home_page(request):
    context = {'page_name': 'main', 'description': ' This is home page of my website', }
    return render (request,'home.html',context)

def contact_us(request):
    context = {'page_name': 'contact', 'description': ' This is contact us page of my website', }
    return render (request,'website/contact.html',context)

def about_us(request):
    context={'page_name':'about', 'description':' This is about page of my website',}

    return render (request,'website/about.html',context)
# Create your views here.

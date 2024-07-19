from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("this is homepage")
    context = {
        'variable':"Fahad",
        'year':"2"
    }
    return render(request,'index.html',context=context)
    
def about(request):
    # return HttpResponse("this is aboutpage")
    return render(request,'about.html')

def contact(request):
    return HttpResponse("this is contactpage")

def services(request):
    return HttpResponse("this is servicespage")
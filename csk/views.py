from django.shortcuts import render

# Create your views here.
def dhoni(request):
    return render(request,'dhoni.html')

def ben(request):
    return render(request,'ben.html')
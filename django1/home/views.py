from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    person={
        'name':'ajay',
        'age':21,
        'place':'Thattayil'

    }
    return render(request,'index.html',person)
def about(request):
    return render(request,'abou.html')
def booking(request):
    return render(request,'booking.html')
def doctors(request):
    return render(request,'doctors.html')
def contact(request):
    return render(request,'contact.html')
def department(request):
    return render(request,'department.html')

from django.shortcuts import render
from .models import *
from carSite.settings import BASE_DIR
# Create your views here.

def index(request):
    # cars_data.objects.all().delete() #To Delete the data
    buses = bus_data.objects.all()
    return render(request, 'index.html', {'buses':buses, 'BASE_DIR':BASE_DIR})


def admin1(request):
    if request.method == 'POST':
        bus = bus_data()
        bus.bus_Name = request.POST.get("bus_name", False)
        bus.ticket_Price = request.POST.get("ticket_price", False)
        bus.bus_Model = request.POST.get("bus_model", False)
        bus.bus_route = request.POST.get("bus_route", False)
        bus.bus_Photo = request.FILES.get("bus_photo", False)
        bus.save()

    
    return render(request, 'admin.html')

def pax(request):
    if request.method == 'POST':
        pax = paxDetails()
        pax.pax_name = request.POST.get("pax_name", False)
        pax.pax_gender = request.POST.get("pax_gender", False)
        pax.contact_num  = request.POST.get("contact_num", False)
        pax.mail = request.POST.get("mail", False)
        # pax.date = request.POST.get("date",False)
        pax.save()
    
    
    return render(request, 'booking.html',{'msg':'Booking Confirmed'})

def confim(request):
    if request.method == 'POST':
        return render(request, 'confirmation.html')


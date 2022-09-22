from multiprocessing import context
from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.

def show_mywatchlist(request):
    return render(request, "mywatchlist.html", context)

data_mywatchlist = MyWatchList.objects.all()
context = {
    'list_mywatchlist' : data_mywatchlist,
    'nama' : "Qistina Muharrifa",
    'npm' : "2106708210"
}

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_html(request):
    data = MyWatchList.objects.all()
    return render(request, "mywatchlist.html", context)

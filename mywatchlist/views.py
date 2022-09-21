from multiprocessing import context
from django.shortcuts import render
from mywatchlist.models import MyWatchList

# Create your views here.

def show_mywatchlist(request):
    return render(request, "mywatchlist.html", context)

data_mywatchlist = MyWatchList.objects.all()
context = {
    'list_mywatchlist' : data_mywatchlist,
    'nama' : "Qistina Muharrifa",
    'npm' : "2106708210"
}

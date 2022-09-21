from django.urls import path
from mywatchlist.views import show_mywatchlist

app_name = 'wishlist'

urlpatterns = [
    path('', show_mywatchlist, name='show_wishlist'),
]
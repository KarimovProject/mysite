from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
def main():

    return HttpResponse("<h1> Hello World")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main)
]

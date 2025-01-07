from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    # print(request.user)
    # return HttpResponse("Привет, это главная страница!")

    return render(request, "home.html")

def about(request):
    return HttpResponse("О проекте")

def contacts(request):
    return HttpResponse("Контакты")
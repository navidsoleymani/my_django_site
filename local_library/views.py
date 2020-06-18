from django.http import HttpResponse
from django.shortcuts import render


def sign_in(request, username, password):
    temp = False
    if username == "nvd" and password == "nvd":
        temp = True
    return HttpResponse(temp)

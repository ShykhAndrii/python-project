from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello")

def about(request):
    return HttpResponse("<h2>Hello</h2>")

def contact(request):
    return HttpResponse("<h2>Contact</h2>")

def param(request, name, age):
    return HttpResponse(f"""
                        <h2>User:</h2>
                        <p>Name: {name} </p>
                        <p>Age: {age} </p>
                        """)
    
def param1(request, name, age):
    return HttpResponse(f"""
                        <h2>User:</h2>
                        <p>Name: {name} </p>
                        <p>Age: {age} </p>
                        """)
    
def comments(request):
    return HttpResponse("<h2>comments</h2>")

def questions(request):
    return HttpResponse("<h2>questions</h2>")

def products(request, id):
    return HttpResponse(F"<h2>products {id} </h2>")

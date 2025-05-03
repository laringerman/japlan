from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return HttpResponse("""<html>
                        <title>JapLAN - Маршруты путешествий</title>
                        <h1>JapLAN</h1>
                        </html>""")

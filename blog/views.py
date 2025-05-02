from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return HttpResponse("""<html>
                        <title>JapLAN</title>
                        <h1>JapLAN</h1>
                        </html>""")

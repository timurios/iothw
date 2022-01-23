from django.shortcuts import render, HttpResponse

def main(request):
    return render(request,"tmp/index.html")

def page2(request):
    return render(request,"tmp/page2.html")

def page3(request):
    return render(request,"tmp/page3.html")


def page4(request):
    return render(request,"tmp/page4.html")

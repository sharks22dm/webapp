from django.shortcuts import render


def service_main(request):
    return render(request, 'service/service_main.html')

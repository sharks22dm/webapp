from django.shortcuts import render


# Create your views here.
def nagornoe_main(request):
    return render(request, 'nagornoe/nagornoe_main.html')

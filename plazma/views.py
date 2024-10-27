from django.shortcuts import render


# Create your views here.
def plazma_main(request):
    return render(request, 'plazma/plazma_main.html')

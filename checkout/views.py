from django.shortcuts import render

# Create your views here.
def checkout(request):
    if request.POST:
        print('checkout')
    return render(request, "checkout/checkout.html")

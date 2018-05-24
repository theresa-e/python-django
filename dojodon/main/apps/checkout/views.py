from django.shortcuts import render, HttpResponse, redirect

def checkout(request):
    print ('*'*10, 'User reached the checkout page', '*'*10)
    return render(request, 'checkout/checkout.html')

def go_back(request):
    print ('*'*10, 'User is being redirected to main page.', '*'*10)
    return redirect('/')
from django.http import HttpResponse
from django.shortcuts import render

def index(request) -> HttpResponse:
    return render(request, 'pages/index.html')

def login(request) -> HttpResponse:
    return render(request, 'pages/auth/login.html') 

def register(request) -> HttpResponse:
    return render(request, 'pages/auth/register.html')

def register_label(request) -> HttpResponse:
    return render(request, 'pages/auth/register-label.html')

def dashboard(request) -> HttpResponse:
    return render(request, 'pages/dashboard.html')

def subscription(request) -> HttpResponse:
    subscriptions = [
        { 'id': 1, 'name': 'Basic', 'price': '100', 'features': [
            'Free Songs with Ads',
            'Free Music Videos',
            'Free Premium Videos',
            'Premium Videos with Ads',
            'Premium Videos with Ads',
        ] },
        { 'id': 2, 'name': 'Premium', 'price': '200', 'features': [
            'Free Songs with Ads',
            'Free Music Videos',
            'Free Premium Videos',
            'Premium Videos with Ads',
            'Premium Videos with Ads',
            'Unlimited Songs',
            'Unlimited Music Videos',
            'Unlimited Premium Videos',
        ] },    
        { 'id': 3, 'name': 'Ultimate', 'price': '300', 'features': [    
            'Free Songs with Ads',
            'Free Music Videos',
            'Free Premium Videos',
            'Premium Videos with Ads',
            'Premium Videos with Ads',
            'Unlimited Songs',
            'Unlimited Music Videos',
            'Unlimited Premium Videos',
            'Unlimited Premium Videos',
         ] },
    ]
    return render(request, 'pages/subscription.html', {'subscriptions': subscriptions})
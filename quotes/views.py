import random
from django.shortcuts import render

def home(request):
    quote_list = [
        "The best way to predict the future is to create it.",
        "Simplicity is the ultimate sophistication.",
        "Code is like humor. When you have to explain it, it’s bad."
    ]
    context = {'quote': random.choice(quote_list)}
    return render(request, 'home.html', context)

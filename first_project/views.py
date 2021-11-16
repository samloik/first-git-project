from django.shortcuts import render
from . import mashine_learnig_model13

def home(request):
    return render(request, 'index.html')

def result(request):
    user_input = request.GET['user_input']
    user_input = mashine_learnig_model13.multiplier(user_input)
    return render(request, 'result.html', {'home_input': user_input})
    # return render(request, 'result.html')

def about(request):
    return render(request, 'about.html')

from django.shortcuts import render
from mad import helpers, data
import random

def home(request):
    if request.method == 'POST':
        res = {
            'story': helpers.tellStory(request.POST)
        }
        return render(request, 'result.html', res)
    rand = random.randint(1, len(data.STORIES))
    resp = {
        'number': rand,
        'clues': helpers.getKeys(rand)
    }
    return render(request, 'home.html', resp)    

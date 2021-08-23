from django.shortcuts import render, HttpResponse, redirect
import random
from datetime import datetime

# Create your views here.
def index(request):
    if 'total_gold' not in request.session or 'registro' not in request.session:
        request.session['total_gold'] = 0
        request.session['registro'] = []
        request.session['registro'].append('welcome!' + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ')')
    return render(request, 'index.html')

def process_money(request):
    if request.method == 'GET':
        return redirect('/')
    elif request.method == 'POST':
        print(request.POST['farming'] == 'farm')

        if request.POST['farming'] == 'farm':
           gold = random.randint(10, 20)
           request.session['registro'].append('Earned ' + str(gold) + ' golds from the farm! ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ')')

        if request.POST['farming'] == 'cave':
           gold = random.randint(5, 10)
           request.session['registro'].append('Earned ' + str(gold) + ' golds from the cave! ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ')')

        if request.POST['farming'] == 'house':
            gold = random.randint(2, 5)
            request.session['registro'].append('Earned ' + str(gold) + ' golds from the house! ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ')')

        if request.POST['farming'] == 'casino':
            gold = random.randint(-50, 50)
            if gold >= 0:
                request.session['registro'].append('Entered a casino and Earned ' + str(gold) + ' golds ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ')')
            else:
                request.session['registro'].append('Entered a casino and lost ' + str(gold)[1:] + ' golds...Ouch.. ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ')')

        request.session['total_gold'] += gold

    return render(request, 'index.html')

def reset(request):
    request.session.flush()
    return redirect('/')

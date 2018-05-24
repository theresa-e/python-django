from django.shortcuts import render,  HttpResponse, redirect

def index(request):
    return render(request, 'index.html')

def process(request):
    if 'name' not in request.session:
        request.session['name'] = request.POST['name']
    request.session['name'] =  request.POST['name']
    if 'location' not in request.session:
        request.session['location'] = request.POST['location']
    request.session['location'] = request.POST['location']
    if 'fav_dish' not in request.session:
        request.session['fav_dish'] = request.POST['fav_dish']
    request.session['fav_dish'] = request.POST['fav_dish']
    if 'comment' not in request.session:
        request.session['comment'] = request.POST['comment']
    request.session['comment'] = request.POST['comment']
    print('*'*10, 'The form was submitted!', '*'*10)
    print(request.session['name'])
    return redirect('results.html')

def results(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    request.session['count'] += 1
    return render(request, 'results.html')
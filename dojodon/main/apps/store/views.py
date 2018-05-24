from django.shortcuts import render, HttpResponse, redirect

def index(request):
    print('*'*10, 'User reached store.', '*'*10)
    return render(request, 'store/index.html')

def buy(request):
    print('*'*10, 'The form was submitted.', '*'*10)

    if 'price' not in request.session:
        request.session['price'] = 0
    if 'total_due' not in request.session:
        request.session['total_due'] = 0
    if 'total_items' not in request.session:
        request.session['total_items'] = 0
    # If user is buying blankets
    if int(request.POST['product_id']) == 1:
        request.session['total_due'] += int(request.POST['blanket']) * 19.99
        request.session['price'] = int(request.POST['blanket']) * 19.99
        request.session['total_items'] += int(request.POST['blanket'])
        if 'blanket' not in request.session:
            request.session['blanket'] = request.POST['blanket']
        request.session['blanket'] = request.POST['blanket']
    # If user is buying whiteboards.
    elif int(request.POST['product_id']) == 2:
        request.session['total_due'] += int(request.POST['whiteboard']) * 199.99
        request.session['price'] += int(request.POST['whiteboard']) * 199.99
        request.session['total_items'] += int(request.POST['whiteboard'])
        if 'whiteboard' not in request.session:
            request.session['whiteboard'] = request.POST['whiteboard']
        request.session['whiteboard'] = request.POST['whiteboard']
    # If user is buying textbooks
    elif int(request.POST['product_id']) == 3:
        request.session['total_due'] += int(request.POST['textbook']) * 29.99
        request.session['price'] += int(request.POST['textbook']) * 29.99
        request.session['total_items'] += int(request.POST['textbook'])
        if 'textbook' not in request.session:
            request.session['textbook'] = request.POST['textbook']
        request.session['textbook'] = request.POST['textbook']
    # If user is buying mugs
    elif int(request.POST['product_id']) == 4:
        request.session['total_due'] += int(request.POST['mug']) * 9.99
        request.session['price'] += int(request.POST['mug']) * 9.99
        request.session['total_items'] += int(request.POST['mug'])
        if 'mug' not in request.session:
            request.session['mug'] = request.POST['mug']
        request.session['mug'] = request.POST['mug']
    return redirect('/checkout')



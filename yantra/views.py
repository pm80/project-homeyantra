from django.shortcuts import render
from .models import Hisab
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect , HttpResponse
# Create your views here.
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from .forms import ImageUploadForm

def signup(request):
    context = {}
    return render(request, 'yantra/signup.html', context)
    
def signup_fun(request):
    if request.method == 'POST' :
        p_id = request.POST['p_id']
        p_type = request.POST['p_type']
        p_name = request.POST['p_name']
        price = request.POST['price']
        quantity = request.POST['quantity']
#        image = request.POST['image']
        form = ImageUploadForm(request.POST, request.FILES)
        if not form.is_valid():
            return HttpResponse('wrong')
#        print(type(image))
        flag = 0
#        return render(request, 'yantra/a.html', {'image':type(image)})
        for i in Hisab.objects.all():
            if i.p_id == p_id :
                flag = 1
                break
        if flag == 0:
            e = Hisab(p_id=p_id, p_type=p_type, p_name=p_name, price=price, image=form.cleaned_data['image'], quantity=quantity)
            e.save()
        if flag == 1:
            messages.error(request,'product id already exists!')
            return HttpResponseRedirect(reverse('yantra:error'))
    return HttpResponseRedirect(reverse('yantra:complete'))
    
def f1(request):
    return render(request, 'yantra/a.html', {'BASE_DIR':BASE_DIR})
def fError(request):
    return render(request, 'yantra/error.html', {'BASE_DIR':BASE_DIR})
def database(request):
    p_i, p_n, p_t, price, q, image = [], [], [], [], [], []
    zpd_p = zip([],[],[],[],[],[] )
    zpd_rp = zip([],[],[],[],[],[] )
    for i in Hisab.objects.all():
        p_i.append(i.p_id)
        p_n.append(i.p_name)
        p_t.append(i.p_type)
        price.append(i.price)
        q.append(i.quantity)
        image.append(i.image.url) #ccc
        #image.append('<a href = '+'"'+BASE_DIR+i.image.url+'"' + '>'+BASE_DIR+i.image.url+'</a>')
        zpd_p = [(i, n, t, qu, p, im) for (p, i, n, t, qu, im) in sorted(zip(price, p_i, p_n, p_t, q, image))]
        zpd_rp = [(i, n, t, qu, p, im) for (p, i, n, t, qu, im) in sorted(zip(price, p_i, p_n, p_t, q, image), reverse = True)]
    context = {'p_i':p_i, 'p_n':p_n, 'p_t':p_t, 'price':price, 'q':q, 'image':image, 'zpd':zip(p_i, p_n, p_t, q, price, image), 'zpd_p':zpd_p, 'zpd_rp':zpd_rp}
    return render(request, 'yantra/database.html', context)

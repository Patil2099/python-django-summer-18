from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from . import models
from django.db.models import Avg
from . import forms


def index(request):
    context={}
    return render(request,r'files\index.html',context)

def Restaurants(request):
    qs=models.Restaurant.objects.all()
    #qs =qs.annotate(average_rating = Avg('review__rating')).order_by('-average_rating')
    f=request.GET['filter']
    r=request.GET['reverse']

    if f=='a2z' and r=='0':
        qs=qs.order_by('name')
    elif f=='a2z' and r=='1':
        qs=qs.order_by('-name')
    elif f=='rating' and r=='0':
        qs=qs.annotate(average_rating=Avg('review__rating')).order_by('average_rating')
    elif f=='rating' and r=='1':
        qs=qs.annotate(average_rating=Avg('review__rating')).order_by('-average_rating')


    print(request.GET)
    context={
        'qs' :qs,
        'r':r,
        'f':f
    }
    return render(request,'files\prest.html',context )
def add_rest(request):
    if request.method == "GET":
         form = forms.RestaurantForm()
    else:
        form = forms.RestaurantForm(request.POST)

        if form.is_valid():
            obj = form.save()
            return HttpResponse("Form Added with id " + str(obj.pk))

    context = {
        'form': form
    }
    return render(request, 'files/addRestaurant.html', context)

def restaurant(request, id):
    
    rest = get_object_or_404(models.Restaurant, pk = id)
    success = False
    
    # Handling the form
    if request.method == "GET":
        form = forms.ReviewForm()
    else:
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            obj = form.save(commit = False)
            obj.restaurant = rest
            obj.save()
            success = True
            form = forms.ReviewForm()

    context = {
        'restaurant': rest,
        'form': form,
        'success': success
    }
    return render(request, r'files\restaurant.html', context)

def review(request, id):
    obj = get_object_or_404(models.Review, pk = id)

    context = {
        'review': obj
    }
    return render(request, 'files/review.html', context)




# Create your views here.

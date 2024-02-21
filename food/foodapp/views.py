from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from foodapp.models import food,track
from foodapp.forms import foodform,editform

# Create your views here.

def index(request):

    data = food.objects.all()
    # for i in data:
    #     print(i.carbs)
            
    return render(request,'index.html',{'data':data})

def new_food(request):
    form = foodform()

    if request.method == 'POST':
        form = foodform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    data = food.objects.all()

    return render(request,'new_food.html',{'form':form})



def track_food(request):
    
    d1 = track.objects.all()
    data = food.objects.all()
    
    # d = {}
    
    if request.method == 'POST':
            name = request.POST.get('op')
            quan = int(request.POST.get('q')) 

            print(name ,quan)

            d = {}

            for i in data:
                if  i.name in name :
                   
                    # if int(i.quantity) == 1 :
                    
                        # print(i.name)
                        # print(i.quantity)
                        # print(i.protein)
                        # print(i.carbs)
                        # print(i.fat)

                        d.update(name=i.name)
                        d.update(quantity = quan)
                        d.update(protein = "{:.2f}".format(i.protein * quan))
                        d.update(carbs = "{:.2f}".format(i.carbs * quan))
                        d.update(fat = "{:.2f}".format(i.fat * quan))
                        d.update(vitamins = i.vitamins)
                        if i.img:
                            d.update(img=i.img)

            print(d)

            instance = track(**d)
            instance.save()

            return redirect('track')

    pro = 0
    carb = 0
    fa = 0
    for da in d1:
        pro += da.protein
        carb += da.carbs
        fa += da.fat

    print(pro,carb,fa)

 
    return render(request,'track.html',{'data':data,'d1':d1,'pro':pro,'carb':carb,'fa':fa,})



def edit(request,pk):
    
    if request.method == 'POST':
        res = track.objects.get(id=pk)
        data = food.objects.get(name=res.name)
        # print(res)
        
        form = editform(request.POST,instance=res)
        if form.is_valid():
            d = {}
            
            d.update(name=res.name)
            d.update(quantity = res.quantity)
            d.update(protein = "{:.2f}".format(data.protein * res.quantity))
            d.update(carbs = "{:.2f}".format(data.carbs * res.quantity))
            d.update(fat = "{:.2f}".format(data.fat * res.quantity))
            d.update(vitamins = data.vitamins)
            if res.img:
                d.update(img=res.img)

            print(d)

            instance = track(**d)
            instance.save()
            res.delete()
            return redirect('track')
    
    res = track.objects.get(id=pk)
    form = editform(instance=res)
    return render(request,'edit.html',{'form':form})

def delete(request,pk):
    res = track.objects.get(id=pk)
    res.delete()
    return redirect('track')

def home(request):
    data = food.objects.all()

    return render(request,'home.html',{'data':data})

def detail(request,pk):

    data = food.objects.get(id=pk)
    is_favourite = False
    
    if data.fav.filter(id=request.user.id).exists():
        is_favourite = True
    fav_food = is_favourite
    print(fav_food)

    data = food.objects.filter(id=pk)
    return render(request,'detail.html',{'data':data})

# def favourite(request,pk):
#     var = get_object_or_404(food,id=request.POST.get('out'))
#     if var.fav.filter(id=request.user.id).exists():
#         var.fav.remove(request.user)
#     else:
#         var.fav.add(request.user)
#     return redirect('detail',pk=pk)

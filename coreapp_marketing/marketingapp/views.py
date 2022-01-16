from django.shortcuts import render, redirect
from marketingapp.models import Products, prod_datacollected

# Create your views here.

def TL_dash(request):
    return render(request, 'TL_dash.html')

def TL_mytasks(request):
    return render(request, 'TL_tasks.html')    

def TL_cardslist(request):
    return render(request, 'TL_cardslist.html')  

def TL_messagecards(request):
    return render(request, 'TL_messagecards.html')

def TL_table(request):
    return render(request, 'TL_table.html')    


# Marketing Executive

def exec_mytasks(request):
    return render(request, 'exec_mytasks.html')       

def exec_products(request):
    product = Products.objects.all() 
    return render(request, "exec_products.html", {'product' : product})     

def exec_productdetails(request,id):
    product = Products.objects.get(id=id)
    return render(request, 'exec_productdetails.html', {'product' : product})    
   
def exec_productdata(request,id):
    product = Products.objects.get(id=id)
    member = prod_datacollected.objects.filter(product_id=product)
    request.session['prod_id']=product.id
    return render(request, 'exec_productdata.html', {'member' : member})  


def exec_savedc(request,id):
    prod_dc = prod_datacollected.objects.get(id=id)
    member = prod_datacollected.objects.filter(product_id= request.session['prod_id'])
    request.session['prod_dc_id']=prod_dc.id
    context = {'member' : member,   'prod_dc' : prod_dc } 
    return render(request, 'exec_assignstatus.html', context)  
   

def exec_savedc1(request,st):   
    print(st)   
    prod_dc = prod_datacollected.objects.get(id=request.session['prod_dc_id'])
    if int(st) == 1:
        prod_dc.status = True
    elif int(st) == 0:
        prod_dc.status = False 
    prod_dc.save()    
    print(prod_dc.status) 
    product_id = request.session["prod_id"]
    return redirect(f'/marketingapp/exec_productdata/{product_id}')
      



    



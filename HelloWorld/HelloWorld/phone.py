from django.shortcuts import render 

 
from TestMode.models import phone
 
def phonedb(request):
    p_list =phone.objects.all()
    
    page_index=60
    sum=int(len(p_list)/page_index)+1

    page_i=request.GET.get('p')
    page_i=int(page_i)
    if(page_i<=1):
        page_i=1
    if(page_i>=sum):
        page_i=sum


    strat=(page_i-1)*page_index
    end=page_i*page_index
    

    context   = {}
    

    up_page=page_i-1
    next_page=page_i+1
    if(page_i<=1):
        up_page=1
    if(page_i>=sum):
        next_page=sum

    context['p_list'] = p_list[strat:end]
    context['up'] = up_page
    context['next'] =next_page
    context['sum'] =sum
    context['page'] =page_i
    return render(request, 'phone.html', context)


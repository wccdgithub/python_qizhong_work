from django.shortcuts import render 


from TestMode.models import weather

def weatherdb(request):
    citycode=["北京","上海","广州","深圳","温州"]
    c_list=[]
    for c in citycode:
        c_city=weather.objects.filter(city=c)
        c_list.append({'city':c,'weather':c_city})
    
    
    context   = {}
    context['c_list'] = c_list



    
    return render(request, 'weather.html', context)
    

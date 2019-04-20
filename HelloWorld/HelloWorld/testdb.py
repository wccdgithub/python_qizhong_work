from django.shortcuts import render 
 
from TestMode.models import pq
 
def testdb(request):
    c_list =pq.objects.all()

    context   = {}
    context['c_list'] = c_list


    return render(request, 'testdb.html', context)




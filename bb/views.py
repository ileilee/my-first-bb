from django.shortcuts import render

# Create your views here.
def cust_list(request):
    return render(request, 'bb/cust_list.html', {})
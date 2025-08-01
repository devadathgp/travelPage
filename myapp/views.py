from urllib.request import Request

from django.contrib.sites import requests

from . forms import *
from django.core.checks import messages

from django.shortcuts import render,redirect
from django.contrib import messages

from . models import *
from . serializers import *
from django.shortcuts import render
from django.views import generic
from rest_framework import generics
from rest_framework.permissions import AllowAny
import requests
from django.contrib import messages




# Create your views here.
class create_travel(generics.CreateAPIView):
    queryset = TravelPage.objects.all()
    serializer_class=TravelSerializer
    permission_classes=[AllowAny]

class detail_travel(generics.RetrieveAPIView):
    queryset=TravelPage.objects.all()
    serializer_class=TravelSerializer

class update_travel(generics.UpdateAPIView):
    queryset = TravelPage.objects.all()
    serializer_class = TravelSerializer

class delete_travel(generics.DestroyAPIView):
    queryset = TravelPage.objects.all()
    serializer_class = TravelSerializer

class search_travel(generics.ListAPIView):
    queryset = TravelPage.objects.all()
    serializer_class = TravelSerializer

    def get_queryset(self):
        name=self.kwargs.get('Name')
        return TravelPage.objects.filter(Name__icontains=name)


def travel_create(request):
    if request.method == 'POST':
        form=TravelPageForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
                api_url=' http://127.0.0.1:8000/create_travel/'
                data=form.cleaned_data
                print (data)
                return redirect('index')
            except RequestException as e:
                messages.error(request,'Error')
        else:
            messages.error(request,'Error')
    else:
        form=TravelPageForm()
    return render(request, 'travel_create.html',{'form':form})
#
# def index(request):
#     api_url='http://127.0.0.1:8000/create_travel/'
#     data={}
#     try:
#         response=requests.get(api_url)
#
#         if response.status_code==200:
#             data=response.json()
#         else :
#             messages.error(request,'Error1')
#     except requests.exceptions.RequestException as e:
#         messages.error(request,'Error')
#
#     return render(request, 'index.html',{'data':data})

def index(request):
    query = request.GET.get('q')  # for search
    if query:
        travels = TravelPage.objects.filter(Name__icontains=query)
    else:
        travels = TravelPage.objects.all()

    return render(request, 'index.html', {'travels': travels, 'query': query})



def travel_detail(request,id):
    api_url=f'http://127.0.0.1:8000/detail_travel/{id}/'
    response=requests.get(api_url)
    data={}
    ingredients={}
    if response.status_code == 200:
        data=response.json()
        ingredients=data.get('description','').split('.')
    return render(request, 'detailTravel.html', {'ingredients':ingredients,'travel':data})



def travel_update(request,id):
    if request.method == 'POST':
        Name=request.POST['Name']
        whether=request.POST['whether']
        location=request.POST['location']
        description=request.POST['description']
        print("image url",request.FILES.get('image'))
        api_url=f'http://127.0.0.1:8000/update_travel/{id}/'
        data={
            'Name':Name,
            'whether':whether,
            'location':location,
            'description':description,
        }
        file={'image':request.FILES.get('image')}
        response=requests.put(api_url, data=data,files=file)
        if response.status_code == 200:
            return redirect('/')
        else:
            messages.error(request, 'Error During API request')
    return render(request, 'updateTravel.html')


def travel_delete(request,id):
    api_url=f'http://127.0.0.1:8000/delete_travel/{id}/'
    response=requests.delete(api_url)
    if response.status_code == 200:
        print("Travel Deleted")
    else:
        print("Error During API request")
    return redirect('/')


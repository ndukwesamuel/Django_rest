from django.shortcuts import render
from django.http import JsonResponse, response
from rest_framework.views import APIView

from .models import CareerModle


# Create your views here.


def home(request):

    return render( request, 'index.html')



def API_NAME(request):
    method = request.method.lower()
    if method == 'get':
        return JsonResponse({'data': ['1',2,3,4,4,5,5]})
    elif method == 'post':
        return JsonResponse({'data':'Update'})

    return JsonResponse({'method': request.method})



class simple(APIView):

    def get(self, request):
        content  = CareerModle.objects.all().values()
        print(content)
        return JsonResponse({"data":list(content)})

    pass
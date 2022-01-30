from django.http import JsonResponse

def home(request):
    return JsonResponse({'message':'this api is working properly'})

# Create your views here.

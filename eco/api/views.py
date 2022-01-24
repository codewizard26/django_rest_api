from django.http import JsonResponse

def home(request):
    return JsonResponse({'name':'nikhil','sirname':'mishra'})

# Create your views here.

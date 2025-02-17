from django.shortcuts import render

# Create your views here.
def home(request, *args, **kwargs):
    return render(request, 'index.html')

def List_Puvl(request, *args, **kwargs):
    return render(request, 'pulverisateur.html')
def List_MatIr(request, *args, **kwargs):
    return render(request, 'MaterielIr.html')

def engrais(request):
    return render(request, 'engrais.html')

def product_view(request):
    return render(request, 'product.html')

def Profil_view(request):
    return render(request, 'profil.html')

#def login_view(request):
  #  return render(request, 'login.html')

#def register_view(request):
 #   return render(request, 'register.html')
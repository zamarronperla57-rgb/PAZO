from django.shortcuts import render

def inicio (request):
    return render(request, 'ZAMARRÓN/inicio.html')
def registro(request):
    return render(request, 'ZAMARRÓN/formregistro.html')
def Baile (request):
    return render(request, 'ZAMARRÓN/Baile.html')




from django.shortcuts import render

# Create your views here.
def professionaldetail(request):
	return render(request=request,template_name='html/professionalapp/professionalapp.html')

def bemark(request):
	return render(request=request,template_name='html/professionalapp/bemark.html')
	
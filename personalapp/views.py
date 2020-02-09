from django.shortcuts import render

# Create your views here.
def personaldetail(request):
	return render(request=request,template_name='html/personalapp/personalapp.html')
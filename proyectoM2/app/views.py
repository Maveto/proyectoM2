from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from app.models import *
from app.forms  import CustomUserForm
from django.contrib.auth import login, authenticate

# Create your views here.
"""def index(response):
	return HttpResponse("<h1>Index</h1>")"""

"""def error404(request,exception):
	return render(request, 'error404.html', status=404)

def error500(request):
	return render(request, 'error500.html', status=500)"""

def login_redirect(request):
	return redirect('accounts/login/')

def index (request):
    return render_to_response('index.html')

def courses(request):
	cursos = Course.objects.all()
	return render_to_response('courses.html', {'cursos':cursos})

def blog(request):
	return render_to_response('blog.html')

def contacto(request):
	return render_to_response('contact.html')

def curso_info(request, curso):
	curso = Course.objects.all().filter(id=curso)
	return render_to_response('base.html',{'curso':curso})

'''
def login(request):
	return render_to_response('registration/login.html')'''

def registro(request):
	return render_to_response('registro.html')

def inicio(request):
	return render_to_response('registration/inicio.html')

def register(request):
	data ={
		'form':CustomUserForm()
	}
	if request.method == 'POST':
		formulario = CustomUserForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			username = formulario.cleaned_data['username']
			password = formulario.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request,user)
			return redirect(to="index")
	return render(request, 'registration/register.html',data)
'''
def register(request):
	if request.method=='POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
		else:
			form = UserCreationForm()
			args = {'form':form}
			return render(request, 'registration/register.html',args)
	else:
		form = UserCreationForm()
		args = {'form':form}
		return render(request, 'registration/register.html',args)'''
'''	
def login(request):
	return render_to_response('login.html')	
	
def registro(CreateView):
	model = User
	template_name="registro.html"
	form_class = RegistroForm
	success_url = reverse('login.html')
	'''

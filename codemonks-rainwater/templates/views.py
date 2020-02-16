from django.shortcuts import render
from .models import User,Maps
from .forms import MapsForm
from django.views.generic import CreateView
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .panels_atlast import main1
from . import forms
from .panels_atlast import main1
from PIL import Image
import logging
from django.core.files.storage import default_storage
from django.conf import settings
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
def index(request):
  return render(request, 'index1.html')

def services(request):
  return render(request,'services.html')

def signup(request):
  if request.method=="POST":
    form = forms.UserCreateForm(request.POST)
    if form.is_valid():
      user=form.save()
      username=form.cleaned_data.get("username")
      email=form.cleaned_data.get("email")
      login(request,user)
      return redirect('index')
    else:
      for msg in form.error_messages:
        print(form.error_messages[msg])

      return render(request = request,
                          template_name = "registration/signup.html",
                          context={"form":form})
  form=forms.UserCreateForm
  return render(request,'registration/signup.html',{'form': form})

  def Login(request):
    if request.method == 'POST': 
        username = request.POST['username'] 
        password = request.POST['password'] 
        user = authenticate(request, username = username, password = password) 
        if user is not None: 
            form = login(request, user) 
            messages.success(request, f' Welcome {username} !!') 
            return redirect('index') 
        else: 
            messages.info(request, f'account done not exit please sign in') 
    form = AuthenticationForm() 
    return render(request, 'registration/login.html', {'form':form, 'title':'log in'}) 

def about(request):
  return render(request, 'trailers.html')

def about1(request):
  return render(request, 'sacred.html')

def about2(request):
  return render(request, 'shark.html')

def epi(request):
  return render(request, 'episodes.html')

def profile(request):
  return render(request,'profile.html')


def delete_user(request,username):

  context = ""
  try:
    u = User.objects.get(username=username)
    print(username)
    u.delete()
    context += 'The user is deleted.'      
  except User.DoesNotExist: 
    context += 'The user is deleted.'
  except Exception as e: 
   context=""

def result(request,response):
  return render(request,'result.html',{'cnt':response})
def maps_image_view(request):
  if request.method == 'POST':
    # form = MapsForm(request.POST) 
    form = MapsForm(request.POST, request.FILES) 
    if form.is_valid(): 
      logging.debug("valid")
      obj=form.save()
      # new_path = settings.STATIC_ROOT +"input.png"
      # name=default_storage.save(new_path,obj.maps_Main_Img)
      # print(name)
      # response=51
      # logging.debug(obj)
      response=main1(obj.maps_Main_Img)
      # result = Image.fromarray(response)
      logging.debug("view",response)
      return redirect('result',response)
      # return HttpResponse(result, content_type="image/png")
  else:
    form = MapsForm()
  return render(request, 'maps_image_form.html', {'form' : form}) 


  
  
def success(request): 
    return HttpResponse('successfully uploaded')
    
     

    

  # return render(request, 'delete.html', {"context":context}) 
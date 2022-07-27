from django.shortcuts import render, redirect
from django.http import FileResponse, HttpResponse
from .forms import FileUpload
from django.contrib.auth.decorators import login_required
from .models import FileUpload as fp
from firebase_admin import credentials, firestore, storage, initialize_app
from firebase_admin import db as jk
import os
import mimetypes
import firebase_admin
from pathlib import Path
#from . import credential as kh

# Create your views here.


BASE_DIR = Path(__file__).resolve().parent.parent

if not firebase_admin._apps:
	# Use a service account
	cred = credentials.Certificate(str(BASE_DIR)+'\\Cloud\\credential.json')
	firebase_admin.initialize_app(cred, {'databaseURL': "https://mgcloud-dd822-default-rtdb.firebaseio.com"})
	#db = firestore.client()
	db=storage.Bucket(name='mgcloud-dd822.appspot.com')
	#op = jk.reference('tests')
	print(op.get())
	print(op)
else:
	#db=storage.bucket(name='mgcloud-dd822.appspot.com')
	op = jk.reference('tests')
	print(op.get())
	print(op)
@login_required(login_url='SignIn/')
def Home(request):
	Upload = FileUpload()
	if request.method == 'POST':
		FileSave = FileUpload(request.POST,request.FILES)
		print(FileSave.errors)
		#print(request.FILES)
		if FileSave.is_valid():
			FSave = FileSave.save()
			request.user.Key.add(FSave)
			print("Successfull")
		else:
			print('sequence failed')
	else:
		print('method error')
	context = {'FileUpload': Upload}
	return render(request, 'Cloud/Home.html', context)

# ------------------------------ FILES VIEW ------------------------------ #

def Files(request):
	Files = fp.objects.all()
	#print(request.user)
	return render(request, 'Cloud/Files.html' )

def About(request):
	return render(request, 'Cloud/About.html')
def Download(request,pk_download):
        dd = fp.objects.get(id=pk_download)
        ddpath = dd.file.path
        mime_type = mimetypes.guess_type(ddpath)
        response = HttpResponse(ddpath, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename="+'(MgCloud) '+ dd.file.name
        return response
def Delete(request,pk_delete):
     delof = fp.objects.get(id=pk_delete)
     delof.delete()
     pt = delof.file.path
     os.remove(pt)
     return redirect('/Files')
def Open(request,pk_open):
        op = fp.objects.get(id=pk_open)
        oppt = op.file.path
        return FileResponse(open(oppt, 'rb'))

from django.shortcuts import render, redirect
from django.http import FileResponse
from .forms import FileUpload
from django.contrib.auth.decorators import login_required
from .models import FileUpload as fp
import os
# Create your views here.

@login_required(login_url='SignIn/')
def Home(request):
	Upload = FileUpload()
	if request.method == 'POST':
		FileSave = FileUpload(request.POST,request.FILES)
		print(FileSave.errors)
		print(request.FILES)
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
	print(request.user)
	return render(request, 'Cloud/Files.html' )

def Download():
	pass
def Delete(request,pk_delete):
     delof = fp.objects.get(id=pk_delete)
     delof = delof.file.path
     delof.delete()
     pt = delof.file.path
     os.remove(pt)
     return redirect('/Files')
def Open(request,pk_open):
        op = fp.objects.get(id=pk_open)
        oppt = op.file.path
        return FileResponse(open(oppt, 'rb'))

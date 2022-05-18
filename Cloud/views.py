from django.shortcuts import render, redirect
from django.http import FileResponse, HttpResponse
from .forms import FileUpload
from django.contrib.auth.decorators import login_required
from .models import FileUpload as fp
import os
import mimetypes
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

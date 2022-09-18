from django.shortcuts import render
from .models import Album
from .forms import AlbumForm
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
	data = Album.objects.all()
	

	if request.method == 'POST':
		form = AlbumForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()

			return HttpResponseRedirect('')
	else:
		form = AlbumForm()
	return render(request, 'album/index.html', {"data": data, "form":form})

def delete(request):
	if request.method == 'POST':
		key = request.POST.get('id')
		try:
			obj = Album.objects.get(id=key)
			obj.delete()
		except Exception as e:
			raise
	return HttpResponseRedirect('/')
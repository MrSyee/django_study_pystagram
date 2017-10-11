from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from .models import Photo
from .forms import PhotoForm

def hello(request):
    return HttpResponse('안녕하세요')

def detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)

    #photo = Photo.objects.get(pk=pk)

    msg = (
    '<p>{pk}번 사진을 보여줄게요.</p>'.format(pk=photo.pk),
    '<p>주소는 {url}</p>'.format(url=photo.image.url),
    '<p>이미지는 <br> <img src="{url}" /></p>'.format(url=photo.image.url),
    )
    return HttpResponse('\n'.join(msg))

def create(request):
    if request.method == "GET":
        form = PhotoForm()
    elif request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save()
            return redirect(obj)

    ctx = {
        'form': form,
    }
    return render(request, 'edit.html', ctx)

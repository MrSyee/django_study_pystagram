from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Photo

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

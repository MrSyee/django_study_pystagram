from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

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

@login_required
def create(request):
    # 로그인하지 않은 사용자가 사진 저장하려하면 로그인 페이지로 보냄.
    if not request.user.is_authenticated():
        return redirect(settings.LOGIN_URL)

    if request.method == "GET":
        form = PhotoForm()
    elif request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save(commit=False) # 데이터를 모델에 연결된 DB테이블에 저장한다.
    # commit은 실제 DB에 반영할것인지 여부  # 저장한 내용이 반영된 모델의 인스턴스 객체를 반환
    # 기본값은 True                       # 따라서 PhotoForm이 아닌 Photo의 인스턴스 객체
            obj.user = request.user # 현재 접속한 user 정보를 Photo.user에 입력
            obj.save()

            return redirect(obj)

    ctx = {
        'form': form,
    }
    return render(request, 'edit.html', ctx)

def profile(request, username):
    User = get_user_model()
    user = get_object_or_404(User, username=username)
    photos = user.photo_set.order_by('-created_at', '-pk')

    ctx = {
        'user': user,
        'photos': photos,
    }

    return render(request, 'profile.html', ctx)


# photo 앱에서 사용하는 Form

from __future_- import unicode_literals
from django import forms
from .models import Photo

# 사진 게시물을 편집하는 폼
class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photofields = ('image', 'content', )

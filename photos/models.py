from django.db import models

class Photo(model.Model):
    id = 'index'
    image = 'origin_image'
    filtered_image = 'filtered_image'
    content = '사진에 대한 설명문'
    created_at = '생성일시'

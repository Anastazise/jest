from django.forms import ModelForm
from .models import Room, Pool
from django import forms

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']

class PoolForm(ModelForm):
    class Meta:
        model = Pool
        fields = '__all__'
        labels = {
        "design": "Дизайн",
        "functionality": "Функционал",
        "creativity": "Креативность",
        "content": "Наполнение",
        "other": "Другое",
        "uname": "Ваше имя"
        }   
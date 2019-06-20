from django import forms
from .models import Board
from django.contrib.auth.hashers import check_password

class WriteForm(forms.Form):
    title = forms.CharField(max_length=64,label="제목",error_messages={'required' : '제목 입력해주세요'})
    contents = forms.CharField(widget=forms.Textarea,label="내용" ,error_messages={'required' : '내용 입력해주세요'})

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields=('title','contents',)
    # title = forms.CharField(max_length=64,label="제목",error_messages={'required' : '제목 입력해주세요'})
    # contents = forms.CharField(widget=forms.Textarea,label="내용" ,error_messages={'required' : '내용 입력해주세요'})


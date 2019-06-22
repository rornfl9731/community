from django import forms
from .models import Board
from django.contrib.auth.hashers import check_password
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class WriteForm(forms.Form):
    title = forms.CharField(max_length=64,label="제목",error_messages={'required' : '제목 입력해주세요'})
    contents = forms.CharField(widget=forms.Textarea,label="내용" ,error_messages={'required' : '내용 입력해주세요'})
    class Meta:
        model = Board
        fields=('title','contents',)

class BoardForm(forms.ModelForm):

    title = forms.CharField(max_length=64,label="제목",error_messages={'required' : '제목 입력해주세요'})
    contents = forms.Textarea()
    class Meta:
        model = Board
        fields=('title','contents',)


# class UpdateForm(forms.ModelForm):
#     title = forms.CharField(widget=forms.Textarea,max_length=64,label="제목",error_messages={'required' : '제목 입력해주세요'})
#     contents = forms.CharField(widget=forms.Textarea,label="내용" ,error_messages={'required' : '내용 입력해주세요'})

class FormFromSomeModel(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'special', 'style': 'width:100%;height:37px'}))
    class Meta:
        model = Board
        fields=('title','contents')
        widgets = {
            'contents' : SummernoteWidget()
        }

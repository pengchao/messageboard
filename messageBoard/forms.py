# _*_ coding:utf-8 _*_

from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class RegistrationForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=30)
    email = forms.EmailField(label='电子邮件')
    password1 = forms.CharField(label='密码',widget=forms.PasswordInput())
    password2 = forms.CharField(label='确认密码',widget=forms.PasswordInput())

    #验证用户输入用户名的合法性
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$',username):
            raise forms.ValidationError('用户名中只能包含字母，数字和下划线！')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('用户名已经存在！')
    #验证用户email
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            User.objects.get(email=email)
        except ObjectDoesNotExist:
            return email
        raise forms.ValidationError('用户数据库中已经有该电子邮件！')
    #验证密码是否一致
    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
            raise forms.ValidationError('密码不匹配！')



class MsgPostForm(forms.Form):
    title = forms.CharField(label='标题',widget=forms.TextInput(attrs=
        {'size':30,'max_length':30}))
    content = forms.CharField(label='内容',widget=forms.Textarea(attrs={'size':10000}))

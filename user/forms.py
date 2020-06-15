from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, label='사용자 이름')
    password = forms.CharField(
        max_length=20, widget=forms.PasswordInput, label='비밀번호')

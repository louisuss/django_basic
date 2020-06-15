from django import forms


class BoardForm(forms.Form):
    title = forms.CharField(
        error_messages={
            'required': '제목을 입력해주세요.'
        },
        max_length=128, label='제목')
    contents = forms.CharField(
        error_messages={
            'required': '내용을 입력해주세요.'
        },
        widget=forms.Textarea, label='내용')
    # required=False 이기 때문에 쓰지 않아도 생성 됨
    tags = forms.CharField(
        required=False, label='태그')

from django import forms


class Registration(forms.Form):
    number = forms.CharField(max_length=250, label='Ваш номер')
    user_name = forms.CharField(max_length=250, label='Имя пользователя')
    pasword = forms.CharField(max_length=250, label='Пароль')
    pasword_confirm = forms.CharField(max_length=250, label='Подтверждение пароля')
    otp = forms.IntegerField(label='OTP')

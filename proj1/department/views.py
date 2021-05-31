from django.shortcuts import render
from .forms import *
from .models import *
from random import randint

form = Registration


def contacts(request):
    if request.method == 'POST':

        random_otp = randint(1000, 9999)
        print(random_otp)

        # Все пользователи в БД
        all_users = User.objects.all()

        # Проверка введенного номера телефона на наличие его в БД
        check = User.objects.filter(phone_number=request.POST.get('number')).values_list('user_name')

        # Проверка, сотрудник или нет
        employee_or_not = User.objects.filter(phone_number=request.POST.get('number')).values_list('it_employee')


        if len(check) == 0 and len(all_users) > 0:
            # Если пользователь с указанным номером телефона не существует
            # и в базе уже есть зарегистрированные пользователи,
            # открывается форма регистрации с полями Фамилия Имя и ОТР-пароль
            return render(request, 'department/registration.html', {'form': form})


        elif len(check) == 0 and len(all_users) == 0:
            # Если пользователь с указанным номером телефона не существует
            # и в базе еще нет зарегистрированных пользователей,
            # открывается форма регистрации с полями
            # Фамилия Имя, пароль, подтверждение пароля, ОТР-пароль;
            return render(request, 'department/registration2.html', {'form': form})


        elif len(check) > 0 and len(str(employee_or_not)) == 20:
            # Если пользователь существует и он является сотрудником,
            # система спрашивает пароль и ОТР-пароль;
            return render(request, 'department/registration3.html', {'form': form})


        elif len(check) > 0 and len(str(employee_or_not)) == 21:
            # Если пользователь существует и он не является сотрудником,
            # система спрашивает только ОТР-пароль
            return render(request, 'department/registration4.html', {'form': form})


    else:
        return render(request, 'department/contacts.html', {'form': form})



from django.shortcuts import render
from .forms import *
from .models import *
from random import randint
from django.http import HttpResponse
import json




def contacts(request):
    form = Registration(request.POST)

    if request.method == 'GET':
        return render(request, 'department/contacts.html', {'form': form, 'users': get_users})

    random_otp = randint(1000, 9999)
    print(f"random_otp: {random_otp}")

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
        # Если регистрируется новый пользователь — мы его добавляем в
        # таблицу с таким условием  если уже есть зарегистрированные пользователи, в статусе
        # “Сотрудник” ставим значение False.
        User.objects.create(status=True, it_employee=False,
                            division=Division.objects.get(divisional_name='Машинный отдел'),
                            phone_number=request.POST.get('number'))
        return render(request, 'department/registration.html', {'otp': random_otp, 'form': form})
    if len(check) > 0 and len(str(employee_or_not)) == 21:
        User.objects.filter(phone_number=request.POST.get('number')).update(user_name=request.POST.get('user_name'))
        return render(request, 'department/say_hello.html', {'all_users': all_users[0]})



    if len(check) == 0 and len(all_users) == 0:
        # Если пользователь с указанным номером телефона не существует
        # и в базе еще нет зарегистрированных пользователей,
        # открывается форма регистрации с полями
        # Фамилия Имя, пароль, подтверждение пароля, ОТР-пароль;
        # если регистрируется первый пользователь, устанавливаем статус
        # “Сотрудник” со значением True
        User.objects.create(status=True, it_employee=True,
                            division=Division.objects.get(divisional_name='Машинный отдел'),
                            phone_number=request.POST.get('number'))
        return render(request, 'department/registration2.html', {'otp': random_otp, 'form': form})
    if len(check) > 0 and len(str(employee_or_not)) == 20:
        User.objects.filter(phone_number=request.POST.get('number')).update(user_name=request.POST.get('user_name'))
        return render(request, 'department/say_hello2.html', {'last_users': all_users[0], 'last_division': Division.objects.all()[0]})




   # if User.objects.filter(phone_number=request.POST.get('number')) and len(str(employee_or_not)) == 20:
   #     # Если пользователь существует и он является сотрудником,
   #     # система спрашивает пароль и ОТР-пароль;
#
   #     return render(request, 'department/registration3.html', {'form': form})
#
   # if len(check) > 0 and len(str(employee_or_not)) == 21:
   #     # breakpoint()
   #     # Если пользователь существует и он не является сотрудником,
   #     # система спрашивает только ОТР-пароль
#
   #     return render(request, 'department/registration4.html', {'form': form})


def get_users(request):
    get_users = User.objects.all().values_list('user_name')
    x = {
        "name": list(get_users)
    }

    y = json.dumps(x)
    return HttpResponse(y)

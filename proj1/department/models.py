from django.db import models


class Division(models.Model):
    # Создать модель Отдел со следующими полями:
    # • Название (текст);
    # • Код отдела (текст);
    divisional_name = models.CharField(max_length=250, verbose_name='Название отдела')
    divisional_code = models.CharField(max_length=250, verbose_name='Код отдела')

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'
        ordering = ['-divisional_name']

    def __str__(self):
        return self.divisional_name


class User(models.Model):
    # Создать модель Пользователь с такими полями:
    # • user (текст);
    # • Номер телефона (текст);
    # • Статус (активен/неактивен) (булевое);
    # • Является сотрудником (булевое);
    # • Отдел (ссылка на отдел);
    user_name = models.CharField(max_length=250, verbose_name='Имя пользователя')
    phone_number = models.CharField(max_length=250, verbose_name='Номер телефона')
    status = models.BooleanField(default=False, verbose_name='Статус (активен/неактивен)')
    it_employee = models.BooleanField(default=False, verbose_name='Является сотрудником')
    division = models.ForeignKey(Division, on_delete=models.PROTECT, blank=True, verbose_name='Название отдела', null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-user_name']

    def __str__(self):
        return self.user_name
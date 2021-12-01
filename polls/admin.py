# Добавляем в файл polls/admin.py следующий код
from django.contrib import admin
from .models import Question

admin.site.register(Question)
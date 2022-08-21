from django.forms import ModelForm
from .models import Post


# Создаём модельную форму
class PostForm(ModelForm):
    # в класс мета, пишем модель, по которой будет строиться форма и перечисляем нужные нам поля.
    class Meta:
        model = Post
        fields = ['selection', 'postAuthor', 'postCategory', 'header', 'text']


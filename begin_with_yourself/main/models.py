from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

IDEA_SCALE = [
    ('ПОД', 'Подъезд'),
    ('ДВО', 'Двор'),
    ('РАЙ', 'Район'),
    ('ГОР', 'Город'),
    ('ОБЛ', 'Область'),
    ('СТР', 'Страна')
]


class IdeaModel(models.Model):

    text = models.CharField(
        verbose_name='Текст',
        help_text='Описание вашей идеи.',
        max_length=5000
    )

    pub_date = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='ideas'
    )

    scale = models.CharField(
        max_length=3,
        choices=IDEA_SCALE,
        default=IDEA_SCALE[0][0]
    )

    coordinate_x = models.FloatField(
        verbose_name='Координаты места',
        help_text='По этим коориднатам будет отражаться метка вашей идеи.',
        default=None
    )

    coordinate_y = models.FloatField(
        verbose_name='Координаты места',
        help_text='По этим коориднатам будет отражаться метка вашей идеи.',
        default=None
    )

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.text[:15]

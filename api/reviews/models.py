from django.db import models

class Reviews(models.Model):
    title = models.CharField(max_length=120, blank=True, verbose_name='Заголовок')
    video_link = models.URLField(max_length=200, null=True, blank=True, verbose_name='Ссылка на видео')
    img = models.ImageField(upload_to='reviews', null=True, blank=True, verbose_name='Фото')
    text = models.TextField(null=True, blank=True, verbose_name='Текст отзыва')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    comment = models.CharField(max_length=220, blank=True, verbose_name='Комментарий')

    class Meta:
        verbose_name_plural = 'Отзывы'
        verbose_name = 'Отзыв'
        ordering = ['-published']





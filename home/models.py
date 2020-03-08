from django.db import models
import datetime




class ContactForm(models.Model):
    name = models.CharField(blank=False, max_length=100, null = True, verbose_name='الاسم بالكامل')
    email = models.EmailField(verbose_name='بريدك الالكتروني')
    message = models.TextField(blank=False, null = True,verbose_name='كتابة الرسالة')
    timestamp = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = 'استمارة التواصل'
        verbose_name_plural = 'استمارة التواصل'

    def __str__(self):
        return self.name

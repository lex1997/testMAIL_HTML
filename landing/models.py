from django.db import models

class EMAIL(models.Model):
    email = models.EmailField()
    text = models.CharField(max_length=128)



    def __str__(self):
        return "Пиьмо от: %s     с текстом: %s" % (self.email, self.text, )

    class Meta:
        verbose_name = 'Emails'
        verbose_name_plural = 'A lot of Emails'
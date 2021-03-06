from django.db import models

# Модель для обработки вопроса
class Question(models.Model):
    text = models.CharField(max_length=500, default="")
    pub_date = models.DateTimeField('date published')
    # В момент конвертации в str()
    def __str__(self):
        return self.text

# Модель для обработки варианта ответа на вопрос
class Choice(models.Model):
    # Связываем Question и Choice
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=500, default="")
    votes = models.IntegerField(default=0)
    # В момент конвертации
    def __str__(self):
        return self.text
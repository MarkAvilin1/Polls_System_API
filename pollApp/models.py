from django.db import models

# Create models.

################### Опросы ###################
class Polls(models.Model):
    poll_title = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.poll_title

    class Meta:
        ordering = ('id',)

############### Вопросы ###############
class Questions(models.Model):
    poll = models.ForeignKey(Polls, related_name='questions', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=400)
    question_type = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text

    class Meta:
        ordering = ('id',)


############### Выбрать Ответ ###############
class Choices(models.Model):
    question = models.ForeignKey(Questions, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text

    class Meta:
        ordering = ('id',)


############### Ответы ###############
class Answers(models.Model):
    user_id = models.IntegerField()
    poll = models.ForeignKey(Polls, related_name='poll', on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, related_name='question', on_delete=models.CASCADE)
    choice = models.ForeignKey(Choices, related_name='choice', on_delete=models.CASCADE, null=True)
    choice_text = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.choice_text

    class Meta:
        ordering = ('id',)
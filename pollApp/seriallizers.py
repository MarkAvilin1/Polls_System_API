from rest_framework import serializers
from pollApp.models import *

################### Опросы ###################
class PollsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Polls
        fields = ('id', 'poll_title', 'start_time', 'end_time', 'description')

############### Вопросы ###############
class QuestionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Questions
        fields = ('id', 'question_text', 'question_type')

############### Выбрать Ответ ################
class ChoicesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choices
        fields = ('id', 'choice_text')

############### Выбрать Ответ ###############
class AnswersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answers
        fields = ('id', 'user_id', 'poll', 'question', 'answer', 'choice_text')

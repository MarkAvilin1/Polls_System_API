from rest_framework import serializers
from pollApp.models import *


class PollsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Polls
        fields = ('id', 'poll_title', 'start_time', 'end_time', 'description')

class QuestionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Questions
        fields = ('id', 'question_text', 'question_type')

class ChoicesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choices
        fields = ('id', 'choice_text')

class AnswersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answers
        fields = ('id', 'user_id', 'poll', 'question', 'answer', 'choice_text')

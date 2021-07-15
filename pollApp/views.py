from django.http.response import JsonResponse
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status

from pollApp.seriallizers import *
from pollApp.models import *

# Create your views here.
################POLLS#################
@api_view(['GET', 'POST'])
def poll_create(request):
    if request.method == 'GET':
        polls = Polls.objects.all()
        poll_title = request.GET.get('poll_title', None)
        start_time = request.GET.get('start_time', None)
        end_time = request.GET.get('end_time', None)
        description = request.GET.get('description', None)
        all_data = [poll_title, start_time, end_time, description]
        if all(all_data):
            polls = polls.filter(name_icontains=all_data)
            polls_serializer = PollsSerializer(polls, many=True)
            return JsonResponse(polls_serializer.data, safe=False)
        elif request.method == 'POST':
            polls_data = JSONParser().parse(request)
            polls_serializer = PollsSerializer(data=polls_data)
            if polls_serializer.is_valid():
                polls_serializer.save()
                return JsonResponse(polls_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(polls_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def poll_update(request, pk):
    try:
        polls = Polls.objects.get(pk=pk)
    except polls.DoesNotExist:
        return JsonResponse({'message': 'Нет опроса!'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        polls_serializer = PollsSerializer(polls)
        return JsonResponse(polls_serializer.data)
    elif request.method == 'PUT':
        polls_data = JSONParser().parse(request)
        polls_serializer = PollsSerializer(polls, data=polls_data)
        if polls_serializer.is_valid():
            polls_serializer.save()
            return JsonResponse(polls_serializer.data)
        return JsonResponse(polls_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        polls.delete()
        return JsonResponse({'message': 'Опрос был успешно удален'}, status=status.HTTP_204_NO_CONTENT)

#########################QUESTIONS####################
@api_view(['GET', 'POST'])
def question_create(request):
    if request.method == 'GET':
        questions = Questions.objects.all()
        question_text = request.GET.get('question_text', None)
        question_type = request.GET.get('question_type', None)
        all_data = [question_text, question_type]
        if all(all_data):
            questions = questions.filter(name_icontains=all_data)
            questions_serializer = QuestionsSerializer(questions, many=True)
            return JsonResponse(questions_serializer.data, safe=False)
        elif request.method == 'POST':
            questions_data = JSONParser().parse(request)
            questions_serializer = QuestionsSerializer(data=questions_data)
            if questions_serializer.is_valid():
                questions_serializer.save()
                return JsonResponse(questions_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(questions_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def question_update(request, pk):
    try:
        questions = Questions.objects.get(pk=pk)
    except questions.DoesNotExist:
        return JsonResponse({'message': 'Нет опроса!'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        questions_serializer = QuestionsSerializer(questions)
        return JsonResponse(questions_serializer.data)
    elif request.method == 'PUT':
        questions_data = JSONParser().parse(request)
        questions_serializer = QuestionsSerializer(questions, data=questions_data)
        if questions_serializer.is_valid():
            questions_serializer.save()
            return JsonResponse(questions_serializer.data)
        return JsonResponse(questions_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        questions.delete()
        return JsonResponse({'message': 'Вопрос был успешно удален'}, status=status.HTTP_204_NO_CONTENT)

##################CHOICES######################
@api_view(['GET', 'POST'])
def choice_create(request):
    if request.method == 'GET':
        choices = Choices.objects.all()
        choice_text = request.GET.get('choice_text', None)
        if choice_text is not None:
            choices = choices.filter(name_icontains=choice_text)
            choices_serializer = ChoicesSerializer(choices, many=True)
            return JsonResponse(choices_serializer.data, safe=False)
        elif request.method == 'POST':
            choices_data = JSONParser().parse(request)
            choices_serializer = ChoicesSerializer(data=choices_data)
            if choices_serializer.is_valid():
                choices_serializer.save()
                return JsonResponse(choices_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(choices_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def choice_update(request, pk):
    try:
        choices = Choices.objects.get(pk=pk)
    except choices.DoesNotExist:
        return JsonResponse({'message': 'Нет опроса!'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        choices_serializer = ChoicesSerializer(choices)
        return JsonResponse(choices_serializer.data)
    elif request.method == 'PUT':
        choices_data = JSONParser().parse(request)
        choices_serializer = ChoicesSerializer(choices, data=choices_data)
        if choices_serializer.is_valid():
            choices_serializer.save()
            return JsonResponse(choices_serializer.data)
        return JsonResponse(choices_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        choices.delete()
        return JsonResponse({'message': 'ВЫбор был успешно удален'}, status=status.HTTP_204_NO_CONTENT)

#######################Answers##################
@api_view(['GET', 'POST'])
def answer_create(request):
    if request.method == 'GET':
        answers = Answers.objects.all()
        user_id = request.GET.get('user_id', None)
        choice_text = request.GET.get('choice_text', None)
        all_data = [user_id, choice_text]
        if all(all_data):
            answers = answers.filter(name_icontains=all_data)
            answers_serializer = AnswersSerializer(answers, many=True)
            return JsonResponse(answers_serializer.data, safe=False)
        elif request.method == 'POST':
            answers_data = JSONParser().parse(request)
            answers_serializer = AnswersSerializer(data=answers_data)
            if answers_serializer.is_valid():
                answers_serializer.save()
                return JsonResponse(answers_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(answers_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def answer_update(request, pk):
    try:
        answers = Questions.objects.get(pk=pk)
    except answers.DoesNotExist:
        return JsonResponse({'message': 'Нет опроса!'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        answers_serializer = AnswersSerializer(answers)
        return JsonResponse(answers_serializer.data)
    elif request.method == 'PUT':
        answers_data = JSONParser().parse(request)
        answers_serializer = AnswersSerializer(answers, data=answers_data)
        if answers_serializer.is_valid():
            answers_serializer.save()
            return JsonResponse(answers_serializer.data)
        return JsonResponse(answers_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        answers.delete()
        return JsonResponse({'message': 'Ответ был успешно удален'}, status=status.HTTP_204_NO_CONTENT)

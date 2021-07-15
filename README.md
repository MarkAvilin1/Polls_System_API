# Polls_System_API
Задача: спроектировать и разработать API для системы опросов пользователей

# Installation guide
  ```
  pip install -r requirements.txt
  python manage.py makemigrations
  python manage.py migrate
  python manage.py createsuperuser
  python manage.py runserver
  ```
# API documentation

### Polls / Questions / Choices / Answers
#To view all Polls / Questions / Choices / Answers
* Request method: GET
* URL: http://localhost:8000/api/pc/ ...for polls
                                 qc/ ...for questions
                                 chc/ ...for choices
                                 ac/ ...for answers

#To create new Polls / Questions / Choices / Answers
* Request method: POST
* URL: http://localhost:8000/api/pc/ ...for polls
                                 qc/ ...for questions
                                 chc/ ...for choices
                                 ac/ ...for answers

#To view specific Polls / Questions / Choices / Answers
* Request method: GET
* URL: http://localhost:8000/api/pu/ ...for polls
                                 qu/ ...for questions
                                 chu/ ...for choices
                                 au/ ...for answers

#To update Polls / Questions / Choices / Answers
* Request method: PUT
* URL: http://localhost:8000/api/pu/ ...for polls
                                 qu/ ...for questions
                                 chu/ ...for choices
                                 au/ ...for answers

#To delete Polls / Questions / Choices / Answers
* Request method: DELETE
* URL: http://localhost:8000/api/pu/ ...for polls
                                 qu/ ...for questions
                                 chu/ ...for choices
                                 au/ ...for answers
  
# Admin registration
* email address: admin@admin.com
* Username: admin
* Password: admin

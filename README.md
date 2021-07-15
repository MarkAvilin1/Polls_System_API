## Polls_System_API
Задача: спроектировать и разработать API для системы опросов пользователей

## Installation guide
  ```
  pip install -r requirements.txt
  python manage.py makemigrations
  python manage.py migrate
  python manage.py createsuperuser
  python manage.py runserver
  ```
## API documentation

For Polls / Questions / Choices / Answers

To view all Polls / Questions / Choices / Answers
* Request method: GET
* URL: http://localhost:8000/api/pc/ ...for polls
* URL: http://localhost:8000/api/qc/ ...for questions
* URL: http://localhost:8000/api/chc/ ...for choices
* URL: http://localhost:8000/api/ac/ ...for answers

To create new Polls / Questions / Choices / Answers
* Request method: POST
* URL: http://localhost:8000/api/pc/ ...for polls
* URL: http://localhost:8000/api/qc/ ...for questions
* URL: http://localhost:8000/api/chc/ ...for choices
* URL: http://localhost:8000/api/ac/ ...for answers

To view specific Polls / Questions / Choices / Answers
* Request method: GET
* URL: http://localhost:8000/api/pu/ ...for polls
* URL: http://localhost:8000/api/qu/ ...for questions
* URL: http://localhost:8000/api/chu/ ...for choices
* URL: http://localhost:8000/api/au/ ...for answers

To update Polls / Questions / Choices / Answers
* Request method: PUT
* URL: http://localhost:8000/api/pu/ ...for polls
* URL: http://localhost:8000/api/qu/ ...for questions
* URL: http://localhost:8000/api/chu/ ...for choices
* URL: http://localhost:8000/api/au/ ...for answers

To delete Polls / Questions / Choices / Answers
* Request method: DELETE
* URL: http://localhost:8000/api/pu/ ...for polls
* URL: http://localhost:8000/api/qu/ ...for questions
* URL: http://localhost:8000/api/chu/ ...for choices
* URL: http://localhost:8000/api/au/ ...for answers
  
## Admin registration
* email address: admin@admin.com
* Username: admin
* Password: admin

# django-chat-notifications
setup Django channels as in documentation https://channels.readthedocs.io/en/latest/tutorial/part_1.html
then setup chat server as in https://channels.readthedocs.io/en/latest/tutorial/part_3.html

### setup notification message as follow 
1. The idea is to create unique channels group for each user(the unique for each user will be id may you can use another fields)
2. then this name you can use it later to send notfication on it to all acoonected devices

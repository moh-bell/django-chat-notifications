# chat/views.py
# Django Channels
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from datetime import datetime
from django.shortcuts import render

def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })

def home(request):
    current_user = request.user # Getting current user
    channel_layer = get_channel_layer()
    data = "notification"+ "...." + str(datetime.now()) # Pass any data based on your requirement
        # Trigger message sent to group
    async_to_sync(channel_layer.group_send)(
            str(current_user.pk),  # Group Name, Should always be string
            {
                "type": "notify",   # Custom Function written in the consumers.py
                "text": data,
            },
        )  


    return render(request,"chat/home.html" )
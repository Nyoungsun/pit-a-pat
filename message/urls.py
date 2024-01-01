from django.urls import path
from . import views

app_name = 'message'
urlpatterns = [
    path('createMessage', views.createMessage, name='createMessage'),
    path('editMessage/<int:message_uid>', views.editMessage, name="editMessage"),
    path('deleteMessage/<int:message_uid>', views.deleteMessage, name="deleteMessage"),
]

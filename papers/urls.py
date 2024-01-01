from django.urls import path
from . import views

app_name = "papers"
urlpatterns = [
    path('createPaper', views.createPaper, name="createPaper"),
    path('<int:paper_uid>', views.loadPaper, name="loadPaper"),
    path('deletePaper/<int:paper_uid>', views.deletePaper, name="deletePaper"),
    path('editPaper/<int:paper_uid>', views.editPaper, name="editPaper"),
]

from django.urls import path
from . import views

app_name = 'cars'
# domain.com/cars/list or add or delete
urlpatterns = [
    path('list/',views.list,name='list'),
    path('add/',views.add,name='add'),
    path('delete/',views.delete,name='delete')
]
from django.urls import path
from . import views

urlpatterns = [
    path('employee_table/', views.employee_table, name='employee_table'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('logout/', views.logout_view, name='logout'), 
]
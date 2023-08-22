from django.urls import path
from .import views


urlpatterns=[
    path('home/',views.home,name="home"),
    path('Employee_Table/',views.Employee_Table,name="Employee_Table"),
    path('Employee_leave/',views.Employee_leave,name="Employee_leave"),
    path('main_per/',views.main_per,name="main_per"), 
    path('emp_info/',views.emp_info,name = "emp_info"),
    path('leave_info/',views.leave_info,name="leave_info"),
    path('permission_info/',views.permission_info,name="permission_info"),

]
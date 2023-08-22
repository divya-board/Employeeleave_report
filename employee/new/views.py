from django.shortcuts import render
from django.http import HttpResponse
from .models import Emp
from .forms import EmpForm
from .models import Empleav
from .forms import EmpLeave
from .models import Empper
from .forms import EmpPermissionForm
import psycopg2

# Create your views here.
def home(request):
    return render(request,'employee.html')


def Employee_Table(request):
    print("calling the leave informaation")
    form = EmpForm() 
    if request.method == 'POST':
        form = EmpForm(request.POST)
        print(form)
        print('CHECK PROJECT FORM IS VALID OR NOT:' ,form.is_valid())
        if form.is_valid():
            print("saving all the data's:",form)
            form.save()
            print("save all the fields from the leaveinformation",form)
            form =EmpForm() 
            return render(request, 'emp_table.html',{'form':form,})
        else:
            print("FORM IS NOT VALID:" ,form)
            return render(request, 'emp_table.html',{'form':form})

    else:
        return render(request, 'emp_table.html',{'form':form})
    
def emp_info(request):
    obj=Emp.objects.all()
    context={
        "obj":obj,
    }
    return render(request,'emp_info.html',context)



def Employee_leave(request):
    print("calling the leaveinfo form")
    form = EmpLeave() 
    if request.method == 'POST':
        form = EmpLeave(request.POST)
        print(form)
        print('CHECK PROJECT FORM IS VALID OR NOT:' ,form.is_valid())
        if form.is_valid():
            print("saving all the data's:",form)
            form.save()
            print("save all the fields from the leaveinformation",form)
            form =EmpLeave() 
            return render(request, 'emp_leave.html',{'form':form})
        else:
            print("FORM IS NOT VALID:" ,form)
            return render(request, 'emp_leave.html',{'form':form})
    else:
        return render(request, 'emp_leave.html',{'form':form})

def leave_info(request):
    obj1=Empleav.objects.all()
    context={
        "obj1":obj1,
    }
    return render(request,'leave_info1.html',context)


def main_per(request):
    print("calling the leaveinfo form")
    form = EmpPermissionForm() 
    if request.method == 'POST':
        form = EmpPermissionForm(request.POST)
        print(form)
        print('CHECK PROJECT FORM IS VALID OR NOT:' ,form.is_valid())
        if form.is_valid():
            print("saving all the data's:",form)
            form.save()
            print("save all the fields from the leaveinformation",form)
            form = EmpPermissionForm() 
            return render(request, 'main.html',{'form':form})
        else:
            print("FORM IS NOT VALID:" ,form)
            return render(request, 'main.html',{'form':form})
    else:
        return render(request, 'main.html',{'form':form})




def permission_info(request):
    obj=Empper.objects.all()
    context={
        "obj":obj,
    }
    return render(request,'permission_det.html',context)


  
  
  

      


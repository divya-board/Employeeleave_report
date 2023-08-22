from django.db import models
from django.db import models
from django.utils import timezone




# Create your models here.
class Emp(models.Model):
    id = models.IntegerField(primary_key=True)
    name=models.CharField(max_length=200,null=True)
    designation = models.CharField(max_length=200,null=True) 
    date = models.DateField(default = timezone.now)
    def __str__(self):
        return f'{self.name}'

class Empleav(models.Model):
    emp_id = models.ForeignKey(Emp, null = True, on_delete=models.CASCADE)
    emp_name = models.CharField(max_length=200,null=True)
    leave_date_from = models.DateTimeField()
    leave_date_to = models.DateTimeField()
    leave_reason=models.CharField(max_length=200,null=True)
    leave_type=models.CharField(max_length=200,null=True)
    leave_session=models.CharField(max_length=200,null=True)
    Status = models.CharField(max_length=200,null=True)
    def __str__(self):
        return f'{self.emp_name}'

class Empper(models.Model):
    # name = models.ForeignKey(emp, on_delete=models.CASCADE)
    permission_date = models.DateTimeField()
    permissionTime_from = models.DateTimeField()
    permissionTime_To = models.DateTimeField()
    reason = models.CharField(max_length=200,null=True)
    Status = models.CharField(max_length=200,null=True)
    # def __str__(self):
    #     return f'{self.name}'
    








from django.db import models
    
class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.EmailField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    createBy = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        null=True,  # Allow null
        blank=True,  # Allow blank in forms
    )
    def __str__(self):
        return "name:{}, position:{}, email:{}, salary:{}, createBy:{}".format(self.name, self.position, self.email, self.salary, self.createBy)
    


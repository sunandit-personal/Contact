from django.db import models

# Create your models here.


class CommonFeatures(models.Model):
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    CRT_DT = models.DateTimeField(auto_now_add=True)
    UPDT_DT = models.DateTimeField(auto_now=True)


class Contact(CommonFeatures):
    first_name = models.CharField(
        "First Name", default="",  max_length=20, blank=True)
    last_name = models.CharField(
        "Last Name", max_length=20, blank=True, default="", null=True)
    email = models.EmailField(
        "Email", db_index=True, max_length=30, null=True, unique=True)
    phone = models.CharField(
        "phone number", max_length=14, blank=True, default="")

    class Meta:
        ordering = ('first_name',)

    def __str__(self):
        if self.first_name and self.phone:
            return self.first_name + ' -- ' + self.phone
        else:
            return self.id
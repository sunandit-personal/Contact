from rest_framework.generics import GenericAPIView
from django.contrib.auth.models import User
from contact.models import *

import json


class CreateOrUpdate(GenericAPIView):
    @staticmethod
    def contactCreateOrUpdate(self, data):
        instance = None
        if data.get('id'):
            instance = Contact.objects.filter(id=data.get('id')).last()
            con = CreateOrUpdate.all_contact(self, data, instance)
            return con
        if not instance:
            instance = Contact()
            con = CreateOrUpdate.all_contact(self, data, instance)
            return con

    def all_contact(self, data, instance):
        instance.first_name = data.get(
            "first_name") if "first_name" in data else instance.first_name if instance.first_name else None
        instance.last_name = data.get(
            "last_name") if "last_name" in data else instance.last_name if instance.last_name else None
        instance.email = data.get(
            "email") if "email" in data else instance.email if instance.email else None
        instance.phone = data.get(
            "phone") if "phone" in data else instance.phone if instance.phone else None
        instance.save()

        return instance
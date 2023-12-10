from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from django.contrib.auth.models import User
from contact.models import *



class ContactInfo(GenericAPIView):

    @staticmethod
    def ContactDetails(self, data):
        instance = None
        contact_id = None
        contact_first_name = None
        contact_last_name = None
        contact_phone = None
        contact_email = None
        is_active = True
        message = "Contact details fetched successfully."

        try:
            if data.get('id'):
                instance = Contact.objects.filter(id=data.get("id")).last()

            if instance:
                contact_id = instance.id
                contact_first_name = instance.first_name
                contact_last_name = instance.last_name
                contact_phone = instance.phone
                contact_email = instance.email
                is_active = instance.is_active
        except Exception as e:
            message = str(e)

        result = {
            "id": contact_id,
            "first_name": contact_first_name,
            "last_name": contact_last_name,
            "phone": contact_phone,
            "email": contact_email,
            "is_active": is_active,
            "message": message
        }

        return result


class ContactDeleteInfo(GenericAPIView):
    @staticmethod
    def ContactDelete(self, data):

        message = "Contact Deleted Successfully."

        try:
            if data.get('id'):
                Contact.objects.filter(id=data.get("id")).delete()

        except Exception as e:
            message = str(e)

        result = {
            "message": message
        }
        return result

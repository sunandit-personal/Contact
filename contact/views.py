from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status, parsers, renderers
from .models import Contact
from .forms import ContactForm
from rest_framework.views import APIView
from Contact.basics.common_return_type import Errors
from contact.create_or_update import CreateOrUpdate
from contact.info import ContactInfo, ContactDeleteInfo
from rest_framework.permissions import AllowAny, IsAuthenticated
from contact.serializers import ContactCreateSerializer, ContactDetailsSerializer, ContactListSerializer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


# Create your views here.


def list_contact(request):
    data = Contact.objects.all().order_by("id")
    return render(request, 'contact/contact_list.html', {'contacts': data})


def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'contact/contact_form.html', {'form': form})


def contact_detail(request, pk):
    record = get_object_or_404(Contact, pk=pk)
    return render(request, 'contact/contact_detail.html', {'contact': record})


def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contact/contact_form.html', {'form': form})


def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return redirect('contact_list')


class ContactView(GenericAPIView):
    """
    Contact APIS
    """
    permission_classes = (AllowAny,)
    serializer_class = ContactCreateSerializer

    @swagger_auto_schema(operation_summary="Contact Create", tags=['Contact'])
    def post(self, request, *args, **kwargs):
        response = {}
        data = request.data

        data_validation = ContactCreateSerializer(data=data)
        is_valid_data = data_validation.is_valid()

        if is_valid_data:
            data = data_validation.validated_data
            instance = CreateOrUpdate.contactCreateOrUpdate(
                self,
                data
            )
            response["id"] = instance.id
            response['message'] = "Contact Saved Successfully."
            status_code = status.HTTP_200_OK

        else:
            status_code = status.HTTP_400_BAD_REQUEST
            errorlist = [data_validation.errors]
            response["errors"] = Errors.combine_allErrors(errorlist)
            response["status"] = status_code

        return Response(response, status=status_code)

    @swagger_auto_schema(operation_summary="Contact Update", request_body=ContactCreateSerializer,
                         tags=['Contact'])
    def put(self, request, *args, **kwargs):
        response = {}
        data = request.data
        print(data)
        contact_id = data.get('id')
        if contact_id == "" or int(contact_id) <= 0:
            status_code = 400
            response["errors"] = "Please provide the contact_id"
            response["status"] = status.HTTP_400_BAD_REQUEST
            return Response(response, status=status_code)

        data_validation = ContactCreateSerializer(data=data)
        is_valid_data = data_validation.is_valid()

        if is_valid_data:
            data = data_validation.validated_data
            instance = CreateOrUpdate.contactCreateOrUpdate(
                self,
                data
            )
            response["id"] = instance.id
            response['message'] = "Contact Update Successfully."
            status_code = 200

        else:
            status_code = 400
            errorlist = [data_validation.errors]
            response["errors"] = Errors.combine_allErrors(errorlist)
            response["status"] = status_code

        return Response(response, status=status_code)

    @swagger_auto_schema(operation_summary="Contact Details", query_serializer=ContactDetailsSerializer,
                         tags=['Contact'])
    def get(self, request, *args, **kwargs):
        response = {}
        data = request.GET
        print(data)
        data_validation = ContactDetailsSerializer(data=data)
        is_valid_data = data_validation.is_valid()

        if is_valid_data:
            data = data_validation.validated_data
            response = ContactInfo.ContactDetails(
                self,
                data
            )
            status_code = 200

        else:
            status_code = 400
            errorlist = [data_validation.errors]
            response["errors"] = Errors.combine_allErrors(errorlist)
            response["status"] = status_code

        return Response(response, status=status_code)

    @swagger_auto_schema(operation_summary="Contact Delete", query_serializer=ContactDetailsSerializer,
                         tags=['Contact'])
    def delete(self, request, *args, **kwargs):
        response = {}

        contact_id = request.GET.get("id")

        Contact.objects.filter(id=contact_id).delete()
        response["message"] = "Contact deleted successfully"
        return Response(response, status=status.HTTP_200_OK)


class ContactList(ListAPIView):  # viewsets.ViewSet
    """
    API endpoint for contact list
    """
    serializer_class = ContactListSerializer
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer, renderers.BrowsableAPIRenderer)
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Contact.objects.all().order_by("id")
        return queryset

    def list(self, request):
        contacts = self.get_queryset().filter(is_deleted=False, is_active=True)
        page = self.paginate_queryset(contacts)

        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)
        else:
            serializer = self.serializer_class(contacts, many=True)
            return Response(serializer.data)

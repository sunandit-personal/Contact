from rest_framework import serializers
from .models import Contact


class ContactCreateSerializer(serializers.Serializer):
    id = serializers.IntegerField(
        required=False
    )
    first_name = serializers.CharField(
        required=True
    )
    last_name = serializers.CharField(
        required=False,
        allow_blank=True
    )
    phone = serializers.CharField(
        required=False
    )
    email = serializers.CharField(
        required=False,
    )
    is_active = serializers.BooleanField(
        default=True,
        required=False
    )
    is_deleted = serializers.BooleanField(
        default=False,
        required=False
    )

    def validate(self, data):

        errors = {}
        contact_id = data.get("id")
        email = data.get("email")
        isexists = Contact.objects.filter(email=email,  is_deleted=False, is_active=True)
        if contact_id is not None and contact_id > 0:
            isexists = isexists.exclude(id=contact_id).exists()
        else:
            isexists = isexists.exists()

        if isexists:
            errors["contact"] = "contact already exists."

        if errors:
            raise serializers.ValidationError(errors)

        return super(ContactCreateSerializer, self).validate(data)


class ContactDetailsSerializer(serializers.Serializer):
    id = serializers.IntegerField(
        required=True
    )

    def validate(self, data):

        errors = {}
        contact_id = data.get("id")
        if int(contact_id) <= 0 or contact_id == "":
            errors["contact"] = "Please select valid contact."
        item_exist = Contact.objects.filter(id=contact_id).exists()
        if not item_exist:
            errors["contact"] = "Contact does not exists."

        if errors:
            raise serializers.ValidationError(errors)

        return super(ContactDetailsSerializer, self).validate(data)


class ContactListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'
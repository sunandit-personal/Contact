from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.
from .models import Contact


class ContactModelTest(TestCase):
    def test_create_contact(self):
        # Test creating a Contact instance
        contact = Contact.objects.create(first_name='Sunandit', last_name='Chaudhuri', email='sunandit.chaudhuri@yahoo.com',
                                         phone='7596945239')

        # Check if the data was saved correctly
        self.assertEqual(contact.first_name, 'Sunandit')
        self.assertEqual(contact.last_name, 'Chaudhuri')
        self.assertEqual(contact.email, 'sunandit.chaudhuri@yahoo.com')
        self.assertEqual(contact.phone, '7596945239')



class ContactViewTest(TestCase):
    def setUp(self):
        self.new_contact_data = {'first_name': 'Arjun', 'last_name': 'Dutta', 'email': 'arjun.dutta@outlook.com',
                            'phone': '7594946697'}


    def contact_data(self):
        response = self.client.post(reverse('contact'), self.new_contact_data, format="json")
        return response


    def test_contact_create_view(self):
        # Test the contact create view
        response = self.contact_data()
        self.assertEqual(response.status_code, 200)

        # Check if the new contact is created
        self.created_contact = Contact.objects.get(first_name='Arjun')

        self.assertEqual(self.created_contact.last_name, 'Dutta')



    def test_contact_list_view(self):
        # Test the contact list view
        self.contact_data()
        response = self.client.get(reverse('contact_list'))
        self.assertEqual(response.status_code, 200)


    def test_contact_detail_view(self):
        # Test the contact detail view
        self.created_contact = self.contact_data()
        response = self.client.get(reverse('contact') + "?id=" + str(self.created_contact.json()["id"]))

        self.assertEqual(response.status_code, 200)


    def test_contact_update_view(self):
        # Test the contact update view
        self.created_contact = self.contact_data()
        updated_data = {'id': self.created_contact.json()["id"],
                        'first_name': 'Sunandit_edited', 'last_name': 'Chaudhuri_test',
                            'email': 'sunandit.chaudhuri@gmail.in', 'phone': '123456789'}

        response = self.client.put(reverse('contact'), data=updated_data, content_type='application/json')

        self.assertEqual(response.status_code, 200)

        # Check if the contact is updated
        updated_contact = Contact.objects.get(id=self.created_contact.json()["id"])
        self.assertEqual(updated_contact.last_name, 'Chaudhuri_test')
        self.assertEqual(updated_contact.first_name, 'Sunandit_edited')

    def test_contact_delete_view(self):
        # Test the contact delete view
        self.created_contact = self.contact_data()

        prev_db_count = Contact.objects.all().count()
        self.assertGreater(prev_db_count, 0)
        self.assertEqual(prev_db_count, 1)
        response = self.client.delete(reverse('contact') + "?id" + str(self.created_contact.json()["id"]))
        self.assertEqual(response.status_code, 200)

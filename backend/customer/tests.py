from django.test import TestCase
from .models import Customer

# Create your tests here.
class CustomerTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(name="Natic Company")
        Customer.objects.create(first_name="Jane", last_name="Doe")

    def test_name_when_first_last_entered(self):
        """when person, the first name - last name combine to populate
        name."""

        person = Customer.objects.get(first_name="Jane")
        person_first = person.first_name
        person_last = person.last_name
        name_test = person_first + " " + person_last

        self.assertEqual(person.name, name_test)

    def test_abstrsact_model_fields(self):
        """when using the abstract natic_template for standard fields.
        Fields are assigned."""

        customer = Customer.objects.get(first_name="Jane")

        self.assertTrue(customer.id, customer.created_date)

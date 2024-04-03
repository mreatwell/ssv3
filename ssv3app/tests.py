from django.test import TestCase
from .forms import YourForm

class YourFormTest(TestCase):
    def test_valid_form(self):
        data = {'name': 'Test', 'email': 'test@example.com'}
        form = YourForm(data=data)
        self.assertTrue(form.is_valid())

# Create your tests here.

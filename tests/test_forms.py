from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from taxi.forms import DriverCreationForm


class FormTest(TestCase):
    def test_driver_creation_form_with_valid_data(self):
        form_data = {"username": "new_test_user",
                     "password1": "pass12345",
                     "password2": "pass12345",
                     "first_name": "First",
                     "last_name": "Last",
                     "license_number": "ABC12345"}

        form = DriverCreationForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_driver_update_form(self):
        driver = get_user_model().objects.create_user(
            username="new_test_user1",
            password="pass12345",
            license_number="ABC12345",
            first_name="First",
            last_name="Last"
        )
        self.client.force_login(driver)

        new_data = {"license_number": "AAA54321"}

        self.client.post(reverse("taxi:driver-update", kwargs={"pk": driver.id}),
                         data=new_data)

        driver = get_user_model().objects.get(pk=driver.id)
        self.assertNotEqual(driver.license_number, new_data["license_number"])

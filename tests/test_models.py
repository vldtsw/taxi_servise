from django.contrib.auth import get_user_model
from django.test import TestCase

from taxi.models import Manufacturer, Car


class ModelTests(TestCase):
    def test_manufacturer_str(self):
        manufacturer = Manufacturer.objects.create(name="test_name",
                                                   country="test_country")

        self.assertEqual(str(manufacturer), f"{manufacturer.name} {manufacturer.country}")

    def test_driver_str(self):
        driver = get_user_model().objects.create_user(username="test_user",
                                                      password="test12345",
                                                      first_name="Test name",
                                                      last_name="Test name")

        self.assertEqual(str(driver), f"{driver.username} ({driver.first_name} {driver.last_name})")

    def test_car_str(self):
        manufacturer = Manufacturer.objects.create(name="Test name",
                                                   country="Test country")
        car = Car.objects.create(model="Test model",
                                 manufacturer=manufacturer)

        self.assertEqual(str(car), car.model)

    def test_create_driver_with_license_number(self):
        username = "test_username"
        password = "test12345"
        license_number = "test license"

        driver = get_user_model().objects.create_user(username=username,
                                                      password=password,
                                                      license_number=license_number)

        self.assertEqual(driver.username, username)
        self.assertTrue(driver.check_password(password))
        self.assertEqual(driver.license_number, license_number)

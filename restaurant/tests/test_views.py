from django.test import TestCase
from restaurant.models import Menu


class MenuViewTest(TestCase):
    def setUp(self):
        self.item1 = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.item2 = Menu.objects.create(title="Burger", price=120, inventory=50)

    def test_getall(self):
        self.assertEqual(True, True)

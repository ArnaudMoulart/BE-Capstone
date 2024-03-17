from django.test import TestCase
from restaurant.models import Menu


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(
            Title="Tanjia",
            Price=15.99,
            Inventory=4
        )
        self.assertEqual(item.__str__(), "Tanjia : 15.99")
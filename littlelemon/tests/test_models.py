from django.test import TestCase

from restaurant.models import Menu


class MenuTest(TestCase):
    """
    Tests for Menu model.
    """

    def __init__(self, *args, **kwargs):
        self.instances = []
        super().__init__(*args, **kwargs)

    def setUP(self):
        """
        Setup a test environment.
        """
        self.instance('IceCream', 80, 100)
        self.instance('IceCream', 80, 20)
        self.instance('Coffee', 50, 100)
        self.instance('Coffee', 25, 100)

    def instance(self, title, price, inventory):
        """
        Creates a new instance of the Menu model and saves it into `self.instances` list.
        :param title: str - the title of the menu item.
        :param price: int - the price of the menu item.
        :param inventory: int - the inventory of the menu item.
        """
        params = {
            'title': title,
            'price': price,
            'inventory': inventory
        }

        self.instances.append(zip(Menu.objects.create(**params), params))

    def test_get_item(self):
        """
        Test how serialized objects are retrieved. E.g. compare __str__ output of Menu instance with expected output.
        """
        for instance, params in self.instances:
            self.assertEqual(instance, f"{params['title']}: {params['price']}")

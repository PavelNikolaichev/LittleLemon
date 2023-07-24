from django.test import TestCase

from restaurant.models import Menu


class MenuViewTest(TestCase):
    """
    Tests for Menu view.
    """

    def __init__(self, *args, **kwargs):
        self.obj_params = []
        super().__init__(*args, **kwargs)

    def setUp(self):
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

        Menu.objects.create(**params)
        self.obj_params.append(params)

    def test_get_all(self):
        instances = Menu.objects.all()

        for instance, params in zip(instances, self.obj_params):
            self.assertEqual(instance.title, params['title'])
            self.assertEqual(instance.price, params['price'])
            self.assertEqual(instance.inventory, params['inventory'])

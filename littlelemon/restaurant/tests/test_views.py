from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from restaurant.views import MenuItemsView

class MenuItemTest(TestCase):
    def setUp(self):
        # Add test instances of the Menu model
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Lemonade", price=20, inventory=1)

    def test_getall(self):
        client = APIClient()
        url = reverse('menu-list')
        response = client.get(url)
        print(response)
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
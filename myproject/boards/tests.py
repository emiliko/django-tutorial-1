from django.test import TestCase
from django.urls import reverse

class HomeTests(TestCase):

    # test the status code of the response
    # status code 200 means success
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200) 


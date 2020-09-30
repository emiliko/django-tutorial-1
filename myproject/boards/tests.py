from django.test import TestCase
from django.urls import reverse
from django.urls import resolve
from .views import home

class HomeTests(TestCase):

    # test the status code of the response
    # status code 200 means success
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200) 

    # Django uses resolve function to match a requested URL with a list
    # of URLS listed in the urls.py module.
    # The test will make sure the URL /, which is the root URL,
    # is returning the home view. 
    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

from django.test import TestCase
from django.urls import reverse
from django.urls import resolve
from .views import home, board_topics
from .models import Board

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

class BoardTopicsTests(TestCase):

    # creates the Board instance to use in the tests
    # gotta do that because the Django testing suite doesn't run tests
    # against the current database
    def setUp(self):
        Board.objects.create(name='Django', description='Django board.')
    
    # test if django returns status code 200 (success) for an existing Board
    def test_board_topics_view_success_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
    
    # test if Django is returning a status code 404 (page not found) for a Board
    # that doesnät exist in the database
    def test_board_topics_view_not_found_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)
    
    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/boards/1/')
        self.assertEquals(view.func, board_topics)

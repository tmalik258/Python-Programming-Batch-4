from django.test import SimpleTestCase

# Create your tests here.

class HomePageViewTest(SimpleTestCase):
    def test_url_exists_at_correct_route(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)

class AboutPageViewTest(SimpleTestCase):
    def test_url_exists_at_correct_route(self):
        response = self.client.get('/about/')

        self.assertEqual(response.status_code, 200)

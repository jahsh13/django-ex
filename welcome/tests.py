import os

from .models import PageView
from .database import info
from django.test import TestCase

# These basic tests are to be used as an example for running tests in S2I
# and OpenShift when building an application image.
class PageViewModelTest(TestCase):
    def test_viewpage_model(self):
        print("Entering test_viewpage_model...")
        pageview = PageView.objects.create(hostname='localhost')
        pagetest = PageView.objects.get(hostname='localhost')
        self.assertEqual(pagetest.hostname, 'localhost')
        print("Leaving test_viewpage_model.  hostname = ",pagetest.hostname)

class PageViewTest(TestCase):
    def test_index(self):
        print("Entering test_index...")
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        print("Leaving test_index. status_code = ", resp.status_code)

class DbEngine(TestCase):
    def setUp(self):
        os.environ['ENGINE'] = 'SQLite'

    def test_engine_setup(self):
        print("Entering test_engine_setup...")
        settings = info()
        self.assertEqual(settings['engine'], 'SQLite')
        self.assertEqual(settings['is_sqlite'], True)
        print("Leaving test_engine_setup.  settings = ", settings)

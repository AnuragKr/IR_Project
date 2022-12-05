from django.test import TestCase
from data.service import DataService
import time
# Create your tests here.
class ServiceTest(TestCase):
  def setUp(self):
    self.ds = DataService()

  def test_data_insertion(self):
    self.ds.insert_data()
    time.sleep(2)
    self.ds.insert_tf_idf_data()


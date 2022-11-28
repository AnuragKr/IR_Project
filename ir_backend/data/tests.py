from django.test import TestCase
from data.service import DataService
# Create your tests here.
class ServiceTest(TestCase):
  def setUp(self):
    self.ds = DataService()

  # def test_index_creation(self):
  #   self.ds.create_index()
  
  def test_data_insertion(self):
    self.ds.insert_data()


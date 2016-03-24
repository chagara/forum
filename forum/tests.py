from django.test import TestCase
from .models import Section

# Create your tests here.
class ModelsTest(TestCase):

	def test_section_model_has_correct_attributes(self):
		first_section = Section.objects.create(name="Section1")
		saved_section = Section.objects.get(name="Section1")
		self.assertEquals(first_section.name, saved_section.name)

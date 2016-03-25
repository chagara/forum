from django.test import TestCase
from .models import Category, Section

# Create your tests here.
class ModelsTest(TestCase):

    def test_section_model_has_correct_attributes(self):
        first_section = Section.objects.create(name="Section1")
        saved_section = Section.objects.get(name="Section1")
        self.assertEquals(first_section.name, saved_section.name)

    def test_category_model_has_correct_attributes(self):
        section = Section.objects.create(name="Section")
        first_category = Category.objects.create(
            name="Category1",
            description="description",
            section=section)
        saved_category = Category.objects.get(name="Category1")
        self.assertEquals(first_category.name, saved_category.name)

    def test_each_category_belongs_to_a_section(self):
        section = Section.objects.create(name="Section")
        category = Category.objects.create(name="Category", section=section)
        saved_category = Category.objects.get(name="Category")
        self.assertEquals(saved_category.section, section)

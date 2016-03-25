from django.test import TestCase
from django.utils import timezone

from .models import Category, Section, Thread

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

    def test_thread_model_has_correct_attributes(self):
        datetime_posted = timezone.now()
        category = Category.objects.create()
        first_thread = Thread.objects.create(
            name="The first thread",
            datetime_posted=datetime_posted,
            category=category)
        saved_thread = Thread.objects.first()

        self.assertEquals(first_thread, saved_thread)
        self.assertEquals(datetime_posted, saved_thread.datetime_posted)

    def test_each_thread_belongs_to_a_category(self):
        section = Section.objects.create()
        category = Category.objects.create(name="A category", section=section)
        thread = Thread.objects.create(
            name="Thread",
            datetime_posted=timezone.now(),
            category=category)

        self.assertEquals(thread.category, category)

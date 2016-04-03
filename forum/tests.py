from django.test import TestCase
from django.utils import timezone

from .models import Category, Comment, Section, Thread


class ModelsTest(TestCase):

    def test_section_model_has_correct_attributes(self):
        first_section = Section(name="Section1")
        self.assertEquals(first_section.name, "Section1")

    def test_category_model_has_correct_attributes(self):
        section = Section(name="Section")
        first_category = Category(
            name="Category1",
            description="description",
            section=section)
        self.assertEquals(first_category.name, "Category1")

    def test_each_category_belongs_to_a_section(self):
        section = Section(name="Section")
        category = Category(name="Category", section=section)
        self.assertEquals(category.section, section)

    def test_thread_model_has_correct_attributes(self):
        datetime_posted = timezone.now()
        section = Section()
        category = Category(section=section)
        first_thread = Thread(
            name="The first thread",
            datetime_posted=datetime_posted,
            category=category)

        self.assertEquals(first_thread.name, "The first thread")
        self.assertEquals(datetime_posted, first_thread.datetime_posted)

    def test_each_thread_belongs_to_a_category(self):
        section = Section()
        category = Category(name="A category", section=section)
        thread = Thread(
            name="Thread",
            datetime_posted=timezone.now(),
            category=category)

        self.assertEquals(thread.category, category)

    def test_comment_model_has_correct_attributes(self):
        datetime_posted = timezone.now()
        section = Section()
        category = Category(section=section)
        thread = Thread(
            datetime_posted=datetime_posted, category=category)

        comment = Comment(
            text="The first comment",
            author="Someone",
            datetime_posted=datetime_posted,
            thread=thread)

        self.assertEquals(comment.text, "The first comment")
        self.assertEquals(comment.author, "Someone")
        self.assertEquals(
            comment.datetime_posted, datetime_posted)

    def test_each_comment_belongs_to_a_thread(self):
        section = Section()
        category = Category(section=section)
        thread = Thread(
            datetime_posted=timezone.now(),
            category=category)
        comment = Comment(
            text="Some text",
            author="Someone",
            datetime_posted=timezone.now(),
            thread=thread)

        self.assertEquals(comment.thread, thread)

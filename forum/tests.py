from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User

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

    def test_comment_model_has_correct_attributes(self):
        the_user = User('user1', 'user1@example.com', 'password1')
        datetime_posted = timezone.now()
        section = Section()
        category = Category(section=section)
        thread = Thread(
            datetime_posted=datetime_posted, category=category,
            author=the_user)
        comment = Comment(
            text="The first comment",
            author=the_user,
            datetime_posted=datetime_posted,
            thread=thread)

        self.assertEquals(comment.text, "The first comment")
        self.assertEquals(comment.author, the_user)
        self.assertEquals(
            comment.datetime_posted, datetime_posted)
        self.assertEquals(comment.thread, thread)


class HomeViewTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/home.html')

    def test_passes_correct_context_to_template(self):
        section = Section.objects.create(name="A section")
        response = self.client.get('/')
        self.assertEqual(
            [section.name for section in response.context['sections']],
            ["A section"]
        )

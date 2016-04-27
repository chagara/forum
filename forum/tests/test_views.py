from django.test import TestCase
from forum.models import Section


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

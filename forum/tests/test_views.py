from django.test import TestCase
from forum.models import Section


class HomeViewTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/home.html')

    def test_passes_sections_context_to_template(self):
        Section.objects.create(name="A section")
        sections = Section.objects.all()
        response = self.client.get('/')

        response_sections = response.context['sections']
        self.assertEqual(list(response_sections), list(sections))


class SectionViewTest(TestCase):

    def test_uses_section_template(self):
        section = Section.objects.create(name="Section")
        response = self.client.get('/section/%d/' % (section.id,))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/section.html')

    def test_passes_section_context_to_template(self):
        section = Section.objects.create(name="Section1")
        response = self.client.get('/section/%d/' % (section.id,))
        self.assertIn('section', response.context)
        self.assertEqual("Section1", response.context['section'].name)

    def test_invalid_section_id_raises_404(self):
        response = self.client.get('/section/87/')
        self.assertEqual(response.status_code, 404)

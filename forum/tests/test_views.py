from django.test import TestCase
from forum.models import Section, Category, Thread


class HomeViewTest(TestCase):

    fixtures = ['test_forum_structure']

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/home.html')

    def test_passes_sections_context_to_template(self):
        sections = Section.objects.all()
        response = self.client.get('/')

        response_sections = response.context['sections']
        self.assertEqual(list(response_sections), list(sections))


class SectionViewTest(TestCase):

    fixtures = ['test_forum_structure']

    def test_uses_section_template(self):
        section = Section.objects.first()
        response = self.client.get('/section/%d/' % (section.id,))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/section.html')

    def test_passes_section_context_to_template(self):
        section = Section.objects.get(name="Section1")
        response = self.client.get('/section/%d/' % (section.id,))
        self.assertIn('section', response.context)
        self.assertEqual("Section1", response.context['section'].name)

    def test_invalid_section_id_raises_404(self):
        response = self.client.get('/section/87ab3/')
        self.assertEqual(response.status_code, 404)

    def test_passes_categories_context_to_template(self):
        categories = Category.objects.all()
        response = self.client.get('/section/1/')
        # Need to changed the name of the response_sections variable
        response_sections = response.context['categories']
        self.assertEqual(list(response_sections), list(categories))


class CategoryViewTest(TestCase):

    fixtures = ['test_forum_structure']

    def test_uses_category_template(self):
        category = Category.objects.first()
        response = self.client.get('/category/%d/' % (category.id,))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/category.html')

    def test_passes_category_context_to_template(self):
        category = Category.objects.get(name="Category1")
        response = self.client.get('/category/%d/' % (category.id,))
        self.assertIn('category', response.context)
        self.assertEqual("Category1", response.context['category'].name)

    def test_invalid_category_id_raises_404(self):
        response = self.client.get('/category/87ab3/')
        self.assertEqual(response.status_code, 404)

    def test_passes_threads_context_to_template(self):
        category = Category.objects.get(name="Category1")
        threads = Thread.objects.filter(category__id=category.id)
        response = self.client.get('/category/%d/' % (category.id,))

        response_threads = response.context['threads']
        self.assertEqual(list(response_threads), list(threads))

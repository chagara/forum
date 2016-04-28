from django.test import TestCase
from forum.models import Section, Category, Thread, Comment


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

    def test_uses_detail_template(self):
        section = Section.objects.first()
        response = self.client.get('/section/%d/' % (section.id,))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/detail.html')

    def test_passes_page_title_to_context(self):
        section = Section.objects.get(name="Section1")
        response = self.client.get('/section/%d/' % (section.id,))
        self.assertIn('page_title', response.context)
        self.assertEqual(section.name, response.context['page_title'])

    def test_passes_forum_children_to_context(self):
        section = Section.objects.get(name="Section1")
        categories = Category.objects.filter(section__pk=section.id)
        response = self.client.get('/section/%d/' % (section.id))

        self.assertIn("forum_children", response.context)
        response_categories = response.context['forum_children']
        self.assertEqual(list(response_categories), list(categories))

    def test_passes_section_context_to_template(self):
        section = Section.objects.get(name="Section1")
        response = self.client.get('/section/%d/' % (section.id,))
        self.assertIn('section', response.context)
        self.assertEqual("Section1", response.context['section'].name)

    def test_invalid_section_id_raises_404(self):
        response = self.client.get('/section/87ab3/')
        self.assertEqual(response.status_code, 404)

    def test_passes_categories_context_to_template(self):
        section = Section.objects.get(name="Section1")
        categories = Category.objects.filter(section__pk=section.id)
        response = self.client.get('/section/%d/' % (section.id))

        response_categories = response.context['categories']
        self.assertEqual(list(response_categories), list(categories))


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
        response = self.client.get('/category/984357/')
        self.assertEqual(response.status_code, 404)

    def test_passes_threads_context_to_template(self):
        category = Category.objects.get(name="Category1")
        threads = Thread.objects.filter(category__id=category.id)
        response = self.client.get('/category/%d/' % (category.id,))

        response_threads = response.context['threads']
        self.assertEqual(list(response_threads), list(threads))


class ThreadViewTest(TestCase):

    fixtures = ['test_forum_structure']

    def test_uses_thread_template(self):
        thread = Thread.objects.first()
        response = self.client.get('/thread/%d/' % (thread.id,))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/thread.html')

    def test_passes_thread_context_to_template(self):
        thread = Thread.objects.get(name="Thread1")
        response = self.client.get('/thread/%d/' % (thread.id,))
        self.assertIn('thread', response.context)
        self.assertEqual("Thread1", response.context['thread'].name)

    def test_invalid_thread_id_raises_404(self):
        response = self.client.get('/thread/2398743/')
        self.assertEqual(response.status_code, 404)

    def test_passes_comments_context_to_template(self):
        thread = Thread.objects.get(name="Thread1")
        comments = Comment.objects.filter(thread__pk=thread.id)
        response = self.client.get('/thread/%d/' % (thread.id,))

        response_comments = response.context['comments']
        self.assertEqual(list(response_comments), list(comments))

from django.test import TestCase
from forum.models import Section, Category, Thread, Comment


class HomeViewTest(TestCase):

    fixtures = ['test_forum_structure']

    def test_uses_overview_template(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/overview.html')

    def test_passes_page_title_to_template(self):
        response = self.client.get('/')
        self.assertEqual("DjangoLearners", response.context['page_title'])

    def test_passes_child_url_to_template(self):
        response = self.client.get('/')
        self.assertEqual("forum:section_view", response.context['child_url'])

    def test_passes_child_class_to_template(self):
        response = self.client.get('/')
        self.assertEqual("section", response.context['child_class'])

    def test_passes_sections_to_template(self):
        sections = Section.objects.all()
        response = self.client.get('/')
        response_sections = response.context['children']
        self.assertEqual(list(response_sections), list(sections))


class SectionViewTest(TestCase):

    fixtures = ['test_forum_structure']

    def test_uses_detail_template(self):
        section = Section.objects.first()
        response = self.client.get('/section/%d/' % (section.id,))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/overview.html')

    def test_passes_page_title_to_context(self):
        section = Section.objects.get(name="Section1")
        response = self.client.get('/section/%d/' % (section.id,))
        self.assertIn('page_title', response.context)
        self.assertEqual(section.name, response.context['page_title'])

    def test_passes_child_class_to_context(self):
        section = Section.objects.get(name="Section1")
        response = self.client.get('/section/%d/' % (section.id,))
        self.assertIn('child_class', response.context)
        self.assertEqual("category", response.context['child_class'])

    def test_passes_child_url_to_context(self):
        section = Section.objects.get(name="Section1")
        response = self.client.get('/section/%d/' % (section.id,))
        self.assertIn('child_url', response.context)
        self.assertEqual('forum:category_view', response.context['child_url'])

    def test_passes_children_to_context(self):
        section = Section.objects.get(name="Section1")
        categories = Category.objects.filter(section__pk=section.id)
        response = self.client.get('/section/%d/' % (section.id))

        self.assertIn("children", response.context)
        response_children = response.context['children']
        self.assertEqual(list(response_children), list(categories))

    def test_invalid_section_id_raises_404(self):
        response = self.client.get('/section/87ab3/')
        self.assertEqual(response.status_code, 404)


class CategoryViewTest(TestCase):

    fixtures = ['test_forum_structure']

    def test_uses_overview_template(self):
        category = Category.objects.first()
        response = self.client.get('/category/%d/' % (category.id,))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/overview.html')

    def test_passes_page_title_to_template(self):
        category = Category.objects.get(name="Category1")
        response = self.client.get('/category/%d/' % (category.id,))
        self.assertEqual(category.name, response.context['page_title'])

    def test_passes_child_url_to_template(self):
        category = Category.objects.get(name="Category1")
        response = self.client.get('/category/%d/' % (category.id,))
        self.assertEqual("forum:thread_view", response.context['child_url'])

    def test_passes_child_class_to_template(self):
        category = Category.objects.get(name="Category1")
        response = self.client.get('/category/%d/' % (category.id,))
        self.assertEqual("thread", response.context['child_class'])

    def test_invalid_category_id_raises_404(self):
        response = self.client.get('/category/984357/')
        self.assertEqual(response.status_code, 404)

    def test_passes_threads_to_template(self):
        category = Category.objects.get(name="Category1")
        threads = Thread.objects.filter(category__id=category.id)
        response = self.client.get('/category/%d/' % (category.id,))

        response_threads = response.context['children']
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

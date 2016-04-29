from functional_test.base import FunctionalTest


class ForumStructureTest(FunctionalTest):

    fixtures = ['test_forum_structure']

    def test_forum_structure(self):
        # Goes to the home page
        self.browser.get(self.live_server_url)
        self.assertEqual(self.browser.current_url, self.live_server_url + '/')

        # Sees DjangoLearners in the title
        self.assertEqual(self.browser.title, "DjangoLearners")

        # There is a table of Sections on the page
        children_table = self.browser.find_element_by_id("children")

        # Sees Section1 and Section2 in the table
        self.assertIn("Section1", children_table.text)
        self.assertIn("Section2", children_table.text)

        # Clicks Section1
        sections = children_table.find_elements_by_class_name("section")
        if len(sections) == 0:
            self.fail("No sections found")
        for section in sections:
            if section.text == "Section1":
                section.click()
                break
        else:
            self.fail("Section1 not found")

        # Is taken to a page which shows the categories in the section
        self.assertEqual(
            self.browser.current_url,
            self.live_server_url + '/section/1/')
        self.assertEqual(self.browser.title, "Section1")

        children_table = self.browser.find_element_by_id("children")

        # Sees Category1 but not Category2 (it's in a different section)
        self.assertIn("Category1", children_table.text)
        self.assertNotIn("Category2", children_table.text)

        # Clicks Category1
        categories = children_table.find_elements_by_class_name(
            "category")
        if len(categories) == 0 :
            self.fail("No categories found")
        for category in categories:
            if category.text == "Category1":
                category.click()
                break
        else:
            self.fail("Category1 not found")

        # Is taken to a page which shows the threads in Category1
        self.assertEqual(
            self.browser.current_url,
            self.live_server_url + '/category/1/')
        self.assertEqual(self.browser.title, "Category1")

        children_table = self.browser.find_element_by_id("children")

        # Sees Thread1 but not Thread2 (because it's in a different category)
        self.assertIn("Thread1", children_table.text)
        self.assertNotIn("Thread2", children_table.text)

        # Clicks Thread1
        threads = children_table.find_elements_by_class_name(
            "thread")
        if len(threads) == 0:
            self.fail("No threads found")
        for Thread in threads:
            if Thread.text == "Thread1":
                Thread.click()
                break
        else:
            self.fail("Thread1 not found")

        # Is taken to a page which shows all of the comments in Thread1
        self.assertEqual(
            self.browser.current_url,
            self.live_server_url + '/thread/1/')
        self.assertEqual(self.browser.title, "Thread1")

        comments_table = self.browser.find_element_by_id("comments")

        # Sees Comment1 but not Comment2 (because it's in a different thread)
        self.assertIn("Comment1", comments_table.text)
        self.assertNotIn("Comment2", comments_table.text)

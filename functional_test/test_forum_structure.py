from functional_test.base import FunctionalTest


class ForumStructureTest(FunctionalTest):

    fixtures = ['test_forum_structure']

    def test_forum_structure(self):
        # Goes to the home page
        self.browser.get(self.live_server_url)
        self.assertEqual(self.browser.current_url, self.live_server_url + '/')

        # Sees DjangoLearners in the title and heading
        self.assertEqual(self.browser.title, "DjangoLearners")
        heading_text = self.browser.find_element_by_tag_name('h1').text
        self.assertEqual(heading_text, "DjangoLearners")

        # There is a table of Sections on the page
        sections_table = self.browser.find_element_by_id("sections")

        # Sees Section1 and Section2 in the table
        self.assertIn("Section1", sections_table.text)
        self.assertIn("Section2", sections_table.text)

        # Clicks Section1
        sections = sections_table.find_elements_by_class_name("section")
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

        categories_table = self.browser.find_element_by_id("forum_children")

        # Sees Category1 but not Category2 (it's in a different section)
        self.assertIn("Category1", categories_table.text)
        self.assertNotIn("Category2", categories_table.text)

        # Clicks Category1
        categories = categories_table.find_elements_by_class_name(
            "category")
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

        threads_table = self.browser.find_element_by_id("threads")

        # Sees Thread1 but not Thread2 (because it's in a different category)
        self.assertIn("Thread1", threads_table.text)
        self.assertNotIn("Thread2", threads_table.text)

        # Clicks Thread1
        threads = threads_table.find_elements_by_class_name(
            "thread")
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

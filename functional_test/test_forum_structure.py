from functional_test.base import FunctionalTest


class BasicForumStructureTest(FunctionalTest):

    fixtures = ['test_forum_structure']

    def click_child_in_children_table(self, children_table, class_, target):
        children = children_table.find_elements_by_class_name(class_)
        if len(children) == 0:
            self.fail("No %ss found" % (class_,))
        for child in children:
            if child.text == target:
                child.click()
                break
        else:
            self.fail("%s not found" % (target,))

    def test_basic_forum_structure(self):
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
        self.click_child_in_children_table(
            children_table, "section", "Section1")

        # Is taken to a page which shows the categories in the section
        self.assertEqual(
            self.browser.current_url,
            self.live_server_url + '/section/1/')
        self.assertEqual(self.browser.title, "Section1")

        # Sees Category1 but not Category2 (it's in a different section)
        children_table = self.browser.find_element_by_id("children")
        self.assertIn("Category1", children_table.text)
        self.assertNotIn("Category2", children_table.text)

        # Clicks Category1
        self.click_child_in_children_table(
            children_table, "category", "Category1")

        # Is taken to a page which shows the threads in Category1
        self.assertEqual(
            self.browser.current_url,
            self.live_server_url + '/category/1/')
        self.assertEqual(self.browser.title, "Category1")

        # Sees Thread1 but not Thread2 (because it's in a different category)
        children_table = self.browser.find_element_by_id("children")
        self.assertIn("Thread1", children_table.text)
        self.assertNotIn("Thread2", children_table.text)

        # Clicks Thread1
        self.click_child_in_children_table(
            children_table, "thread", "Thread1")

        # Is taken to a page which shows all of the comments in Thread1
        self.assertEqual(
            self.browser.current_url,
            self.live_server_url + '/thread/1/')
        self.assertEqual(self.browser.title, "Thread1")

        # Sees Comment1 but not Comment2 (because it's in a different thread)
        comments_table = self.browser.find_element_by_id("comments")
        self.assertIn("Comment1", comments_table.text)
        self.assertNotIn("Comment2", comments_table.text)

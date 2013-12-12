from django.test import TestCase
from models import Page
from django.utils import timezone
from django.db import IntegrityError
# Create your tests here.


class TestForPages(TestCase):

    def create_page(self, word, content, creation_date):
        return Page.objects.create(word=word,
                                   content=content,
                                   creation_date=creation_date)

    def test_add_instance(self):
        Page.objects.create(word='try',
                            content="This is a try",
                            creation_date=timezone.now())

        pages = Page.objects.all()
        self.assertEqual(len(pages), 1)

    #def test_word_with_capital_letter(self):
    #    self.assertEqual(Page.objects.create(
    #        word='CaPital!',
    #        content='This should fail',
    #        creation_date=timezone.now()
    #        ), "Enter a valid value."
    #    )

    #def test_double_entry(self):
    #
    #    #Page.objects.clear()
    #    self.create_page(word='try',
    #                     content="This is a try",
    #                     creation_date=timezone.now())
    #    #pages = Page.objects.all()
    #    self.assertRaises(IntegrityError,
    #                      self.create_page(
    #                          word='try',
    #                          content="This is a try",
    #                        creation_date=timezone.now())
    #    )
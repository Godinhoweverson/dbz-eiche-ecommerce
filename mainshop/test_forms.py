from django.test import TestCase
from mainshop.forms import CommentForm, EditCommentForm

class TestCommentForms(TestCase):
    def test_comment_form_valid_data(self):
        form = CommentForm(data={'text': 'This is a test comment'})
        self.assertTrue(form.is_valid())

    def test_comment_form_no_data(self):
        form = CommentForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    def test_edit_comment_form_valid_data(self):
        form = EditCommentForm(data={'text': 'Edited comment'})
        self.assertTrue(form.is_valid())

    def test_edit_comment_form_no_data(self):
        form = EditCommentForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)
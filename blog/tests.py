from django.test import TestCase
from django.urls import reverse

# Create your tests here.


# class EntryDetailViewTests(TestCase):

#     def test_submit_invalid_comment(self):
#         """
#         status 200 form is re-rendered because of value error
#         """
#         response = self.client.post(
#             reverse('blog:comment', kwargs={'entry_id': 1}), {'comment': 'shrt'})
#         self.assertEqual(response.status_code, 200)

#     def test_submit_valid_comment(self):
#         """
#         status 302 form is submitted and value is saved to DB
#         """
#         response = self.client.post(
#             reverse('blog:comment', kwargs={'entry_id': 1}), {'comment': 'long enouugh'})
#         self.assertEqual(response.status_code, 302)

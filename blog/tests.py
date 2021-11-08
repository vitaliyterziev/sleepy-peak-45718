from django.utils import timezone
from datetime import date
from django.test import TestCase
from django.urls import reverse
from .models import Entry

# Create your tests here.


class IndexView(TestCase):
    def test_no_entries(self):
        """
        If no posts exist, an appropriate message is displayed
        """
        response = self.client.get(reverse('blog:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No posts are available.")
        self.assertQuerysetEqual(response.context['latest_entry_list'], [])


class EntryDetailViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # prepare at least 1 test database record because test DB is empty
        Entry.objects.create(entry_title='test1',
                             entry_content='test1', pub_date=timezone.now())

    def test_submit_invalid_comment(self):
        """
        status 200, form is re-rendered because of value error
        """
        response = self.client.post(
            reverse('blog:comment', kwargs={'entry_id': 1}), {'comment': 'shrt'})
        self.assertEqual(response.status_code, 200)

    def test_submit_valid_comment(self):
        """
        status 302, form is submitted and value is saved to DB
        """
        response = self.client.post(
            reverse('blog:comment', kwargs={'entry_id': 1}), {'comment': 'long enouugh'})
        self.assertEqual(response.status_code, 302)


class EntryMonthArchiveViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # prepare at least 1 test database record because test DB is empty
        Entry.objects.create(entry_title='test1',
                             entry_content='test1', pub_date=date(2021, 11, 3))

    def test_valid_month_archive(self):
        """
        status 200, valid month archive
        """
        response = self.client.get(
            reverse('blog:archive_month_numeric', kwargs={'year': 2021, 'month': 11}))
        self.assertEqual(response.status_code, 200)

    def test_invalid_month_archive(self):
        """
        status 404, the month archive does not exist
        """
        response = self.client.get(
            reverse('blog:archive_month_numeric', kwargs={'year': 2021, 'month': 12}))
        self.assertEqual(response.status_code, 404)


class MembershipFormView(TestCase):
    def test_submit_email(self):
        """
        test creating a new membership record, 302 email is in the DB
        """
        response = self.client.post(
            reverse('blog:subscribe'), {'email_address': 'vito@gmail.com'})
        self.assertEqual(response.status_code, 302)

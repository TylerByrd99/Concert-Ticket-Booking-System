# TO RUN THIS TEST
# Go to the terminal in the bottom, then youre going to run this command
# "py manage.py test"

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from MyApps.models import Performance, Concert, Venue, Ticket


class ViewTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

        self.concert = Concert.objects.create(artist='Test Artist')
        self.venue = Venue.objects.create(name='Test Venue', city='Test City', state='Test State')
        self.performance = Performance.objects.create(concert=self.concert, venue=self.venue, date='2023-05-01')

        self.ticket = Ticket.objects.create(performance=self.performance, user=self.user, quantity=2)

    def test_home_view(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_login_view(self):
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_profile_view(self):
        url = reverse('profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')

    def test_find_shows_view(self):
        url = reverse('find_shows')
        response = self.client.post(url, {'searched': 'Test Artist'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'find_shows.html')
        self.assertEqual(response.context['searched'], 'Test Artist')
        self.assertEqual(response.context['performance'], self.performance)

        response = self.client.post(url, {'searched': 'Invalid Artist'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'find_shows.html')
        self.assertEqual(response.context['searched'], 'Invalid Artist')
        self.assertIsNone(response.context['performance'])

    def test_sign_up_view(self):
        url = reverse('sign_up')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sign_up.html')

    def test_tickets_view(self):
        url = reverse('tickets')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tickets.html')

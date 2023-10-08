import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
        
        
class PollsURLsTest(TestCase):
    def test_index_url(self):
        url = reverse("polls:index")
        self.assertEqual(url, "/polls/")

    def test_detail_url(self):
        # Assuming pk=1 for testing purposes
        url = reverse("polls:detail", args=[1])
        self.assertEqual(url, "/polls/1/")

    def test_results_url(self):
        # Assuming pk=1 for testing purposes
        url = reverse("polls:results", args=[1])
        self.assertEqual(url, "/polls/1/results/")

    def test_vote_url(self):
        # Assuming question_id=1 for testing purposes
        url = reverse("polls:vote", args=[1])
        self.assertEqual(url, "/polls/1/vote/")

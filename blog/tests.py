from django.test import TestCase
from . import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta

User = get_user_model()

# Create your tests here.
class BaseTestCase(TestCase):
    def setUp(self):
        # users
        user1 = User.objects.create(username='user1', email='user1@test.com', password='password')
        user2 = User.objects.create(username='user2', email='user2@test.com', password='password')

        # posts
        models.Post.objects.create(
            title='Current Post',
            body='This is a wonderful post.',
            author=user1,
            published_at=timezone.now() - timedelta(days=1)
        )

        models.Post.objects.create(
            title='Future Post',
            body='Another wonderful post to come.',
            author=user2,
            published_at=timezone.now() + timedelta(days=1)
        )

class PostTestCase(BaseTestCase):
    def test_current_post_is_published(self):
        post = models.Post.objects.get(title='Current Post')
        self.assertTrue(post.published)

    def test_future_post_is_not_published(self):
        post = models.Post.objects.get(title='Future Post')
        self.assertFalse(post.published)

    def test_unable_to_like_multiple_times(self):
        user1 = User.objects.get(username='user1')
        post = models.Post.objects.get(title='Current Post')
        post.likes.add(user1)
        post.likes.add(user1)
        self.assertEqual(post.number_of_likes, 1)


class CommentTestCase(TestCase):
    def setUp(self):
        super().setUp()
        current_post = models.Post.objects.get(title='Current Post')
        future_post = models.Post.objects.get(title='Future Post')
        
        user1 = models.User.objects.get(username='user1')
        user2 = models.User.objects.get(username='user2')

        models.Comment.objects.create(
            author=user1,
            post=future_post,
            body='What a great post.'
        )

        models.Comment.objects.create(
            author=user2,
            post=current_post,
            body='Thanks for posting this.'
        )

    def test_unable_to_like_multiple_times(self):
        comment = models.Comment.objects.get(
            body='Thanks for posting this.'
        )
        user1 = models.User.objects.get(username='user1')
        comment.likes.add(user1)
        comment.likes.add(user1)
        self.assertEqual(comment.number_of_likes, 1)
import graphene
from graphene_django import DjangoConnectionField, DjangoObjectType
from graphql_auth.relay import UserNode

from . import models


class PostNode(DjangoObjectType):
    published = graphene.Boolean(source='published')
    banner_url = graphene.String(source='banner_url')
    number_of_likes = graphene.Int(source='number_of_likes')
    author = graphene.Field(UserNode, source='author')
    likes = graphene.List(UserNode)

    def resolve_likes(self, info, **kwargs):
        return self.likes.all()

    class Meta:
        model = models.Post
        interfaces = (graphene.relay.Node,)
        filter_fields = {
            'title': ['icontains', 'exact'],
            'comments__body': ['icontains'],
            'body': ['icontains'],
            'published_at': ['gte', 'lte'],
            'slug': ['exact']
        }


class CommentNode(DjangoObjectType):
    number_of_likes = graphene.Int(source='number_of_likes')
    author = graphene.Field(UserNode, source='author')
    likes = graphene.List(UserNode)

    def resolve_likes(self, info, **kwargs):
        return self.likes.all()

    class Meta:
        model = models.Comment
        interfaces = (graphene.relay.Node,)

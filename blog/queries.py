import graphene
from graphene_django import DjangoConnectionField
from graphene_django.filter import DjangoFilterConnectionField as DFCF

from . import types


class Query(graphene.ObjectType):
    post = graphene.relay.Node.Field(types.PostNode)
    posts = DFCF(types.PostNode)

    comment = graphene.relay.Node.Field(types.CommentNode)
    comments = DjangoConnectionField(types.CommentNode)

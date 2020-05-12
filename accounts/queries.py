import graphene
from . import types
from graphql_auth.schema import UserQuery, MeQuery


class Query(UserQuery, MeQuery, graphene.ObjectType):
    pass
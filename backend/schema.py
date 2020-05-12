import graphene

from accounts.queries import Query as AccountsQuery
from accounts.mutations import Mutation as AccountsMutation
from blog.queries import Query as BlogQuery
from blog.mutations import Mutation as BlogMutation
from graphql_auth.relay import UserNode

class Query(AccountsQuery, BlogQuery, graphene.ObjectType):
    pass


class Mutation(AccountsMutation, BlogMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
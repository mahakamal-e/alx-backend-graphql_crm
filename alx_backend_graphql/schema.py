import graphene
from crm.schema import Query as CRMQuery, Mutation as CRMMutation

# تعريف استعلام hello بسيط
class HelloQuery(graphene.ObjectType):
    hello = graphene.String(description="Returns a greeting message")

    def resolve_hello(self, info):
        return "Hello, GraphQL!"


class Query(HelloQuery, CRMQuery, graphene.ObjectType):
    pass


class Mutation(CRMMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)

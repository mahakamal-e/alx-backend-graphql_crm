import graphene


class Query(graphene.ObjectType):
    hello = graphene.String(description="Returns a greeting message")

    def resolve_hello(self, info):
        return "Hello, GraphQL!"

schema = graphene.Schema(query=Query)

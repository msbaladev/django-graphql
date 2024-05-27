import graphene
import REST_API.schema

class Query(REST_API.schema.Query, graphene.ObjectType):
    # Combine the queries from different apps
    pass


class Mutation(REST_API.schema.Mutation, graphene.ObjectType):
    # Combine the mutations from different apps
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
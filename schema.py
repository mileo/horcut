import graphene
import core.schema as coreSchema

class Query(coreSchema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=coreSchema.Mutation)
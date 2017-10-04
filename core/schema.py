import graphene
from graphene_django.types import DjangoObjectType
from .models import User, Community


class UserType(DjangoObjectType):

    class Meta:
        model = User


class CommunityType(DjangoObjectType):

    class Meta:
        model = Community


class Query(graphene.AbstractType):
    all_users = graphene.List(UserType)
    user = graphene.Field(UserType, name=graphene.String())

    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_user(self, info, name, **kwargs):
        return User.objects.get(name=name)


class CreateUser(graphene.Mutation):

    class Arguments:
        name = graphene.String(required=True)
        age = graphene.Int(required=True)
        gender = graphene.String()
        profile_pic = graphene.String()

    user = graphene.Field(lambda: UserType)

    def mutate(root, info, name, age, gender="", profile_pic=""):

        user = User.objects.create(
            name=name,
            age=age,
            gender=gender,
            profile_pic=profile_pic,
        )

        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()

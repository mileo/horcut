import graphene

class User(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String(required=True)
    age = graphene.Int(required=True)
    gender = graphene.String()
    profile_pic = graphene.String()
    friends = graphene.List(lambda: User)
    communities = graphene.List(lambda: Community)


class Community(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String(required=True)
    category = graphene.String(required=True)
    users = graphene.List(User)


class Query(graphene.ObjectType):
    all_users = graphene.List(lambda: User)
    user = graphene.Field(
        lambda: User, 
        name=graphene.String()
    )

    def resolve_all_users(self, info):
        return info.context.get('users')

    def resolve_user(self, info, name):
        users = info.context.get('users')

        for user in users:
            if user.name == name:
                return user

class CreateUser(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        age = graphene.Int(required=True)
        gender = graphene.String()
        profile_pic = graphene.String()

    user = graphene.Field(lambda: User)

    def mutate(root, info, name, age, gender, profile_pic):

        user = User(
            name=name,
            age=age,
            gender=gender,
            profile_pic=profile_pic,
        )
        info.context.get('users').append(user)
        return CreateUser(user=user)

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
context = {
    "users": [
            User(
                name="Daenerys Targaryen",
                age=14,
                gender="Female",
                profile_pic="http://bit.ly/3gHeUps"
            ),
            User(
                name="Arya Stark",
                age=10,
                gender="Female",
                profile_pic="http://bit.ly/4hIfVot"
            ),
            User(
                name="John Snow",
                age=15,
                gender="Male",
                profile_pic="http://bit.ly/2hLdTor"
            )
        ]}

result_all_users = schema.execute(
    '''{ 
        allUsers { 
            name
            profilePic
        }
    }''',
    context_value=context
)


result_get_user = schema.execute(
    '''query getUser($name: String) { 
        user(name: $name) { 
            id
            name
            profilePic
        }
    }''',
    context_value=context,
    variable_values={'name': 'John Snow'}
)

result_mutation = schema.execute(
    '''mutation { 
        createUser(name:"Cersei Lannister", age:30, gender:"Female", profilePic:"") { 
            user {
                id
                name
            }
        }
    }''',
    context_value=context,
)


print(result_mutation.data)

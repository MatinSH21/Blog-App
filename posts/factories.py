import factory
from factory.django import DjangoModelFactory
from .models import Post


class PostFactory(DjangoModelFactory):

    class Meta:
        model = Post

    title = factory.Faker('sentence')
    content = factory.Faker('text')
    author = factory.Faker('name')


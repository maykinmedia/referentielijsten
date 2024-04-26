import factory
from factory.django import DjangoModelFactory

from referentielijsten.token.models import TokenAuth


class TokenAuthFactory(DjangoModelFactory):
    contact_persoon = factory.Faker("name")
    email = factory.Faker("email")

    class Meta:
        model = TokenAuth

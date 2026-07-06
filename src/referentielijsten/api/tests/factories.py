import factory
from factory.django import DjangoModelFactory

from ..models import Item, Tabel


class TabelFactory(DjangoModelFactory):
    code = factory.Sequence(lambda n: str(n + 1))
    naam = factory.Faker("word")

    class Meta:  # pyright: ignore[reportIncompatibleVariableOverride]
        model = Tabel


class ItemFactory(DjangoModelFactory):
    tabel = factory.SubFactory(TabelFactory)
    code = factory.Sequence(lambda n: str(n + 1))
    naam = factory.Faker("word")

    class Meta:  # pyright: ignore[reportIncompatibleVariableOverride]
        model = Item

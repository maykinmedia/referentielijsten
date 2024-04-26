import factory.fuzzy

from ..models import Item, Tabel


class TabelFactory(factory.django.DjangoModelFactory):
    code = factory.Sequence(lambda n: str(n + 1))
    naam = factory.Faker("word")

    class Meta:
        model = Tabel


class ItemFactory(factory.django.DjangoModelFactory):
    tabel = factory.SubFactory(TabelFactory)
    code = factory.Sequence(lambda n: str(n + 1))
    naam = factory.Faker("word")

    class Meta:
        model = Item

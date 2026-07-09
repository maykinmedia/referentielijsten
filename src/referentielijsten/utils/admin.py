from django.contrib import admin


def filter_title(title: str):
    class Wrapper(admin.FieldListFilter):
        def __new__(cls, *args, **kwargs):
            instance = admin.FieldListFilter.create(*args, **kwargs)
            assert isinstance(instance, admin.FieldListFilter)
            instance.title = title
            return instance

    return Wrapper

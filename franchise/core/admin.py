from django.contrib import admin

from .models import Collectable, Collection, Franchise


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('__str__',)


@admin.register(Collectable)
class CollectableAdmin(admin.ModelAdmin):
    list_display = ('__str__',)


@admin.register(Franchise)
class FranchiseAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'value', 'quantity')

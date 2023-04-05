from django import template

from django.db.models import Count, QuerySet
from typing import TypeVar

from django import template

register = template.Library()
from veter.models import Pet
from website.templatetags.tags import register


@register.simple_tag
def pets():
    return Pet.objects.all()

# @register.filter(name="is_staticfile_exist")
# def is_staticfile_exist(your_image_path: str) -> bool:
#     return bool(finders.find(your_image_path))
# @register.simple_tag
# def get_countries(scope: str) -> QuerySet:
#     """Scopes defined in thrdb.blocks.REGION_SCOPE_CHOICES. Here processing only all_* scopes"""
#     r = Region.objects.all().order_by("name")
#     if scope.startswith("all_countries"):
#         r = r.filter(parent=None)
#     if not scope.endswith("_incl_empty"):
#         r = r.filter(dataset__is_visible__exact=True).annotate(
#             count_visible=Count("name", distinct=True)
#         )
#     return r

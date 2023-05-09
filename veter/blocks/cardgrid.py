from django.contrib.auth.models import User
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail import blocks

from veter.models import Pet, Visit
from website.templatetags.tags import has_group


class PetCardGrid(blocks.StructBlock):
    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        context["Pets"] = Pet.objects.filter()
        return context

    class Meta:
        template = "veter/blocks/pet_card_grid.html"
        label = 'Pet card grid'
# class PetCardGrid(blocks.StructBlock):
#     def get_context(self, value, parent_context=None):
#         context = super().get_context(value, parent_context)
#         context["Pets"] = Pet.objects.filter()
#         return context
#
#     class Meta:
#         template = "veter/blocks/pet_card_grid.html"
#         label = 'Pet card grid'
class VisitCardGrid(blocks.StructBlock):
    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        context["Visits"] = Visit.objects.all()
        return context

    class Meta:
        template = "veter/blocks/visit_card_grid.html"
        label = 'Visit card grid'

class ClientCardGrid(blocks.StructBlock):
    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        context["Clients"] = User.objects.filter(groups__name="Clients")
        print( context["Clients"])
        return context

    class Meta:
        template = "veter/blocks/client_card_grid.html"
        label = 'Clients card grid'

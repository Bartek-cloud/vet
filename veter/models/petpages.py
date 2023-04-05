from django.http import HttpResponseRedirect
from wagtail.contrib.routable_page.models import RoutablePageMixin, route

from django.utils.safestring import mark_safe
from wagtail.search import index

from veter.models import Pet
from website.models import WebPage


class PetPage(RoutablePageMixin, WebPage):


    class Meta:
        verbose_name = "PetPage"

    template = "veter/pages/petspage.html"

    # @property
    # def body_preview(self):
    #     """
    #     A shortened version of the page body without HTML tags.
    #     """

    @route(r"^$")
    def pets_view(self, request, *args, **kwargs):
        pets = Pet.objects.all()
        #     < a href = "{%  url 'wagtailadmin_home' %}thrdb/systemnarrative/edit/{{ narrative_smoke.id }}/"target = "_blank" > < imgsrc = "{% static 'thrdb/icons/pencil.svg' %}" > < / a >
        return self.render(
            request,
            context_overrides={
                 "pets": pets
                # "iso": iso.lower(),
                # "nds_id": 0,  # no NDS selected on main country profile page
                # "nds_short_names": ndss_short_names,
                # "narrative_smoke": narrative_smoke,
                # "narrative_vape": narrative_vape,

            },
            # {% include 'thrdb/snippets/uplot_smoking.html' %}
            # template="regions/region_details.html",
        )
    @route(r"^(\d+)/$")
    def pet_view(self, request, pet_id, *args, **kwargs):
        #     < a href = "{%  url 'wagtailadmin_home' %}thrdb/systemnarrative/edit/{{ narrative_smoke.id }}/"target = "_blank" > < imgsrc = "{% static 'thrdb/icons/pencil.svg' %}" > < / a >
        pet = Pet.objects.get(id=pet_id)
        return self.render(
            request,
            context_overrides={
                "pet": pet
                # "region": self.region,
                # "iso": iso.lower(),
                # "nds_id": 0,  # no NDS selected on main country profile page
                # "nds_short_names": ndss_short_names,
                # "narrative_smoke": narrative_smoke,
                # "narrative_vape": narrative_vape,

            },
            # {% include 'thrdb/snippets/uplot_smoking.html' %}
             template="veter/pages/petpage.html",
        )

    #
    # @route(r"^$")  # will override the default Page serving mechanism
    # def redirect_to_parent(self, request):
    #     """
    #     Calling the country profile without a
    #      country code should redirect to the parent page - list of countries
    #     """
    #     return HttpResponseRedirect(self.get_parent().get_url())


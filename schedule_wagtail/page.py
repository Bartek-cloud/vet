from coderedcms.project_template.basic.website.models import FormPage
from django import forms
from django.shortcuts import render
from modelcluster.fields import ParentalKey
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel

class ContactPage(FormPage):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        InlinePanel('form_fields', label="Form fields"),
    ]



class FormField(AbstractFormField):
    page = ParentalKey('ContactPage', on_delete=models.CASCADE, related_name='form_fields')

class ContactForm(AbstractEmailForm):
    name = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(max_length=255, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        verbose_name = "Contact form"

ContactPage.subpage_types = []
ContactPage.form_builder_function = 'wagtail.contrib.forms.forms.get_form_for_model'


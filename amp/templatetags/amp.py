from django import template
from amp_handler.utils import get_amphtml_path, get_amp_img, get_amp_iframe, get_file_content
from django.urls import reverse
import re
from django.utils.safestring import SafeString
from amp_handler import get_amp_state


register = template.Library()


@register.simple_tag(takes_context=True, name="amp_url")
def amp_url(context, value):
    if get_amp_state():
        return get_amphtml_path(reverse(value))
    return reverse(value)


@register.filter(name="amp_link")
def amp_link(value):
    if get_amp_state():
        return get_amphtml_path(value)
    return value


get_img = re.compile(r'(<img[^>]*>)')
get_iframe = re.compile(r'(<iframe[^>]*>[^<]*</iframe>)')


@register.filter(name='amp_safe')
def amp_safe(value):
    if get_amp_state():
        elements = get_img.findall(value)
        amp_elements = []
        for element in elements:
            amp_elements.append(get_amp_img(element))

        for i in range(len(elements)):
            value = value.replace(elements[i], amp_elements[i])

        elements.clear()
        amp_elements.clear()

        elements = get_iframe.findall(value)

        for element in elements:
            amp_elements.append(get_amp_iframe(element))

        for i in range(len(elements)):
            value = value.replace(elements[i], amp_elements[i])

    return SafeString(value)


@register.simple_tag(takes_context=True)
def import_file(context, path):
    request = context.get("request")
    return SafeString(get_file_content(path))

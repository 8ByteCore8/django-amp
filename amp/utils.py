from .settings import settings
import re
from string import Template
from os.path import join


AMP_PARAM = '%s=%s' % (
    settings.AMP_GET_PARAMETER, settings.AMP_GET_VALUE)


def add_param_to_path(path, param):
    if path.find('?') == -1:
        return "%s?%s" % (path, param)
    else:
        return "%s&%s" % (path, param)


def get_canonical_path(path):
    parts = path.split("?")
    base: str = parts[0]
    params = []
    if len(parts) > 1:
        params = list(set(parts[1].split('&')))

    if AMP_PARAM in params:
        params.remove(AMP_PARAM)

    for param in params:
        base = add_param_to_path(base, param)

    return base


def get_amphtml_path(path):
    return add_param_to_path(get_canonical_path(path), AMP_PARAM)


get_src = re.compile(r'src=\"([^\"]*)\"')
get_alt = re.compile(r'alt=\"([^\"]*)\"')
get_width = re.compile(r'width=\"([^\"]*)\"')
get_height = re.compile(r'height=\"([^\"]*)\"')


amp_img_template = Template(settings.AMP_IMG_TEMPLATE)
amp_iframe_template = Template(settings.AMP_IFRAME_TEMPLATE)


def get_amp_img(img):
    src = get_src.search(img)
    if src:
        src = src.group(1)
    else:
        return ''

    alt = get_alt.search(img)
    if alt:
        alt = alt.group(1)

    width = get_width.search(img)
    if width:
        width = width.group(1)

    height = get_height.search(img)
    if height:
        height = height.group(1)
    return amp_img_template.substitute(src=src, alt=(alt or ''), width=(width or settings.AMP_DEFAULT_WIDTH), height=(height or settings.AMP_DEFAULT_HEIGHT))


def get_amp_iframe(img):
    src = get_src.search(img)
    if src:
        src = src.group(1)
    else:
        return ''

    width = get_width.search(img)
    if width:
        width = width.group(1)

    height = get_height.search(img)
    if height:
        height = height.group(1)

    return amp_iframe_template.substitute(src=src, width=(width or settings.AMP_DEFAULT_WIDTH), height=(height or settings.AMP_DEFAULT_HEIGHT))


FILE_CACHE = {}


def get_file_content(path):
    full_path = join(settings.BASE_DIR, path)

    if full_path in FILE_CACHE:
        print("file %s load from cache" % (full_path,))
        return FILE_CACHE[full_path]
    else:
        content = ''
        with open(full_path) as file:
            content = file.read()

        FILE_CACHE.update({full_path: content})
        print("file %s load to cache" % (full_path,))

        return content

from django.conf import settings as django_settings
import django


class SettingsProxy(object):
    def __init__(self, settings, defaults):
        self.settings = settings
        self.defaults = defaults

    def __getattr__(self, attr):
        try:
            return getattr(self.settings, attr)
        except AttributeError:
            try:
                return getattr(self.defaults, attr)
            except AttributeError:
                raise AttributeError(
                    u'settings object has no attribute "%s"' % attr)


class defaults(object):
    USE_AMP = False
    AMP_GET_PARAMETER = u'amp'
    AMP_GET_VALUE = u'1'
    AMP_TEMPLATE_PREFIX = u"amp/"
    AMP_GEN_PATH = True
    AMP_DEFAULT_WIDTH = 1.5
    AMP_DEFAULT_HEIGHT = 1
    AMP_IMG_TEMPLATE = u'<amp-img src="$src" width="$width" height="$height" layout="responsive" alt="$alt"></amp-img>'
    AMP_IFRAME_TEMPLATE = u'<amp-iframe width="$width" height="$height" sandbox="allow-scripts allow-same-origin" layout="responsive" frameborder="0" src="$src"></amp-iframe>'


settings = SettingsProxy(django_settings, defaults)

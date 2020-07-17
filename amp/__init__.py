import threading
from .settings import settings


_local = threading.local()


def set_amp_state(is_amp=False, request=None):
    """
        Меняет состояние AMP.
    """
    request = request or getattr(_local, 'request', None)
    if request:
        request.is_amp = is_amp
    _local.is_amp = is_amp


def get_amp_state():
    """
        Возвращяет состояние AMP.
    """
    return getattr(_local, 'is_amp', False)


def get_template_name(template_name: str, request=None):
    if get_amp_state():
        return "%s%s" % (settings.AMP_TEMPLATE_PREFIX, template_name)
    return template_name
from .settings import settings
from . import set_amp_state, get_amp_state
from .utils import add_param_to_path, get_canonical_path, get_amphtml_path


class AMPMiddleware(object):

    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):
        self.process_request(request)
        response = self.get_response(request)
        return response

    def process_request(self, request):
        if settings.USE_AMP:
            if request.GET.get(settings.AMP_GET_PARAMETER) == settings.AMP_GET_VALUE:
                set_amp_state(is_amp=True, request=request)
            else:
                set_amp_state(is_amp=False, request=request)

            if settings.AMP_GEN_PATH:
                request.canonical_path = get_canonical_path(
                    request.get_full_path())
                request.amphtml_path = get_amphtml_path(
                    request.get_full_path())

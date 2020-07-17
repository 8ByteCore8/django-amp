from django.test import TestCase
from . import get_template_name, set_amp_detect, get_amp_detect
from .settings import settings

# Create your tests here.


class AMPTestCase(TestCase):

    def setUp(self):
        pass

    def test_get_template_name(self):
        template_name = 'test/index.html'

        settings.USE_AMP = True
        
        set_amp_detect(False)
        self.assertEqual(get_template_name(template_name), 'test/index.html')
        
        set_amp_detect(True)

        settings.AMP_USE_TEMPLATE_POSTFIX = False
        self.assertEqual(get_template_name(
            template_name), 'amp/test/index.html')

        settings.AMP_USE_TEMPLATE_POSTFIX = True
        self.assertEqual(get_template_name(
            template_name), 'test/amp/index.html')


    def test_amp_detect(self):
        settings.USE_AMP = False
        set_amp_detect(True)
        self.assertEqual(get_amp_detect(), False)
        set_amp_detect(False)
        self.assertEqual(get_amp_detect(), False)
        settings.USE_AMP = True
        set_amp_detect(True)
        self.assertEqual(get_amp_detect(), True)
        set_amp_detect(False)
        self.assertEqual(get_amp_detect(), False)

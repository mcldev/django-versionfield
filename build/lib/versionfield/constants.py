from django.conf import settings

DEFAULT_NUMBER_BITS = getattr(settings, 'VERSION_FIELD_NUMBER_BITS', (8, 8, 16))
DEFAULT_INPUT_SIZE  = getattr(settings, 'VERSION_FIELD_WIDGET_INPUT_SIZE', 10)
DEFAULT_VERSION_VALUE = getattr(settings, 'VERSION_FIELD_DEFAULT_VALUE', "0.0.0")
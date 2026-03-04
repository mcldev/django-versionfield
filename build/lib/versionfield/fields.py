from django.db import models
import django

from . import forms
from .constants import DEFAULT_NUMBER_BITS
from .version import Version
from .utils import convert_version_int_to_string


class VersionField(models.Field):

    """
    A Field where version numbers are input/output as strings (e.g. 3.0.1)
    but stored in the db as converted integers for fast indexing
    """

    description = "A version number (e.g. 3.0.1)"

    def __init__(self, number_bits=DEFAULT_NUMBER_BITS, *args, **kwargs):
        self.number_bits = number_bits
        super().__init__(*args, **kwargs)

    def db_type(self, connection):
        """Use integer as internal representation."""
        return "integer"

    def to_python(self, value):
        if not value:
            return None

        if isinstance(value, Version):
            return value

        if isinstance(value, str):
            return Version(value, self.number_bits)

        return Version(
            convert_version_int_to_string(value, self.number_bits),
            self.number_bits
        )

    if django.VERSION < (2, 0):
        def from_db_value(self, value, expression, connection, context):
            return self.get_from_db_value(value, expression, connection)
    else:
        def from_db_value(self, value, expression, connection):
            return self.get_from_db_value(value, expression, connection)

    def get_from_db_value(self, value, expression, connection):
        """Convert data from database."""
        if value is None:
            return value
        return Version(
            convert_version_int_to_string(value, self.number_bits),
            self.number_bits)

    def get_prep_value(self, value):
        if isinstance(value, str):
            return int(Version(value, self.number_bits))

        if value is None:
            return None

        return int(value)

    def formfield(self, **kwargs):
        defaults = {
            'form_class': forms.VersionField,
            'number_bits': self.number_bits
        }
        defaults.update(kwargs)
        return super().formfield(**defaults)

    def __str__(self, value):
        return str(value)

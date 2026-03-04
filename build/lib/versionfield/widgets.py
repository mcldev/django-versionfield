from django.forms.widgets import TextInput
from django.template.loader import render_to_string

from .constants import DEFAULT_INPUT_SIZE, DEFAULT_VERSION_VALUE


class VersionWidget(TextInput):

    class Media:
        css = {
            'all': ('django-versionfield/css/bootstrap.css',)
        }
        js = (
            'django-versionfield/js/jquery-3.5.1.min.js',
            'django-versionfield/js/bootstrap.min.js',
        )

    def render(self, name, value, attrs=None, **kwargs):

        # Get Attrs and set as read-only and reduce size
        attrs = attrs or {}
        if 'size' not in attrs:
            attrs['size'] = DEFAULT_INPUT_SIZE
        if value is None:
            value = DEFAULT_VERSION_VALUE

        # Get the default input html (as read-only text input field)
        input_html = super().render(name, value, attrs=attrs, **kwargs)

        # Render the Version Input widget
        rendered = render_to_string(
            'admin/django-versionfield/widgets/version-field.html',
            {
                'input_html': input_html,
                'value': value,
                'name': name,
                'is_required': self.is_required,
            },
        )
        return rendered

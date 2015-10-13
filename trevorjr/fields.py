from django.db.models.fields import Field
from django.forms import Widget
from django.forms.utils import flatatt
from django.utils.encoding import force_text, smart_text
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _


class TrevorJrWidget(Widget):
    def __init__(self, attrs=None):
        default_attrs = {'class': 'trevorjr'}
        if attrs:
            default_attrs.update(attrs)
        super(TrevorJrWidget, self).__init__(default_attrs)

    class Media:
        css = {
            'all': ('trevorjr/sir-trevor.css', 'trevorjr/sir-trevor-icons.css')
        }
        js = ('//code.jquery.com/jquery-latest.min.js', 'trevorjr/sir-trevor.min.js',)

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        return mark_safe(format_html(
            '<br><textarea{}>{}</textarea>',
            flatatt(final_attrs),
            force_text(value)
        ) + '<script>new SirTrevor.Editor({ el: $(".trevorjr") });</script>')


class TrevorJrField(Field):
    description = _("TrevorJr")

    def get_internal_type(self):
        return "TextField"

    def to_python(self, value):
        if isinstance(value, str) or value is None:
            return value
        return smart_text(value)

    def get_prep_value(self, value):
        value = super(TrevorJrField, self).get_prep_value(value)
        return self.to_python(value)

    def formfield(self, **kwargs):
        defaults = {'widget': TrevorJrWidget}
        defaults.update(kwargs)
        return super(TrevorJrField, self).formfield(**defaults)

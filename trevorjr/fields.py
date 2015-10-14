from django.forms import Widget
from django.forms.utils import flatatt
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
try:
    from django.contrib.postgres.fields.jsonb import JSONField
except:
    from postgres.fields.jsonb import JSONField


class TrevorJrWidget(Widget):
    class Media:
        css = {
            'all': ('trevorjr/sir-trevor.css', 'trevorjr/sir-trevor-icons.css')
        }
        js = ('//code.jquery.com/jquery-latest.min.js', 'trevorjr/sir-trevor.min.js',)

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        return mark_safe(
            '<br><textarea%s>%s</textarea><script>new SirTrevor.Editor({ el: $("#%s") });</script>' % (
                flatatt(final_attrs),
                conditional_escape(value),
                final_attrs['id'],
            )
        )


class TrevorJrField(JSONField):
    description = _("TrevorJr")

    def formfield(self, **kwargs):
        defaults = {'widget': TrevorJrWidget}
        defaults.update(kwargs)
        return super(TrevorJrField, self).formfield(**defaults)

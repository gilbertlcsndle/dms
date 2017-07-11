from django.views.generic import TemplateView

from dms.mixins import OfficialRequiredMixin

class MapIndex(OfficialRequiredMixin, TemplateView):
    template_name = "maps/index.html"

from django.views.generic import TemplateView
from django.views import View

from dms.mixins import ChairSecTreasureRequiredMixin

from apps.officials.models import Official

class CertificateIndex(ChairSecTreasureRequiredMixin, TemplateView):
    def get_template_names(self):
        template_name = "certificates/" + self.request.GET.get("cert_name", "index.html")

        return template_name

    def get_context_data(self, **kwargs):
        context = super(CertificateIndex, self).get_context_data(**kwargs)
        
        try:
            official = Official.objects.get(position='chair', user__is_active=True)

            context['punong_brgy'] = '%s %s %s' \
                %(
                    official.resident.fname, 
                    official.resident.mname[0] + '.', # middle initial 
                    official.resident.lname
                )
        except:
            # there must be one punong barangay
            context['punong_brgy'] = ''

        return context
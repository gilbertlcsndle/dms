from django.urls import reverse_lazy
from dms import mixins

def custom_processors(request):
    position_keys = mixins.position_keys
    perm_denied_msg = 'To proceed, please login as '
    
    chairsectreasure = '{0}{1}{2}'.format(position_keys[0], position_keys[1], position_keys[2])    

    if request.GET.get('perm') == position_keys[0]:
        perm_denied_msg += 'chairman or secretary.'

    if request.GET.get('perm') == position_keys[2]:
        perm_denied_msg += 'treasurer.'

    if request.GET.get('perm') == chairsectreasure:
        perm_denied_msg += 'chairman, secretary or treasurer.'
    
    if request.GET.get('perm') == position_keys[3]:
        perm_denied_msg += 'councilor.'

    if (request.GET.get('perm') not in position_keys and
        request.GET.get('perm') != chairsectreasure):
        perm_denied_msg += 'official.'


    return {
        'perm_denied_msg': perm_denied_msg,
        'position_keys': position_keys,
        'current_page': request.path
    }

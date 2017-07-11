import random, string
from datetime import date

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse_lazy

from apps.officials.models import Official

position_keys = [position[0] for position in Official.POSITION_CHOICES]

class ChairSecRequiredMixin(LoginRequiredMixin):
    """
    View mixin which requires that the aunthenticated user is a chairman or secretary.
    Superuser will be exempted.
    """

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            if hasattr(request.user, 'official'):
                if request.user.official.position not in position_keys[:2]:
                    return redirect(
                        '{0}?next={1}&perm={2}' 
                        .format(settings.LOGIN_URL, request.path, position_keys[0])
                    )

                return super(ChairSecRequiredMixin, self).dispatch(request, *args, **kwargs)
            if not request.user.is_superuser:
                return redirect(
                    '{0}?next={1}&perm={2}' 
                    .format(settings.LOGIN_URL, request.path, position_keys[0])
                )
        return super(ChairSecRequiredMixin, self).dispatch(request, *args, **kwargs)

class TreasureRequiredMixin(LoginRequiredMixin):
    """
    View mixin which requires that the aunthenticated user is a treasurer.
    Superuser will be exempted.
    """

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            if hasattr(request.user, 'official'):
                if request.user.official.position != position_keys[2]:
                    return redirect(
                        '{0}?next={1}&perm={2}' 
                        .format(settings.LOGIN_URL, request.path, position_keys[2])
                    )

                return super(TreasureRequiredMixin, self).dispatch(request, *args, **kwargs)
            if not request.user.is_superuser:
                return redirect(
                    '{0}?next={1}&perm={2}' 
                    .format(settings.LOGIN_URL, request.path, position_keys[2])
                )

        return super(TreasureRequiredMixin, self).dispatch(request, *args, **kwargs)

class ChairSecTreasureRequiredMixin(LoginRequiredMixin):
    """
    View mixin which requires that the aunthenticated user is a chairman, secretary or treasurer.
    Superuser will be exempted.
    """

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            if hasattr(request.user, 'official'):
                if request.user.official.position not in position_keys[:3]:
                    return redirect(
                        '{0}?next={1}&perm={2}' 
                        .format(settings.LOGIN_URL, 
                                request.path, 
                                '{0}{1}{2}'
                                .format(position_keys[0], 
                                        position_keys[1], 
                                        position_keys[2]))
                    )

                return super(ChairSecTreasureRequiredMixin, self).dispatch(request, *args, **kwargs)
            if not request.user.is_superuser:
                return redirect(
                    '{0}?next={1}&perm={2}' 
                    .format(settings.LOGIN_URL, 
                            request.path, 
                            '{0}{1}{2}'
                            .format(position_keys[0], 
                                    position_keys[1], 
                                    position_keys[2]))
                )
        return super(ChairSecTreasureRequiredMixin, self).dispatch(request, *args, **kwargs)

class OfficialRequiredMixin(LoginRequiredMixin):
    """
    View mixin which requires that the aunthenticated user is an official.
    Superuser will be exempted.
    """

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            if hasattr(request.user, 'official'):
                if request.user.official.position not in position_keys:
                    return redirect(
                        '{0}?next={1}'
                        .format(settings.LOGIN_URL, request.path)
                    )

                return super(OfficialRequiredMixin, self).dispatch(request, *args, **kwargs)
            if not request.user.is_superuser:
                return redirect(
                    '{0}?next={1}' 
                    .format(settings.LOGIN_URL, request.path)
                )

        return super(OfficialRequiredMixin, self).dispatch(request, *args, **kwargs)

class UserIdGeneratorMixin:
    """
    Generates a unique user id.
    """
    def create_id(self):
        rangenum = list(range(10))

        # restriction in module
        # 1st arg must be higher than 2nd arg
        randnum_list = random.sample(rangenum, 7)
        randnum      = ''.join(str(i) for i in randnum_list)

        # the final generated id consist of 7 random numbers
        user_id = randnum

        check_id = User.objects.filter(username = user_id)

        # loop until no match is found
        while check_id.exists():
            randnum_list = random.sample(rangenum, 7)
            randnum      = ''.join(str(i) for i in randnum_list)
            
            user_id = randnum
            
            check_id = User.objects.filter(username = user_id)

        return user_id

class CalculateAgeMixin:
    def get_age(self, born):
        today = date.today()     
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))

        # if age is negative always return 0
        return age if age > 0 else 0

        
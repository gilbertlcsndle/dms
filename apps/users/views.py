from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from apps.users.forms import SetPasswordForm

class ForgotPassword(FormView):
    template_name = "users/forgot-pass.html"

    def get_form(self):
        form_class = SetPasswordForm
        user = User.objects.get(username=self.request.POST['username'])

        return form_class(user, **self.get_form_kwargs())

    def form_invalid(self, form):
        errors = []
        for key in form.errors:
            errors += [v for v in form.errors[key]]

        data = {
            'is_valid': form.is_valid(),
            'errors': errors
        }

        return JsonResponse(data)

    def form_valid(self, form):
        form.save()

        return JsonResponse({ 'is_valid': form.is_valid() })

def get_security_info(request):
    if request.method == 'GET':
        user = User.objects.filter(username=request.GET.get('username'))

        # use in validating ID
        data = {
            'is_valid': False, 
            'error': 'Sorry, we don\'t recognize your ID'
        }

        if user:
            user = user.get()

            data = {
                'is_valid': True, # use in validating ID
                'question1': user.official.get_question1_display(),
                'question2': user.official.get_question2_display(),
                'question3': user.official.get_question3_display()
            }

        return JsonResponse(data)

    if request.method == 'POST':
        user = User.objects.get(username=request.POST['username'])

        answers = [user.official.answer1,
                   user.official.answer2,
                   user.official.answer3]

        request_answers = [request.POST['answer1'], 
                           request.POST['answer2'], 
                           request.POST['answer3']]

        return JsonResponse({ 'is_valid': answers == request_answers })

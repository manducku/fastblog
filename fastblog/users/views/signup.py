from django.views.generic import View 
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse

class SignupView(view):

    template_name="users/signup.html"

    def post(request):
        username=request.POST.get('username')
        password=request.POST.get('password')
        phonenumber=request.POST.get('phonenumber')

        User = get_user_model()
        user = User.objects.create_user(
                username=username,
                password=password,
                phonenumber=phonenumber,
                )

        return reverse(
                "home"
                )

         




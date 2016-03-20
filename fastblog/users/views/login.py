from django.views.generic import TemplateView 
from django.core.urlresolvers import reverse
from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib import messages

class LoginView(TemplateView):

    template_name="users/login.html"

    def post(self, request):

        username=request.POST.get("username")
        password=request.POST.get("password")
        
        user=authenticate(
                username=username,
                password=password,
                )

        if user:
            login(request, user)
            messages.add_message(
                    request, 
                    messages.SUCCESS,
                    "회원가입에 성공하였습니다",
                    )

            return redirect(
                    reverse(
                        "home"
                        )
                    )
        return redirect(
            reverse(
                "login"
                )
            )



        
        

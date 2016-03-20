from django.views.generic import View
from django.contrib.auth import logout 
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

class LogoutView(View):

    def get(self, request):
        logout(request)

        messages.add_message(
                request,
                messages.SUCCESS,
                "logout sucess"
                )

        return redirect(
                reverse(
                    "home"
                    )
                )


    

# from typing_extensions import Self
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserChangeForm





# class UserEditView(generic.CreateView):
#     form_class = UserChangeForm
#     template_name = '/change/profile.html'
#     success_url = reverse_lazy('account/edit_profile')

#     def get_object(self):
#         return self.request.user

def changepass (request):

    return render(request, "change/changepass.html")



# def profile_up(request):

#     return render(request,"change/profile.html")

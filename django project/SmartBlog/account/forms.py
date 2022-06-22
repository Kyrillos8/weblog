from multiprocessing import allow_connection_pickling
import profile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin

# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ['username','email']
		#fields = '__all__'


	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

# class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
#     template_name = 'account/change_password.html'
#     success_message = "Successfully Changed Your Password"
#     success_url = reverse_lazy('account/profile')



from django.urls import path
# from django.views import UserEditView
from . import views


urlpatterns = [

    # path('<int:id>/update', views.update, name='update_post'), # PUT (UPDATE)
    # path('<int:id>/delete', views.destroy, name='delete_post')  # Delete (DELETE)
    # path('edit_profile', UserEditView.as_view(), name="edit_profile")
    path('changepass', views.changepass, name="changepass"), # change_pass


    
    
    ]

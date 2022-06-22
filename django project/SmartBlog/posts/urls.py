from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path('create', views.create, name="create_post"), # GET
    path('store', views.store, name="store_post"),
    path('<int:id>', views.show, name='show_post'), # GET  (READ)
    path('<slug:slug>',views.findBySlug),
    path('<int:id>/edit', views.edit, name='edit_post'), # GET
    path('<int:id>/update', views.update, name='update_post'), # PUT (UPDATE)
    path('<int:id>/delete', views.destroy, name='delete_post'),  # Delete (DELETE)
    path("myposts/", views.myposts, name="myposts"),
]

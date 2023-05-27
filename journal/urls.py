from django.urls import path
from . import views

urlpatterns = [
    # home page
    path("", views.home, name="home"),

    # register
    path("register", views.register, name="register"),

    # login
    path("my-login", views.my_login, name="my-login"),

    # dashboard
    path("dashboard", views.dashboard, name="dashboard"),

    # logout
    path("user-logout", views.user_logout, name="user-logout"),

    # notes-form
    path("post-notes", views.post_notes, name="post-notes"),

    # my notes
    path('my-notes', views.my_notes, name='my-notes'),

    # update note

    path('update-note/<str:pk>', views.update_note, name='update-note'),

    # delete note

    path('delete-note/<str:pk>', views.delete_note, name='delete-note'),

    # profile management
    path('profile-management', views.profile_management, name='profile-management'),


]

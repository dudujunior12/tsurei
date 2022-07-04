from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login_view, name="login"),
    path('register/', views.register_view, name="register"),
    path('logout/', views.logout_view, name="logout"),
    path('upload/', views.upload, name="upload"),
    path('manga/get/<int:id>', views.get_manga, name="get_manga"),
    path('manga/<int:id>', views.show_manga, name="show_manga"),
    path('manga/<int:id>/new-comment', views.new_comment, name="new_comment"),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login_view, name="login"),
    path('register/', views.register_view, name="register"),
    path('logout/', views.logout_view, name="logout"),
    path('upload/', views.upload, name="upload"),
    path('latest/', views.latest, name="latest"),
    path('categories/<str:category>', views.categories, name="categories"),
    path('profile/<str:username>', views.profile, name="profile"),
    path('manga/get/<int:id>', views.get_manga, name="get-manga"),
    path('manga/<int:id>', views.show_manga, name="show-manga"),
    path('manga/<int:manga_id>/add-bookmark', views.add_bookmark, name="add-bookmark"),
    path('manga/<int:manga_id>/new-chapter', views.new_chapter, name="new-chapter"),
    path('manga/<int:manga_id>/chapter/<int:chapter_id>', views.manga_chapter, name="manga-chapter"),
]
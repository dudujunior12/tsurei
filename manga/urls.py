from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login_view, name="login"),
    path('register/', views.register_view, name="register"),
    path('logout/', views.logout_view, name="logout"),
    path('upload/', views.upload, name="upload"),
    path('bookmarks/', views.bookmarks, name="bookmarks"),
    path('latest/', views.latest, name="latest"),
    path('categories/', views.categories, name="categories"),
    path('profile/<str:username>', views.profile, name="profile"),
    path('profile/<str:username>/follow', views.follow, name="follow"),
    path('manga/get/<int:id>', views.get_manga, name="get_manga"),
    path('manga/<int:id>', views.show_manga, name="show_manga"),
    path('manga/<int:manga_id>/add-bookmark', views.add_bookmark, name="add-bookmark"),
    path('manga/<int:id>/new-comment', views.new_comment, name="new_comment"),
    path('manga/<int:manga_id>/edit-comment/<int:comment_id>', views.edit_comment, name="edit-comment"),
    path('manga/<int:manga_id>/like-comment/<int:comment_id>', views.like_comment, name="like-comment"),
]
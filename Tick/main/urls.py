from django.urls import path, include
from main.views import PostView,PostDetail,AddPost,UpdatePost,DeletePost,ProfileView, CommentPost

app_name='main'



urlpatterns = [
    path('',PostView.as_view(), name='home'),
    path('create_post/', AddPost.as_view(), name="create" ),
    path('details/<int:pk>', PostDetail.as_view(), name="details"),
    path('detail/update/<int:pk>',UpdatePost.as_view(), name="update"),
    path('detail/<int:pk>/Delete',DeletePost.as_view(), name="Delete"),
    path('profile/',ProfileView, name='profile'),
    path('details/<int:pk>/comment', CommentPost.as_view(), name='add_comment'),
]

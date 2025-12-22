from django.urls import path, include
from .views import (UserProfileViewSet, CategoryListAPIView,CategoryDetailAPIView,GenreListAPIView,GenreDetailAPIView,
                    CountryViewSet, DirectorViewSet,
                    ActorViewSet, ActorImageViewSet,MovieListAPIView,MovieDetailAPIView, MovieFrameViewSet,
                    MovieVideoViewSet, RatingViewSet, ReviewViewSet,
                    ReviewLikeViewSet, FavoriteItemViewSet, FavoriteViewSet,HistoryViewSet)


from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'user',UserProfileViewSet)
router.register(r'country', CountryViewSet)
router.register(r'director', DirectorViewSet)
router.register(r'actor', ActorViewSet)
router.register(r'rating', RatingViewSet)
router.register(r'review', ReviewViewSet)
router.register(r'favorite', FavoriteViewSet)
router.register(r'history', HistoryViewSet)
router.register(r'actorimage', ActorImageViewSet)
router.register(r'favoriteitems', FavoriteItemViewSet)
router.register(r'movievideo', MovieVideoViewSet)
router.register(r'movieframe', MovieFrameViewSet)
router.register(r'reviewlike', ReviewLikeViewSet)




urlpatterns = [
    path('', include(router.urls)),
    path('category/', CategoryListAPIView.as_view()),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('genre/', GenreListAPIView.as_view(), name='genre_list'),
    path('genre/<int:pk>/', GenreDetailAPIView.as_view(), name='genre_detail'),
    path('movie/', MovieListAPIView.as_view(), name='movie_list'),
    path('movie/<int:pk>/', MovieDetailAPIView.as_view(), name='movie_detail'),
]
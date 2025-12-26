from .serializers import (UserProfileListSerializer,UserProfileDetailSerializer,CategoryListSerializer,CategoryDetailSerializer ,
                          GenreListSerializer,GenreDetailSerializer,
                          CountryListSerializer,CountryDetailSerializer, DirectorListSerializer,DirectorDetailSerializer,
                          ActorListSerializer,ActorDetailSerializer, ActorImageSerializer,
                          MovieListSerializer,MovieDetailSerializer,  RatingSerializer,
                          ReviewSerializer, ReviewLikeSerializer, FavoriteSerializer, FavoriteItemSerializer,
                            HistorySerializer)
from .models import (UserProfile, Category, Genre, Country, Director, Actor, ActorImage,
                     Movie, Rating, Review, ReviewLike, Favorite, History, FavoriteItem)
from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters  import SearchFilter, OrderingFilter
from .pagination import MovieListPagination, CategoryListPagination,GenreListPagination

class UserProfileListAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileListSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id )

class UserProfileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileDetailSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id )

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    pagination_class = CategoryListPagination

class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer

class GenreListAPIView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreListSerializer
    pagination_class = GenreListPagination

class GenreDetailAPIView(generics.RetrieveAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreDetailSerializer

class CountryListAPIView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryListSerializer

class CountryDetailAPIView(generics.RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryDetailSerializer

class DirectorListAPIView(generics.ListAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorListSerializer

class DirectorDetailAPIView(generics.RetrieveAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorDetailSerializer

class ActorListAPIView(generics.ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorListSerializer

class ActorDetailAPIView(generics.RetrieveAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorDetailSerializer

class ActorImageViewSet(viewsets.ModelViewSet):
    queryset = ActorImage.objects.all()
    serializer_class = ActorImageSerializer

class MovieListAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    search_fields = ['movie_name']
    ordering_fields = ['year']
    pagination_class = MovieListPagination
    filterset_fields = {
        'country': ['exact'],
        'genre': ['exact'],
        'actor': ['exact'],
        'movie_status': ['exact'],
    }

class MovieDetailAPIView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer

class RatingCreateAPIView(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewLikeViewSet(viewsets.ModelViewSet):
    queryset = ReviewLike.objects.all()
    serializer_class = ReviewLikeSerializer

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

class FavoriteItemViewSet(viewsets.ModelViewSet):
    queryset = FavoriteItem.objects.all()
    serializer_class = FavoriteItemSerializer

class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer

class CountryDetailAPIVew(generics.RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryDetailSerializer
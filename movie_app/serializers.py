from .models import (UserProfile, Category, Genre, Country, Director, Actor, ActorImage,
                     Movie, MovieVideo, MovieFrame, Rating, Review, ReviewLike, Favorite, FavoriteItem, History)


from rest_framework import serializers

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']

class GenreNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['genre_name']

class CategoryDetailSerializer(serializers.ModelSerializer):
    genres = GenreNameSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['category_name', 'genres']

class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'genre_name']

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']

class MovieListSerializer(serializers.ModelSerializer):
    year = serializers.DateField(format('%Y'))
    country = CountrySerializer(many=True)
    genre = GenreNameSerializer(many=True)
    class Meta:
        model = Movie
        fields = ['id', 'movie_poster', 'movie_name', 'year','country', 'genre','movie_status']

class GenreDetailSerializer(serializers.ModelSerializer):
    genres_movies = MovieListSerializer(many=True, read_only=True)
    class Meta:
        model = Genre
        fields = ['genre_name','genres_movies']


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class ActorImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActorImage
        fields = '__all__'

class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class MovieVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieVideo
        fields = '__all__'

class MovieFrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieFrame
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ReviewLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewLike
        fields = '__all__'

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'

class FavoriteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteItem
        fields = '__all__'

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'
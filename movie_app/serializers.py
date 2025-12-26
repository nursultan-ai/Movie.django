from .models import (UserProfile, Category, Genre, Country, Director, Actor, ActorImage,
                     Movie, MovieVideo, MovieFrame, Rating, Review, ReviewLike, Favorite, FavoriteItem, History)


from rest_framework import serializers

class UserProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id','user_photo', 'username','status']

class UserProfileDetailSerializer(serializers.ModelSerializer):
    date_registered = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))
    class Meta:
        model = UserProfile
        fields = ['first_name','last_name', 'username','email','age',
                  'phone_number','user_photo','status','date_registered']

class UserProfileNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']

class UserProfileReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id','user_photo', 'username']


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

class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'country_name']

class MovieListSerializer(serializers.ModelSerializer):
    year = serializers.DateField(format('%Y'))
    country = CountryListSerializer(many=True)
    genre = GenreNameSerializer(many=True)
    class Meta:
        model = Movie
        fields = ['id', 'movie_poster', 'movie_name', 'year','country', 'genre','movie_status']

class CountryDetailSerializer(serializers.ModelSerializer):
    country_movies = MovieListSerializer(many=True, read_only=True)
    class Meta:
        model = Country
        fields = ['country_name','country_movies']

class GenreDetailSerializer(serializers.ModelSerializer):
    genres_movies = MovieListSerializer(many=True, read_only=True)
    class Meta:
        model = Genre
        fields = ['genre_name','genres_movies']

class DirectorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id','full_name']

class DirectorDetailSerializer(serializers.ModelSerializer):
    birth_date = serializers.DateField(format('%d-%m-%Y'))
    director_movies = MovieListSerializer(many=True, read_only=True)
    class Meta:
        model = Director
        fields = ['full_name','director_photo','bio','birth_date','director_movies']

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['full_name']

class ActorImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActorImage
        fields = '__all__'


class ActorListSerializer(serializers.ModelSerializer):
    images = ActorImageSerializer(read_only=True)
    class Meta:
        model = Actor
        fields = ['id','full_name']

class ActorDetailSerializer(serializers.ModelSerializer):
    birth_date = serializers.DateField(format('%d-%m-%Y'))
    actor_movies = MovieListSerializer(many=True, read_only=True)
    class Meta:
        model = Actor
        fields = ['full_name','birth_date','bio','actor_movies']


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['full_name']


class MovieVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieVideo
        fields = ['video_name','video']

class MovieFrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieFrame
        fields = ['image']

class RatingSerializer(serializers.ModelSerializer):
    user = UserProfileNameSerializer()
    class Meta:
        model = Rating
        fields = ['user','stars']

class ReviewSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))
    user = UserProfileReviewSerializer()
    class Meta:
        model = Review
        fields = ['user','comments','parent','created_date']

class MovieDetailSerializer(serializers.ModelSerializer):
    year = serializers.DateField(format='%d-%m-%Y')
    country = CountryListSerializer(many=True)
    genre = GenreNameSerializer(many=True)
    director = DirectorSerializer(many=True)
    actor = ActorSerializer(many=True)
    videos = MovieVideoSerializer(many=True, read_only=True)
    frames = MovieFrameSerializer(many=True, read_only=True)
    ratings = RatingSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    get_avg_rating = serializers.SerializerMethodField()
    get_count_ratings = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = ['movie_name', 'slogan', 'year', 'country','genre','director',
                  'movie_type','movie_time','actor','movie_poster','trailer',
                  'description','movie_status','videos','frames','get_avg_rating',
                  'get_count_ratings','ratings','reviews']

    def get_avg_rating(self, obj):
        return obj.movie_avg_rating()

    def get_count_ratings(self, obj):
        return obj.get_count_rating()



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
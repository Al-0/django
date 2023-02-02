from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.caption


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Post(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.CharField(max_length=300)
    image = models.ImageField(upload_to='posts', null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, related_name="posts", null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag)


class Comment(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField()
    text = models.TextField(max_length=500)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

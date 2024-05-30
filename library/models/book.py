from django.db import models
from django.core.validators import MaxValueValidator

from library.models import Author

BOOK_GENRES = [
    ('Fiction', 'Fiction'),
    ('Non-Fiction', 'Non-Fiction'),
    ('Science Fiction', 'Science Fiction'),
    ('Fantasy', 'Fantasy'),
    ('Mystery', 'Mystery'),
    ('Biography', 'Biography'),
    ('Other', 'Other'),
]


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name='books', null=True)
    publish_date = models.DateField(auto_now_add=True)

    description = models.TextField(null=True, blank=True)
    genres = models.CharField(max_length=50, choices=BOOK_GENRES, default='Other')
    pages = models.PositiveSmallIntegerField(validators=[MaxValueValidator(10000)], null=True, blank=True)

    def __str__(self):
        return self.title

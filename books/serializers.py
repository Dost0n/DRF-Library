from rest_framework import serializers
from books.models import Book
from rest_framework.exceptions import ValidationError


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title', 'subtitle','author', 'isbn', 'price')
    
    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)
        if not title.isalpha():
            raise ValidationError(
                {
                    'status':False,
                    "message":"Iltimos to'g'ri ma'lumot kiriting!!!"
                }
            )
        book = Book.objects.filter(title=title, author = author)
        if book:
            raise ValidationError(
                {
                    'status':False,
                    "message":"Ushbu ma'lumot mavjud!"
                }
            )
        return data


    def validate_price(self, price):
        if price < 0:
            raise ValidationError(
                {
                    'status':False,
                    "message":"Narx noto'g'ri kiritilgan"
                }
            )
        else:
            return price
from books.models import Book
from books.serializers import BookSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

# class BookListApi(ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookViewset(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookListAPIView(APIView):
    
    def get(self, request):
        books= Book.objects.all()
        serializer_data = BookSerializer(books, many = True).data
        data = {
            'status':status.HTTP_200_OK,
            'books': serializer_data
        }
        return Response(data)


# class BookCreateApi(CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookCreateAPIView(APIView):
    
    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'status': status.HTTP_200_OK,
                'books': data
            }
            return Response(data)
        else:
            data = {
                'status': status.HTTP_404_NOT_FOUND,
                'message': "Data not valid"
            }
            return Response(data)
        
    

# class BookRetrieveApi(RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookRetrieveAPIVIew(APIView):

    def get(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            serializer_data = BookSerializer(book).data
            data = {
                'status':status.HTTP_200_OK,
                'books': serializer_data
            }
            return Response(data)

        except Exception:
            data = {
                'status':status.HTTP_404_NOT_FOUND,
                'message': "Book is not found"
            }
            return Response(data)


# class BookUpdateApi(UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookUpdateAPIView(APIView):
    def put(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            data = request.data
            serializer = BookSerializer(instance = book, data = data, partial = True)
            if serializer.is_valid():
                book_saved = serializer.save()
                data = {
                    'status':status.HTTP_200_OK,
                    'message': f"Book {book_saved} updated successfully"
                }
                return Response(data)
            else:
                data = {
                    'status':status.HTTP_404_NOT_FOUND,
                    'message': "Data not valid"
                }
                return Response(data)
        except Exception:
            data = {
                'status':status.HTTP_404_NOT_FOUND,
                'message': "Book is not found"
            }
            return Response(data)


# class BookDestroyApi(DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookDestroyAPIView(APIView):

    def delete(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            book.delete()
            data = {
                'status':status.HTTP_200_OK,
                'message': "Successfull deleted"
            }
            return Response(data)

        except Exception:
            data = {
                'status':status.HTTP_404_NOT_FOUND,
                'message': "Book is not found"
            }
            return Response(data)
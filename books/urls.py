from django.urls import path
from books.views import BookListAPIView, BookRetrieveAPIVIew, BookDestroyAPIView, BookUpdateAPIView, BookCreateAPIView, BookViewset
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('books', BookViewset, basename = 'books')


urlpatterns = [
    # path('books/', BookListAPIView.as_view(), name='book-list' ),
    # path('books/create', BookCreateAPIView.as_view(), name='book-create' ),
    # path('books/<int:pk>/', BookRetrieveAPIVIew.as_view(), name='book-retrieve' ),
    # path('books/<int:pk>/delete/', BookDestroyAPIView.as_view(), name='book-delete' ),
    # path('books/<int:pk>/update/', BookUpdateAPIView.as_view(), name='book-update' ),
]

urlpatterns = urlpatterns + router.urls
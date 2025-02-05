from main import BooksCollector


def test_get_books_with_specific_genre_valid_genre_good():
    collector = BooksCollector()
    collector.books_genre = {'Игра престолов': 'Фантастика',
                             'Еретик' : 'Ужасы',
                             'Каштановые человечки' : 'Детектив',
                             'Моана' : 'Мультфильм',
                             'Американский пирог' : 'Комедии'
                             }
    assert collector.get_books_with_specific_genre('Ужасы') == ['Еретик']


def test_set_book_genre():
    collector = BooksCollector()
    collector.books_genre = {'Игра престолов': 'Фантастика',
                             'Еретик' : 'Ужасы',
                             'Каштановые человечки' : 'Детектив',
                             'Моана' : 'Мультфильм',
                             'Американский пирог' : 'Комедия'
                             }
    collector.set_book_genre('Моана' , 'Комедия')
    assert collector.books_genre ['Моана'] == 'Мультфильм'


def get_books_for_children_no_added():
    collector = BooksCollector()
    collector.books_genre = {'Игра престолов': 'Фантастика',
                             'Еретик': 'Ужасы',
                             'Каштановые человечки': 'Детектив',
                             'Моана': 'Мультфильм',
                             'Американский пирог': 'Комедии'
                             }
    assert collector.get_books_for_children() == ['Моана']


def add_book_in_favorites_my_again():
    collector = BooksCollector()
    collector.books_genre = {'Каштановые человечки': 'Детектив'}
    collector.favorites = ['Каштановые человечки']
    collector.add_book_in_favorites('Каштановые человечки')
    assert collector.favorites == ['Каштановые человечки'] and len(collector.favorites) == 1



def test_get_book_genre_good():
    collector = BooksCollector()
    collector.books_genre = {'Игра престолов': 'Фантастика',
                                'Еретик' : 'Ужасы',
                                'Каштановые человечки' : 'Детектив',
                                'Моана' : 'Мультфильм',
                                'Американский пирог' : 'Комедии'
                                 }
    assert collector.get_book_genre('Каштановые человечки') == collector.books_genre['Каштановые человечки']

def test_get_list_of_favorites_books_true(self):
    collector = BooksCollector()
    collector.favorites = ['Моана', 'Игра престолов', 'Каштановые человечки']
    assert collector.get_list_of_favorites_books() == collector.favorites

def test_add_new_book_add_one_books(self):
    collector = BooksCollector()
    collector.add_new_book('Облако')
    assert len(collector.get_books_genre()) == 1
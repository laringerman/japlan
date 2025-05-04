from django.test import TestCase
from django.http import HttpRequest  
from blog.views import home_page, article_page
from blog.models import Article
from django.urls import resolve
from datetime import datetime
import pytz

class ArticlePageeEst(TestCase):
    def test_article_page_displays_correct_article(self):
        Article.objects.create(
            title='title 1',
            summary='summary 1',
            full_text='full text 1',
            pubdate=datetime.now(pytz.utc),
            slug='slug-1',
            )
        
        
        request = HttpRequest()  
        response = article_page(request, 'slug-1')  
        html = response.content.decode("utf8")  
 
        self.assertIn("title 1", html)
        self.assertIn("full text 1", html)
        self.assertNotIn("summary 1", html)
        


class HomePageTest(TestCase):

    def test_home_page_displays_articles(self):
        Article.objects.create(
            title='title 1',
            summary='summary 1',
            full_text='full text 1',
            pubdate=datetime.now(pytz.utc),
            slug='slug-1',
            )
        
        Article.objects.create(
            title='title 2',
            summary='summary 2',
            full_text='full text 2',
            pubdate=datetime.now(pytz.utc),
            slug='slug-2',
            )
        
        request = HttpRequest()  
        response = home_page(request)  
        html = response.content.decode("utf8")  
 
        self.assertIn("title 1", html)
        self.assertIn("/blog/slug-1", html)
        self.assertIn("summary 1", html)
        self.assertNotIn("full text 1", html)

        self.assertIn("title 2", html)
        self.assertIn("/blog/slug-2", html)
        self.assertIn("summary 2", html)
        self.assertNotIn("full text 2", html)



    def test_root_url_resolves_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)



    def test_home_page_returns_correct_html(self):
        request = HttpRequest()  
        response = home_page(request)  
        html = response.content.decode("utf8")  


        self.assertTrue(html.startswith("<html>"))  
        self.assertIn("<title>JapLAN - Маршруты путешествий</title>", html)  
        self.assertIn("<h1>JapLAN</h1>", html)  
        self.assertTrue(html.endswith("</html>")) 


class ArticleModelTest(TestCase):

    def test_article_model_save_and_retrieve(self):
        # создай статью й
        article_1 = Article(
            title='article 1',
            full_text='full text 1',
            summary='summary 1',
            category='category 1',
            pubdate=datetime.now(pytz.utc),
            slug='slug-1',
        )
        # сохрани статью 1 в базе
        article_1.save()

        # создай статью 2
        article_2 = Article(
            title='article 2',
            full_text='full text 2',
            summary='summary 2',
            category='category 2',
            pubdate=datetime.now(pytz.utc),
            slug='slug-2',
        )
        # сохрани статью 2 в базе
        article_2.save()

        # загрузи из базы все статьи
        all_articles = Article.objects.all()

        # проверь - статей должно быть 2
        self.assertEqual(len(all_articles), 2)

        # проверь - первая загруженная статья == статья 1 по названию и слагу
        self.assertEqual(
            all_articles[0].title,
            article_1.title
        )
        self.assertEqual(
            all_articles[0].slug,
            article_1.slug
        )

        # проверь - вторая загруженная из базы статья == статья 2 по названию и слагу
        self.assertEqual(
            all_articles[1].title,
            article_2.title
        )

        self.assertEqual(
            all_articles[1].slug,
            article_2.slug
        )
        
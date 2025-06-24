from selenium import webdriver
from selenium.webdriver.common.by import By
from django.test import LiveServerTestCase, Client
from blog.models import Article
from datetime import datetime
import unittest
import pytz
import os

# Жил Марк
# Марк планирует отпуск в Японию
# Макр захотел найти какой-нибудь готовый план путешествия, т.к. в новой стране еще не разбирается
# Марк вбил в гугл 'планы путешествия по Японии' и кликнул по одной ихз ссылок

class BlogTests(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server
        else:
            # Создаём данные только для локального тестового сервера
            Article.objects.create(
                title='title 1',
                summary='summary 1',
                full_text='full_text 1',
                pubdate=datetime.utcnow().replace(tzinfo=pytz.utc),
                slug='slug-1',
                category='category-1',
                og_image=File(open('test_images/test_image_1.png', 'rb'))
            )
        print("STAGING_SERVER:", os.environ.get('STAGING_SERVER'))
        
    def tearDown(self):  
        self.browser.quit()

    def test_home_page_title(self):  

        # В браузере открылся сайт (по адрусу...)
        self.browser.get(self.live_server_url)  

        # В заголовке сайта Макр прочитал  'JapLAN'
        self.assertIn('JapLAN - Маршруты путешествий', self.browser.title)  


    def test_home_page_header(self):  

        # В шапке сайта написано 'JapLAN'
        self.browser.get(self.live_server_url)  
        header = self.browser.find_element(By.TAG_NAME, 'h1')

        self.assertIn('JapLAN', header.text)      
  
        

    def test_layout_and_styling(self):
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        footer = self.browser.find_element(By.CLASS_NAME, 'footer')
        self.assertTrue(footer.location['y'] > 600)

    def test_home_page_blog(self):
        # А под шапкой расположен блог со статьями
        self.browser.get(self.live_server_url)
        article_list = self.browser.find_element(By.CLASS_NAME, 'article-list')        
        self.assertTrue(article_list)

    
    def test_home_page_articles_look_correct(self):
        # У каждой статьи есть заголовок и короткое описание
        self.browser.get(self.live_server_url)
        article_title = self.browser.find_element(By.CLASS_NAME, 'article-title')            
        article_summary = self.browser.find_element(By.CLASS_NAME, 'article-summary')
        self.assertTrue(article_title) 
        self.assertTrue(article_summary)   

    
    def test_home_page_article_title_link_leads_to_article_page(self):
        # Марк кликнул по заголовку и у него открылась страница с полным текстом статьи

        # открываем главную страницу
        self.browser.get(self.live_server_url)
        # находим статью
        # находим заголовок статьи
        article_title = self.browser.find_element(By.CLASS_NAME, 'article-title')
        # cохраняем заголовок статьи
        article_title_text = article_title.text
        # находим ссылку в заголовке статьи
        article_link = article_title.find_element(By.TAG_NAME, 'a')
        # переходим по ссылке
        self.browser.get(article_link.get_attribute('href'))
        # ожидаем что на открывшейся странице есть нужная статья
        article_page_title = self.browser.find_element(By.CLASS_NAME, 'article-title')
        self.assertEqual(article_title_text, article_page_title.text)


 #self.fail('Finish the test!') 



# На странице статьи Марк прочитал заголовок страницы с названием статьи


# Марк попытался открыть несуществующую статью и ему открылась красивая страница 'Станица не найдена'


# Прочитав статью Марк кликнул по тексту 'JapLAN' в шапке сайта и попал на главную страницу обратно


# Если некоторые статьи есть в адмике и они не опубликованы
# Статьи открываются с красивым коротким адресом
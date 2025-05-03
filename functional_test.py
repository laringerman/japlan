from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

# Жил Марк
# Марк планирует отпуск в Японию
# Макр захотел найти какой-нибудь готовый план путешествия, т.к. в новой стране еще не разбирается
# Марк вбил в гугл "планы путешествия по Японии" и кликнул по одной ихз ссылок

class BasicInstallTest(unittest.TestCase):  
    def setUp(self):  
        self.browser = webdriver.Chrome()  

    def tearDown(self):  
        self.browser.quit()

    def test_home_page_title(self):  

        # В браузере открылся сайт (по адрусу...)
        self.browser.get("http://127.0.0.1:8000")  

        # В заголовке сайта Макр прочитал  "JapLAN"
        self.assertIn('JapLAN - Маршруты путешествий', self.browser.title)  


    def test_home_page_header(self):  

        # В шапке сайта написано "JapLAN"
        self.browser.get("http://127.0.0.1:8000")  
        header = self.browser.find_element(By.TAG_NAME, "h1")

        self.assertIn('JapLAN', header.text)      
  
        #self.fail("Finish the test!")  


    def test_home_page_blog(self):
        # А под шапкой расположен блог со статьями
        self.browser.get("http://127.0.0.1:8000")
        article_list = self.browser.find_element(By.CLASS_NAME, 'article-list')        
        self.assertTrue(article_list)

    
    def test_home_page_articles_look_correct(self):
        # У каждой статьи есть заголовок и короткое описание
        self.browser.get("http://127.0.0.1:8000")
        article_tittle = self.browser.find_element(By.CLASS_NAME, 'article-tittle')            
        article_summary = self.browser.find_element(By.CLASS_NAME, 'article-summary')
        self.assertTrue(article_tittle) 
        self.assertTrue(article_summary)   


if __name__ == "__main__":  
    unittest.main()  








# Марк кликнул по заголовку и у него открылась страница с полным текстом статьи

# Прочитав статью Марк кликнул по тексту "JapLAN" в шапке сайта и попал на главную страницу обратно


# Если некоторые статьи есть в адмике и они не опубликованы
# Статьи открываются с красивым коротким адресом
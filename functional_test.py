from selenium import webdriver
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
        self.assertIn('JapLAN', self.browser.title)  


    def test_home_page_header(self):  

        # В шапке сайта написано "JapLAN"
        browser = self.browser.get("http://127.0.0.1:8000")  
        header = browser.find_elements_by_tag_name('h1')[0]

        self.assertIn('JapLAN', header)      
  
        #self.fail("Finish the test!")  


if __name__ == "__main__":  
    unittest.main()  




# А под шапкой расположен блог со статьями

# У каждой статьи есть заголовок и короткое описание

# Марк кликнул по заголовку и у него открылась страница с полным текстом статьи

# Прочитав статью Марк кликнул по тексту "JapLAN" в шапке сайта и попал на главную страницу обратно



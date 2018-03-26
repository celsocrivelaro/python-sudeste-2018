import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class ListagemProdutos(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

        produto1 = Produto(nome='Produto 1', valor=99.99)
        produto2 = Produto(nome='Produto 2', valor=199.99)
        produto3 = Produto(nome='Produto 3', valor=79.99)

    def test_listagem(self):
        driver = self.driver
        driver.get("http://endereco.com/listagem")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

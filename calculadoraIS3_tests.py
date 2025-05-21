import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class TestCalculadoraIS3(unittest.TestCase):

    def setUp(self):
        # Configuración inicial del navegador
        self.driver = webdriver.Edge()
        self.driver.get("https://gerabarud.github.io/is3-calculadora/") 
        time.sleep(2)  # Espera a que la página cargue completamente 
        self.input_operador1 = self.driver.find_element(By.ID, "number1Field")
        self.input_operador2 = self.driver.find_element(By.ID, "number2Field")
        self.input_operador1.clear()
        self.input_operador2.clear()
        self.boton_calcular = self.driver.find_element(By.ID, "calculateButton")

    def test_caso_prueba1(self):
        driver = self.driver
        # Encuentra el campo de entrada y envía una expresión matemática
        self.input_operador1.clear()
        self.input_operador2.clear()
        self.input_operador1.send_keys("2")
        self.input_operador2.send_keys("2")
        
        # Encuentra el botón de suma y haz clic en él
        self.boton_calcular.click()

        # Espera un momento para que se procese la solicitud
        time.sleep(2)

        # Verifica el resultado
        result = driver.find_element(By.ID, "numberAnswerField").get_attribute("value")
        self.assertEqual(result, "4")


    def tearDown(self):
        # Cierra el navegador después de cada prueba
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
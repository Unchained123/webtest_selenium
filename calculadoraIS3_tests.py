import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

class TestCalculadoraIS3(unittest.TestCase):

    def setUp(self):
        # Configuración inicial del navegador
        self.driver = webdriver.Edge()
        self.driver.get("https://gerabarud.github.io/is3-calculadora/") 
        self.driver.minimize_window()
        time.sleep(2)  # Espera a que la página cargue completamente 
        self.input_operador1 = self.driver.find_element(By.ID, "number1Field")
        self.input_operador2 = self.driver.find_element(By.ID, "number2Field")
        self.input_operador1.clear()
        self.input_operador2.clear()
        self.selector_build= Select(self.driver.find_element(By.ID, "selectBuild"))
        self.selector_build.select_by_visible_text("9")
        self.selector_operacion= Select(self.driver.find_element(By.ID, "selectOperationDropdown"))
        self.botonIntegers= self.driver.find_element(By.ID, "integerSelect")
        self.boton_calcular = self.driver.find_element(By.ID, "calculateButton")
        self.resultado = self.driver.find_element(By.ID, "numberAnswerField")

    def test_caso_prueba1(self): # Prueba suma entera valida
        if not(self.botonIntegers.is_selected()):
            self.botonIntegers.click()
        # Configurar selectores
        self.selector_operacion.select_by_visible_text("Add")
        # Encuentra el campo de entrada y envía una expresión matemática
        self.input_operador1.clear()
        self.input_operador2.clear()
        self.input_operador1.send_keys("9999999999")
        self.input_operador2.send_keys("9999999999")
        
        # Encuentra el botón de suma y haz clic en él
        self.boton_calcular.click()

        # Espera un momento para que se procese la solicitud
        time.sleep(2)

        # Verifica el resultado
        result = self.resultado.get_attribute("value")
        self.assertEqual(result, "19999999998", "CP 1 fallo.")

    def test_caso_prueba2(self): # Prueba suma real valida
        # Configurar selectores
        self.selector_operacion.select_by_visible_text("Add")

        if self.botonIntegers.is_selected():
            self.botonIntegers.click()

        # Encuentra el campo de entrada y envía una expresión matemática
        self.input_operador1.clear()
        self.input_operador2.clear()
        self.input_operador1.send_keys("9.999999999 ")
        self.input_operador2.send_keys("9.999999999")
        
        # Encuentra el botón de suma y haz clic en él
        self.boton_calcular.click()

        # Espera un momento para que se procese la solicitud
        time.sleep(2)

        # Verifica el resultado
        result = self.resultado.get_attribute("value")
        self.assertEqual(result, "19.99999998", "CP 2 fallo.")

    def test_caso_prueba3(self): # Prueba suma invalida op2
        # Configurar selectores
        self.selector_operacion.select_by_visible_text("Add")

        # Encuentra el campo de entrada y envía una expresión matemática
        self.input_operador1.clear()
        self.input_operador2.clear()
        self.input_operador1.send_keys("99999999999")
        self.input_operador2.send_keys("K")
        
        # Encuentra el botón de suma y haz clic en él
        self.boton_calcular.click()

        # Espera un momento para que se procese la solicitud
        time.sleep(2)

        # Verifica el resultado
        error = self.driver.find_element(By.ID, "errorMsgField").text
        self.assertIsNotNone(error, "CP 3 fallo.")

    def test_caso_prueba4(self): # Prueba suma invalida op1
        # Configurar selectores
        self.selector_operacion.select_by_visible_text("Add")

        # Encuentra el campo de entrada y envía una expresión matemática
        self.input_operador1.clear()
        self.input_operador2.clear()
        self.input_operador1.send_keys("K")
        self.input_operador2.send_keys("99999999999")
        
        # Encuentra el botón de suma y haz clic en él
        self.boton_calcular.click()

        # Espera un momento para que se procese la solicitud
        time.sleep(2)

        # Verifica el resultado
        error = self.driver.find_element(By.ID, "errorMsgField").text
        self.assertIsNotNone(error, "CP 4 fallo.")

    def test_caso_prueba5(self): # Prueba suma invalida ambos operadores
        # Configurar selectores
        self.selector_operacion.select_by_visible_text("Add")

        # Encuentra el campo de entrada y envía una expresión matemática
        self.input_operador1.clear()
        self.input_operador2.clear()
        self.input_operador1.send_keys("K")
        self.input_operador2.send_keys("A")
        
        # Encuentra el botón de suma y haz clic en él
        self.boton_calcular.click()

        # Espera un momento para que se procese la solicitud
        time.sleep(2)

        # Verifica el resultado
        error = self.driver.find_element(By.ID, "errorMsgField").text
        self.assertIsNotNone(error, "CP 5 fallo.")

    def test_caso_prueba6(self): # Prueba resta entera valida
        if not(self.botonIntegers.is_selected()):
            self.botonIntegers.click()
        # Configurar selectores
        self.selector_operacion.select_by_visible_text("Subtract")
        # Encuentra el campo de entrada y envía una expresión matemática
        self.input_operador1.clear()
        self.input_operador2.clear()
        self.input_operador1.send_keys("9999999999")
        self.input_operador2.send_keys("9999999999")
        
        # Encuentra el botón de suma y haz clic en él
        self.boton_calcular.click()

        # Espera un momento para que se procese la solicitud
        time.sleep(2)

        # Verifica el resultado
        result = self.resultado.get_attribute("value")
        self.assertEqual(result, "0", "CP 6 fallo.")

    def test_caso_prueba7(self): # Prueba resta real valida
        # Configurar selectores
        self.selector_operacion.select_by_visible_text("Subtract")

        if self.botonIntegers.is_selected():
            self.botonIntegers.click()

        # Encuentra el campo de entrada y envía una expresión matemática
        self.input_operador1.clear()
        self.input_operador2.clear()
        self.input_operador1.send_keys("9999999999")
        self.input_operador2.send_keys("-9999999999")
        
        # Encuentra el botón de suma y haz clic en él
        self.boton_calcular.click()

        # Espera un momento para que se procese la solicitud
        time.sleep(2)

        # Verifica el resultado
        result = self.resultado.get_attribute("value")
        self.assertEqual(result, str(9999999999-(-9999999999)), "CP 7 fallo.")

    def test_caso_prueba8(self): # Prueba resta invalida op2
        # Configurar selectores
        self.selector_operacion.select_by_visible_text("Subtract")

        # Encuentra el campo de entrada y envía una expresión matemática
        self.input_operador1.clear()
        self.input_operador2.clear()
        self.input_operador1.send_keys("99999999999")
        self.input_operador2.send_keys("M")
        
        # Encuentra el botón de suma y haz clic en él
        self.boton_calcular.click()

        # Espera un momento para que se procese la solicitud
        time.sleep(2)

        # Verifica el resultado
        error = self.driver.find_element(By.ID, "errorMsgField").text
        self.assertIsNotNone(error, "CP 3 fallo.")

    def test_caso_prueba9(self): # Prueba resta invalida op1
        # Configurar selectores
        self.selector_operacion.select_by_visible_text("Subtract")

        # Encuentra el campo de entrada y envía una expresión matemática
        self.input_operador1.clear()
        self.input_operador2.clear()
        self.input_operador1.send_keys("E")
        self.input_operador2.send_keys("99999999999")
        
        # Encuentra el botón de suma y haz clic en él
        self.boton_calcular.click()

        # Espera un momento para que se procese la solicitud
        time.sleep(2)

        # Verifica el resultado
        error = self.driver.find_element(By.ID, "errorMsgField").text
        self.assertIsNotNone(error, "CP 9 fallo.")

    def test_caso_prueba10(self): # Prueba suma invalida ambos operadores
        # Configurar selectores
        self.selector_operacion.select_by_visible_text("Subtract")

        # Encuentra el campo de entrada y envía una expresión matemática
        self.input_operador1.clear()
        self.input_operador2.clear()
        self.input_operador1.send_keys("E")
        self.input_operador2.send_keys("M")
        
        # Encuentra el botón de suma y haz clic en él
        self.boton_calcular.click()

        # Espera un momento para que se procese la solicitud
        time.sleep(2)

        # Verifica el resultado
        error = self.driver.find_element(By.ID, "errorMsgField").text
        self.assertIsNotNone(error, "CP 10 fallo.")

    def test_caso_prueba11(self): # Prueba multiplicacion entera valida
        if not(self.botonIntegers.is_selected()):
            self.botonIntegers.click()
        # Configurar selectores
        self.selector_operacion.select_by_visible_text("Multiply")
        # Encuentra el campo de entrada y envía una expresión matemática
        self.input_operador1.clear()
        self.input_operador2.clear()
        self.input_operador1.send_keys("9999999999")
        self.input_operador2.send_keys("9999999999")
        
        # Encuentra el botón de suma y haz clic en él
        self.boton_calcular.click()

        # Espera un momento para que se procese la solicitud
        time.sleep(2)

        # Verifica el resultado
        result = self.resultado.get_attribute("value")
        self.assertEqual(result, "99999999980000000001", "CP 11 fallo.")

    def test_caso_prueba12(self): # Prueba multiplicacion real valida
        # Configurar selectores
        self.selector_operacion.select_by_visible_text("Multiply")

        if self.botonIntegers.is_selected():
            self.botonIntegers.click()

        # Encuentra el campo de entrada y envía una expresión matemática
        self.input_operador1.clear()
        self.input_operador2.clear()
        self.input_operador1.send_keys("-9.9999999")
        self.input_operador2.send_keys("9.999999999 ")
        
        # Encuentra el botón de suma y haz clic en él
        self.boton_calcular.click()

        # Espera un momento para que se procese la solicitud
        time.sleep(2)

        # Verifica el resultado
        result = self.resultado.get_attribute("value")
        self.assertEqual(result, "-99.999998900000001", "CP 12 fallo.")

    def test_caso_prueba13(self): # Prueba multiplicacion invalida op1
        # Configurar selectores
        self.selector_operacion.select_by_visible_text("Multiply")

        # Encuentra el campo de entrada y envía una expresión matemática
        self.input_operador1.clear()
        self.input_operador2.clear()
        self.input_operador1.send_keys("e8.")
        self.input_operador2.send_keys("9999999999")
        
        # Encuentra el botón de suma y haz clic en él
        self.boton_calcular.click()

        # Espera un momento para que se procese la solicitud
        time.sleep(2)

        # Verifica el resultado
        error = self.driver.find_element(By.ID, "errorMsgField").text
        self.assertIsNotNone(error, "CP 13 fallo.")

    def test_caso_prueba14(self): # Prueba multiplicacion invalida op2
        # Configurar selectores
        self.selector_operacion.select_by_visible_text("Multiply")

        # Encuentra el campo de entrada y envía una expresión matemática
        self.input_operador1.clear()
        self.input_operador2.clear()
        self.input_operador1.send_keys("99999999999")
        self.input_operador2.send_keys("-.")
        
        # Encuentra el botón de suma y haz clic en él
        self.boton_calcular.click()

        # Espera un momento para que se procese la solicitud
        time.sleep(2)

        # Verifica el resultado
        error = self.driver.find_element(By.ID, "errorMsgField").text
        self.assertIsNotNone(error, "CP 14 fallo.")

    def test_caso_prueba15(self): # Prueba division entera valida
        if not(self.botonIntegers.is_selected()):
            self.botonIntegers.click()
        # Configurar selectores
        self.selector_operacion.select_by_visible_text("Divide")
        # Encuentra el campo de entrada y envía una expresión matemática
        self.input_operador1.clear()
        self.input_operador2.clear()
        self.input_operador1.send_keys("9999999999")
        self.input_operador2.send_keys("9999999999")
        
        # Encuentra el botón de suma y haz clic en él
        self.boton_calcular.click()

        # Espera un momento para que se procese la solicitud
        time.sleep(2)

        # Verifica el resultado
        result = self.resultado.get_attribute("value")
        self.assertEqual(result, "1", "CP 15 fallo.")

    def test_caso_prueba16(self): # Prueba division real valida
        # Configurar selectores
        self.selector_operacion.select_by_visible_text("Divide")

        if self.botonIntegers.is_selected():
            self.botonIntegers.click()

        # Encuentra el campo de entrada y envía una expresión matemática
        self.input_operador1.clear()
        self.input_operador2.clear()
        self.input_operador1.send_keys("9999999999")
        self.input_operador2.send_keys("999.99999")
        
        # Encuentra el botón de suma y haz clic en él
        self.boton_calcular.click()

        # Espera un momento para que se procese la solicitud
        time.sleep(2)

        # Verifica el resultado
        result = self.resultado.get_attribute("value")
        self.assertEqual(result, str(9999999999/999.99999), "CP 16 fallo.")

    def test_caso_prueba17(self): # Prueba division entera valida primer operando menor
        # Configurar selectores
        self.selector_operacion.select_by_visible_text("Divide")

        if not(self.botonIntegers.is_selected()):
            self.botonIntegers.click()

        # Encuentra el campo de entrada y envía una expresión matemática
        self.input_operador1.clear()
        self.input_operador2.clear()
        self.input_operador1.send_keys("99999")
        self.input_operador2.send_keys("9999999999")
        
        # Encuentra el botón de suma y haz clic en él
        self.boton_calcular.click()

        # Espera un momento para que se procese la solicitud
        time.sleep(2)

        # Verifica el resultado
        result = self.resultado.get_attribute("value")
        self.assertEqual(result, "0", "CP 17 fallo.")

    def test_caso_prueba18(self): # Prueba division entera invalida
        if not(self.botonIntegers.is_selected()):
            self.botonIntegers.click()
        # Configurar selectores
        self.selector_operacion.select_by_visible_text("Divide")
        # Encuentra el campo de entrada y envía una expresión matemática
        self.input_operador1.clear()
        self.input_operador2.clear()
        self.input_operador1.send_keys("9999999999")
        self.input_operador2.send_keys("0")
        
        # Encuentra el botón de suma y haz clic en él
        self.boton_calcular.click()

        # Espera un momento para que se procese la solicitud
        time.sleep(2)

        # Verifica el resultado
        result = self.resultado.get_attribute("value")
        error = self.driver.find_element(By.ID, "errorMsgField").text
        self.assertTrue(result == "Infinity" or result == "-Infinity" or error!=None, "CP 18 fallo.")

    def test_caso_prueba19(self): # Prueba division entera invalida
        if not(self.botonIntegers.is_selected()):
            self.botonIntegers.click()
        # Configurar selectores
        self.selector_operacion.select_by_visible_text("Divide")
        # Encuentra el campo de entrada y envía una expresión matemática
        self.input_operador1.clear()
        self.input_operador2.clear()
        self.input_operador1.send_keys("0")
        self.input_operador2.send_keys("0")
        
        # Encuentra el botón de suma y haz clic en él
        self.boton_calcular.click()

        # Espera un momento para que se procese la solicitud
        time.sleep(2)

        # Verifica el resultado
        result = self.resultado.get_attribute("value")
        error = self.driver.find_element(By.ID, "errorMsgField").text
        self.assertTrue(result == "Infinity" or result == "-Infinity" or error!=None, "CP 19 fallo.")

    def test_caso_prueba20(self): # Prueba concatenacion valida
        # Configurar selectores
        self.selector_operacion.select_by_visible_text("Concatenate")
        # Encuentra el campo de entrada y envía una expresión matemática
        self.input_operador1.clear()
        self.input_operador2.clear()
        self.input_operador1.send_keys("ABCDEFGHIJ")
        self.input_operador2.send_keys("KMNLOPQRST")
        
        # Encuentra el botón de suma y haz clic en él
        self.boton_calcular.click()

        # Espera un momento para que se procese la solicitud
        time.sleep(2)

        # Verifica el resultado
        result = self.resultado.get_attribute("value")
        self.assertEqual(result, "ABCDEFGHIJKMNLOPQRST", "CP 20 fallo.")


    def tearDown(self):
        # Cierra el navegador después de cada prueba
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

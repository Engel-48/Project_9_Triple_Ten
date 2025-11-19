import time
from time import sleep

import data
import pages
import helpers
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options






class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono

        options = Options()

        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})

        cls.driver = webdriver.Chrome(service=Service(), options=options)
#1. Establecer dirección
    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = pages.UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to
#2. Selección taxi
    def test_click_on_request_taxi_button (self):
        routes_page = pages.UrbanRoutesPage(self.driver)
        routes_page.click_on_request_taxi_button()

       # button = self.driver.find_element(*routes_page.request_taxi_button)
       # assert routes_page.get_request_taxi_button().text == button

#3. Seleccionar tarifa 'Confort'
    def test_select_confort_rate (self):
       # self.test_set_route()
        routes_page = pages.UrbanRoutesPage(self.driver)
        #routes_page.click_on_request_taxi_button()

        routes_page.click_on_confort_rate_option()
        assert routes_page.get_confort_rate_option().text == 'Comfort'

#4 Seleccionar teléfono
    def test_click_on_cellphone_number_field (self):
        routes_page = pages.UrbanRoutesPage(self.driver)
        routes_page.click_on_cellphone_number_field()


#5 Enviar número de teléfono
    def test_send_keys_phone_number (self):
        routes_page = pages.UrbanRoutesPage(self.driver)
        cellphone_number = data.phone_number
        routes_page.set_cellphone_number(cellphone_number)

#6. Seleccionar botón siguiente
    def test_click_on_next_button(self):
        routes_page = pages.UrbanRoutesPage(self.driver)
        routes_page.click_next_button()

#7 Enviar código
    def test_receive_code_of_number_phone_number_field (self):
        routes_page = pages.UrbanRoutesPage(self.driver)
        cellphone_code = helpers.retrieve_phone_code(self.driver)

        routes_page.set_phone_code_number_field(cellphone_code)
#8. Seleccionar botón de confirmación
    def test_click_on_confirm_button_code_cellphone (self):
        routes_page = pages.UrbanRoutesPage(self.driver)
        routes_page.click_on_confirm_button_code_cellphone()

        assert routes_page.get_phone_number() == '+1 123 123 12 12'

#9. Seleccionar método de pago

    def test_click_on_pay_method_field(self):
        routes_page = pages.UrbanRoutesPage(self.driver)
        routes_page.click_pay_method_field()
#10. Seleccionar agregar tarjeta
    def test_click_on_add_card_button(self):
        routes_page = pages.UrbanRoutesPage(self.driver)
        routes_page.click_on_add_card_button()

        title_text = routes_page.get_add_card_text_field()


        assert title_text == 'Agregar tarjeta'
#11. Enviar número de tarjeta
    def test_number_card_field_send_keys (self):
        routes_page = pages.UrbanRoutesPage(self.driver)

        number_card_field = data.card_number
        routes_page.set_card_number_field(number_card_field)
#12. Enviar número de código
    def test_card_code_field (self):
        routes_page = pages.UrbanRoutesPage(self.driver)
        card_code_number = data.card_code
        routes_page.set_card_number_code_field(card_code_number)
        assert routes_page.add_card_payment_add_button().is_displayed(), "El campo de verificación no se mostró"
#13. Seleccionar agregar tarjeta
    def test_click_add_card_buton(self):
        routes_page = pages.UrbanRoutesPage(self.driver)
        routes_page.click_add_card_button_submit()

#14. Cerrar método de pago
    def test_click_on_close_pay_method_button(self):
        routes_page = pages.UrbanRoutesPage(self.driver)
        routes_page.click_on_close_pay_method_button()
#15. Enviar comentario al conductor
    def test_send_comment_to_driver (self):
        routes_page = pages.UrbanRoutesPage(self.driver)
        comment_driver = data.message_for_driver
        routes_page.set_comment_driver_field(comment_driver)

        comment_assert = routes_page.get_message_for_driver_text()
        assert comment_assert == "show museum's path"

#16. SCROLL
    def test_scroll_space(self):
        routes_page = pages.UrbanRoutesPage(self.driver)
        routes_page.set_scroll_space()

#17. Seleccionar mantas
    def test_slider_round_element(self):
        routes_page = pages.UrbanRoutesPage(self.driver)
        routes_page.click_on_slider_round_element()
        assert routes_page.slider_round_element_assert().is_displayed(), "El botón de activado no se moestró"
#18. Seleccionar 2 helados
    def test_click_on_ice_crem_button(self):
        routes_page = pages.UrbanRoutesPage(self.driver)
        routes_page.click_on_ice_crem_button()
        count_ice_cream = int(routes_page.count_number_of_ice_cream_())
        number_of_ice_cream = 2
        assert count_ice_cream == number_of_ice_cream


#19. Seleccionar en pedir taxi
    def test_click_on_ask_taxi_button(self):
        routes_page = pages.UrbanRoutesPage(self.driver)
        routes_page.click_on_ask_taxi_button()

        image = WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(routes_page.image_bender))
        assert image.is_displayed(), "La imágen de bender no es visible"
#20. Validación de información del conductor
    def test_validation_driver_information(self):
        routes_page = pages.UrbanRoutesPage(self.driver)
        routes_page.driver_info()
        rating_driver, image_driver, name_driver = routes_page.get_information_driver()
        assert rating_driver
        assert image_driver
        assert name_driver
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

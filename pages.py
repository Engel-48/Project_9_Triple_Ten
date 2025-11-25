import elements
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

#ángel ramírez_3



class UrbanRoutesPage:



    def __init__(self, driver):
        self.driver = driver
#1. Set from to

    def set_from(self, from_address):
        #self.driver.find_element(*self.from_field).send_keys(from_address)
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(elements.from_field)).send_keys(from_address)

    def set_to(self, to_address):
        #self.driver.find_element(*self.to_field).send_keys(to_address)
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(elements.to_field)).send_keys(to_address)

#2. Set route
    def get_from(self):
        return self.driver.find_element(*elements.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*elements.to_field).get_property('value')

    def set_route (self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def get_request_taxi_button (self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(elements.request_taxi_button))

    def click_on_request_taxi_button (self):
        self.get_request_taxi_button().click()

#3. Select comfort option

    def get_confort_rate_option(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(elements.confort_rate_option))

    def click_on_confort_rate_option(self):
        self.get_confort_rate_option().click()

#4. Click on cellphone option
    def get_cellphone_number_field(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(elements.cellphone_number_field))

    def click_on_cellphone_number_field (self):
        self.get_cellphone_number_field().click()

#5. Set cellphone field option with send keys
    def get_cellphone(self):
        return self.driver.find_element(*elements.cellphone_number)

    def set_cellphone_number (self, phone):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(elements.cellphone_number)).send_keys(phone)
       # time.sleep(10)



#6. Click on next button in number field
    def get_next_button_number(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(elements.next_button_number_field))

    def click_next_button(self):
        self.get_next_button_number().click()
#        time.sleep(10)
#7. Set code field with send keys
    def get_phone_code_number_field(self):
        return self.driver.find_element(*elements.code_phone_field)

    def set_phone_code_number_field (self, code):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(elements.code_phone_field)).send_keys(code)


    #time.sleep(10)
#8. Click on confirmation button click
    def get_confirm_button_code_cellphone (self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(elements.button_code_confirm_cellphone))

    def click_on_confirm_button_code_cellphone(self):
        self.get_confirm_button_code_cellphone().click()


    def get_phone_number(self):
        return self.driver.find_element(*elements.confirmation_assert_cellphone_number).text





#9.Click on Method pay field
    def get_pay_method_field(self):
        return WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(elements.pay_method_field))

    def click_pay_method_field (self):
        self.get_pay_method_field().click()



#10. Click on add card button
    def get_add_card_button(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(elements.add_card_button))

    def click_on_add_card_button(self):
        self.get_add_card_button().click()
        #time.sleep(10)
#11. Set Card number field with send keys
    def get_card_number_field(self):
        return self.driver.find_element(*elements.card_number_field)

    def set_card_number_field (self, number):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(elements.card_number_field)).send_keys(number)
#        time.sleep(10)

#12. Set card code field with send keys
    def get_code_card_field(self):
        return self.driver.find_element(*elements.card_number_code_field)


    def set_card_number_code_field(self, code_card):
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(elements.card_number_code_field)).send_keys(code_card)
        #time.sleep(10)
    def add_card_payment_add_button(self):
        return self.driver.find_element(*elements.card_code_add_button)

#13. Click on add card number button
    def get_add_card_button_submit(self):
        return self.driver.find_element(*elements.card_code_add_button)

    #time.sleep(10)


    def click_add_card_button_submit(self):
        self.get_add_card_button_submit().click()
        #time.sleep(10)
#14. Click on close method pay button
    def get_close_pay_method_button(self):
        return self.driver.find_element(*elements.close_button_pay_method)
    def click_on_close_pay_method_button(self):
        self.get_close_pay_method_button().click()
    #time.sleep(10)
#15. Set comment for driver with send keys
    def get_comment_driver_field(self):
        return self.driver.find_element(*elements.comment_driver_field)
    def set_comment_driver_field (self, comment):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(elements.comment_driver_field)).send_keys(comment)
    def get_message_for_driver_text (self):
        return self.driver.find_element(*elements.comment_driver_field).get_property('value')

#16. Set a scroll
    def get_scroll_space(self):
        return self.driver.find_element(*elements.scroll_space)
    def set_scroll_space(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.get_scroll_space())

       # time.sleep(10)
#17. Click on slide element
    def get_slider_round_element(self):
        return self.driver.find_element(*elements.slider_round_element)
    def click_on_slider_round_element(self):
        self.get_slider_round_element().click()

#18. Click on add ice crem button twice
    def get_ice_crem_button(self):
        return self.driver.find_element(*elements.ice_cream_element)

    time.sleep(10)

    time.sleep(10)
    def click_on_ice_crem_button(self):
        button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(elements.ice_cream_element))
        for _ in range(2):
            button.click()
        time.sleep(10)
#19. Click on ssk taxi button
    def get_ask_taxi_button(self):
        return self.driver.find_element(*elements.ask_taxi_button)

    def click_on_ask_taxi_button(self):
        self.get_ask_taxi_button().click()

#20 Funciones para comprobar 'assert'
    def get_add_card_text_field(self):
        return self.driver.find_element(*elements.add_card_field_text).text
    def slider_round_element_assert (self):
        return self.driver.find_element(*elements.slider_round_element)
    def count_number_of_ice_cream_(self):
        return self.driver.find_element(*elements.ice_cream_count).text
    def image_of_bender(self):
        return self.driver.find_element(*elements.image_bender)
    def driver_info (self):
        WebDriverWait(self.driver,40).until(EC.visibility_of_element_located(elements.order_modal))
        self.driver.find_element(*elements.order_rating)
        self.driver.find_element(*elements.order_image)
        self.driver.find_element(*elements.order_name)
    def get_information_driver(self):
        rating_driver = self.driver.find_element(*elements.order_rating).text
        image_driver = self.driver.find_element(*elements.order_image).get_property('src')
        name_driver = self.driver.find_element(*elements.order_name).text
        return rating_driver, image_driver, name_driver
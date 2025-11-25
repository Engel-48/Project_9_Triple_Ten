from selenium.webdriver.common.by import By

from_field = (By.ID, "from")
to_field = (By.ID, "to")
request_taxi_button = (By.CSS_SELECTOR, ".button.round")

# confort_rate_option = (By.XPATH, "//div[@class='tcard-icon']/img[@alt='Comfort']")
confort_rate_option = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[2]")
cellphone_number_field = (By.CLASS_NAME, "np-text")
cellphone_number = (By.ID, "phone")
next_button_number_field = (By.XPATH, "//*[@id='root']/div/div[1]/div[2]/div[1]/form/div[2]/button")
code_phone_field = (By.XPATH, "//*[@id='code']")
button_code_confirm_cellphone = (By.XPATH, "//*[@id='root']/div/div[1]/div[2]/div[2]/form/div[2]/button[1]")
pay_method_field = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[2]/div[1]")
add_card_button = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]")
card_number_field = (By.ID, "number")
card_number_code_field = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/form/div[1]/div[2]/div[2]/div[2]/input")
card_code_add_button = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]/form/div[3]/button[1]")
close_button_pay_method = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/button")
comment_driver_field = (By.ID, "comment")
scroll_space = (By.XPATH, "//*[@id='root']/div/div[3]")
slider_round_element = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span")
ice_cream_element = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]")
ask_taxi_button = (By.XPATH, "//*[@id='root']/div/div[3]/div[4]/button")
ice_cream_count = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[2]")

confirmation_assert_cellphone_number = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[1]/div")
add_card_field_text = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]/div")
image_bender = (By.XPATH, "//*[@id='root']/div/div[5]/div[2]/div[2]/div[1]/div[1]/div[1]/img")

# Cómo crear xpath -> ?
order_rating = (By.CLASS_NAME, "order-btn-rating")
order_name = (By.XPATH, "//div[@class='order-btn-group'][1]/div[2]")
order_image = (By.XPATH, "//div[@class='order-button']//img")
order_modal = (By.CLASS_NAME, "order-header-title")

#Propiedades: localizadores o atributos de clase o atributos hacen refencia a las características
#Método usando localizador usando t.ext -> generalmente para textos que están implicitos en el diseño, es decir que no se mueven
#Pero para textos o valores que sean variables, o que el usuario los ingrese o los pueda modificar, se usa el get_property('value')

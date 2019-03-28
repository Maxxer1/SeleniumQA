def set_fields(driver, date, parent_approval=False, doctor_approval=False, name="John", surname="Jhonson"):
    name_field = driver.find_element_by_id("inputEmail3")
    name_field.send_keys(name)
    surname_field = driver.find_element_by_id("inputPassword3")
    surname_field.send_keys(surname)
    date_field = driver.find_element_by_id("dataU")
    date_field.send_keys(date)
    parent_approval_field = driver.find_element_by_id("rodzice")
    if parent_approval is True:
        parent_approval.click()
    doctor_approval_field = driver.find_element_by_id("lekarz")
    if doctor_approval is True:
        doctor_approval_field.click()
    submit_button = driver.find_element_by_css_selector(
        "#formma > div:nth-child(6) > div > button")
    submit_button.click()


def close_alerts(driver, self):
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()
    alert = driver.switch_to.alert
    alert.accept()

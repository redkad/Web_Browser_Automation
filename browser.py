from selenium import webdriver
import time


browser = webdriver.Chrome()

browser.maximize_window()
browser.get('https://docs.google.com/forms/d/1_XyTRmCotkVFmU_V83Mma9uGUMY460CDFEe64-QgYM0/edit')
browser.implicitly_wait(30)

elem = browser.find_element_by_css_selector('.isUndragged > span:nth-child(3) > span:nth-child(1)')
time.sleep(2)
elem.click()
elems = browser.find_element_by_css_selector('#identifierId' or '#Email')
elems.send_keys('example@gmail.com')

next = browser.find_element_by_css_selector('.RveJvd')
next.click()
time.sleep(1)
browser.implicitly_wait(20)
password = browser.find_element_by_css_selector(
    "#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input" or '//*[@id="password"]')
time.sleep(1)
password.send_keys('my_password')

next2 = browser.find_element_by_css_selector('#passwordNext > span:nth-child(3) > span:nth-child(1)')
next2.click()
time.sleep(2)
full_name = browser.find_element_by_css_selector(
    'div.freebirdFormviewerViewNumberedItemContainer:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)')
full_name.send_keys('Collins Mawutor Tenge')

browser.implicitly_wait(10)
time.sleep(1)
for i in range(0, 2):
    gender = browser.find_element_by_css_selector(
        '#mG61Hd > div > div > div.freebirdFormviewerViewItemList > div:nth-child(2) > div > div:nth-child(2) > div > span > div > div:nth-child(1) > label > div > div.appsMaterialWizToggleRadiogroupElContainer.exportContainerEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div')
    browser.implicitly_wait(10)
    time.sleep(2)
    gender.click()
browser.implicitly_wait(10)
time.sleep(1)
browser.execute_script("window.scrollTo(0, window.scrollY + 350)")
browser.implicitly_wait(10)

time.sleep(2)
form_email = browser.find_element_by_css_selector(
    '#mG61Hd > div > div > div.freebirdFormviewerViewItemList > div:nth-child(3) > div > div.freebirdFormviewerViewItemsTextItemWrapper > div > div.quantumWizTextinputPaperinputMainContent.exportContent > div > div.quantumWizTextinputPaperinputInputArea > input')
form_email.send_keys('example@gmail.com')
browser.implicitly_wait(10)
time.sleep(2)
next_button = browser.find_element_by_css_selector(
    '#mG61Hd > div > div > div.freebirdFormviewerViewNavigationNavControls > div.freebirdFormviewerViewNavigationButtonsAndProgress > div')
next_button.click()

browser.implicitly_wait(10)
time.sleep(2)
school = browser.find_element_by_css_selector(
    '#mG61Hd > div > div > div.freebirdFormviewerViewItemList > div:nth-child(2) > div > div.freebirdFormviewerViewItemsTextItemWrapper > div > div.quantumWizTextinputPaperinputMainContent.exportContent > div > div.quantumWizTextinputPaperinputInputArea > input')
school.send_keys('Ho Technical University')
browser.execute_script("window.scrollTo(0, window.scrollY + 150)")
browser.implicitly_wait(10)
time.sleep(2)
address = browser.find_element_by_css_selector(
    '#mG61Hd > div > div > div.freebirdFormviewerViewItemList > div:nth-child(3) > div > div.quantumWizTextinputPapertextareaEl.modeLight.freebirdFormviewerViewItemsTextLongText.freebirdThemedInput > div.quantumWizTextinputPapertextareaMainContent.exportContent > div.quantumWizTextinputPapertextareaContentArea.exportContentArea > textarea')
address.send_keys('My_Address')

browser.execute_script("window.scrollTo(0, window.scrollY + 150)")
browser.implicitly_wait(10)
time.sleep(2)
phone = browser.find_element_by_css_selector(
    '#mG61Hd > div > div > div.freebirdFormviewerViewItemList > div:nth-child(4) > div > div.freebirdFormviewerViewItemsTextItemWrapper > div > div.quantumWizTextinputPaperinputMainContent.exportContent > div > div.quantumWizTextinputPaperinputInputArea > input')
phone.send_keys('0248134300')
browser.execute_script("window.scrollTo(0, window.scrollY + 150)")
browser.implicitly_wait(10)
time.sleep(2)

comments = browser.find_element_by_css_selector(
    '#mG61Hd > div > div > div.freebirdFormviewerViewItemList > div:nth-child(5) > div > div.quantumWizTextinputPapertextareaEl.modeLight.freebirdFormviewerViewItemsTextLongText.freebirdThemedInput > div.quantumWizTextinputPapertextareaMainContent.exportContent > div.quantumWizTextinputPapertextareaContentArea.exportContentArea > textarea')
comments.send_keys('I will be very grateful to be selected to do my National Service at Stanbic Bank. ')
browser.implicitly_wait(10)
time.sleep(2)

# submit = browser.find_element_by_css_selector('#mG61Hd > div > div > div.freebirdFormviewerViewNavigationNavControls > div.freebirdFormviewerViewNavigationButtonsAndProgress > div > div.appsMaterialWizButtonEl.appsMaterialWizButtonPaperbuttonEl.appsMaterialWizButtonPaperbuttonFilled.freebirdFormviewerViewNavigationSubmitButton.freebirdThemedFilledButtonM2 > span')
# submit.click()
browser.implicitly_wait(10)
time.sleep(2)
browser.quit()

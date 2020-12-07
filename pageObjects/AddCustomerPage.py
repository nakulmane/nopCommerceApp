import time
from selenium.webdriver.support.ui import Select


class AddCustomer:
    # Add customer page
    lnk_Customers_menu_text = 'Customers'
    lnk_Customers_submenu_xpath = '/html/body/div[3]/div[2]/div/ul/li[4]/ul/li[1]/a/i'
    btn_add_new_xpath = '/html/body/div[3]/div[3]/div/form[1]/div[1]/div/a'
    txt_email_id = 'Email'
    txt_password_id = 'Password'
    txt_firstname_id = 'FirstName'
    txt_lastname_id = 'LastName'
    rd_genderMale_id = 'Gender_Male'
    rd_genderFemale_id = 'Gender_Female'
    txt_dob_id = 'DateOfBirth'
    txt_companyname_id = 'Company'
    txt_companyPhone_id = 'customer_attribute_1'
    chk_tax_id = 'IsTaxExempt'
    txt_customerRoll_xpath = '//*[@id="customer-info"]/div[2]/div[1]/div[10]/div[2]/div/div[1]/div'
    lstItem_admin_xpath = '//*[@id="SelectedCustomerRoleIds"]/option[1]'
    lstItem_forum_xpath = '//*[@id="SelectedCustomerRoleIds"]/option[2]'
    lstItem_guests_xpath = '//*[@id="SelectedCustomerRoleIds"]/option[3]'
    lstItem_reg_xpath = '//*[@id="SelectedCustomerRoleIds_listbox"]/li[4]'
    lstItem_vendor_xpath = '//*[@id="SelectedCustomerRoleIds"]/option[5]'
    lstItem_warehouse_xpath = '//*[@id="SelectedCustomerRoleIds_taglist"]/li/span[1]'
    drp_mngOfVendor_id = 'VendorId'
    lstItem_vendor1_xpath = '//*[@id="VendorId"]/option[2]'
    lstItem_vendor2_xpath = '//*[@id="VendorId"]/option[3]'
    txt_admin_comment_id = 'AdminComment'
    btn_save_xpath = '/html/body/div[3]/div[3]/div/form/div[1]/div/button[1]'

    def __init__(self, driver):
        self.driver = driver

    def clickCustomerMenu(self):
        self.driver.find_element_by_link_text(self.lnk_Customers_menu_text).click()

    def clickCustomerSubmenu(self):
        self.driver.find_element_by_xpath(self.lnk_Customers_submenu_xpath).click()

    def clickAddNew(self):
        self.driver.find_element_by_xpath(self.btn_add_new_xpath).click()

    def enterEmail(self, email):
        self.driver.find_element_by_id(self.txt_email_id).send_keys(email)

    def enterPassword(self, password):
        self.driver.find_element_by_id(self.txt_password_id).send_keys(password)

    def enterFirstname(self, firstname):
        self.driver.find_element_by_id(self.txt_firstname_id).send_keys(firstname)

    def enterLastname(self, lastname):
        self.driver.find_element_by_id(self.txt_lastname_id).send_keys(lastname)

    def selectGender(self, gender):
        if gender == 'male':
            self.driver.find_element_by_id(self.rd_genderMale_id).click()
        elif gender == 'female':
            self.driver.find_element_by_id(self.rd_genderFemale_id).click()
        else:
            self.driver.find_element_by_id(self.rd_genderFemale_id).click()

    def enterDOB(self, dob):
        self.driver.find_element_by_id(self.txt_dob_id).send_keys(dob)

    def enterCompany(self, company):
        self.driver.find_element_by_id(self.txt_companyname_id).send_keys(company)

    def enterCompanyPhone(self, phone):
        self.driver.find_element_by_id(self.txt_companyPhone_id).send_keys(phone)

    def enterCustomerRole(self, role):
        self.driver.find_element_by_xpath('//*[@id="SelectedCustomerRoleIds_taglist"]/li/span[2]').click()
        time.sleep(2)
        if role == 'registered':
            self.driver.find_element_by_xpath(self.txt_customerRoll_xpath).click()
            time.sleep(3)
            self.driver.find_element_by_xpath(self.lstItem_reg_xpath).click()
        elif role == 'administrators':
            self.driver.find_element_by_xpath(self.txt_customerRoll_xpath).click()
            time.sleep(3)
            self.driver.find_element_by_xpath(self.lstItem_admin_xpath).click()
        elif role == 'forum moderators':
            self.driver.find_element_by_xpath(self.txt_customerRoll_xpath).click()
            time.sleep(3)
            self.driver.find_element_by_xpath(self.lstItem_forum_xpath).click()
        elif role == 'guests':
            self.driver.find_element_by_xpath(self.txt_customerRoll_xpath).click()
            time.sleep(3)
            self.driver.find_element_by_xpath('//*[@id="SelectedCustomerRoleIds_listbox"]/li[3]').click()
        elif role == 'vendors':
            self.driver.find_element_by_xpath(self.txt_customerRoll_xpath).click()
            time.sleep(3)
            self.driver.find_element_by_xpath(self.lstItem_vendor_xpath).click()

        time.sleep(3)

    def setManagerOfVendor(self, value):
        drp = self.driver.find_element_by_id(self.drp_mngOfVendor_id)
        d = Select(drp)
        d.select_by_visible_text(value)

    def setAdminContent(self, content):
        self.driver.find_element_by_id(self.txt_admin_comment_id).send_keys(content)

    def clickSave(self):
        self.driver.find_element_by_xpath(self.btn_save_xpath).click()

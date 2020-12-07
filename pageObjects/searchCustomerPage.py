class SearchCustomer:
    txt_email_id = 'SearchEmail'
    txt_firstname_id = 'SearchFirstName'
    txt_lastname_id = 'SearchLastName'

    btn_search_id = 'search-customers'

    tableSearchResults_xpath = '//*[@id="customers-grid"]'
    table_xpath = '//*[@id="customers-grid"]/tbody'
    table_rows_xpath = '// *[ @ id = "customers-grid"] / thead / tr'
    tr = '//*[@id="customers-grid"]/tbody/tr[1]'
    table_col_xpath = '//*[@id="customers-grid_wrapper"]/div[2]'

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element_by_id(self.txt_email_id).clear()
        self.driver.find_element_by_id(self.txt_email_id).send_keys(email)

    def setFirstname(self, fname):
        self.driver.find_element_by_id(self.txt_firstname_id).clear()
        self.driver.find_element_by_id(self.txt_firstname_id).send_keys(fname)

    def setLastname(self, lname):
        self.driver.find_element_by_id(self.txt_lastname_id).clear()
        self.driver.find_element_by_id(self.txt_lastname_id).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element_by_id(self.btn_search_id).click()

    def getNoOfRows(self):
        table_elem = self.driver.find_element_by_xpath(self.table_xpath)
        row_elem = table_elem.find_elements_by_tag_name('tr')
        return len(row_elem)

    def searchCustomerByEmail(self, Email):
        flag = False
        table_elem = self.driver.find_element_by_xpath(self.table_xpath)
        for r in range(1, self.getNoOfRows()+1):
            table_elem = self.driver.find_element_by_xpath(self.table_xpath)
            email = table_elem.find_element_by_xpath('//*[@id="customers-grid"]/tbody/tr['+str(r)+']/td[2]').text
            if email == Email:
                flag = True
                break

        return flag

    def searchCustomerByName(self, Name):
        flag = False
        table_elem = self.driver.find_element_by_xpath(self.table_xpath)
        for r in range(1, self.getNoOfRows()+1):
            table_elem = self.driver.find_element_by_xpath(self.table_xpath)
            name = table_elem.find_element_by_xpath('//*[@id="customers-grid"]/tbody/tr['+str(r)+']/td[3]').text
            if name == Name:
                flag = True
                break

        return flag

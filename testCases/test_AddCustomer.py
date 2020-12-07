import pytest
import time

from pageObjects.LoginPage import login
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen
import string
import random


class Test_003_addCustomer:
    baseUrl = ReadConfig.getAppUrl()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = logGen.generateLogs()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("****************** Test_003_AddCustomer ***********************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp = login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****************Login successful*******************")

        self.logger.info("************** Starting Add Customer Test **************")

        self.addCus = AddCustomer(self.driver)
        self.addCus.clickCustomerMenu()
        self.addCus.clickCustomerSubmenu()

        self.addCus.clickAddNew()

        self.logger.info("*************** Providing customer info ******************")

        self.email = random_generator() + '@gmail.com'
        self.addCus.enterEmail(self.email)
        self.addCus.enterPassword('test123')
        self.addCus.enterCustomerRole('guests')
        self.addCus.setManagerOfVendor('Vendor 2')
        self.addCus.selectGender('male')
        self.addCus.enterFirstname('Nakul')
        self.addCus.enterLastname('Mane')
        self.addCus.enterDOB('02/26/1993')      # MM/DD/YYYY
        self.addCus.enterCompany('busyQA')
        self.addCus.setAdminContent('This is for testing............')
        # self.addCus.enterCompanyPhone('915656565656')
        self.addCus.clickSave()

        self.logger.info("************** Saving customer info ****************")

        self.logger.info(" ******************* Add Customer Validation started **************")

        self.msg = self.driver.find_element_by_tag_name('body').text

        print(self.msg)
        if "The new customer has been added successfully." in self.msg:
            assert True == True
            self.logger.info("********** Add customer test passed ***********")
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_addCust_scr.png")     # screenshot
            self.logger.error("************** Add customer test failed ***********")
            assert True == False

        self.driver.close()
        self.logger.info("*********************** Ending Test_003_AddCustomer *********************")


def random_generator(size=8, char=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(char) for x in range(size))

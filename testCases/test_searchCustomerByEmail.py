import time
import pytest

from pageObjects.LoginPage import login
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.searchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen


class Test_searchCustomerByEmail:
    baseUrl = ReadConfig.getAppUrl()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = logGen.generateLogs()

    @pytest.mark.regression
    def test_searchCustomerByEmail_004(self, setup):
        self.logger.info("************* search customer by email test 004 *************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp = login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************** Login successful *******************")

        self.logger.info("**************** Starting test searchCustomerByEmail **************")

        self.addCust = AddCustomer(self.driver)
        self.addCust.clickCustomerMenu()
        self.addCust.clickCustomerSubmenu()

        self.logger.info("*********** Searching customer by email *****************")

        searchCust = SearchCustomer(self.driver)
        searchCust.setEmail('victoria_victoria@nopCommerce.com')
        searchCust.clickSearch()
        time.sleep(5)
        status = searchCust.searchCustomerByEmail('victoria_victoria@nopCommerce.com')
        assert True == status

        self.logger.info("************** TC_searchCustomerByEmail_004 is finished **************")
        self.driver.close()

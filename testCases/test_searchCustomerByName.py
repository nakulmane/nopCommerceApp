import time
import pytest

from pageObjects.LoginPage import login
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.searchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen


class Test_searchCustomerByName_005:
    baseUrl = ReadConfig.getAppUrl()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = logGen.generateLogs()

    @pytest.mark.regression
    def test_searchCustomerByName(self, setup):
        self.logger.info("************* search customer by name test 005 *************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp = login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************** Login successful *******************")

        self.logger.info("**************** Starting test searchCustomerByName **************")

        self.addCust = AddCustomer(self.driver)
        self.addCust.clickCustomerMenu()
        self.addCust.clickCustomerSubmenu()

        self.logger.info("*********** Searching customer by Name *****************")

        searchCust = SearchCustomer(self.driver)
        searchCust.setFirstname('Victoria')
        searchCust.setLastname('Terces')
        searchCust.clickSearch()
        time.sleep(5)
        status = searchCust.searchCustomerByName('Victoria Terces')
        assert True == status

        self.logger.info("************** TC_searchCustomerByName_005 is finished **************")
        self.driver.close()

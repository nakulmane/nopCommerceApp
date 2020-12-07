import pytest
from selenium import webdriver
from pageObjects.LoginPage import login
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen
from utilities import XLUtils
import time


class Test_002_DDT_login:
    baseUrl = ReadConfig.getAppUrl()
    path = './/testData//loginData.xlsx'
    logger = logGen.generateLogs()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info('************ Test_002_DDT_login *************')
        self.logger.info('************ Verifying login DDT test *************')
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = login(self.driver)

        self.rows = XLUtils.getRowCount(self.path, "Sheet1")
        print('No of rows in sheet are: ', self.rows)

        lst_status = []
        for r in range(2, self.rows+1):
            self.user = XLUtils.readData(self.path, "Sheet1", r, 1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUtils.readData(self.path, "Sheet1", r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == 'pass':
                    self.logger.info("***** Passed ********")
                    self.lp.clickLogout()
                    lst_status.append('Pass')
                elif self.exp == 'fail':
                    self.logger.info("******* Failed ******")
                    self.lp.clickLogout()
                    lst_status.append('Fail')

            elif act_title != exp_title:
                if self.exp == 'pass':
                    self.logger.info("***** Failed ********")
                    lst_status.append('Fail')
                elif self.exp == 'fail':
                    self.logger.info("******* Passed ******")
                    lst_status.append('Pass')

        if 'Fail' not in lst_status:
            self.logger.info("******* Login DDT test passed *******")
            self.driver.close()
            assert True
        else:
            self.logger.info("******* Login DDT test failed *******")
            self.driver.close()
            assert False

        self.logger.info('******* End of DDT login test *******')
        self.logger.info('******* Completed TC_LoginDDT_002 ******')

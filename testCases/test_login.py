import pytest
from selenium import webdriver
from pageObjects.LoginPage import login
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen


class Test_001_login:
    baseUrl = ReadConfig.getAppUrl()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = logGen.generateLogs()

    @pytest.mark.regression
    def test_homepageTitle(self, setup):
        self.logger.info('************ Started Test_001_login *************')
        self.logger.info('************ Verifying home page title *************')
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        if act_title == 'Your store. Login':
            self.logger.info('************ Home page title test is passed *************')
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot('.\\screenshots\\' + 'test_homepageTitle.png')
            self.logger.error('************ Home page title test failed *************')
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info('************ Verifying login *************')
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == 'Dashboard / nopCommerce administration':
            self.logger.info('************ Login test passed *************')
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot('.\\screenshots\\' + 'test_login.png')
            self.logger.error('************ Login test failed *************')
            self.driver.close()
            assert False

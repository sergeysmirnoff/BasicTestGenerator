import argparse


# command lines arguments:  generated_script.py basic_login \"https://profile.w3schools.com/\"
def generate_pytest_script(filename, map_file, url_to_test):
    with open(filename, 'w') as f:
        f.write(f"from interactions.selenium_driver import SeleniumDriver\n")
        f.write(f"from selenium import webdriver\n")
        f.write(f"from selenium.webdriver.chrome.service import Service\n")
        f.write(f"from utilities.custom_logger import CustomLogger\n")
        f.write(f"from utilities.verify import Verify\n")
        f.write(f"from {map_file} import Basic_login\n")

        f.write(f"\n\nclass TestBasicLogin:\n")
        f.write(f"\tdriver = None\n")
        f.write(f"\tlogin = None\n")
        f.write(f"\tsd = None\n")
        f.write(f"\tverify = None\n")
        f.write(f"\tusername = 'gocelax227@loongwin.com'\n")
        f.write(f"\tc_password = 'hackaTon2023!'\n")
        f.write(f"\ti_password = c_password + '$'\n")

        f.write(f"\n\t@classmethod\n")
        f.write(f"\tdef setup_class(cls):\n")
        f.write(f"\t\tservice = Service(executable_path='C://Users//swuser//PycharmProjects//TemplateProject9//chromedriver.exe')\n")
        f.write(f"\t\tcls.driver = webdriver.Chrome(service=service)\n")
        f.write(f"\t\tcls.logger = CustomLogger('template test', 'logs')\n")
        f.write(f"\t\tcls.sd = SeleniumDriver(driver=cls.driver, logger=cls.logger)\n")
        f.write(f"\t\tcls.driver.get({url_to_test})\n")
        f.write(f"\t\tcls.login = Basic_login(cls.sd)\n")
        f.write(f"\t\tcls.verify = Verify(cls.sd)\n")
        f.write(f"\t\tcls.logger.debug('setup')\n")

        f.write(f"\n\tdef test1(self):\n")
        f.write(f"\t\t# incorrect credentials check\n")
        f.write(f"\t\tself.sd.clear_input_field(element=self.login.email_text())\n")
        f.write(f"\t\tself.sd.send_keys(element=self.login.email_text(), data=self.username)\n")
        f.write(f"\t\tself.sd.clear_input_field(element=self.login.current_password_password())\n")
        f.write(f"\t\tself.sd.send_keys(element=self.login.current_password_password(), data=self.i_password)\n")
        f.write(f"\t\tself.sd.element_click(element=self.login.login_btn())\n")
        f.write(f"\t\tself.sd.wait(10)\n")
        f.write(f"\t\tself.verify.verify_values_match(expected='https://profile.w3schools.com/', actual=self.sd.get_current_url())\n")

        f.write(f"\n\tdef test2(self):\n")
        f.write(f"\t\t# correct credential check\n")
        f.write(f"\t\tself.sd.clear_input_field(element=self.login.email_text())\n")
        f.write(f"\t\tself.sd.send_keys(element=self.login.email_text(), data=self.username)\n")
        f.write(f"\t\tself.sd.clear_input_field(element=self.login.current_password_password())\n")
        f.write(f"\t\tself.sd.send_keys(element=self.login.current_password_password(), data=self.c_password)\n")
        f.write(f"\t\tself.sd.element_click(element=self.login.login_btn())\n")
        f.write(f"\t\tself.sd.wait(10)\n")
        f.write(f"\t\tself.verify.verify_values_match(expected='https://my-learning.w3schools.com/', actual=self.sd.get_current_url())\n")

        f.write(f"\n\t@classmethod\n")
        f.write(f"\tdef teardown_class(cls):\n")
        f.write(f"\t\tcls.sd.close_browser()\n")
        f.write(f"\t\tcls.logger.debug('teardown')\n")

        f.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate a pytest script.')
    parser.add_argument('filename', type=str, help='The name of the pytest script to generate.')
    parser.add_argument('map_file', type=str, help='The name of the map file to use.')
    parser.add_argument('url_to_test', type=str, help='The url of the website to test.')
    args = parser.parse_args()

    generate_pytest_script(args.filename, args.map_file, args.url_to_test)
import argparse


# command lines arguments:  generated_script.py basic_map \"https://www.w3schools.com/\"
def generate_pytest_script(filename, map_file, url_to_test):
    with open(filename, 'w') as f:
        f.write(f"import time\n")
        f.write(f"import pytest\n")
        f.write(f"from selenium import webdriver\n")
        f.write(f"from selenium.webdriver.common.keys import Keys\n")
        f.write(f"from {map_file} import Basic_map\n")

        f.write(f"\n\nclass TestBasic:\n")
        f.write(f"\t@classmethod\n")
        f.write(f"\tdef setup_class(cls):\n")
        f.write(f"\t\tcls.driver = webdriver.Chrome()\n")
        f.write(f"\t\tcls.url = {url_to_test}\n")
        f.write(f"\t\tcls.basic_map = Basic_map(cls.driver)\n")

        f.write(f"\n\t@pytest.fixture(autouse=True)\n")
        f.write(f"\tdef run_around_tests(self):\n")
        f.write(f"\t\tself.driver.get(self.url)\n")

        f.write(f"\n\t@staticmethod\n")
        f.write(f"\tdef get_function(*args):\n")
        f.write(f"\t\tfunctions_names_lst = dir(Basic_map)\n")
        f.write(f"\t\tfor func_name in functions_names_lst:\n")
        f.write(f"\t\t\tif all([arg in func_name for arg in args]):\n")
        f.write(f"\t\t\t\treturn getattr(Basic_map, func_name)\n")

        f.write(f"\n\tdef test1(self):\n")
        f.write(f"\t\tsearch_func = self.get_function('text', 'search')\n")
        f.write(f"\t\tsearch_element = search_func(self.basic_map)\n")
        f.write(f"\t\tsearch_element.send_keys('Python')\n")
        f.write(f"\t\tsearch_element.send_keys(Keys.RETURN)\n")
        f.write(f"\t\ttime.sleep(2)\n")
        f.write(f"\t\tassert 'Python' in self.driver.title\n")

        f.write(f"\n\tdef test2(self):\n")
        f.write(f"\t\tsearch_func = self.get_function('text', 'search')\n")
        f.write(f"\t\tsearch_element = search_func(self.basic_map)\n")
        f.write(f"\t\tsearch_element.send_keys('HTML')\n")
        f.write(f"\t\tbutton_func = self.get_function('button', 'search')\n")
        f.write(f"\t\tbutton_element = button_func(self.basic_map)\n")
        f.write(f"\t\tbutton_element.click()\n")
        f.write(f"\t\ttime.sleep(2)\n")
        f.write(f"\t\tassert 'HTML' in self.driver.title\n")

        f.write(f"\n\tdef test3(self):\n")
        f.write(f"\t\ta_func = self.get_function('_a')\n")
        f.write(f"\t\ta_element = a_func(self.basic_map)\n")
        f.write(f"\t\tassert a_element.is_displayed()\n")

        f.write(f"\n\tdef test4(self):\n")
        f.write(f"\t\ta_func = self.get_function('_a')\n")
        f.write(f"\t\ta_element = a_func(self.basic_map)\n")
        f.write(f"\t\tassert a_element.is_enabled()\n")

        f.write(f"\n\t@pytest.mark.parametrize('input_email, input_password, title', [\n")
        f.write(f"\t\t('aaa.bbb', 'aaa.bbb', 'Log in'),\n")
        f.write(f"\t\t('gocelax227@loongwin.com', 'hackaTon2023!', 'My learning')\n")
        f.write(f"\t])\n")
        f.write(f"\tdef test5(self, input_email, input_password, title):\n")
        f.write(f"\t\tself.go_to_login()\n")
        f.write(f"\t\temail_func = self.get_function('id', 'email')\n")
        f.write(f"\t\temail_element = email_func(self.basic_map)\n")
        f.write(f"\t\temail_element.send_keys(input_email)\n")
        f.write(f"\t\tpassword_func = self.get_function('password', 'id')\n")
        f.write(f"\t\tpassword_element = password_func(self.basic_map)\n")
        f.write(f"\t\tpassword_element.send_keys(input_password)\n")
        f.write(f"\t\tlogin_btn_func = self.get_function('login', 'button')\n")
        f.write(f"\t\tlogin_btn_element = login_btn_func(self.basic_map)\n")
        f.write(f"\t\tlogin_btn_element.click()\n")
        f.write(f"\t\ttime.sleep(5)\n")
        f.write(f"\t\tassert title in self.driver.title\n")

        f.write(f"\n\tdef go_to_login(self):\n")
        f.write(f"\t\tlogin_func = self.get_function('login', 'action')\n")
        f.write(f"\t\tlogin_element = login_func(self.basic_map)\n")
        f.write(f"\t\tlogin_element.click()\n")
        f.write(f"\t\ttime.sleep(5)\n")

        f.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate a pytest script.')
    parser.add_argument('filename', type=str, help='The name of the pytest script to generate.')
    parser.add_argument('map_file', type=str, help='The name of the map file to use.')
    parser.add_argument('url_to_test', type=str, help='The url of the website to test.')
    args = parser.parse_args()

    generate_pytest_script(args.filename, args.map_file, args.url_to_test)
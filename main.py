import argparse


# command lines arguments:  generated_script.py map_creator \"https://www.w3schools.com/\" \"id\"
def generate_pytest_script(filename, map_file, url_to_map, identifier_to_map):
    with open(filename, 'w') as f:
        f.write(f'# map_file: {map_file}\n\n\n')
        f.write(f"import time\n")
        f.write(f"import pytest\n")
        f.write(f"from selenium import webdriver\n")
        f.write(f"from selenium.webdriver.common.keys import Keys\n")
        f.write(f"from {map_file} import search_and_create\n")

        f.write(f"\n\nclass TestBasic:\n")
        f.write(f"\t@classmethod\n")
        f.write(f"\tdef setup_class(cls):\n")
        f.write(f"\t\tcls.driver = webdriver.Chrome()\n")
        f.write(f"\t\tcls.url = {url_to_map}\n")
        f.write(f"\t\tsearch_and_create(cls.url, {identifier_to_map}, 'basic_map', 'w')\n")
        f.write(f"\t\tcls.map_file_name = 'basic_map'\n")
        f.write(f"\t\tfrom basic_map import Basic_map\n")
        f.write(f"\t\tcls.basic_map = Basic_map(cls.driver)\n")

        f.write(f"\n\t@pytest.fixture(autouse=True)\n")
        f.write(f"\tdef run_around_tests(self):\n")
        f.write(f"\t\tself.driver.get(self.url)\n")

        f.write(f"\n\t@staticmethod\n")
        f.write(f"\tdef get_function(type_of_element):\n")
        f.write(f"\t\tfrom basic_map import Basic_map\n")
        f.write(f"\t\tlst_a = dir(Basic_map)\n")
        f.write(f"\t\tfor func_name in lst_a:\n")
        f.write(f"\t\t\tif type_of_element in func_name:\n")
        f.write(f"\t\t\t\treturn getattr(Basic_map, func_name)\n")

        f.write(f"\n\tdef test1(self):\n")
        f.write(f"\t\tsearch_func = self.get_function('text')\n")
        f.write(f"\t\tsearch_element = search_func(self.basic_map)\n")
        f.write(f"\t\tsearch_element.send_keys('Python')\n")
        f.write(f"\t\tsearch_element.send_keys(Keys.RETURN)\n")
        f.write(f"\t\ttime.sleep(2)\n")
        f.write(f"\t\tassert 'Python' in self.driver.title\n")

        f.write(f"\n\tdef test2(self):\n")
        f.write(f"\t\tsearch_func = self.get_function('text')\n")
        f.write(f"\t\tsearch_element = search_func(self.basic_map)\n")
        f.write(f"\t\tsearch_element.send_keys('HTML')\n")
        f.write(f"\t\tbutton_func = self.get_function('button')\n")
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

        f.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate a pytest script.')
    parser.add_argument('filename', type=str, help='The name of the pytest script to generate.')
    parser.add_argument('map_creator_file', type=str, help='The name of the mapper file to use.')
    parser.add_argument('url_to_map', type=str, help='The url of the website to map.')
    parser.add_argument('identifier_to_map', type=str, help='The identifier to map by.')
    args = parser.parse_args()

    generate_pytest_script(args.filename, args.map_creator_file, args.url_to_map, args.identifier_to_map)
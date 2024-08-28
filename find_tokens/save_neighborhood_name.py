from selenium import webdriver
from selenium.webdriver.common.by import By
from mongo_util import get_all_tokens,add_field_to_record_by_token
import time

# Set up the Selenium WebDriver (you can choose Chrome, Firefox, etc.)
driver = webdriver.Chrome()  # Ensure you have the appropriate WebDriver installed


def __find_neighborhood_by_selenium(token):
    url = "https://divar.ir/v/" + token
    driver.get(url)

    # Wait for the page to load (adjust the time as needed)
    time.sleep(2)

    try:
        # Locate the element containing the neighborhood name
        description_element = driver.find_element(By.CLASS_NAME, "kt-page-title__subtitle--responsive-sized")
        description = description_element.text
        neighborhood_name = description.split('،')[1]
        return neighborhood_name
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def main():
    tokens = get_all_tokens()

    for token in tokens:
        try:
            neighborhood_name = __find_neighborhood_by_selenium(token)
            if neighborhood_name:
                add_field_to_record_by_token("neighborhood",neighborhood_name,token)
            else:
                print("============================")
                print(token)
                print("Neighborhood name not found, the element might not be present on the page.")
        except Exception as e:
            print("============================")
            print(token)
            print(f"An error occurred: {e}")
            continue


if __name__ == "__main__":
    main()



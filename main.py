from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # webdriver-manager
import time
from seleniumwire import webdriver

service = Service(executable_path=ChromeDriverManager().install())

options = Options()
options.add_argument("--window-size=1920,1200")
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
driver = webdriver.Chrome(service=service, options=options)

# driver.scopes = []
driver.get('https://limakid.com/modelito/lk/921824')

driver.find_element(By.XPATH, '//a[@href="https://limakid.com/votar/"]').click()
# wait = WebDriverWait(driver, 15)
# wait.until(driver.get_screenshot_as_file(os.getcwd() + '/images/' + str(datetime.datetime.now()) + '.png'))

driver.close()
driver.quit()

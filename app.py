import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# Load environment variables
load_dotenv()
# GET ENV VAR VALUES
HJSESSIONUSER = os.getenv('HJSESSIONUSER')
WELLFOUND = os.getenv('WELLFOUND')
AJSUSERID = os.getenv('AJSUSERID')
AJSANONYMOUSID = os.getenv('AJSANONYMOUSID')
DATADOME = os.getenv('DATADOME')
EXPIRY = int(os.getenv('EXPIRY'))

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')

# Wellfound credentials


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    # Message from the user
    message = request.form.get('message')
    if not message:
        return jsonify({"status": "error", "message": "Message is required!"})
    print(message)
    # Thread URL
    thread_url = os.getenv('THREAD_URL')


    try:
        # Setup WebDriver
        print("Launching WebDriver...")
        driver = webdriver.Chrome(service=Service("chromedriver.exe"))

        print("Opening Wellfound...")
        driver.get("https://wellfound.com")
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        time.sleep(2)
        print('Deleting existing cookies')
        driver.delete_all_cookies()
        print('Cookies deleted successfully')
        time.sleep(2)

        # Set cookies
        print("Adding cookies...")
        try:
            driver.add_cookie({
            "domain": ".wellfound.com",
            "name": "_hjSessionUser_1444722",
            "value": HJSESSIONUSER,
            "path": "/",
            "secure": True,
            "httpOnly": False,
            "expiry": EXPIRY
            })
            print('one cookie added')
            time.sleep(2)

            driver.add_cookie({
            "domain": "wellfound.com",
            "name": "_wellfound",
            "value": WELLFOUND,
            "path": "/",
            "secure": True,
            "httpOnly": True,
            "expiry": EXPIRY
            })
            print('second cookie added')
            time.sleep(2)

            driver.add_cookie({
            "domain": ".wellfound.com",
            "name": "ajs_user_id",
            "value": AJSUSERID,
            "path": "/",
            "secure": True,
            "httpOnly": False,
            "expiry": EXPIRY
            })
            print('third cookie added')
            time.sleep(2)

            driver.add_cookie({
            "domain": ".wellfound.com",
            "name": "ajs_anonymous_id",
            "value": AJSANONYMOUSID,
            "path": "/",
            "secure": True,
            "httpOnly": False,
            "expiry": EXPIRY
            })
            print('fourth cookie added')
            time.sleep(2)

            driver.add_cookie({
            "domain": ".wellfound.com",
            "name": "datadome",
            "value": DATADOME,
            "path": "/",
            "secure": True,
            "httpOnly": False,
            "expiry": EXPIRY
            })
            print('fifth cookie added')
            time.sleep(2)

        except Exception as e:
            print("Error adding cookies:", e)
        
        time.sleep(2)
    

        # Set session storage
        # print("Setting session storage...")
        # driver.execute_script(
        #     "window.sessionStorage.setItem('persist:hs-beacon-session-555ee66a-6ab0-4ff7-9c32-1089d7fbc687', session_storage_value)"
        # )

        print("Navigating to thread...")
        driver.get(thread_url)

        print("Locating textarea...")
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "form-input--body")))
        time.sleep(2)

        print("Locating textarea and sending message...")
        textarea = driver.find_element(By.ID, "form-input--body")
        textarea.send_keys(message)
        time.sleep(2)

        #delete element with class name css-vo3hmo
        print("Checking for element with class name css-vo3hmo...")

        # Check if element with class 'css-vo3hmo' exists
        element = driver.find_elements(By.CLASS_NAME, "css-vo3hmo")
        if element:
            print("Element found. Deleting...")
            driver.execute_script("document.querySelector('.css-vo3hmo').remove()")
        else:
            print("Element not found. Skipping deletion.")
        time.sleep(2)
        
        print("Locating submit button...")
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))

        time.sleep(2)
        print("Submitting message...")
        button = driver.find_element(By.XPATH, "//button[@type='submit']")
        button.click()


        return jsonify({"status": "success", "message": "Message sent successfully!"})

    except Exception as e:
        print("Error:", e)
        return jsonify({"status": "error", "message": str(e)})

      
if __name__ == '__main__':
    app.run(debug=True)
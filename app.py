import logging
from flask import Flask, render_template, request, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from urllib.parse import quote_plus

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

def setup_driver():
    print("Setting up Chrome driver")
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    return webdriver.Chrome(options=chrome_options)

def fetch_amazon_info(url):
    print(f"Fetching Amazon info for URL: {url}")
    driver = setup_driver()
    try:
        driver.get(url)
        wait = WebDriverWait(driver, 10)
        
        print("Fetching product name")
        product_name_element = wait.until(EC.presence_of_element_located((By.ID, 'productTitle')))
        product_name = product_name_element.text.strip()
        print(f"Product name: {product_name}")
        
        print("Fetching image URL")
        image_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#landingImage')))
        image_url = image_element.get_attribute('src')
        print(f"Image URL: {image_url}")
        
        print("Fetching price")
        try:
            price_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.a-price .a-offscreen')))
            price = price_element.get_attribute('innerHTML').strip()
        except:
            price = "Price not found"
        print(f"Price: {price}")
        
        return {
            'product_name': product_name,
            'image_url': image_url,
            'amazon_price': price
        }
    finally:
        driver.quit()

def send_product_ping(product_name, amazon_price, amazon_url):
    print("Sending product ping")
    xmtp_service_url = "http://localhost:3000/send-ping"
    walmart_url = f"https://www.walmart.com/search?q={quote_plus(product_name)}"
    data = {
        "productName": product_name,
        "price": amazon_price,
        "amazonUrl": amazon_url,
        "walmartUrl": walmart_url
    }
    try:
        response = requests.post(xmtp_service_url, json=data)
        if response.status_code == 200:
            print("Product ping sent successfully")
        else:
            print(f"Failed to send product ping: {response.text}")
    except Exception as e:
        print(f"Error sending product ping: {str(e)}")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print("POST request received")
        url = request.form['url']
        print(f"URL received: {url}")
        
        amazon_info = fetch_amazon_info(url)
        
        print(f"Product info: {amazon_info}")
        
        send_product_ping(amazon_info['product_name'], amazon_info['amazon_price'], url)
        
        return jsonify(amazon_info)
    print("GET request received, rendering index.html")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

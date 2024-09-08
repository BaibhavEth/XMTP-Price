# PriceAlert: Amazon Product Tracker with XMTP Integration

PriceAlert is a web application that allows users to track Amazon product prices and receive alerts via XMTP (Extensible Message Transport Protocol). This project was developed for [Hackathon Name].

## 🚀 Features

- Fetch and display Amazon product information
- Send price alerts via XMTP
- Compare prices with Walmart (link provided)
- User-friendly web interface

## 🛠️ Technologies Used

- Python 3.x
- Flask
- Selenium WebDriver
- Node.js
- Express
- XMTP.js
- Ethers.js

## 📋 Prerequisites

- Python 3.x
- Node.js and npm
- Chrome WebDriver

## 🔧 Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/pricealert.git
   cd pricealert
   ```

2. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Install Node.js dependencies:
   ```
   npm install
   ```

## 🚦 Usage

1. Start the Flask server:
   ```
   python app.py
   ```

2. In a new terminal, start the XMTP service:
   ```
   node xmtp_service.js
   ```

3. Open your web browser and navigate to `http://localhost:5000`

4. Enter an Amazon product URL and click "Fetch Product Info"

## 🧩 Project Structure

- `app.py`: Flask server for web interface and Amazon scraping
- `xmtp_service.js`: Node.js server for XMTP messaging
- `templates/index.html`: Web interface template

## 🔍 How It Works

1. User enters an Amazon product URL
2. Flask server scrapes product information
3. Product details are displayed on the web page
4. Information is sent to the XMTP service
5. XMTP service sends an initial message with product details
6. After 10 seconds, a follow-up message with a Walmart link is sent

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/yourusername/pricealert/issues).

## 📝 License

This project is [MIT](https://choosealicense.com/licenses/mit/) licensed.

## 👥 Authors

- [Your Name](https://github.com/yourusername)

## 🙏 Acknowledgements

- [XMTP](https://xmtp.org/) for the messaging protocol
- [Selenium](https://www.selenium.dev/) for web scraping capabilities
- [Flask](https://flask.palletsprojects.com/) for the web framework

---

Made with ❤️ for [Hackathon Name]

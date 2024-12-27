# AutoMessageBot

AutoMessageBot is a Python-based automation tool that interacts with the Wellfound platform. It automates the process of sending messages to a specific thread by simulating user actions in a browser using Selenium WebDriver.

## Features

- Automates the addition of cookies and session data.
- Navigates to the desired thread on Wellfound.
- Submits a message to the thread.
- Displays the result of the operation directly on the UI.
- Handles dynamic page elements and JavaScript-based interactions.

## Prerequisites

1. **Python**: Ensure Python 3.8+ is installed.
2. **Browser**: Install Google Chrome.
3. **WebDriver**: Download the corresponding version of [ChromeDriver](https://sites.google.com/chromium.org/driver/).
4. **Dependencies**: Install the required Python libraries using:

   ```bash
   pip install -r requirements.txt
   ```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/automessagebot.git
   cd automessagebot
   ```

2. Set up environment variables:

   - Create a `.env` file in the root directory.
   - Add the following keys:

     ```
     HJSESSIONUSER=""
     WELLLFOUND=""
     AJSUSERID=""
     AJSANONYMOUSID=""
     DATADOME=""
     EXPIRY=""
     THREAD_URL=""
    ```

3. Start the application:

   ```bash
   python app.py
   ```

## Usage

1. Open the web interface in your browser at `http://127.0.0.1:5000`.
2. Enter the message you wish to send in the provided form.
3. Click "Send Message" and wait for the result to display on the same screen.

## Code Highlights

- **Dynamic Element Handling**: Ensures elements are interacted with only when they are present.
- **Environment Variable Integration**: Secures sensitive data like cookies using `.env` files.
- **User Interface**: Provides a simple web interface for user input and result display.

## Technologies Used

- **Python**
- **Flask**
- **Selenium**
- **dotenv**
- **HTML/CSS** for UI

## Troubleshooting

1. **WebDriver Error**:
   - Ensure ChromeDriver matches your installed Chrome version.
   - Check the WebDriver path in your script.

2. **Blocked Access**:
   - Avoid triggering anti-bot mechanisms by simulating human-like delays and interactions.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributions

Contributions are welcome! Please open an issue or submit a pull request for any suggestions or improvements.

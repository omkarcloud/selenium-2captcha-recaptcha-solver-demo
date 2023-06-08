# Selenium 2captcha Recaptcha Solver Demo

This is the final code for the tutorial you learn how to solve captcha using 2captcha. The general steps for solving captchas using 2captcha in Selenium are as follows:

1. Create an account on 2captcha, add funds, and note the API Key.
2. Note the Site key of the target Captcha.
3. Submit the Site Key and Page URL to 2Captcha to solve the Captcha.
4. Set the solved Captcha code on the appropriate element and submit the form.

Please refer to ARTICLE_LINK for a detailed tutorial on solving captchas using 2captcha.

## Usage 
- Replace "2CAPTCHA_API_KEY" with your 2captcha API Key.
- Replace "SITE_KEY" with the Site Key of the Captcha you want to solve.
- Install dependencies by running `python -m pip install 2captcha-python selenium webdriver-manager`.
- Run `python main.py`.s
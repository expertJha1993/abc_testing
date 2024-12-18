from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # Set headless=True to run without opening the browser
    page = browser.new_page()
    page.goto("https://www.example.com")
    page.screenshot(path="example.png")
    browser.close()
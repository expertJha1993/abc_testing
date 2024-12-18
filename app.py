from playwright.sync_api import sync_playwright
import random
import time

# List of websites to visit
nlp_websites = [
    # Educational Resources
    "https://nlp.stanford.edu/",
    "https://deepai.org/machine-learning-glossary-and-terms/natural-language-processing",
    "https://www.coursera.org/courses?query=nlp",
    "https://www.edx.org/learn/natural-language-processing",
    "https://www.kaggle.com/learn/natural-language-processing",

    # Research Papers and Updates
    "https://arxiv.org/list/cs.CL/recent",
    "https://ai.googleblog.com/search/label/NLP",
    "https://aclanthology.org/",
    "https://www.semanticscholar.org/",
    "https://medium.com/tag/nlp",

    # Datasets and Challenges
    "https://huggingface.co/datasets",
    "https://www.kaggle.com/datasets",
    "https://datasetsearch.research.google.com/",
    "https://paperswithcode.com/area/natural-language-processing",
    "https://allennlp.org/",

    # Libraries and Tools
    "https://huggingface.co/transformers/",
    "https://spacy.io/",
    "https://www.nltk.org/",
    "https://platform.openai.com/",
    "https://radimrehurek.com/gensim/",

    # Practical Tutorials
    "https://www.geeksforgeeks.org/natural-language-processing/",
    "https://realpython.com/natural-language-processing-spacy-python/",
    "https://towardsdatascience.com/tagged/nlp",
    "https://www.analyticsvidhya.com/blog/category/nlp/",
    "https://www.datacamp.com/tutorials/search?query=nlp",

    # Competitions and Projects
    "https://www.kaggle.com/competitions",
    "https://www.drivendata.org/",
    "https://www.aicrowd.com/challenges?tags=nlp",
    "https://codeforces.com/",
    "https://nlpprogress.com/"
]

# Function to scroll down slowly with a random pause between scrolls
def slow_scroll(page):
    scroll_height = page.evaluate("document.body.scrollHeight")
    current_scroll = 0
    scroll_step = 300  # Pixels to scroll in each step

    while current_scroll < scroll_height:
        page.evaluate(f"window.scrollBy(0, {scroll_step});")
        current_scroll += scroll_step
        
        # Random pause between 100ms and 200ms for each scroll step
        scroll_pause_time = random.uniform(50, 90)  # Pause between 100ms and 200ms
        time.sleep(scroll_pause_time)

# Start Playwright with Chromium (Opera uses Chromium engine)
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=["--disable-blink-features=AutomationControlled"])  # Ensure browser is visible and cursor is active
    context = browser.new_context()
    page = context.new_page()

    # Making sure the cursor is visible by adding custom CSS to prevent it from being hidden
    page.add_style_tag(content="* { cursor: auto !important; }")

    # Visit each website
    try:
        for website in nlp_websites:
            print(f"Opening {website}...")
            page.goto(website)
            time.sleep(3)  # Wait for the page to load
            
            slow_scroll(page)  # Scroll down the page

            time.sleep(2)  # Pause before moving to the next website

    finally:
        browser.close()

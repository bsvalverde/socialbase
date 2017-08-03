from selenium import webdriver

def before_all(context):
    context.browser = webdriver.Firefox()
    #context.browser = webdriver.Chrome()
    #context.browser = webdriver.InternetExplorer()

def after_all(context):
    context.browser.quit()
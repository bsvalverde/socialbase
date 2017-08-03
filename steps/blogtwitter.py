from behave import *
from selenium.common.exceptions import NoSuchElementException

@given('the post {title} is on the blog')
def step_title(context, title):
	#context.browser.get('http://www.culturacolaborativa.com')
	#pages = context.browser.find_elements_by_xpath('//div/a[@class="page-numbers"]');
	#lastPage = int(pages[len(pages)-1].text)
	#for i in range(1, lastPage+1):
	#	context.browser.get('http://www.culturacolaborativa.com/page/' + str(i) + '/')
	#	for post in context.browser.find_elements_by_xpath('//h2[@class="post-content__title"]/a'):
	#		context.posts.append(post.text)
	context.title = title
	assert len(context.title) > 0

@then('there should be a tweet about it')
def step_impl(context):
	success = True
	context.browser.get('https://twitter.com/search?l=&q=' + context.title + '%20from%3ASocialBaseBR&src=typd')
	try:
		tweet = context.browser.find_element_by_xpath('//div[@class="js-tweet-text-container"]')#//a[@data-expanded-url]').get_attribute('data-expanded-url')
	except NoSuchElementException:
		print(context.title + ' is not on Twitter')
		success = False
	assert success is True
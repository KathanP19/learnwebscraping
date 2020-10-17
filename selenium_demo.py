from selenium import webdriver 
opts = webdriver.ChromeOptions()
opts.headless =True

driver = webdriver.Chrome(executable_path= r"D:\PythonL\Learning\Webscraper\chromedriver_win32\chromedriver.exe", options =opts)
driver.get('http://www.gutenberg.org/ebooks/search/%3Fsort_order%3Drelease_date')
books = driver.find_elements_by_class_name('booklink')
count = 0
while True:
    if count==5:
        break
    count +=1
    print('page ',count)
    books = driver.find_elements_by_class_name('booklink')
    
    
    for book in books:
        try:
            name = book.find_elements_by_class_name('title')[0].text
            try:
                author = book.find_elements_by_class_name('subtitle')[0].text
            except:
                author = 'Not availbale'
            try:
                date = book.find_elements_by_class_name('extra')[0].text
            except:
                date = 'Not availbale'
            print('name:', name)
            print('author :', author)
            print('date :', date)
            print('_'*100)
        except:
            pass
        
    driver.find_elements_by_class_name('statusline')[0].find_elements_by_tag_name('a')[-1].click()
    print('|'*100)
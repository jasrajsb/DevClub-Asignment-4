from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "C:\Program Files (x86)\chromedriver.exe"

print("Welcome to Automatic Moodle Captch Solver")

id = input("Enter your Kerberos ID: ")
passw = input("Enter your Kerberos Password: ")
print("Please wait while I Chrome and fill in the details for you...")
driver = webdriver.Chrome(PATH)


def solve(captcha):
    # print(captcha.split(' '))
    if (captcha.split(' ')[0] == 'add'):
        # print(captcha.split(' '))
        return str(int(captcha.split(' ')[1]) + int(captcha.split(' ')[3]))

    if (captcha.split(' ')[0] == 'subtract'):
        # print(captcha.split(' '))
        return str(int(captcha.split(' ')[1]) - int(captcha.split(' ')[3]))

    if (captcha.split(' ')[0] == 'enter'):
        if (captcha.split(' ')[1] == 'first'):
            return captcha.split(' ')[3]

        if (captcha.split(' ')[1] == 'second'):
            return captcha.split(' ')[5]


driver.get('https://moodle.iitd.ac.in')
captcha = driver.find_element_by_id("login").text.split('Please ')[1].split('\n')[0]
inputa = driver.find_element_by_name("valuepkg3")
driver.find_element_by_name("username").clear()
driver.find_element_by_name("username").send_keys(id)
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys(passw)
inputa.clear()
inputa.send_keys(solve(captcha))
inputa.send_keys(Keys.RETURN)
# driver.quit()

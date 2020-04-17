from browserActions import ChromeBrowser
from playsound import playsound
import datetime
import time

login = ''
password = ''

sleep_time = 6              # время в часах между проверками
min_balance = 2             # пороговое значение баланса

sleep_time = sleep_time * 60 * 60


def check_balance():
    browser = ChromeBrowser('--headless')
    browser.get("https://my.beltelecom.by/check-balance")
    browser.fill_form(text=login, css="input[name='login']")
    browser.fill_form(text=password, css="input[name='password']")
    browser.find_element_by_css_selector("button[type='submit']").click()
    browser.waiting(xpath="//div[@class='balance']/span", delay=30)
    balance = float(browser.find_element_by_xpath("//div[@class='balance']/span").text)
    if balance <= min_balance:
        playsound("alert.wav")
    now = datetime.datetime.now()
    print(f"[{now.strftime('%H:%M %d/%m')}] Баланс: {balance}")
    browser.close()


def main():
    while True:
        check_balance()
        time.sleep(sleep_time)


if __name__ == "__main__":
    main()

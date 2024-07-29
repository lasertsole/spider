from DrissionPage import WebPage, ChromiumOptions, SessionOptions
def createWebPage(headless=False, incognito=False):
    co = ChromiumOptions().set_paths(browser_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe')
    so = SessionOptions()

    if headless:
        co.headless()
        co.set_user_agent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36")  # 将user-agent的headless覆盖掉
    if incognito:
        co.incognito(True)#无痕模式
    page = WebPage(chromium_options=co, session_or_options=so)
    return page

def quitWebPage(page):
    page.quit()
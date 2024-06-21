import win32api
import win32con
import time
time.sleep(2)

word = "chatgpt.com"

def click(key):
    win32api.keybd_event(key, 0, 0, 0)
    win32api.keybd_event(key, 0, win32con.KEYEVENTF_KEYUP, 0)

def click_ord(key):
    win32api.keybd_event(ord(key), 0, 0, 0)
    win32api.keybd_event(ord(key), 0, win32con.KEYEVENTF_KEYUP, 0)

def chatgpt_writer(slow_time):
    for i in range(len(word)):
        if word[i] == '.':
            click(win32con.VK_DECIMAL)
        else:
            letter = word[i].upper()
            click_ord(letter)
            time.sleep(slow_time)

def writer(letter, slow_time):
        light_click(letter, slow_time)

chatgpt_writer(0.01)
click(win32con.VK_RETURN)



































# def chatgpt_writer(letter, slow_time):

#     writer(slow_time)



# win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)
# win32api.keybd_event(ord('S'), 0, 0, 0)
# time.sleep(0.5)

# win32api.keybd_event(ord('S'), 0, win32con.KEYEVENTF_KEYUP, 0)
# win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)
# time.sleep(same_time)

# win32api.keybd_event(win32con.VK_RETURN, 0, 0, 0)
# win32api.keybd_event(win32con.VK_RETURN, 0, win32con.KEYEVENTF_KEYUP, 0)
# time.sleep(same_time)

# win32api.keybd_event(win32con.VK_TAB, 0, 0, 0)
# win32api.keybd_event(win32con.VK_TAB, 0, win32con.KEYEVENTF_KEYUP, 0)
# time.sleep(same_time)

# win32api.keybd_event(win32con.VK_RETURN, 0, 0, 0)
# win32api.keybd_event(win32con.VK_RETURN, 0, win32con.KEYEVENTF_KEYUP, 0)
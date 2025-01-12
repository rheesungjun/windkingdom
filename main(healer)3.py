# python version = 3.9.6 64bit




import threading
import time
from pynput.mouse import Controller as MouseController
from pynput.mouse import Button
from pynput.keyboard import Key, Listener, KeyCode, Controller as KeyboardController
import pyautogui


# 마우스 및 키보드 컨트롤러 초기화
mouse = MouseController()
keyboardC = KeyboardController()

# 메타변수
stop = 0
full_mp = 0
HP = 0
wait = 0
kill=0
MP=0

# 기본기능힘수
def send_key(k):
    keyboardC.press(k)
    keyboardC.release(k)
    return
def ctrl_n(n):
    time.sleep(0.01)
    keyboardC.press(Key.ctrl)
    time.sleep(0.04)
    keyboardC.press(n)
    keyboardC.release(n)
    time.sleep(0.04)
    keyboardC.release(Key.ctrl)
    time.sleep(0.01)
    return
def send_2key(k1,k2):
    time.sleep(0.01)
    keyboardC.press(k1)
    time.sleep(0.04)
    keyboardC.press(k2)
    keyboardC.release(k2)
    time.sleep(0.04)
    keyboardC.release(k1)
    time.sleep(0.01)
    return
def send_key_enter(k):
    send_key(k)
    time.sleep(0.05)
    send_key(Key.enter)
    time.sleep(0.05)


# 자동힐
def auto_heal():
    global wait,kill
    count=0
    print('start auto heal')
    while 1:
        if kill==1:break
        send_key('8')
        time.sleep(0.05)
        for i in range(5):
            send_key('4')
            time.sleep(0.2)
        
        send_key('5')
        time.sleep(0.1)
        if HP==1:
            self_heal()
        if MP==1:

            time.sleep(0.05)
            send_key('3')
            time.sleep(0.05)
        # if count>10:
        #     count=0
        #     shotr_debuff()
        # else:
        #     count=count+1
        send_key('7')
        



def self_heal():
    send_key(Key.esc)
    time.sleep(0.05)
    send_key('8')
    time.sleep(0.05)
    send_key(Key.home)
    time.sleep(0.05)
    send_key(Key.enter)
    time.sleep(0.05)
    for i in range(2):
        send_key('4')
        time.sleep(0.05)
        send_key(Key.home)
        time.sleep(0.05)
        send_key(Key.enter)
        time.sleep(0.05)
    send_key('5')
    time.sleep(0.05)
    send_key(Key.enter)
    time.sleep(0.05)
    send_key(Key.esc)
    time.sleep(0.05)
    send_key(Key.tab)
    time.sleep(0.2)
    send_key(Key.tab)
    time.sleep(0.2)

def debuff():
    global stop
    send_key(Key.esc)
    time.sleep(0.05)
    for i in range(20):
        if stop==1:
            break
        send_key('1')
        time.sleep(0.05)
        send_key(Key.left)
        time.sleep(0.05)
        send_key(Key.enter)
        time.sleep(0.05)
    send_key(Key.tab)
    time.sleep(0.1)
    send_key(Key.tab)
    time.sleep(0.1)
    return
def shotr_debuff():
    send_key(Key.esc)
    time.sleep(0.05)
    for i in range(4):
        send_key('1')
        time.sleep(0.05)
        send_key(Key.left)
        time.sleep(0.05)
        send_key(Key.enter)
        time.sleep(0.05)
    send_key(Key.tab)
    time.sleep(0.2)
    send_key(Key.tab)
    time.sleep(0.2)
    return

def debuff_th():
    global stop
    stop=0
    att=threading.Thread(target=debuff)
    att.daemon=True
    att.start()
def autoheal_th():
    global stop,kill
    stop=0
    kill=0
    heal=threading.Thread(target=auto_heal)
    heal.daemon=True
    heal.start()
    check_mp_th()
    check_hp_th()

def check_mp_th():
    check_mp_thr=threading.Thread(target=check_mp)
    check_mp_thr.daemon=True
    check_mp_thr.start()
def check_hp_th():
    check_hp_thr=threading.Thread(target=check_hp)
    check_hp_thr.daemon=True
    check_hp_thr.start()
def click_hon_th():
    click_hon_thr=threading.Thread(target=click_hon)
    click_hon_thr.daemon=True
    click_hon_thr.start()



# 반복 멈추기
def stop_sign():
    global stop
    stop=1

def check_mp():
    global MP
    print('마나통을 체크 합니다.')
    while 1:
        if kill==1:break
        
        try:
            pyautogui.locateCenterOnScreen(image="mana_low2.png",confidence=0.95)
            print('공증을 쓰시오')
            MP=1
        except:
            MP=0

def check_hp():
    global kill,HP
    print('피통을 체크 합니다.')
    while 1:
        if kill==1:break
        
        try:
            pyautogui.locateCenterOnScreen(image="hp_low.png",confidence=0.95)
            print('low hp')
            HP=1
        except :
            HP=0
            None

def click_hon():
    global stop
    while 1:
        if stop==1:
            break
        send_key('1')
        time.sleep(0.05)
        mouse.click(Button.left,2)
        time.sleep(0.05)
        send_key(Key.enter)
        time.sleep(0.05)

# 키 할당
def on_press(key):

    
    if key==KeyCode(char='-'): # 공격!
        print(key,"를 눌렀습니다.")
        self_heal()
        return

    if key==KeyCode(char='='): # 중지!
        print(key,"를 눌렀습니다.")
        stop_sign()
        return



    if key==KeyCode(char='['): # 국내성 출
        print(key,"를 눌렀습니다.")
        debuff_th()

        return

    if key==KeyCode(char=']'): # 사냥터 출
        print(key,"를 눌렀습니다.")
        autoheal_th()
        return
    
    if key==KeyCode(char='~'): # 사냥터 출
        global kill,stop,wait
        print(key,"를 눌렀습니다.")
        kill=1
        return
    
    if key==KeyCode(char='!'): # 공격!
        print(key,"를 눌렀습니다.")
        click_hon_th()
        return





# 메인함수
if __name__ == "__main__":

    with Listener(on_press=on_press) as listener:
        listener.join()




# python version = 3.9.6 64bit




import threading
import time

from pynput.mouse import Controller as MouseController
from pynput.mouse import Button
from pynput.keyboard import Key, Listener, KeyCode, Controller as KeyboardController
import keyboard
import pyautogui
import cv2
import numpy as np



# 마우스 및 키보드 컨트롤러 초기화
mouse = MouseController()
keyboardC = KeyboardController()

# 메타변수
stop = 0
full_mp = 0
hp = 'ok'
wait = 0
kill=0

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
    print('start auto heal')
    while 1:
        if kill==1:break
        if wait==0:
            send_key('4')
            time.sleep(0.2)
            send_key('5')
            time.sleep(0.5)
        else:
            print('auto_heal waitting...')
            time.sleep(1)


def self_heal():
    send_key(Key.esc)
    time.sleep(0.05)
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
    for i in range(3):
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

def debuff_th():
    global stop
    stop=0
    att=threading.Thread(target=debuff)
    att.daemon=True
    att.start()
def autoheal_th():
    global stop
    stop=0
    heal=threading.Thread(target=auto_heal)
    heal.daemon=True
    heal.start()
    check_mp_th()
    check_hp_th()

def check_mp_th():
    check_mp_thr=threading.Thread(target=check_mp2)
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
    global stop, wait
    if stop==0:
        stop=1
        wait=1
    else:
        stop=0
        wait=0



def check_mp():
    global wait
    while 1:
        if wait==0:
            try:
                print('마나통을 체크 합니다.')
                pyautogui.locateCenterOnScreen(image="mana_low2.png",confidence=0.95)
                print('공증을 쓰시오')
                wait=1
                while 1:
                    try:
                        send_key('3')
                        time.sleep(0.1)
                        pyautogui.locateCenterOnScreen(image="mana_low2.png",confidence=0.95,grayscale=True)
                        time.sleep(0.1)
                        
                    except:
                        wait=0
                        break
            except:
                print('mana-full')
                
        else:
            print('ckech_mp 비활성중')
            time.sleep(2)
def check_mp2():
    global wait,kill
    while 1:
        if kill==1:break
        if wait==0:
            try:
                print('마나통을 체크 합니다.')
                pyautogui.locateCenterOnScreen(image="mana_low2.png",confidence=0.95)
                print('공증을 쓰시오')
                send_key('3')
                time.sleep(0.1)    
            except:
                print('mana-full')
                
        else:
            print('ckech_mp 비활성중')
            time.sleep(2)



def check_hp():
    global wait,kill
    while 1:
        if kill==1:break
        if wait==0:
            try:
                print('피통을 체크 합니다.')
                pyautogui.locateCenterOnScreen(image="hp_low.png",confidence=0.9)
                print('low hp')
                wait=1
                time.sleep(0.35)
                self_heal()
                time.sleep(0.15)
                self_heal()
                time.sleep(0.15)
                for i in range(5):
                    send_key('7')
                    time.sleep(0.05)
                # time.sleep(0.15)
                shotr_debuff()
                wait=0
            except :
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

    # print(key)
    
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
        if kill==0:
            kill=1
            
            print('시스템 종료')
        else:
            kill=0
            stop=0
            wait=0
            print('오토힐 시스템 활성화')
        return
    
    if key==KeyCode(char='!'): # 공격!
        print(key,"를 눌렀습니다.")
        click_hon_th()
        return





# 메인함수
if __name__ == "__main__":

    with Listener(on_press=on_press) as listener:
        listener.join()




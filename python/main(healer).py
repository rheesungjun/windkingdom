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
import easyocr
import random


# 마우스 및 키보드 컨트롤러 초기화
mouse = MouseController()
keyboardC = KeyboardController()

# 메타변수
stop = 0

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

# 자동신수
def attack():
    global stop
    while 1:
        if stop==1:
            print("스톱사인이 들어왔습니다.",stop)
            break
        print("도사가 공격을 시작합니다.",stop)
        for i in range(3):
            if stop==1:
                print("스톱사인이 들어왔습니다.",stop)
                break
            rand_sleep()
            send_key('2')
            rand_sleep()
            send_key(Key.left)
            rand_sleep()
            send_key(Key.enter)
            time.sleep(1)
            for j in range(4):
                for i in range(2):
                    for j in range(3):
                        send_key('2')
                        rand_sleep()
                        send_key(Key.enter)
                        time.sleep(1)
                    send_key(Key.tab)
                    rand_sleep()
                    send_key(Key.tab)
                    rand_sleep()
                    send_key('4')
                    rand_sleep()
                    send_key(Key.esc)
                    rand_sleep()
                mp_fill()
                send_key(Key.tab)
                rand_sleep()
                send_key(Key.tab)
                rand_sleep()
                send_key('4')
                rand_sleep()
                send_key('5')
                rand_sleep()
                send_key('6')
                rand_sleep()
                send_key(Key.esc)
                rand_sleep()
                
        change_channel()
        time.sleep(5)

# 자동힐
def auto_heal():
    if stop==1:
        print('stop!')
        return
    mp_count=0
    print('start auto heal')
    while stop==0:
        # if stop==1:
        #     print('stop!')
        #     return
        send_key('4')
        time.sleep(0.05)
        send_key('5')
        time.sleep(0.1)
        self_heal()
        time.sleep(0.1)
        if mp_count>2:
            print('동동주 먹자')
            send_2key(Key.ctrl,'a')
            time.sleep(0.1)
            send_2key(Key.ctrl,'a')
        send_key('3')
        time.sleep(0.1)
        if check_mp():
            print('공증 성공')
            mp_count=0
        else:
            mp_count=mp_count+1


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
    time.sleep(0.1)
    send_key(Key.tab)
    time.sleep(0.05)

def change_channel():
    print('채널 체인지')
    change_img_check('change_1.png')
    # pyautogui.moveTo(100,200,duration=0.3)
    change_img_check('change_2.png')
    # pyautogui.moveTo(200,250,duration=0.3)
    change_img_check('change_3.png')
    # pyautogui.moveTo(300,300,duration=0.3)
    change_img_check('change_4.png')
    # pyautogui.moveTo(400,350,duration=0.3)
    change_img_check('change_5.png')
    # pyautogui.moveTo(500,400,duration=0.3)
    change_img_check('change_6.png')

    return

def debuff():
    send_key(Key.esc)
    time.sleep(0.05)
    for i in range(20):
        if stop==1:
            # send_key(Key.esc)
            # time.sleep(0.05)
            # send_key(Key.tab)
            # time.sleep(0.05)
            # send_key(Key.tab)
            # time.sleep(0.1)
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

def change_img_check(img):
    while 1:
        try:
            x,y=pyautogui.locateCenterOnScreen(image=img,confidence=0.9)
            print('success!!')
            time.sleep(0.5)
            pyautogui.leftClick(x/2,y/2)
            time.sleep(0.5)
            pyautogui.leftClick(x/2,y/2)
            time.sleep(0.5)
            pyautogui.leftClick(x/2,y/2)
            time.sleep(0.5)
            return
        except:
            print('실패')
            time.sleep(0.5)
            try:
                x,y=pyautogui.locateCenterOnScreen("timeout_1.png",confidence=0.9)
                print('타임아웃 발생')
                time.sleep(0.5)
                pyautogui.leftClick(x/2,y/2)
                time.sleep(0.5)
                pyautogui.leftClick(x/2,y/2)
                time.sleep(0.5)
                
                while 1:
                    try:
                        x,y=pyautogui.locateCenterOnScreen("timeout_2.png",confidence=0.9)
                        time.sleep(0.5)
                        pyautogui.leftClick(x/2,y/2)
                        time.sleep(0.5)
                        pyautogui.leftClick(x/2,y/2)
                        time.sleep(0.5)
                        pyautogui.leftClick(x/2,y/2)
                        time.sleep(0.5)
                        break
                    except:
                        print('타임아웃2 실패')
                    
            except:
                print('타임아웃1 실패')
    return

def att_th():
    global stop
    stop=0
    # att=threading.Thread(target=attack)
    att=threading.Thread(target=auto_heal)
    att.daemon=True
    att.start()
def debuff_th():
    global stop
    stop=0
    # att=threading.Thread(target=attack)
    att=threading.Thread(target=debuff)
    att.daemon=True
    att.start()



# 반복 멈추기
def stop_sign():
    global stop
    stop=1


def mp_fill():
    while check_mp():
        send_key('3')
        rand_sleep()
        send_key(Key.esc)
        rand_sleep()

def check_mp():
    try:
        pyautogui.locateCenterOnScreen(image="mana_full.png",confidence=0.9)
        print('mana-full')
        return 0
    except Exception as e:
        return 1

def rand_sleep():
    arr=[0.1, 0.13, 0.15, 0.18, 0.2]
    sec = random.choice(arr)
    time.sleep(sec)





# 키 할당
def on_press(key):

    # print(key)
    
    if key==KeyCode(char='-'): # 공격!
        print(key,"를 눌렀습니다.")
        att_th()
        return

    if key==KeyCode(char='='): # 중지!
        print(key,"를 눌렀습니다.")
        stop_sign()
        return

    if key==Key.f1: # 종료하기
        print(key,'를 눌러 종료합니다.')
        listener.stop()
        return

    if key==KeyCode(char='q'): # 퀘스트받기
        print(key,"를 눌렀습니다.")

        return

    if key==KeyCode(char='['): # 국내성 출
        print(key,"를 눌렀습니다.")
        debuff_th()

        return

    if key==KeyCode(char=']'): # 사냥터 출
        print(key,"를 눌렀습니다.")

        return





# 메인함수
if __name__ == "__main__":

    with Listener(on_press=on_press) as listener:
        listener.join()
        



# python version = 3.9.6 64bit


# 출캐이름
국내성_출캐 = "춻춻"
사냥터_출캐 = "몸둥이"


import threading
import time
import os
from pynput.mouse import Controller as MouseController
from pynput.mouse import Button
from pynput.keyboard import Key, Listener, KeyCode, Controller as KeyboardController
import keyboard
import pyautogui
import cv2
import numpy as np
import easyocr



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


# 자동비투평
def attack():
    global stop
    print("도적이 공격을 시작합니다.",stop)
    for i in range(30):
        if stop==1:
            print("스톱사인이 들어왔습니다.",stop)
            break
        keyboardC.press('2')
        keyboardC.release('2')
        time.sleep(0.03)

        keyboardC.press('1')
        keyboardC.release('1')
        time.sleep(0.1)

        keyboard.press_and_release('space')
        time.sleep(0.01)
        keyboard.press_and_release('space')
        time.sleep(0.05) 
def att_th():
    global stop
    stop=0
    att=threading.Thread(target=attack)
    att.daemon=True
    att.start()
# 반복 멈추기
def stop_sign():
    global stop
    stop=1
# 출두
def chul2(name):
    print('출두!!')
    fly_door()
    time.sleep(0.1)
    send_2key(Key.shift,'z')
    time.sleep(0.05)
    send_2key(Key.shift,'z')
    time.sleep(0.1)
    keyboardC.type(name)
    time.sleep(0.05)
    send_key(Key.enter)
    time.sleep(0.5)
    return


# 왕퀘받기
def walk_king():
    for i in range(2):
        keyboardC.press(Key.right)
        time.sleep(0.1)
        keyboardC.release(Key.right)
        time.sleep(0.1)
    for i in range(4):
        keyboardC.press(Key.up)
        time.sleep(0.1)
        keyboardC.release(Key.up)
        time.sleep(0.1)
        try:
            x,y=pyautogui.locateCenterOnScreen(image="kinghome.png",confidence=0.9)
        except Exception as e:
            None
    

    for i in range(50):
        keyboardC.press(Key.left)
        time.sleep(0.01)
        keyboardC.release(Key.left)
        time.sleep(0.01)
        try:
            x,y=pyautogui.locateCenterOnScreen(image="king0006.png",confidence=0.95)
            print('0006 arrive!!')
            break
        except Exception as e:
            None
    
    keyboardC.press(Key.up)
    time.sleep(7)
    keyboardC.release(Key.up)
    time.sleep(0.05)

    for i in range(50):
        keyboardC.press(Key.up)
        time.sleep(0.01)
        keyboardC.release(Key.up)
        time.sleep(0.01)
        try:
            x,y=pyautogui.locateCenterOnScreen(image="king0010.png",confidence=0.95)
            print('0010 arrive!!')
            break
        except Exception as e:
            None
    quest()
def que_th():
    global stop
    stop=0
    que=threading.Thread(target=quest)
    que.daemon=True
    que.start()
def quest():
    print('퀘스트를 받자')

    '''
    왕을 클릭한다? -> 왕의 위치를 파악한다. -> 캐릭터의 위치에 따라 다르다. -> 이미지 서치를 하자
    
    '''
    for i in range(100):
        try:
            x,y=pyautogui.locateCenterOnScreen(image="king.png",confidence=0.7)
            pyautogui.click(x=x/2,y=y/2)
            time.sleep(0.01)
            pyautogui.click(x=x/2,y=y/2)
            time.sleep(0.3)
            pyautogui.moveTo(100,100)
        except Exception as e:
            print('fail')
            break
        mouse.click(Button.left,1)
        time.sleep(0.2)
        mouse.click(Button.left,1)
        time.sleep(0.2)
        keyboard.press_and_release('space')
        time.sleep(0.3)
        keyboardC.press(Key.shift)
        time.sleep(0.1)
        keyboard.press_and_release('down')
        time.sleep(0.1)
        keyboardC.release(Key.shift)
        time.sleep(0.1)
        keyboard.press_and_release('space')
        time.sleep(0.2)
        keyboard.press_and_release('space')
        time.sleep(0.2)
        keyboard.press_and_release('space')
        time.sleep(0.2)
        keyboard.press_and_release('space')
        time.sleep(2)

        


        try:
            x,y=pyautogui.locateCenterOnScreen(image="king.png",confidence=0.7)
            pyautogui.click(x=x/2,y=y/2)
            time.sleep(0.01)
            pyautogui.click(x=x/2,y=y/2)
            time.sleep(0.3)
            pyautogui.moveTo(100,100)
        except Exception as e:
            print('fail')
            break
        keyboard.press_and_release('space')
        time.sleep(0.2)
        keyboard.press_and_release('space')
        time.sleep(0.3)
        keyboard.press_and_release('down')
        time.sleep(0.1)
        keyboard.press_and_release('space')
        time.sleep(0.2)
        try:
            x,y=pyautogui.locateCenterOnScreen(image="fast_skel.png",confidence=0.8)
            print('독충 받았다!')
            quest_go()
            break
        except:
            try:
                x,y=pyautogui.locateCenterOnScreen(image="skel.png",confidence=0.8)
                print('해골 받았다!')
                quest_go()
                break
            except:
                None
        keyboard.press_and_release('space')
        time.sleep(0.2)
        keyboard.press_and_release('space')
        time.sleep(2)
def quest_go():
    keyboardC.press(Key.esc)
    time.sleep(0.05)
    keyboardC.release(Key.esc)
    time.sleep(0.05)
    keyboardC.press('s')
    keyboardC.release('s')
    time.sleep(0.1)
    keyboardC.press('s')
    keyboardC.release('s')
    time.sleep(0.05)
    for j in range(5):
        keyboardC.press(Key.page_down)
        keyboardC.release(Key.page_down)
        time.sleep(0.2)
    ctrl_n("c")
    time.sleep(1)
    return
    # fly_door()
    # walk_skel()


# 왕퀘받기2
def que_th2():
    global stop
    stop=0
    que=threading.Thread(target=quest2)
    que.daemon=True
    que.start()

def quest2():
    stack=0
    print('퀘스트를 받자2')
    while stop==0:
        try:
            click_king()
            script()
            time.sleep(1)
        except:
            print('fail2')
            for i in range(3):
                send_key(Key.esc)
                time.sleep(0.05)
            stack=stack+1
            if stack>2:
                break



def click_king():
    x,y=pyautogui.locateCenterOnScreen(image="king.png",confidence=0.7,grayscale=True)
    time.sleep(0.01)
    pyautogui.click(x=x/2,y=y/2)
    time.sleep(0.01)
    pyautogui.click(x=x/2,y=y/2)
    time.sleep(0.3)
    pyautogui.moveTo(500,100)

def script():
    # 퀘 받는다? get_q()
    # 퀘 취소한다? cancel_q()
    # 경험치 받는다? reward()
    # 아무것도 아니다? esc!!

    try:
        x,y=pyautogui.locateCenterOnScreen(image="get_q.png",confidence=0.8,grayscale=True)
        print('퀘를 받자')
        get_q()
        return
    except:
        try:
            x,y=pyautogui.locateCenterOnScreen(image="cancel.png",confidence=0.8,grayscale=True)
            print('안잡아!')
            cancel_q()
            return
        except:
            try:
                x,y=pyautogui.locateCenterOnScreen(image="reward.png",confidence=0.8,grayscale=True)
                print('빨리 줘!')
                reward()
                return
            except:
                send_key(Key.esc)
                time.sleep(0.05)
                send_key(Key.esc)
                time.sleep(0.05)
                return

    



def get_q():
    # 스페이스 스페이스 아래 스페이스 받은거판단 액션
    for i in range(2):
        send_key(Key.space)
        print('space')
        time.sleep(0.25)
    send_key(Key.down)
    time.sleep(0.05)
    send_key(Key.space)
    picking()
    send_key(Key.esc)
    


    

def cancel_q():
    # 스페이스 아래 스페이스 스페이스 스페이스
    send_key(Key.space)
    time.sleep(0.25)
    keyboard.press_and_release('down')
    time.sleep(0.05)
    for i in range(3):
        send_key(Key.space)
        time.sleep(0.25)
    None
def reward():
    send_key(Key.space)
    None

def picking():
    global stop
    # mon1 picking
    time.sleep(0.5)
    try:
        x,y=pyautogui.locateCenterOnScreen(image="poison.png",confidence=0.75,grayscale=True)
        print('독충')
        send_key(Key.esc)
        time.sleep(0.5)
        etc()
        stop=1
        time.sleep(0.5)
        buy_yellow()
        time.sleep(0.5)
        chul2(사냥터_출캐)
        return
    except:
        print('독충 실패')

    try:
        x,y=pyautogui.locateCenterOnScreen(image="ghost.png",confidence=0.75,grayscale=True)
        print('몽달')
        send_key(Key.esc)
        time.sleep(0.5)
        etc()
        stop=1
        time.sleep(0.5)
        buy_yellow()
        time.sleep(0.5)
        chul2(사냥터_출캐)
        return
    except:
        print('꽝')
        return

def etc():
    # 비서쓰고
    send_2key(Key.ctrl,'c')
    time.sleep(0.3)
    # 퀘스트창 열고
    for i in range(3):
        send_key('s')
        time.sleep(0.1)
    for i in range(5):
        send_key(Key.page_down)
        time.sleep(0.1)

def buy_yellow():
    send_key(Key.enter)
    time.sleep(0.3)
    keyboardC.type('노란비서 3개 줘')
    time.sleep(0.3)
    send_key(Key.enter)
    time.sleep(0.3)
    return


# 비영사천문
def fly_door():
    time.sleep(0.1)
    keyboardC.press('0')
    keyboardC.release('0')
    time.sleep(0.1)
    keyboardC.press('4')
    keyboardC.release('4')
    time.sleep(0.1)
    keyboard.press_and_release('enter')
    time.sleep(0.1)
    keyboardC.press(Key.esc)
    time.sleep(0.05)
    keyboardC.release(Key.esc)
    time.sleep(0.05)
    return














# 키 할당
def on_press(key):

    # print(key)
    
    if key==KeyCode(char='-'): # 공격!
        print(key,"를 눌렀습니다.")
        yoon_th()
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
        que_th2()
        return

    if key==KeyCode(char='['): # 국내성 출
        print(key,"를 눌렀습니다.")
        chul2(국내성_출캐)
        return

    if key==KeyCode(char=']'): # 사냥터 출
        print(key,"를 눌렀습니다.")
        chul2(사냥터_출캐)
        return


def yoon_th():
    global stop
    stop=0
    que=threading.Thread(target=yoondo)
    que.daemon=True
    que.start()
def yoondo():
    while 1:
        if stop==1:
            break
        send_key(Key.tab)
        time.sleep(0.3)
        send_key(Key.enter)
        time.sleep(0.3)
        for j in range(3):
            send_key(Key.down)
            time.sleep(0.3)
        for j in range(4):
            send_key(Key.enter)
            time.sleep(0.3)
        time.sleep(1)



def test():
    x,y=pyautogui.position()
    print("x=",x,", y=",y)


def text_reader(img):
    reader = easyocr.Reader(['ko','en'])
    results= reader.readtext(img)
    _,text,_=results[0]
    print(text)

def capture(x,y):
    img = pyautogui.screenshot('test.png',(1133,910,1284,928))
    
    return



# (
#     [[np.int32(16), np.int32(6)], [190, np.int32(6)], [190, np.int32(56)], [np.int32(16), np.int32(56)]],
#       '국내성왕궁', 
#       np.float64(0.7899191877314634)
# )




# 메인함수
if __name__ == "__main__":

    with Listener(on_press=on_press) as listener:
        listener.join()







# 스샷찍는 코드(더이상 안씀!)
# save_path="screenshot2.png"
# screenshot = pyautogui.screenshot(region=(501-25,160-25,50,50))
# screenshot_np = np.array(screenshot)
# screenshot_bgr = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)
# screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)
# cv2.imwrite(save_path, screenshot_gray)


# def chul():
    print('출두!!')
    fly_door()
    time.sleep(0.5)
    keyboardC.press(Key.shift)
    time.sleep(0.05)
    keyboardC.press('z')
    keyboardC.release('z')
    time.sleep(0.2)
    keyboardC.press('z')
    keyboardC.release('z')
    time.sleep(0.05)
    keyboardC.release(Key.shift)
    time.sleep(0.2)
    keyboardC.type('춻춻')
    time.sleep(0.05)
    keyboard.press_and_release('enter')
    time.sleep(0.5)
    walk_king()
# def walk_skel():
#     time.sleep(1)
#     try:
#         x,y=pyautogui.locateCenterOnScreen(image="goback.png",confidence=0.95)
#         print('비영!!')
#         fly_door()
#         walk_skel()
#         return
#     except Exception as e:
#         None



#     keyboardC.press(Key.down)
#     time.sleep(4)
#     keyboardC.release(Key.down)
#     time.sleep(0.05)
#     for i in range(50):
#         keyboardC.press(Key.down)
#         time.sleep(0.01)
#         keyboardC.release(Key.down)
#         time.sleep(0.01)
#         try:
#             x,y=pyautogui.locateCenterOnScreen(image="skel0026.png",confidence=0.95)
#             print('0026 arrive!!')
#             break
#         except Exception as e:
#             None

    
#     keyboardC.press(Key.right)
#     time.sleep(12)
#     keyboardC.release(Key.right)
#     time.sleep(0.05)
#     for i in range(100):
#         keyboardC.press(Key.right)
#         time.sleep(0.01)
#         keyboardC.release(Key.right)
#         time.sleep(0.01)
#         try:
#             x,y=pyautogui.locateCenterOnScreen(image="skel0147.png",confidence=0.95)
#             print('0147 arrive!!')
#             break
#         except Exception as e:
#             None


#     for i in range(20):
#         keyboardC.press(Key.up)
#         time.sleep(0.01)
#         keyboardC.release(Key.up)
#         time.sleep(0.01)
#         try:
#             x,y=pyautogui.locateCenterOnScreen(image="skel_arrive.png",confidence=0.95)
#             print('arrive!!')
#             break
#         except Exception as e:
#             None

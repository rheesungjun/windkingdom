import tkinter
from threading import Thread
import pyautogui
import time

TrueisGo = 1
activation = [1, 0]
# toggle bool = activation[0] default = 1
# thread bool = activation[1] default = 0

# 핸들을 글로벌 변수로 사용하기 위함
G_hwnd=0

# 글로벌 시간. 시간을 세는 기준
G_t=1

# 몇초까지 시간을 셀 것인지 타이머
timer = 10



def counter_th():
    global activation
    if activation[1] == 0:

        t = 0

        while activation[0]:
            activation[1] = 1
            label1.configure(text='act[1]:' + str(activation[1]))
            t = t + 1
            print(t, 'second')
            time.sleep(1)

            if t > 10:
                print('----------------- 10 seconds')
                t = 0
        if activation[0] == 0:
            print('토글이 off상태입니다.')
    else:
        print('이미 실행중입니다.')


# 스레드 간섭장치
def toggle_th():
    global activation
    activation[1] = 0
    activation[0] = -(activation[0]) + 1
    if activation[0]:
        label2.configure(text='act[0]:' + str(activation[0]))
        print('get ready!')
    else:
        label1.configure(text='act[1]:' + str(activation[1]))
        label2.configure(text='act[0]:' + str(activation[0]))

        print('quit thread')

# 스레드 시작, main 함수 호출
def thread_start():
    gg = Thread(target=main)
    gg.start()



# 버프 시간세기
def check():
    global G_t, timer
    print(G_t, timer)
    if G_t > timer-1:
        G_t = 1
        time.sleep(1)
    else :
        G_t = G_t + 1
        time.sleep(1)



# 메인 함수
def main():
    global G_t, activation
    if activation[1] == 0:
        while activation[0]:
            activation[1] = 1
            label1.configure(text='act[1]:' + str(activation[1]))
            label6.configure(text=G_t)
            check()
        if activation[0] == 0:
            print('토글이 off상태입니다.')
    else:
        print('이미 실행중입니다.')



# 핸들 잡는 기능
import win32gui
# import win32con
def gethandle():
    def enumHandler(hwnd, lParam):
        tfind = "연습장"
        global G_hwnd        
        if tfind in win32gui.GetWindowText(hwnd):
            G_hwnd = hwnd
            print("python handle : ", G_hwnd,win32gui.GetWindowText(hwnd))
            label3.configure(text=win32gui.GetWindowText(hwnd))
            
    win32gui.EnumWindows(enumHandler,None)

def top_window():
    global show_bool
    # win32gui.GetTopWindow(G_hwnd) 안먹힘
    # SetForegroudWindow로 특정창을 가장 상위로 불러낸다. 이를 통해 특정키 입력을 특정창에 보내는 것이 가능해진다.
    win32gui.SetForegroundWindow(G_hwnd)
    # win32gui.ShowWindow(G_hwnd,show_bool)

import keyboard

# 기능모음
def action():
    print('action!!')
    top_window()
    time.sleep(2)
    # pyautogui.typewrite('액션버튼을 눌렀습니다.') 메모장에 글씨 안써짐.
    keyboard.write('액션을 클릭했습니다.')
    # 입력이 잘된다!





# tkinter module
root = tkinter.Tk()
width = 300
height = 300
wi = root.winfo_screenwidth()
he = root.winfo_screenheight()

root.geometry('%dx%d+%d+%d' % (width, height, wi / 2 - width / 2, he / 2 - height / 2))
root.title = "thread tester"
label1 = tkinter.Label(root, width="12", text="비활성화")
label1.grid(row=1, column=0)
label2 = tkinter.Label(root, width="12", text="활성화")
label2.grid(row=1, column=1)
label3 = tkinter.Label(root, width="12", text="handle")
label3.grid(row=3, column=2)
label4 = tkinter.Label(root, width="12", text="글로벌 타임")
label4.grid(row=2, column=0)
label5 = tkinter.Label(root, width="12", text="타이머")
label5.grid(row=2, column=1)
label6 = tkinter.Label(root, width="12", text="숫자")
label6.grid(row=3, column=0)
label7 = tkinter.Label(root, width="12", text="숫자")
label7.grid(row=3, column=1)


btn1 = tkinter.Button(root, width="12", text='thread start', command=thread_start).grid(row=0, column=0)
btn2 = tkinter.Button(root, width="12", text='toggle', command=toggle_th).grid(row=0, column=1)
btn3 = tkinter.Button(root, width="12", text='get handle', command=gethandle).grid(row=2, column=2)

btn_show = tkinter.Button(root, width="12", text='창맨앞으로', command=top_window).grid(row=4, column=2)
btn_action = tkinter.Button(root, width="12", text='function', command=action).grid(row=5, column=2)

root.mainloop()

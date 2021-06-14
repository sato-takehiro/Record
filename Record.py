#Teamsの会議に自動で出席し、録画することができるプログラム　参加したい会議のリンクを130行目に張る

#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!pip3 install pyautogui #pyautoguiをインストール
#!pip3 install pyperclip #pyperclipをインストール
#!pip3 install schedule


# In[2]:


import pyautogui as pgui
import pyperclip as pclip
import datetime
import schedule
import time
import sys


# In[3]:

pgui.FAILSAFE = True #緊急停止

# In[4]:

def open_application(string): #あるアプリケーションstringを開く関数
    time.sleep(0.8) #0.8秒処理を停止する
    pgui.hotkey('win') #検索窓を開ける
    time.sleep(0.8) #0.8秒処理を停止する
    pclip.copy(string)
    time.sleep(0.8) #0.8秒処理を停止する
    pgui.hotkey('ctrl','v')
    time.sleep(0.8) #0.8秒処理を停止する
    pgui.hotkey('enter') #エンターキーを押す


# In[5]:


def attend_teams(string): #Teamsのリンクstringにアクセスする関数
    open_application(string)
    time.sleep(20) #20秒処理を停止する
    pgui.hotkey('win', 'up') #ウィンドウ全体に表示させる
    time.sleep(20) #20秒処理を停止する
    #pgui.click(x=1116, y=568, duration=1) #Teamsでミュートにする
    time.sleep(0.8) #0.8秒処理を停止する
    pgui.click(x=1505, y=858, duration=1) #Teamsで会議に参加する


# In[6]:


def exit_teams(): #Teamsの会議から退出する関数
    time.sleep(10) #10秒処理を停止する
    pgui.hotkey('ctrl', 'shift', 'b') #会議を退出する
    time.sleep(0.8) #0.8秒処理を停止する
    pgui.hotkey('ctrl', 'w') #Teamsのタブを閉じる


# In[7]:


def start_recording(): #ZOOMでPCの内部音声と画面の録画を開始する関数
    time.sleep(0.8) #0.8秒処理を停止する
    pgui.hotkey('ctrl') #マウスの位置確認
    pgui.click(x=1919, y=100, duration=1) #画面右上をクリックしてWinメニューを消す
    time.sleep(0.8) #0.8秒処理を停止する
    pgui.hotkey('ctrl') #マウスの位置確認
    open_application('ZOOM')
    time.sleep(10) #10秒処理を停止する
    pgui.hotkey('ctrl') #マウスの位置確認
    pgui.hotkey('win', 'up') #ウィンドウ全体に表示させる
    time.sleep(10) #10秒処理を停止する
    pgui.hotkey('ctrl') #マウスの位置確認
    pgui.click(x=819, y=62, duration=1) #ZOOMでホームを選択
    time.sleep(0.8) #0.8秒処理を停止する
    pgui.hotkey('ctrl') #マウスの位置確認
    pgui.click(x=592, y=450, duration=1) #ZOOMで新規MTGを開始する
    time.sleep(10) #10秒処理を停止する
    pgui.hotkey('ctrl') #マウスの位置確認
    pgui.hotkey('win', 'up') #ウィンドウ全体に表示させる
    time.sleep(10) #10秒処理を停止する
    pgui.hotkey('ctrl') #マウスの位置確認
    pgui.hotkey('alt', 'r') #レコーディングを開始する
    time.sleep(10) #10秒処理を停止する
    pgui.hotkey('ctrl') #マウスの位置確認
    pgui.click(x=1139, y=620, duration=1) #ミュートのままレコーディングを開始する
    pgui.hotkey('ctrl') #マウスの位置確認
    pgui.hotkey('alt', 's') #共有を開始する
    time.sleep(0.8) #0.8秒処理を停止する
    pgui.click(x=403, y=790, duration=1) #音声を共有ボタンを押す
    time.sleep(0.8) #0.8秒処理を停止する
    pgui.click(x=411, y=895, duration=1) #音声を共有ボタンを押す
    time.sleep(0.8) #0.8秒処理を停止する
    pgui.click(x=497, y=351, duration=1) #共有する画面を押す
    time.sleep(0.8) #0.8秒処理を停止する
    pgui.click(x=1475, y=892, duration=1) #共有を開始する
    time.sleep(0.8) #0.8秒処理を停止する
    pgui.click(x=1487, y=788, duration=1) #共有を開始する
    time.sleep(0.8) #0.8秒処理を停止する


# In[8]:


def finish_recording(): #ZOOMでPCの内部音声と画面の録画を終了する関数
    pgui.moveTo(x=1011, y=0, duration=1) #画面上部へ移動
    time.sleep(0.8) #0.8秒処理を停止する
    pgui.moveTo(x=1418, y=25, duration=1) #詳細へ移動
    time.sleep(0.8) #0.8秒処理を停止する
    pgui.click(x=1437, y=396, duration=1) #終了を選択
    time.sleep(0.8) #0.8秒処理を停止する
    pgui.click(x=966, y=481, duration=1) #終了を選択
    time.sleep(0.8) #0.8秒処理を停止する
    pgui.hotkey('alt', 'q') #レコーディングを終了する


# In[9]:


def first_processing(): #会議開始前の処理を書いた関数
    start_recording() #ZOOMでレコーディングを開始する
    #Teamsの会議に出席する
    #Teamsの会議のリンクを以下に張る
    attend_teams('https://teams.microsoft.com/l/meetup-join/19:meeting_YzRhMjQ1MjgtMTBkNC00NmY1LWI4NjAtMzI1MzAzODBkZWVl@thread.v2/0?context=%7B%22Tid%22:%22017b3621-1879-4c5e-a9a9-f81002ae18dd%22,%22Oid%22:%221d2ecdaa-9680-4b18-80a9-e7433534c3dd%22%7D')


# In[10]:


def last_processing(): #会議終了後の処理を書いた関数
    exit_teams() #Teamsの会議を退出する
    finish_recording() #レコーディングを終了する
    time.sleep(0.8) #0.8秒処理を停止する
    sys.exit() #録画が終了したら、プログラムを終了させる


# In[11]:

def main(): #メイン関数
    #既定の時刻になると授業に出席し、録画を開始する
    schedule.every().day.at("09:00").do(first_processing)
    #既定の時刻になると授業を退出し、録画を終了する
    schedule.every().day.at("12:20").do(last_processing)

    while True:
            schedule.run_pending()
            pgui.moveTo(100,100,0.25)
            pgui.moveTo(100,120,0.25)
            time.sleep(1)

if __name__ == '__main__': #このファイルがメインで実行されたら、メイン関数を実行する
    main()
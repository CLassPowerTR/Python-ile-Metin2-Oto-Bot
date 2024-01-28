import win32gui, win32ui, win32con, win32api
import cv2
import numpy as np
import pyautogui
import time
import math

class PyBotOpenCV:
    def __init__(self,hwnd):
        self.hwnd = hwnd
    def screenshot(self):
        left, top, right, bottom = win32gui.GetWindowRect(self.hwnd)
        width = right - left
        height = bottom - top
        width = width 
        height = height 
        
        hwndDC = win32gui.GetWindowDC(self.hwnd)
        mfcDC = win32ui.CreateDCFromHandle(hwndDC)
        saveDC = mfcDC.CreateCompatibleDC()
        
        saveBitMap = win32ui.CreateBitmap()
        saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)
        saveDC.SelectObject(saveBitMap)
        
        result = saveDC.BitBlt((0, 0), (width, height), mfcDC, (0, 0), win32con.SRCCOPY)

        bmp_info = saveBitMap.GetInfo()
        bmp_array = np.frombuffer(saveBitMap.GetBitmapBits(True), np.uint8)
        img = bmp_array.reshape(bmp_info['bmHeight'], bmp_info['bmWidth'], 4)
        
        win32gui.DeleteObject(saveBitMap.GetHandle())
        saveDC.DeleteDC()
        mfcDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, hwndDC)

        return img

    def listWindowNames(self):
        def winEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                print("ID=",hwnd, "TitLe= "+'"' + win32gui.GetWindowText(hwnd) + '"')
        win32gui.EnumWindows(winEnumHandler, None)


    def locateOnScreen(self,image,  matchvalue=0.8,region=None):
        if region != None:
            img2 = self.imageArea(region[0],region[1],region[2],region[3])
        if region == None:
            img2 = self.screenshot()
        img1 = cv2.imread(image)
        
        img1 = cv2.cvtColor(img1,cv2.COLOR_RGB2RGBA)
        img2 = cv2.cvtColor(img2,cv2.COLOR_RGB2RGBA)

        result = cv2.matchTemplate(img1,img2,cv2.TM_CCOEFF_NORMED)

        matchvalue = matchvalue
        
        w,h = np.array(img1).shape[1], np.array(img1).shape[0]
        
        y,x = np.where(result >= matchvalue)

        if len(x) > 0:
            for (xloc, yloc) in zip(x,y):
                cv2.rectangle(img2,(xloc,yloc),(xloc+w,yloc+h),(0,255,255),2)
        return xloc,yloc,xloc+w,yloc+h
        
    def locateCenterOnScreen(self, image, matchvalue=0.8,region=None):
        if region != None:
            img2 = self.imageArea(region[0],region[1],region[2],region[3])
        if region == None:
            img2 = self.screenshot()
        img1 = cv2.imread(image)
        
        img1 = cv2.cvtColor(img1,cv2.COLOR_RGB2RGBA)
        img2 = cv2.cvtColor(img2,cv2.COLOR_RGB2RGBA)

        result = cv2.matchTemplate(img1,img2,cv2.TM_CCOEFF_NORMED)

        matchvalue = matchvalue
        
        w,h = np.array(img1).shape[1], np.array(img1).shape[0]
        y,x = np.where(result >= matchvalue)

        if len(x) > 0:
            for (xloc, yloc) in zip(x,y):
                cv2.rectangle(img2,(xloc,yloc),(xloc+w,yloc+h),(0,255,255),2)
            sonuc = xloc,yloc,w,h
            sonuc =xloc+(w/2), yloc+(h/2)
            sonuc = int(sonuc[0]),int(sonuc[1])
            del img1,img2,result,matchvalue,w,h,y,x
            return sonuc
        else:
            del img1,img2,result,matchvalue,w,h,y,x
            return None

    def matchTemplateImage(self,image, matchvalue=0.8,region=None):
        if region != None:
            img2 = self.imageArea(region[0],region[1],region[2],region[3])
        if region == None:
            img2 = self.screenshot()
        img1 = cv2.imread(image)
        
        img1 = cv2.cvtColor(img1,cv2.COLOR_RGB2RGBA)
        img2 = cv2.cvtColor(img2,cv2.COLOR_RGB2RGBA)

        result = cv2.matchTemplate(img1,img2,cv2.TM_CCOEFF_NORMED)

        matchvalue = matchvalue
        
        w,h = np.array(img1).shape[1], np.array(img1).shape[0]
        y,x = np.where(result >= matchvalue)

        if len(x) > 0:
            del x,y,w,h,img1,img2,result,matchvalue
            return True
        else:
            return None
        
    def ImgBGcolorDetection(self,RGB1,RGB2):
        img = self.screenshot()
        img = np.array(img)
        
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        
        RGB1.reverse()
        RGB2.reverse()

        RGB1 = np.array(RGB1)
        RGB2 = np.array(RGB2)

        result = cv2.inRange(img, RGB1, RGB2) 
        
        resultral = cv2.bitwise_or(img,img,mask=result) 
        
        return resultral
        
    def imageArea(self,x0,y0,x1,y1):
        img = img = self.screenshot()
        img = np.array(img)
        w, h = img.shape[1], img.shape[0]
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = img[y0:y1,x0:x1]
        del w,h
        return img
        
    def findStone(self,image,matchvalue=0.5,debug_mode=None):
        img1 = cv2.imread(image,cv2.IMREAD_UNCHANGED)
        img2 = self.screenshot()
        
        img1_w = img1.shape[1]
        img1_h = img1.shape[0]
        
        method = cv2.TM_CCOEFF_NORMED
        
        result = cv2.matchTemplate(img1,img2,method)

        matchvalue = matchvalue
        
        locations = np.where(result >= matchvalue)
        locations = list(zip(*locations[::-1]))
        
        rectangles = []
        for loc in locations:
            rect = [int(loc[0]),int(loc[1]), img1_w, img1_h]
            rectangles.append(rect)
        print(rectangles)
        rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.5)
        points = []
        if len(rectangles):
            print('Found needle.')

            line_color = (0, 255, 0)
            line_type = cv2.LINE_4
            marker_color = (255, 0, 255)
            marker_type = cv2.MARKER_CROSS

            for (x, y, w, h) in rectangles:

                center_x = x + int(w/2)
                center_y = y + int(h/2)
                points.append((center_x, center_y))
                if debug_mode == 'rectangles':
                    top_left = (x, y)
                    bottom_right = (x + w, y + h)
                    cv2.rectangle(img2, top_left, bottom_right, color=line_color, 
                                 lineType=line_type, thickness=2)
                elif debug_mode == 'points':
                    cv2.drawMarker(img2, (center_x, center_y), 
                                  color=marker_color, markerType=marker_type, 
                                  markerSize=40, thickness=2)
        return points
    
    def AllLocateOnScreen(self, image, matchvalue=0.8,region=None):
        if region != None:
            img2 = self.imageArea(region[0],region[1],region[2],region[3])
        if region == None:
            img2 = self.screenshot()
        middle = (region[0]+region[2])/2,(region[1]+region[3])/2
        img1 = cv2.imread(image)
        
        img1 = cv2.cvtColor(img1,cv2.COLOR_RGB2RGBA)
        img2 = cv2.cvtColor(img2,cv2.COLOR_RGB2RGBA)

        result = cv2.matchTemplate(img1,img2,cv2.TM_CCOEFF_NORMED)

        matchvalue = matchvalue
        
        w,h = np.array(img1).shape[1], np.array(img1).shape[0]
        y,x = np.where(result >= matchvalue)
        
        coords = []
        if len(x) > 0:
            for (xloc, yloc) in zip(x, y):
                coords.append((int(xloc+(w/2)), int(yloc+(h/2))))
            del middle,img1,img2,result,matchvalue,w,h,y,image,region
            return coords
        else:
            del middle,img1,img2,result,matchvalue,w,h,y,image,region
            return None
    
    
    
class PyBotWin32:
    def __init__(self,hwnd):
        self.hwnd = hwnd

    def click_pg(self, x,y,left, top):
        coordinates = (y << 16) | x
        win32api.SetCursorPos((left+x, top+y))
        time.sleep(0.1)
        win32gui.PostMessage(self.hwnd, win32con.WM_LBUTTONDOWN ,win32con.MK_LBUTTON , coordinates)
        win32gui.PostMessage(self.hwnd, win32con.WM_LBUTTONUP ,0 ,coordinates)

    def click(self,x,y,left,top):
        set_cursor=win32api.MAKELONG(x,y)
        win32gui.SendMessage(self.hwnd, win32con.WM_MOUSEMOVE, set_cursor)
        win32gui.SendMessage(self.hwnd, win32con.WM_LBUTTONDOWN,win32con.MK_LBUTTON,set_cursor)
        win32gui.SendMessage(self.hwnd, win32con.WM_LBUTTONUP,win32con.MKF_LEFTBUTTONSEL,set_cursor)

    def bagirma(self, key):
        win32gui.SendMessage(self.hwnd,win32con.WM_CHAR, ord("!"))
        win32api.SendMessage(self.hwnd,win32con.WM_KEYDOWN, win32con.VK_RETURN, int('0x1C0001',0))
        win32api.SendMessage(self.hwnd,win32con.WM_KEYUP, win32con.VK_RETURN, int('0xC0000001',0))
        for i in key:
            win32gui.PostMessage(self.hwnd,win32con.WM_CHAR, ord(i))
            win32api.PostMessage(self.hwnd,win32con.WM_KEYDOWN, win32con.VK_RETURN, int('0x1C0001',0))
            win32api.PostMessage(self.hwnd,win32con.WM_KEYUP, win32con.VK_RETURN, int('0xC0000001',0))
            time.sleep(0.1)
        press_Enter()

    def writeWord(self,key):
        for i in key:
            win32gui.PostMessage(self.hwnd,win32con.WM_CHAR, ord(i))
            time.sleep(0.1)

    def press_Key(self,key):
        win32api.PostMessage(self.hwnd,win32con.WM_CHAR , ord(key),0)

    def press_Space(self):
        win32api.PostMessage(self.hwnd, win32con.WM_SYSKEYDOWN , 0x73, 0)
        win32api.PostMessage(self.hwnd, win32con.WM_SYSKEYUP, 0x73, 0)
        
    def press_Enter(self):
        win32gui.PostMessage(self.hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, int('0x1C0001',0))
        win32gui.PostMessage(self.hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, int('0xC0000001',0))

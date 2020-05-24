import cv2
import pyautogui
import numpy as np
import requests
import io
import json
# import screenshot
import tkinter
import os

top = tkinter.Tk()

def main():
    file_path = "txt/"
# To take screenshot

    add_path = "screenshot/"
    myScreenshot = pyautogui.screenshot()
    img_path = os.path.join(add_path,"image"+".png")
    myScreenshot.save(img_path)
#to read screenshot
    img = cv2.imread(img_path)

    url_api = "https://api.ocr.space/parse/image"

    _ , compressedimage = cv2.imencode(".png", img, [1, 90])
    file_bytes = io.BytesIO(compressedimage)

    result = requests.post(url_api,
        files = {img_path:file_bytes},
        data = {"apikey":"<API_KEY>", #generate your api key from https://api.ocr.space because i don't want to make my api key public
                "isTable":True,
                "OCREngine":2},
                )

    result = result.content.decode()
    result = json.loads(result)
    text_detected = result.get("ParsedResults")[0].get("ParsedText")
    # print(text_detected)
    count=1
    while count:
            if os.path.exists(os.path.join(file_path,"output"+str(count)+".txt")):
                count+=1
            else:
                txt_path = os.path.join(file_path,"output"+str(count)+".txt")
                break


    file1 = open(txt_path, "a+")
    # #
    # #     # providing the name of the image
    file1.write(img_path+"\n")
    # #
    # #     # providing the content in the image
    file1.write(text_detected+"\n")
    file1.close()

#     cv2.imshow('img', img)
# # # cv2.imshow('Image',img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    os.remove(img_path)


if __name__ == '__main__':

    b = tkinter.Button(top, text = "Take Screenshot",padx = 5, pady = 5, command = main)
    b.pack()
    top.mainloop()

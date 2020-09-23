#[todo1] 내가 만든 모듈 임포트하기

import cv2

# overlay function
def overlay_transparent(background_img, img_to_overlay_t, x, y, overlay_size=None):
  bg_img = background_img.copy()
  if bg_img.shape[2] == 3:
    bg_img = cv2.cvtColor(bg_img, cv2.COLOR_BGR2BGRA)

  if overlay_size is not None:
    img_to_overlay_t = cv2.resize(img_to_overlay_t.copy(), overlay_size)

  b, g, r, a = cv2.split(img_to_overlay_t)
  mask = cv2.medianBlur(a, 5)

  h, w, _ = img_to_overlay_t.shape
  roi = bg_img[int(y-h/2):int(y+h/2), int(x-w/2):int(x+w/2)]

  img1_bg = cv2.bitwise_and(roi.copy(), roi.copy(), mask=cv2.bitwise_not(mask))
  img2_fg = cv2.bitwise_and(img_to_overlay_t, img_to_overlay_t, mask=mask)

  bg_img[int(y-h/2):int(y+h/2), int(x-w/2):int(x+w/2)] = cv2.add(img1_bg, img2_fg)
  bg_img = cv2.cvtColor(bg_img, cv2.COLOR_BGRA2BGR)

  return bg_img

#[todo2] 테스트용 이미지 준비 예) happy6.jpg
img = cv2.imread('happy6.jpg')
#[todo3] 배경이 투명한 이미지 준비 예) mask.png
overlay = cv2.imread('mask.png', cv2.IMREAD_UNCHANGED)
#[todo4] 내가 만든 함수이용하여 얼굴인식정보를 임포트하기
data =  

for i in data['faces']:
    if i['landmark']==None:
        continue
    #마스크가 있을 수 있는 영역
    lipsize = i['landmark']['rightMouth']['x']-i['landmark']['leftMouth']['x'] 
    lipcenterx = i['landmark']['leftMouth']['x']+ lipsize//2
    lipcentery = i['landmark']['rightMouth']['y']
    mask_width = i['roi']['width']+i['roi']['width']//4
    mask_height = int(i['roi']['height']*0.7)

    x1 = i['roi']['x']
    y1 = i['roi']['y']
    x2 = x1 + i['roi']['width']
    y2 = y1 + i['roi']['height']  

    img = overlay_transparent(img, overlay, lipcenterx, lipcentery, overlay_size=(mask_width, mask_height))
    
cv2.imshow('output', img)
cv2.waitKey(0)

'''

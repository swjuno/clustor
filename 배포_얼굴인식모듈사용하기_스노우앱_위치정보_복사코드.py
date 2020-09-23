# 스노우앱
# 오버레이되는 이미지의 위치 정하기 (얼굴영역에 상대적으로)

    #[1]가면를 씌운다면 
    mask_width = int(i['roi']['width']*1.5) #얼굴영역의 너비보다 조금더(150%) 넓게 
    mask_height = int(i['roi']['height']*1.2) #얼굴영역의 높이의 120% 정도

    x1 = i['roi']['x']
    y1 = i['roi']['y']
    x2 = x1 + i['roi']['width']
    y2 = y1 + i['roi']['height']
    lipcenterx = x1 + i['roi']['width']//2 #얼굴영역의 중간(x지점)
    lipcentery = y1 + i['roi']['height']//2 #얼굴영역의 중간(y지점)

#--------------------------------------------------------------

    #[2]안경을 씌운다면
    mask_width = int(i['roi']['width']*1.25) #얼굴영역의 너비보다 조금더(40%) 넓게 
    mask_height = int(i['roi']['height']*0.6) #얼굴영역의 높이의 60% 정도

    x1 = i['roi']['x']
    y1 = i['roi']['y']
    x2 = x1 + i['roi']['width']
    y2 = y1 + i['roi']['height']
    lipcenterx = x1 + i['roi']['width']//2 #얼굴영역의 중간(x지점)
    lipcentery = y1 + int(i['roi']['height']*0.25) #얼굴영역시작 + 얼굴높이의 1/4 지점(y지점)
    
#--------------------------------------------------------------

    #[3] 모자를 쓴다면 
    mask_width = int(i['roi']['width']*1.5) #얼굴영역의 너비보다 조금더(150%) 넓게 
    mask_height = int(i['roi']['height']*0.75) #얼굴영역의 높이의 75% 정도

    x1 = i['roi']['x']
    y1 = i['roi']['y']
    x2 = x1 + i['roi']['width']
    y2 = y1 + i['roi']['height']
    lipcenterx = x1 + i['roi']['width']//2 #얼굴영역의 중간(x지점)
    lipcentery = y1 - i['roi']['height']//2 #얼굴영역의 위쪽(y지점) - 높이의 1/2만큼 위


#--------------------------------------------------------------
    #[4] 마스크를 씌운다면 
    mask_width = i['roi']['width']+ i['roi']['width']//4 #얼굴영역의 너비보다 조금더(40%) 넓게 
    mask_height = int(i['roi']['height']*0.7) #얼굴영역의 높이의 70% 정도

    x1 = i['roi']['x']
    y1 = i['roi']['y']
    x2 = x1 + i['roi']['width']
    y2 = y1 + i['roi']['height']
    lipcenterx = x1 + i['roi']['width']//2 #얼굴영역의 중간(x지점)
    lipcentery = y1 + int(i['roi']['height']*0.75) #얼굴영역시작 + 얼굴높이의 3/4 지점(y지점)    
    

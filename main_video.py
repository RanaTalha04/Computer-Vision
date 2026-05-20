import cv2

# ### READING VIDEO

# vid_capture = cv2.VideoCapture('data/Video1.mp4')
vid_capture = cv2.VideoCapture(0)

if vid_capture.isOpened() == False:
    print("Error Opening Video File")
else:
    
    fps = int(vid_capture.get(cv2.CAP_PROP_FPS))
    print(f"FPS: {fps}, Frame per second")
    
    frame_count = int(vid_capture.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Frame count: {frame_count}")
    
while(vid_capture.isOpened()):
    ret, frame = vid_capture.read()
    
    if ret:
        cv2.imshow('Video captured',frame)
        k = cv2.waitKey(1)
        
        if k == 113:
            break
    else:
        break
    
vid_capture.release()
cv2.destroyAllWindows()    


#### WRITING VIDEO


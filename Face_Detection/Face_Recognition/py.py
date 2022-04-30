from sre_constants import SUCCESS
import cv2
import numpy as np

#cap=cv2.VideoCapture()

#img =np.zeros((512,512,3))
#img[200:300,100:300]=0,255,0
#cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),2)
#cv2.rectangle(img,(0,0),(100,350),(0,0,255),3)
#cv2.circle(img,(300,250),100,(255,0,0),10)
#cv2.putText(img,"CHINTUKLA PAGAL HAI",(0,500),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
#cv2.imshow("zeroes",img)
#cv2.waitKey(0)


img=cv2.imread("C:\\Users\\DHRUV SAINI\\Dropbox\\PC\\Downloads\\cards.jpg")

width,height = 250,350
pt1=np.float32([[674,183],[841,10],[1104,406],[1199,189]])
pt2=np.float32([[254,211],[552,155],[706,490],[380,568]])
pt= np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix1 =cv2.getPerspectiveTransform(pt1,pt)
matrix2 = cv2.getPerspectiveTransform(pt2,pt)
imgoutput = cv2.warpPerspective(img,matrix1,(width,height))
imgoutput2 = cv2.warpPerspective(img,matrix2,(width,height))
cv2.imshow("image",img)
cv2.imshow("output",imgoutput)
cv2.imshow("output2",imgoutput2)
cv2.waitKey(0)

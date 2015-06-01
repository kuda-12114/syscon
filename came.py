import cv2

def main():
  cap = cv2.VideoCapture(0)
  cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
  #cascade = cv2.CascadeClassifier("lbpcascade_animeface.xml")
  i=0

  while(1):
    i+=1
    ret, im = cap.read()
    face=cascade.detectMultiScale(im, 1.1, 3)
    if(i==3):
      for (x, y, w, h) in face:
        cv2.rectangle(im, (x, y),(x + w, y + h),(0, 50, 255), 3)
      i=0
    cv2.imshow("Camera Test", im)
    if cv2.waitKey(10) > 0:
      cap.release()
      cv2.destroyAllWindows
      break

  cap.release()
  cv2.destroyAllWindows()

if __name__ == '__main__':
  main()
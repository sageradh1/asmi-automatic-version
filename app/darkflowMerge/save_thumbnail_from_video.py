# from app import app
# from app.utils.dataUtilsCode import uniqueClassSetAndDict,uniqueDictonairies,arrangeNnumberOfDictionary,returnList,writeListAsAJsonFile

import cv2
# from darkflow.net.build import TFNet
import numpy as np
import time
from datetime import datetime
import os
basedir = os.path.abspath(os.path.dirname(__file__))



# capture = cv2.VideoCapture(app.config["VIDEO_UPLOADS_FOLDER"]+"/"+"20200420140600Intex Inflatable One Person Chair Sofa Bed in Action - Outdoorleisuredirect.mp4")

#  #   capture = cv2.VideoCapture(_videoname)

# colors = [tuple(255 * np.random.rand(3)) for i in range(5)]

# framecounter =0

# listOfResultsWithTuple = []
# listOfResultsWithoutTuple = []

# classSet = set()
# classDict= dict()
# confidenceDict = dict()
# numberOfTimesEmergedDict = dict()
# averageConfidenceDict= dict()
# FrameDict = dict()
# originalFrameArray=[]
# newframeArray=[]
# generatedVideoFilename=''
# generatedVideoStartingTime=datetime.utcnow()
# fps = 20

# (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
 
 
# if int(major_ver)  < 3 :
#     fps = capture.get(cv2.cv.CV_CAP_PROP_FPS)
# else :
#     fps = capture.get(cv2.CAP_PROP_FPS)

# print("The video fps is : {:f}".format(fps))
# print("Processing each frame ..... ")

# while (capture.isOpened()):
#     stime = time.time()
#     ret, frame = capture.read()

#     originalFrame = frame

#     if ret:
#         framecounter=framecounter+1
#         frame_msec = capture.get(cv2.CAP_PROP_POS_MSEC)
#         print("Frame number : {:d} TimeStamp: {:f}".format(framecounter,frame_msec))
#         #print("Frame No \t Objects Count \t Object Label \t Confidence ")        
#         results = tfnet.return_predict(frame)
#         # print("Results : ",results)

#         listOfResultsWithTuple.append((results,frame_msec))
#         listOfResultsWithoutTuple.append(results)
#         #print(results)

#         if framecounter==30:
#             thumb = image_to_thumbs(frame)
#             # os.makedirs(app.config['THUMBNAIL_FOR_UPLOADED_VIDEO_FOLDER'])
#             for k, v in thumb.items():
#                 print("In 30th frame , the value of k is {}".format(k))
#                 cv2.imwrite(app.config['THUMBNAIL_FOR_UPLOADED_VIDEO_FOLDER']+'/'+str(k)+'.png' , v)


#         for eachObject in results:

#             tl = (eachObject['topleft']['x'],eachObject['topleft']['y'])
#             br = (eachObject['bottomright']['x'],eachObject['bottomright']['y'])

#             rectFrameWidth = br[0]-tl[0]
#             rectFrameHeight = br[1]-tl[1]

#             iconWidth = int (0.2*rectFrameWidth)
#             iconHeight = int (0.2*rectFrameHeight)

#             # iconWidth = 40
#             # iconHeight = 40

#             if iconWidth==0 or iconHeight==0:
#                 continue
#             icon_img = cv2.imread(basedir +"/icon6.png")
#             icon_img1= cv2.resize(icon_img, (iconWidth,iconHeight))
            

#             x_offset=br[0]-iconWidth
#             y_offset=int((tl[1]+br[1])/2)-iconHeight
            
#             frame[y_offset:y_offset+icon_img1.shape[0], x_offset:x_offset+icon_img1.shape[1]] = icon_img1

#         newframeArray.append(frame)
#         originalFrameArray.append(originalFrame)            
        
#     else:
#         capture.release()
#         cv2.destroyAllWindows()
#         print("listOfResultsWithTuple")
#         print(listOfResultsWithTuple)
#         print("\nlistOfResultsWithoutTuple")
#         print(listOfResultsWithoutTuple)


def run_example():
  """Extract frames from the video and creates thumbnails for one of each"""
  # Extract frames from video
  print("Extract frames from video")
  frames = video_to_frames('/home/sagar/workingDir/asmi-automatic-version/app/static/video/uploaded/20200420140600Intex Inflatable One Person Chair Sofa Bed in Action - Outdoorleisuredirect.mp4')

  # Generate and save thumbs
  print("Generate and save thumbs")
  for i in range(len(frames)):
    thumb = image_to_thumbs(frames[i])
    os.makedirs('frames/%d' % i)
    for k, v in thumb.items():
      cv2.imwrite('frames/%d/%s.png' % (i, k), v)

def video_to_frames(video_filename):
    """Extract frames from video"""
    cap = cv2.VideoCapture(video_filename)
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    frames = []
    if cap.isOpened() and video_length > 0:
        frame_ids = [0]
        if video_length >= 4:
            frame_ids = [0,
                         round(video_length * 0.25),
                         round(video_length * 0.5),
                         round(video_length * 0.75),
                         video_length - 1]
        count = 0
        success, image = cap.read()
        while success:
            if count in frame_ids:
                frames.append(image)
            success, image = cap.read()
            count += 1
    return frames

def image_to_thumbs(img):
    """Create thumbs from image"""
    height, width, channels = img.shape
    thumbs = {"original": img}
    sizes = [640, 320, 160]
    for size in sizes:
        if (width >= size):
            r = (size + 0.0) / width
            max_size = (size, int(height * r))
            thumbs[str(size)] = cv2.resize(img, max_size, interpolation=cv2.INTER_AREA)
    return thumbs

if __name__ == '__main__':
    run_example()
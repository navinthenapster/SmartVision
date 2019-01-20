import sys

import dlib

detector = dlib.get_frontal_face_detector()
#win = dlib.image_window()

def faceDetect(images):
	results= []
	for f in images:
	    #print("Processing file: {}".format(f))
	    img = dlib.load_rgb_image(f)
	    # The 1 in the second argument indicates that we should upsample the image
	    # 1 time.  This will make everything bigger and allow us to detect more
	    # faces.
	    dets, scores, idx = detector.run(img, 1, -1)
	    image={}
	    #print("Number of faces detected: {}".format(len(dets)))
	    image["count"]=len(dets)
	    faces=[]
	    for i, d in enumerate(dets): 
		face={}
		#print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(i, d.left(), d.top(), d.right(), d.bottom()))
		face["position"]=str(d)
		face["score"]=scores[i]
		face["face_type"]=int(idx[i])
		faces.append(face)
	    
	    image["faces"]=faces
	    results.append(image)
	    #win.clear_overlay()
	    #win.set_image(img)
	    #win.add_overlay(dets)
	    #dlib.hit_enter_to_continue()
	    return results
	
if __name__ =="__main__":
	res=faceDetect(sys.argv[1:])
	print res

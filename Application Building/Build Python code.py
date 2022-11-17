#!/usr/bin/env python
# coding: utf-8

# In[ ]:


@app.route('/predict',methods=['GET','POST'])
def upload(): 
if request.method == "POST":
f=request.files['file']
basepath-os.path.dirname(_file_)storing the file directory
filepath-os.path.join(basepath, "uploads", f.filename) #storing the file
f.save(filepath)#saving the file


#Loading the saved model
print("[INFO] Loading model...")
model= pickle.loads (open('parkinson.pkt', "rb").read())
# pre-process the image in the same manner we did earlier
image cv2.imread(filepath)
output =image.copy()
#load the input image, convert it to grayscale, and resize 
output = cv2.resize(output, (128, 128))
image cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.resize(image, (200, 200))
image = cv2.threshold (image, 0, 255,
cv2.THRESH BINARY INV | cv2.THRESH_OTSU)[1]


#quantify the image and make predictions based on the extracted
# features using the last trained Random Forest
features= feature.hog(image, orientations=9,
pixels_per_cell-(10, 10), cells_per_block-(2, 2),
transform_sqrt=True, block_norm="L1")
preds = model.predict([features])
print(preds)
1s=["healthy", "parkinson"]
result =Is[preds[0]]



# draw the colored class label on the output image and add it
# the set of output images
color= (0, 255, 0) if result == "healthy" else (0, 0, 255)
cv2.putText(output,result, (3, 20), cv2.FONT HERSHEY SIMPLEX,0.5,color,2)
cv2.imshow("Output", output)
cv2.waitKey(0)
return result
return None


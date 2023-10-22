from flask import Flask, render_template, request, redirect, jsonify
from PIL import Image
import os 
# import cartoon
import numpy as np
import os
import cv2
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/imagedisplay')
def imagedisplay():
    linkOriginal = request.args.get('link1')
    linkConverted = request.args.get('link2')    
    return render_template('display.html', source1=linkOriginal, source2 = linkConverted)

@app.route('/upload', methods=['POST'])
def upload():
    k = int(request.form['k']) #color quantization parameter
    blur = request.form['blur']
    print (blur)
    file = request.files['image']
    print (type(blur))
    img = Image.open(file)
    fileName = file.filename
    file_path = os.path.join("static", "images", fileName)
    img.save(file_path)
    print (file_path)
    img=cv2.imread(file_path)
    if img is None:
        print("Error: Image not read correctly")
        return "Error: Image not read correctly"
    line_size = 7  #n x n pixels to consider surrounding a pixel
    blur_value = 9  #how blurry the black and white image looks, lower blur_value means easier to find the edges of the image
    edges = edge_mask(img, line_size, blur_value)
    cv2.imwrite("extras/sampleEdge.png", edges)
    # unique_colors = count_unique_colors(filename)  #NUMBER OF COLORS IN THE IMAGE
    newimg = color_quantization(img,k)  #newimg is the color-quantized image
    cv2.imwrite("extras/cartoonImage.png",newimg)
    blurred = cv2.bilateralFilter(newimg, d=4, sigmaColor=100,sigmaSpace=100)
    cv2.imwrite("extras/blurredCartoonImage.png", blurred)
    if blur=="false": #if you want to skip blurring the final image
     blurred = newimg   
    cartoon = cv2.bitwise_and(blurred, blurred, mask=edges)
    cv2.imwrite('static/images/' + "CAR_" + fileName,cartoon)
    url_converted = f'/static/images/{"CAR_" + fileName}'
    url_original = f'/static/images/{fileName}'
    response = {'message': 'File uploaded successfully', 'link_original':url_original, 'link_converted':url_converted}
    return jsonify(response)

def edge_mask(img, line_size, blur_value):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #convert to greyscale
    cv2.imwrite("extras/sampleGray.png", gray)
    gray_blur = cv2.medianBlur(gray, blur_value)  # apply a blur to the greyscale image
    cv2.imwrite("extras/sampleBlur.png",gray_blur)
    edges = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, line_size, blur_value)
    #Say line_size = 5, now take each pixel, take average of the 5x5 pixels surrounding that pixel, subtract the pixel value and the blur value, assign this value to this pixel
    cv2.imwrite("extras/sampleEdges.png",edges)
    return edges

def color_quantization(img, k):
# Transform the image
  data = np.float32(img).reshape((-1, 3))
#So in the case of a 640x480 pixels image, the first 640 rows of data correspond to the first row of the image, the next 640 rows correspond to the second row of the image, and so on, until the 307,200th row corresponds to the last pixel in the bottom-right corner of the image.
# Determine criteria
  criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)

# Implementing K-Means
  ret, label, center = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
  
  #ret contains the sums of squares between each cluster and its data points
  #label assigns each pixel to a cluster
  #center contains the pixels of each cluster center

  center = np.uint8(center)  #just to convert to integers
  
  result = center[label.flatten()]  #FIRST: label.flatten() converts array to 1d, like [2 2 2 ... 4 4 4]
  # THEN: map each pixel to the color of the centroid to which it belongs

  result = result.reshape(img.shape) #FIRST: img.shape() returns the dimensions of the image
  #THEN: the pixels in result are shaped according to img.shape() 
  return result



if __name__ == "__main__":
    app.run(debug=True)
## Working

### Installations

OpenCV: "pip install opencv-python"
cvlib: "pip install cvlib"
Keras: "https://pypi.org/project/Keras/"
email: "pip install email-to"
ibm_watson: "pip install --upgrade "watson-developer-cloud>=2.4.1""
json: "json" or "jsonlib"
tensorflow: 'pip install tensorflow'
Files from OpenCV located in the same working folder: "haarcascade_frontalface_alt.xml" and "haarcascade_frontalface_default.xml"

images datasets: https://lionbridge.ai/datasets/12-free-retail-image-datasets-for-computer-vision/

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

step 1 define tools:

Fisrts of all we should know what tools are we going to use and wich inputs should have those tools.
It´s not a easy proces, there a lot of tools but part of succes is to select the right tool.

In this proeject for face recognition is used VisualRecognitionV3, a library from IBM wattson
For things recognition in phictures is used cvlib a library based on yolov3
The last tool is a fruit recognizer trained with a keras CNN 

Image captures are used because computer resources but also streeming video can be used with powerfull equipments.
My computer resources intel i5 7th gen, nvidia 1050 gtx, and 8gb ram.

step 2 get data:

IBM watson model: 14 people with 14 photos (250px,250px,3RGB) from each one.

cvlib: cvlib identifies by itself 80 item types.

keras CNN: Fruists images (100px,100px,3RGB)

Step 3 recognizers:


step 4 make tests:


step 5 join toghether all subprograms:


step 6 ready to production:


Comming soon...
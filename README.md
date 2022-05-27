# Face-recognition-attendence-system-software
# ABSTRACT
There is no reason why a vital event in the educational sector, such as attendance, should be done in the old boring traditional method in this day of rapidly rising innovative technologies.
For both students and class teachers, an attendance monitoring system will save a significant amount of time and energy.
For both students and class teachers, an attendance monitoring system will save a significant amount of time and energy.
The face recognition algorithm will keep track of attendance by separating the students faces from the rest of the items and labelling them as present. The system will be pre-loaded with photographs of all of the students, and the algorithm will use this data to recognise those who are present and match their features to previously saved images of them.
# INTRODUCTION
The goal of the face recognition attendance monitoring system is to simplify the attendance procedure, which takes a lot of time and effort. It is a convenient and simple method for students and teachers. The technology will take pictures of the children and use a face recognition algorithm to fill out the attendance form. This method, the class teacher's attendance will be recorded without having to spend time on traditional attendance recording.
One of the usual security operations is the identification process to determine the presence of a person in a room or place. Every person who enters a room or building must first go through a series of authentication procedures, so that these details can later be utilised to monitor every single activity in the room for security purposes. The authentication method for detecting the presence of a person in a room or building is still in flux. The procedure differs depending on whether a name and signature are written in the attendance list, an identity card is used, or biometric authentication technologies such as a fingerprint or face scanner are used.
# BASIC FLOWCHART DIAGRAM
![image](https://user-images.githubusercontent.com/98527045/170731584-137d3182-fb68-4370-907f-f88acfc47135.png)
![image](https://user-images.githubusercontent.com/98527045/170731726-0d65e70d-9cd0-491b-8ac6-5abc27e8563e.png)
# SYSTEM DESIGN
# HAAR CASCADE ALGORITHM
Haar-like properties are the foundation for Haar classifier object detection. Rather of using a pixel's intensity values, these features employ the difference in contrast values between consecutive rectangular groupings of pixels. To establish relative light and dark areas, the contrast variances between pixel groups are used. A Haar-like feature is formed by two or three neighbouring groups with a relative contrast variance. To detect an image, Haar-like features are used, as seen in the figure. By adjusting the size of the pixel group under investigation, Haar characteristics can be easily scaled. This makes it possible to employ features to detect objects of varied sizes. Only the sub-images with the highest probability are assessed for all Haar-features that distinguish an object thanks to the classifiers cascade. It also enables for the adjustment of a classifier's accuracy. By reducing the number of phases, one can improve both the false alarm rate and the positive hit rate. This also holds true in reverse. With only 100 simple traits, Viola and Jones were able to detect a human face with a 90 percent accuracy rate. Human facial features such as the lips, eyes, and nose must be detected. The OpenCV library, which includes an implementation of Haar classifier detection and training, is designed to be used in conjunction with applications in the fields of HCI, robotics, biometrics, image processing, and other areas where visualisation is crucial. As a result, the system will detect the person's face in the video with the help of this algorithm. As a result of the detection process, the person's face is marked with a green square. As soon as a face is spotted, the user can pause the video and enter information about the individual who was detected, such as their name, residence, profession, and criminal history, if any. If the individual detected has a criminal past, it can be classified as a suspect. The technology provides a check box option for the user to select whether the person is a suspect or not. The initial module's operation is seen here, in which a sample video is browsed and a face is detected
![image](https://user-images.githubusercontent.com/98527045/170731829-c8740156-7b6c-4dd8-8df7-57b30bff9c34.png)
# Local Binary Pattern Histogram (LBPH):
Local Binary Pattern (LBP) is a basic yet effective texture operator that labels pixels in an image by thresholding each pixel's vicinity and treating the result as a binary number.

The LBPH's first computational step is to build an intermediate image that better describes the original image by highlighting the facial features. To accomplish so, the algorithm employs a sliding window idea based on the radius and neighbours parameters.

# Applying the LBP operation:
The LBPH's first computational step is to build an intermediate image that better describes the original image by highlighting the facial features. To accomplish so, the algorithm employs a sliding window idea based on the radius and neighbours parameters.
This method is depicted in the diagram below:
![image](https://user-images.githubusercontent.com/98527045/170731926-8dc7331e-2c91-4028-9d97-aada424a2d2d.png)
# Performing the face recognition
• The algorithm has already been trained at this point. Each image from the training dataset is represented by a different histogram. As a result, given an input image, we repeat the steps for this new image, resulting in a histogram that reflects the image.
• To identify the image that corresponds to the supplied image, simply compare two histograms and return the image with the closest histogram.
• To compare histograms (compute the distance between two histograms), we can use a variety of methods, such as Euclidean distance, chi-square, absolute value, and so on. We can utilise the Euclidean distance (which is well-known) in this case, which is calculated using the formula:
![image](https://user-images.githubusercontent.com/98527045/170731991-54215f49-84f5-4cb5-a296-6a0d8f74c3d6.png)
• As a result, the ID from the image with the closest histogram is the algorithm's output. The calculated distance, which can be used as a 'confidence' measurement, should also be returned by the algorithm. Note that despite the label 'confidence,' lower confidences are desirable because they indicate a closer distance between the two histograms.

•After that, we can use a threshold and the 'confidence' to determine whether the algorithm accurately detected the image. If the confidence is less than the stated threshold, we can assume that the algorithm has effectively recognised it.
# TRAINING THE ALGORITHM:
We must first train the algorithm. To accomplish so, we'll need a dataset containing the faces of the persons we're trying to recognise. We must also assign each image an ID (which might be a number or a person's name) so that the algorithm can recognise an input image and provide you with an output.
The ID for all images of the same individual must be the same. Let's look at the LBPH computational steps now that the training set has been built.
# APPLYING LBH OPERATIONS
The LBPH's first computational step is to build an intermediate image that better describes the original image by highlighting the facial features. To accomplish so, the algorithm employs a sliding window idea based on the radius and neighbours parameters
# IMPORTANT POINTS 
•	Assume we have a grayscale image of a face.

•	We can get a 3x3 pixel window of a portion of this image.

•	It can alternatively be represented as a 3x3 matrix with each pixel's intensity (0255).

•	After that, we need to utilise the matrix's centre value as the threshold.

•	This value will be used to define the 8 neighbours' new values.
We create a new binary value for each neighbour of the core value (threshold). We used a 1 for numbers that were equal to or higher than the threshold, and a 0 for those that were lower.
![image](https://user-images.githubusercontent.com/98527045/170732198-d3f91d84-62e5-4046-b7fb-74b580c60828.png)
# EXTRACTING THE HISTOGRAM
Now, utilising the image created in the previous phase, we can divide it into numerous grids using the Grid X and Grid Y parameters, as seen in the accompanying image.
![image](https://user-images.githubusercontent.com/98527045/170732236-4f7899a6-8078-49d7-b369-1941409b3570.png)

We may extract the histogram of each region as follows using the image above:
• Because we're working with a grayscale image, each histogram (from each grid) will only have 256 places (0-255) to indicate each pixel intensity.
• After that, we must concatenate each histogram to make a new, larger histogram. In the case of 8x8 grids, the final histogram will have 8x8x256=16.384 places. The original image's attributes are represented by the final histogram.
There are no entries in the table of figures.
The algorithm has already been trained at this point. Each image from the training dataset is represented by a different histogram. As a result, given an input image, we repeat the steps for this new image, resulting in a histogram that reflects the image.
So, all we have to do to identify the image that matches the input image is compare two histograms and return the image with the closest histogram.
To compare histograms (compute the distance between two histograms), we can use a variety of methods, such as euclidean distance, chi-square, absolute value, and so on. We can utilise the Euclidean distance (which is well-known) in this case, which is calculated using the formula:
![image](https://user-images.githubusercontent.com/98527045/170732276-768cc24e-8f3b-4081-96b3-ab88432bd4b1.png)
As a result, the ID from the image with the closest histogram is returned by the algorithm. The calculated distance, which can be used as a 'confidence' measurement, should also be returned by the algorithm. Don't be deceived by appearances.
• The name 'confidence' comes from the fact that lower confidences are desirable because they indicate a closer distance between the two histograms.

Then we can use a threshold and the 'confidence' to determine whether the algorithm accurately recognised the image. If the confidence is less than the stated threshold, we can assume that the algorithm has effectively recognised it.
![image](https://user-images.githubusercontent.com/98527045/170732326-53b30d1d-d4f0-44f2-977d-484a99761bd2.png)
# Advantages:
1. It is simple to operate.
2. It is a relatively quick method of recording attendance.
3. Is highly dependable, with an approximation of the user's output.
4. The most user-friendly interface.
5. Accuracy of up to 85% is possible.
# Conclusion: 
• The Attendance Management System, which was created using Machine Learning, achieves the system's goals. All bugs have been eliminated, and the system has achieved a stable condition. The system runs at a very high level of efficiency. The problem is solved by the system.
• The system can recognise and identify the face with an accuracy of 85 percent at a face distance of 40 cm from the camera with appropriate lighting, according to the requirement specification.

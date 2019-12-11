# Bake-Off 2
**The goal of this Bake Off was to integrate Human-Artificial Intelligence interaction.**
---
## Project Title: Explainable CamIoT
**CamIoT (camera-based Internet of Things device ) is the name of a research project under Prof. Chen. The detailed code and documentation of camIoT is not discussed and shared here as the project is currently at journel submission pending status (Hopefully it will be uploaded soon).**
---
## More about CamIoT first:

### Utilizing machine learning the wrist worn CamIoT lets users interact with home appliances by taking a picture of the appliance user's pointing at. 
#### CamIoT includes three main sections:

1. Triggering mechanism: The user would lift his arm from stationary state and point toward the object he likes to interact with. This gesture would tell CamIoT to start taking picture. 
2. Object Classification: Using a pretrained VGG-19 and by only taking 3 pictures (and data augmentation)from each appliance we train CamIoT's classification model.
3. Interact with appliances using the Index finger. 

---
## Now what is Explainale CamIoT:
In Explainale CamIoT we focused on section 1 and 3 of CamIoT. Our goal was to improve camIoT behavior in triggering and interacting with the index finger.


### Triggering Mechanism Improvement:
The triggering mechanism was developed using Decision Tree classification, training only on a single person. So to enhance the triggering performance. We developed a GUI that trains the users how to perform the triggering mechanism correctly. We applied Rule Extraction to give feedback to users. For training the gesture, we used acceleration data in x,y,z axes (Ax,AY,Az) using [MPU-6050](https://www.sparkfun.com/products/11028) IMU sensor. Our study showed each triggering gesture includes a max followed by a min in Ax and Ay axes. Calculating the min and max ranges, changes in velocities and proportional time stamps of where such points happened in training data we analyzed our users' performance. Our GUI would then turned those analysis into simple implicit feedbacks such as : "Seems like you started early, go a bit slower next time... ".After user learns the triggering gesture, we run another test this time in continous domain, this time user would move around the testing room while randomly performing the gesture. This stage was mainly to improve on the rate of false of positive labels. In this round an on-board LED used to provide feedback to users. The users' data are saved and used later on to improve the model overall performance. So far from three iterations of running the model on participants and retraining the model based on found feedbacks, we brought the false positive rate from ~50% to ~3%. 



### What is your proposed approach? Describe the planned system architecture, algorithms etc. Take as much space as needed, and include figures if necessary.
*** We are aiming to use to rule extraction in modeling the behavior of user performed triggering mechanism and give feedback in such way that user would improve his/her triggering action in later rounds.


For more information please refer to our mid-term presentation, which you may find here: [explainale CamIoT midter presentation](https://github.com/Amir-Omidfar/m209As/blob/master/bakeOff2/Bake%20off%202.pptx.pdf)


#### Things to keep in mind while training the server:
    1. Data file format should be.csv
    2. First row should be the titles, first row first column is "Class" and the remaining columns of the first row are xi,yi,zi i being from 1-42
    3. 

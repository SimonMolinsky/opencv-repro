# PROGRAM SETUP

## List of contents:
* Environment setup: Git and Conda
* Download repository
* Create conda environment
* Run and setup conda envioronment (and hints how to close it)
* Program: before the run
* Program: point selection phase
* Program: ROI selection phase
* Program: Output (ROI)
* Program: horizontal reprojection


### Environment setup

I assume that you're using Linux operating system, but if you are able to install conda and git on your Windows machine then it's not a problem! To use this repository you must either install Git agent and Conda open source package management system. 
- Conda installation process is descibed here: https://conda.io/projects/conda/en/latest/user-guide/install/linux.html
- Git installation process is described here: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git


### Download repository

1. To download this repository navigate through console to the folder where you want to put it (use *cd* command followed by the directory name to change directory and *ls* command to print a list of directories and files in the actual path in terminal; if you want to move to the parent directory then use command *cd ../*).
2. When you're in your desired folder write in the console:
> git clone https://github.com/szymon-datalions/opencv-repro.git
3. Move to the project folder:
> cd opencv-repro


### Create conda environment

1. To run program you need to install specific Python packages, especially OpenCV.
2. There are two ways to do it. The first way is to use .yml file and give conda opportunity to install everything automatically. The second, harder way is to do it by hand. We will explore the second way - I didn't put .yml file in the repository up to this moment.
3. Write in terminal:
> conda create --name opencv-env Python==3.7
4. Select *y* when asked.
5. Congratulations! You've created your first conda repo. Now it is time to fill it with the appriopriate Python packages. We need three libraries: _matplotlib_ used as a graphical interface of our application, _numpy_ used as the linear algebra library and the most important _OpenCV_ which is designed for image processing.


### Run and setup conda environment

1. To run your newly created environment write in the console:
> source activate opencv-env
2. You should see *(opencv-env)* in terminal before your directory path. It is a signal that you are now working in the special conda environment and if you install any Python packages they will not affect your system from this position.
3. To install all needed packages type in terminal (only if your environment is active! -> you should see *(opencv-env)* at the beginning of each line):
> conda install -c conda-forge opencv numpy matplotlib
4. Select *y* when asked.
5. If you don't see any errors then it is pleasure to invite you to the practical part of the tutorial :) But before that few hints:
- always close your environment when you end your work (type in terminal: *conda deactivate* or *source deactivate*),
- if you use keybord keys: *ctrl + c* in the terminal then you stop any process from the execution,
- if you use: *ctrl + d* then you stop any Python script.


### Program: before the run

1. Make sure that you're in the opencv-repro project folder. Type *ls* and if you see _main.py_ file then you're in!
2. Make sure that your conda environment is active. If not then type: *source activate opencv-env*


### Program: Point Selection Phase

1. Run program from terminal typing:
> python main.py
2. New window opens. You see your sample there:
![Sample Image](/tutorial_images/img1.png)
3. We must enclose the sample in ROI. To achieve this you must instruct program where the sample is placed and you need for it a set of points. If you use _left mouse double-click_ then you select a point. Select a group of points along the sample as in the image:
![Points](/tutorial_images/img2.png)
4. If you end your selection _click right button of the mouse_. You should see special entry in the terminal:
![Sample Image](/tutorial_images/img3.png)


### Program: ROI selection phase, Output (ROI) and horizontal reprojection

1. Use your _mouse scroll button_ to resize ROI to the desired dimension and use _right button_ to apply it:
![Sample Image](/tutorial_images/img4.png)
2. Close the window and look into the ROI selection before and after denoising by median filter:
![Sample Image](/tutorial_images/img5.png)
3. Close the windows and look into a final product of a projection:
![Sample Image](/tutorial_images/img6.png)
4. You may save it from the matplotlib window and use it for different purposes.

-----

Last comment: This is still a MVP phase. Program is not optimized from the UI/UX as well as with the reprojection functionality.
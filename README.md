# codemonks-devhack2-iitdharwad

Our project comprises of two important social measures going forward
1) Solar Panel Installation Detector
2) Rainwater Harvesting Installation Detector

We have used Canny Edge Detection, CNN, K-Means for the detection and analysis of the requirements in a particular area

So, basically we have two folders

i) Solar:

Why this project?

Lower monthly electric bills:
Solar is more affordable and accessible today because the cost of solar systems has dropped and a range of financing options can help you meet your goals. Whether you lease, take out a loan, or purchase a system, you may be able to start generating savings right away.
Solar can save you money by replacing electricity from the grid with solar electricity generated on your roof. The cost of solar plus any remaining electric bill amount may be lower than what it was before solar. 

An approx area of 12,000 sqft over a period of 15 years can save around 4 crore INR

It is used to detect the number of solar panels which can be installed on a particular sunroof which is selected upon by the user by giving a manual input in a search box. We have used the Google Maps API for getting the map image at 20th zoom level.
We have used:
Hough Transform
Watershed Segmentation
Pixel Wise Polygon filling

For the maps:

    The whole region is on top of the pyramid (zoom=0) covered by 256x256 pixels tile,every lower zoom level resolution is always divided by two.
    At every zoom level, there is Meter per pixel value which gives distance in meters according to the difference in pixel values.
    
ii) Rainwater Harvesting

Carrying forward the idea of solar panel detection, we first carried out an analysis taking Bengaluru area into consideration and also used the Google Maps Elevation API for finding out the elevation at a particular region over a period of 1km.
This allows us to find out the essential analysis requirement before carrying out this project.

We have used:
CNN
K-Means Clustering ( Analysis )
Computer Vision Models using openCV and Watershed Segmentation

We have also given a Dashboard for the analysis carried out after training the model.

The calculation for the Return of Investment depends upon electricity generation, number of members in the family and location. The location and annual rainfall of the particular area have been set for convenience at this level.

In order to start the project,

1) Navigate to codemonks-rainwater
2) run python app.py
3) Navigate to codemonks-solar
4) run python manage.py runserver --noreload --nothreading
5) Start the browser and you would be good to go!


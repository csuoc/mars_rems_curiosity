# MarsToday: evaluating Mars climate through REMS sensor onboard Curiosity Mars rover


A Mars rover is a motor vehicle designed to travel on the surface of Mars. Rovers have several advantages over stationary landers: they examine more territory, they can be directed to interesting features, they can place themselves in sunny positions to weather winter months, and they can advance the knowledge of how to perform very remote robotic vehicle control.

Curiosity landed in the crater Gale on planet Mars. The landing site coordinates are: 4.5895°S 137.4417°E. The location was named Bradbury Landing on 22 August 2012, in honor of science fiction author Ray Bradbury. Gale, an estimated 3.5 to 3.8 billion-year-old impact crater, is hypothesized to have first been gradually filled in by sediments; first water-deposited, and then wind-deposited, possibly until it was completely covered.

![](images/Gale_crater.jpg)

Curiosity has a lot of instruments onboard. One of them, REMS (Rover Environmental Monitoring Station) measures and provides daily and seasonal reports on atmospheric pressure, humidity, ultraviolet radiation at the Martian surface, air temperature, and ground temperature around the rover. REMS was develeoped in Spain by the Centro de Astrobología (CAB/CSIC-INTA) in collaboration with NASA and JPL-Caltech.

![](images/Installation.jpg)
REMS installation. Credit NASA/JPL-Caltech/CAB

The data contained in this project represents the weather conditions on Mars from Sol 1 (August 7, 2012 on Earth) to Sol 1895 (February 27, 2018 on Earth). Sol is equivalent to 1 Martian day (1 Martian day = 24h 40 min).

However, REMS does not take measurements continuously and it takes measurements at different times from one day to another. For different reasons (instrument maintenance, instrument calibration, instrument degradation, etc.), some or all of the magnitudes in this project were not be available.

# 1. Objective

The main questions I considered are the following:

- How is the weather on Mars?
- How it compares to its twin location on Earth?
- Is it possible to predict the weather with the missing data?
- BONUS: can I obtain pictures from Mars and complement the data?

# 2. Data acquisition

The base data was extracted from Kaggle, "Mars weather data" by Kannan.K.R. Source: https://www.kaggle.com/datasets/imkrkannan/mars-weather-data

The data was complemented with weather data from Papua New Guinea (twin location of Curiosity on Earth) avaialble on NOAA Global Surface Summary of the Day services, in the same range of dates as provided by Kannan.K.R. Source: https://www.ncei.noaa.gov/access/search/data-search/global-summary-of-the-day

Data prediction and current weather information were extracted using Selenium from the CAB-CSIC/INTA webpage. Source: http://cab.inta-csic.es/rems//

# 3. File contents

- src/ --> Contains the executable python files of the cleaning and visualization process. 
- images/ --> All the necessary pictures data/ --> Contains an edited version of the original dataframe 
- README --> What you are reading right now.

# 4. Data wrangling and cleaning


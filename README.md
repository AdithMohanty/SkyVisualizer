### README for Sky Observation and Plotting Code

This Python code provides functionality for analyzing and visualizing the positions of celestial objects (the Sun and Moon) from a specified geographical location over time. It uses libraries such as **NumPy**, **Matplotlib**, and **PyEphem** to compute and plot the azimuth and altitude of these objects, either for a single time instance or over a range of days or hours.

#### Key Features:
1. **Observer Location**: The code allows setting up an observer at a fixed location, defined by latitude and longitude. By default, the location is set to Campanile in California (latitude 37.871873, longitude -122.258347).

2. **Data Capture**: The code uses **PyEphem** to calculate the positions of celestial objects (the Sun and Moon) based on the observer's location and time.

3. **Visualizations**: 
   - **Polar Plot**: Displays the azimuth (angular direction) and altitude of objects in a circular format.
   - **Rectangular Plot**: Displays azimuth and altitude in a Cartesian format, providing another way to view the positions of the Sun and Moon.

4. **Functions**:
   - **`plot_sky(latitude, longitude, date_time)`**: Plots the current position of the Sun and Moon in both polar and rectangular plots for the specified date and time.
   - **`get_altandaz_camp(latitude, longitude, date_time)`**: Computes the azimuth and altitude for the Sun and Moon at a given time and location.
   - **`plot_object_over_x_days_n_times(object, start_date, entries, period)`**: Tracks the position of a celestial object (Sun or Moon) over a set number of days, plotting observations spaced out by a defined period (default 5 days).
   - **`object_over_a_day(year, month, day, object)`**: Plots the position of an object (Sun or Moon) over a single day, with observations taken every hour.
   
5. **Customization**:
   - The location and time can be easily customized by adjusting the **latitude**, **longitude**, and **start_date** variables.
   - The number of observations and the time interval between them can also be specified in the plotting functions.

#### Dependencies:
- **NumPy**: For numerical operations (like trigonometric functions).
- **Matplotlib**: For generating the plots (polar and rectangular).
- **PyEphem**: For calculating the positions of celestial objects.
- **pytz**: For handling time zones.

#### How to Use:
1. **Install Dependencies**: You need to install the required libraries:
   ```bash
   pip install numpy matplotlib ephem pytz
   ```

2. **Modify Observer Location**: Set the latitude and longitude for the desired location.

3. **Run Visualizations**:
   - To plot the current positions of the Sun and Moon, uncomment and run `plot_sky()`.
   - To track an object over a range of days or times, use `plot_object_over_x_days_n_times()` or `object_over_a_day()`.

4. **Customization**: You can modify the `start_date` and other parameters to explore different celestial events or time periods.


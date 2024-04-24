import numpy as np
import matplotlib.pyplot as plt
import ephem
from datetime import datetime, timezone

def plot_sky(latitude, longitude, date_time):
    """
    Plots the position of the Sun and the Moon in the sky.

    Parameters:
        latitude (float): Latitude of the observer (in degrees).
        longitude (float): Longitude of the observer (in degrees).
        date_time (datetime): Date and time of observation (timezone aware).

    Returns:
        None
    """
    # Observer's location
    observer = ephem.Observer()
    observer.lat = np.deg2rad(latitude)
    observer.lon = np.deg2rad(longitude)
    observer.date = date_time

    # Define celestial objects
    sun = ephem.Sun(observer)
    moon = ephem.Moon(observer)

    # Compute positions
    sun.compute(observer)
    moon.compute(observer)

    # Plotting the Sun
    sun_azimuth = np.rad2deg(sun.az)
    sun_altitude = 90 - np.rad2deg(sun.alt)

    # Plotting the Moon
    moon_azimuth = np.rad2deg(moon.az)
    moon_altitude = 90 - np.rad2deg(moon.alt)

    # Polar plot
    plt.subplot(121, projection='polar')
    plt.plot(np.deg2rad(sun_azimuth), sun_altitude, 'o', color='yellow', label='Sun')
    plt.plot(np.deg2rad(moon_azimuth), moon_altitude, 'o', color='gray', label='Moon')
    plt.title('Polar Plot')
    plt.gca().set_theta_zero_location('N')
    plt.gca().set_theta_direction(-1)
    plt.legend(loc='upper right')
    plt.grid(True)
    # Draw compass
    r = np.arange(0, 90, 0.01)
    directions = {'N': 0, 'NE': 45, 'E': 90, 'SE': 135, 'S': 180, 'SW': 225, 'W': 270, 'NW': 315}
    for direction, angle in directions.items():
        plt.text(np.deg2rad(angle), 95, direction, horizontalalignment='center', fontsize=8)
        plt.plot([np.deg2rad(angle)] * len(r), r, color='black', alpha=0.3)

    # Rectangular plot
    plt.subplot(122)
    plt.plot(sun_azimuth, sun_altitude, 'o', color='orange', label='Sun')
    plt.plot(moon_azimuth, moon_altitude, 'o', color='gray', label='Moon')

    plt.title('Rectangular Plot')
    plt.xlabel('Azimuth (degrees)')
    plt.ylabel('Altitude (degrees)')
    plt.xlim(0, 360)
    plt.ylim(0, 90)
    plt.gca().invert_xaxis()
    plt.gca().invert_yaxis()
    plt.legend(loc='upper right')
    plt.grid(True)

    plt.tight_layout()
    plt.show()


# Location of Campinile
latitude = 37.871873
longitude = -122.258347
date_time = datetime.now(timezone.utc)

plot_sky(latitude, longitude, datetime.now(timezone.utc))

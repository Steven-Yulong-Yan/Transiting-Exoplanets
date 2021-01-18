# Install matplotlib
from pylab import *

SCIENCE_ROOKIE = 1
SCIENCE_ENTHUSIAST = 2

# radius of the star is 695510km
RADIUS_STAR = 695510

# radius of the earth is 6371km
RADIUS_EARTH = 6371

# earth's orbital speed is 107208km per hour
VELOCITY_EARTH = 107208

# earth's distance from sun is 149600000km
DIST_EARTH_SUN = 149600000

# average rate of star formation (per year) in the galaxy
DRAKE_EQUATION_R = 7

# proportion of stars with planetary systems
DRAKE_EQUATION_P = 0.5

# number of planets per system with conditions suitable for life
DRAKE_EQUATION_N = 1

# average lifetime (in years) of such a civilisation within the detection window
DRAKE_EQUATION_L = 10000


def get_period_of_planet(dist_exo_star, velocity_exo):
    """
    Get the period of the exoplanet.
    :param dist_exo_star: The distance between the exoplanet and its star
    :param velocity_exo: The velocity of the exoplanet
    :return: the period of the planet
    """
    return 2 * pi * dist_exo_star / velocity_exo


def get_transit_time(velocity_exo, radius_star):
    """
    Get the transit time of the exoplanet through its star's diameter.
    :param velocity_exo: The velocity of the exoplanet
    :param radius_star: The radius of the exoplanet's star
    :return: The transit time of the exoplanet
    """
    return 2 * radius_star / velocity_exo


def get_self_transit_time(velocity_exo, radius_exo):
    """
    Get the transit time of the exoplanet moving through the equivalent
    distance of its own diameter.
    :param velocity_exo: The velocity of the exoplanet
    :param radius_exo: The radius of the exoplanet
    :return: The transit time of the exoplanet specified
    """
    return 2 * radius_exo / velocity_exo


def get_min_rel_intensity(radius_exo, radius_star):
    """
    Get the minimum relative intensity - the ratio of the observed intensity
    when the exoplanet is in front of the star to the observed intensity when
    the exoplanet is not in front of the star.
    :param radius_exo: The radius of the exoplanet
    :param radius_star: The radius of the exoplanet's star
    :return: The minimum relative intensity
    """
    return 1 - (radius_exo / radius_star) ** 2


# Welcome message
print("***********************************************************************")
print("Hi all! Welcome aboard our most exciting deep space exploration\n"
      "program to model and detect planets in the Milky Way\n"
      "where no one has gone before in search of galactic civilisations.\n"
      "So strap in and enjoy the ride!\n\n")

# Prompt the user to enter their patron type
patron_type = 0
while patron_type != SCIENCE_ROOKIE and patron_type != SCIENCE_ENTHUSIAST:
    patron_input = input("Please enter your patron type."
                         "\n(Enter either \"Science Rookie\" or "
                         "\"Science Enthusiast\" with matching cases.\n"
                         "Type \"SR\" or \"SE\" for is also fine.)\n--> ")
    if patron_input == "Science Rookie" or patron_input == "SR":
        patron_type = SCIENCE_ROOKIE
    elif patron_input == "Science Enthusiast" or patron_input == "SE":
        patron_type = SCIENCE_ENTHUSIAST

# Intro about other planets and other potential civilisations in our galaxy
print("\n")
print("-----------------------------------------------------------------------")
if patron_type == SCIENCE_ROOKIE:
    print("Wonders never cease! Come along with us to find alien planets and\n"
          "the cultures that they live in. Look far and beyond into space to\n"
          "meet with civilisations our ancestors have never managed to find.\n"
          "There is an interesting equation to figure out the number of\n"
          "fascinating civilisations out there. Bear with us for a moment\n"
          "and let's find out!\n\n")
elif patron_type == SCIENCE_ENTHUSIAST:
    print("Our galaxy is incredibly vast and old with more planets than\n"
          "the population on Earth and one can never cease to wonder about\n"
          "the possibility of potential civilisations in the vicinity of\n"
          "our home planet. Some of those who came before us had attempted\n"
          "to gauge the boundaries of the Milky Way and the civilisations\n"
          "that might have come into being within it. Dr. Frank Drake devised\n"
          "an equation in the 1960s with the purpose to determine the number\n"
          "of extraterrestrial civilisations based on quantifiable factors.\n"
          "The following section will run you through this equation.\n\n")

# Ask the user what they think is the proportion (or percentage)
# of habitable planets that develop technological civilisations
if patron_type == SCIENCE_ROOKIE:
    drake_equation_c = float(input("Guess a number between 0 and 1 to get the "
                                   "number of civilisations.\n--> "))
else:
    drake_equation_c = float(input("Please estimate the proportion of "
                                   "potentially habitable planets on which "
                                   "a technological civilisation develops.\n"
                                   "(A proportion would ideally be a number "
                                   "greater than 0 less than 1 and typically "
                                   "this value is very small.)\n--> "))

# Calculate using the estimates and print out with a message
drake_equation_result = DRAKE_EQUATION_R * DRAKE_EQUATION_P * \
                        DRAKE_EQUATION_N * drake_equation_c * DRAKE_EQUATION_L
print("\n")
if patron_type == SCIENCE_ROOKIE:
    print("Great work! We have found", round(drake_equation_result),
          "civilisations.")

elif patron_type == SCIENCE_ENTHUSIAST:
    print("The number of extraterrestrial civilisations in our galaxy with\n"
          "which we might expect to be able to communicate is",
          round(drake_equation_result))

# Introduce the idea of searching for planets around stars other than our own
print("\n")
print("-----------------------------------------------------------------------")
if patron_type == SCIENCE_ROOKIE:
    print("Now let's continue and try to actually find those planets. What\n"
          "we are going to do is work out how long it will take for a planet\n"
          "to pass in front of its star. If we can find such an event then\n"
          "we can tell that a planet exists.\n\n")
elif patron_type == SCIENCE_ENTHUSIAST:
    print("The next section will introduce you to the detection of\n"
          "extraterrestrial planets. There are several ways we have\n"
          "at our disposal that have yielded success. The method we are going\n"
          "to be using is the Kepler space telescope modelling. This method\n"
          "detects planets by measuring the transit light curve as a planet\n"
          "traverses between its star and the Earth. If a dimming at every\n"
          "regular interval is detected through the transit then it is safe\n"
          "to assume that there is a fair chance that an orbital planet is\n"
          "passing in front of the star.\n\n")

exit_program = 0
while exit_program == 0:

    # Ask the user for the relative size of the planet they want to find
    relative_radius = float(input("Please enter the relative size of the "
                                  "planet you want to find.\n"
                                  "(A multiplier with which you want the "
                                  "program to calculate in relation to "
                                  "Earth's radius.\n"
                                  "e.g. 10 will give the value of "
                                  "10 * 6371 = 63710(km))\n--> "))
    radius_exoplanet = RADIUS_EARTH * relative_radius
    print()

    # Ask the user for the relative distance of that planet to its star
    relative_dist = float(input("Please enter the relative distance of that "
                                "planet to its star.\n"
                                "(A multiplier with which you want the program "
                                "to calculate in relation to Earth's distance "
                                "from the sun.\n"
                                "e.g. 10 will give the value of "
                                "10 * 149600000 = 1496000000(km))"
                                "\n--> "))
    dist_exoplanet_star = DIST_EARTH_SUN * relative_dist

    velocity_exoplanet = VELOCITY_EARTH * sqrt(DIST_EARTH_SUN /
                                               dist_exoplanet_star)

    # Calculate the period for the planet's orbit
    period_exoplanet = get_period_of_planet(dist_exoplanet_star,
                                            velocity_exoplanet)

    # Calculate the transit time for the planet
    transit_time = get_transit_time(velocity_exoplanet, RADIUS_STAR)

    # Calculate the minimum relative intensity of the planet
    I_min = get_min_rel_intensity(radius_exoplanet, RADIUS_STAR)

    print("\n\nThe period of the orbit of the exoplanet is",
          round(period_exoplanet, 2), "hours",
          "\nThis is the time for the exoplanet to make one complete orbit\n"
          "around its star. The period of orbit is determined by the\n"
          "exoplanet's speed, and the distance the exoplanet is from its star.")
    print("\n\nThe transit time of the exoplanet is", round(transit_time, 2),
          "hours\nThe velocity of the exoplanet and the diameter of its star\n"
          "will determine the transit time. The faster the exoplanet is moving,"
          "\nthe shorter the transit time and, likewise, the larger the\n"
          "diameter of the star, the longer the transit time.")
    print("\n\nThe minimum relative intensity of the exoplanet is",
          round(I_min, 2),
          "\nWhen the exoplanet is fully between the Earth and the\n"
          "exoplanet's star, the intensity of the star observed from\n"
          "the Earth will be decreased as the exoplanet blocks some of\n"
          "the light from the star. The minimum relative intensity is the\n"
          "ratio of the observed intensity when the exoplanet is in front of\n"
          "the star to the observed intensity when the exoplanet is not in\n"
          "front of the star.\n\n")

    if patron_type == SCIENCE_ENTHUSIAST:

        self_transit_time = get_self_transit_time(velocity_exoplanet,
                                                  radius_exoplanet)

        times = arange(0, transit_time + 2 * self_transit_time, 0.01)
        rel_intensities = zeros(size(times))

        # Set the starting x position of the exoplanet relative to its star
        x_start = - (RADIUS_STAR + 2 * radius_exoplanet)

        time = 0
        iteration = 0
        while time < transit_time + 2 * self_transit_time:
            # Update the x position relative to the star
            x_pos_rel_star = x_start + velocity_exoplanet * time

            # Exoplanet fully outside of the star
            if abs(x_pos_rel_star) > RADIUS_STAR + radius_exoplanet:
                I_relative = 1

            # Exoplanet fully inside the star
            elif abs(x_pos_rel_star) < RADIUS_STAR - radius_exoplanet:
                I_relative = I_min

            # Exoplanet overlapping the edge of the star
            else:
                x_out = RADIUS_STAR + radius_exoplanet
                x_in = RADIUS_STAR - radius_exoplanet
                x = abs(x_pos_rel_star)
                I_relative = 1 - (x - x_out) / (x_in - x_out) * (1 - I_min)

            # Update the relative intensity in the array
            rel_intensities[iteration] = I_relative

            # Increment time
            time = time + 0.01

            # Increment the loop counter
            iteration = iteration + 1

        plot(times, rel_intensities)
        xlabel("Time (hours)")
        ylabel("Relative Intensity")
        title("Motion of the exoplanet across the fact of its star")
        ticklabel_format(useOffset=False)
        show()

        # Limitations of the modelling
        print("---------------------------------------------------------------")
        print("The transit light curve method is highly effective and sensitive"
              "\nfor detecting extraterrestrial planets. However, it is not\n"
              "without limitations. One of the problems is that an orbital\n"
              "cycle of a planet could have months or years, but a transit\n"
              "is mostly completed in hours or days, so a transit period\n"
              "only makes up a small portion of an entire orbital cycle.\n"
              "Therefore, an actual transit could be extremely hard to\n"
              "observed. This proves to be more difficult as often we need to\n"
              "measure multiple instances of a planet's transit in order to\n"
              "ascertain the existence of the exoplanet. Additionally,\n"
              "in order for the transit light curved to be observed,\n"
              "the transit planet needs to pass between its star and\n"
              "the Earth, which is extremely rare, and thus most transits\n"
              "are simply never detected.\n\n")

    # Inform the user whether their chosen planet could be detected or not
    detection = False
    if get_min_rel_intensity(radius_exoplanet, RADIUS_STAR) < 9999 / 10000:
        detection = True
    if detection is True:
        print("Great news! The exoplanet can be detected.\n\n")
    else:
        print("Unfortunately the exoplanet cannot be detected.\n\n")

    # Ask the user if they want to try again with another exoplanet search
    print("-------------------------------------------------------------------")
    restart = input("Would you like to try again with another "
                    "exoplanet search?\n"
                    "(Please enter either \"Yes\" or \"No\" "
                    "with matching cases.\n"
                    "Type \"Y\" or \"N\" is also fine.)\n--> ")
    if restart == "No" or restart == "N":
        # A farewell message
        print(
            "\n\nThank you brave explorers! We hope you had fun and\n"
            "will see you in our next journey into space.")
        exit_program = 1
    elif restart == "Yes" or restart == "Y":
        print("\n")
        print("***************************************************************")
        exit_program = 0

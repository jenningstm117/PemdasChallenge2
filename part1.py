from geopy import Point
from geopy.distance import VincentyDistance
import argparse

BEARING_EAST = 90  # East
BEARING_NORTH = 360   # North


def generate_grid(min_latitude, max_latitude, min_longitude, max_longitude):
    output_grid = []
    index = -1

    # setup initial values
    start_latitude, start_longitude = min_latitude, min_longitude
    current_latitude, current_longitude = min_latitude, min_longitude

    # continue to add rows as long as we haven't reached the max values
    # if the starting latitude and longitude are greater than the max it means
    while start_latitude < max_latitude and start_longitude < max_longitude:
        # move east across the grid
        output_grid.append([])
        index += 1
        start_latitude, start_longitude = current_latitude, current_longitude
        output_grid[index].append((current_latitude, current_longitude,))
        while current_longitude < max_longitude:
            current_latitude, current_longitude = get_new_point(current_latitude, current_longitude, BEARING_EAST)
            output_grid[index].append((current_latitude, current_longitude,))

        # move north one km and repeat
        current_latitude, current_longitude = get_new_point(start_latitude, start_longitude, BEARING_NORTH)

    return output_grid


def get_new_point(lat, lon, bearing):
    point = VincentyDistance(kilometers=1).destination(Point(lat, lon), bearing)
    return point.latitude, point.longitude


def print_coords(output_grid):
    for row in output_grid:
        for point in row:
            print '{0},{1}'.format(point[0], point[1])


if __name__ == '__main__':
    # setup arguments for running through the terminal. an error will be raised if there are not enough arguments
    parser = argparse.ArgumentParser()

    # first 4 positional args are for latitude and longitude points
    parser.add_argument("min_lat", help="Minimum Latitude", type=float)
    parser.add_argument("max_lat", help="Maximum Latitude", type=float)
    parser.add_argument("min_lon", help="Minimum Longitude", type=float)
    parser.add_argument("max_lon", help="Maximum Longitude", type=float)

    # optional args for printing out the grid
    parser.add_argument("--coords", help="Print the resulting grid as a single list of comma seperated coordinates",
                        action="store_true")
    parser.add_argument("--grid", help="Print the resulting grid as a list", action="store_true")
    args = parser.parse_args()

    # pull the values from the args
    min_lat = args.min_lat
    max_lat = args.max_lat
    min_lon = args.min_lon
    max_lon = args.max_lon

    # generate the grid
    output_grid = generate_grid(min_lat, max_lat, min_lon, max_lon)

    # print out the grid if necessary
    if args.coords:
        print_coords(output_grid)

    if args.grid:
        print output_grid

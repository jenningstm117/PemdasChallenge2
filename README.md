# Pemdas Challenge 2
* Tested using python 2.7

#### Setup
from the root directory of the repo run `pip install -r requirements.txt`
to install the required modules.

## Part 1 - Grid Generation

### Implementation Summary
Coordinate point generation and traversal is done using the geopy module and an ellipsoid earth model.
starting at the origin point and moving east by 1km at a time a new point is generated and added
to the current of row of points parallel to the latitude lines. Once a point is generated with a
longitude value greater than the given max longitude, the loop returns to the row starting point
and moves North 1km, then starts again with a new row. When the row starting latitude and longitude
are greater than the given max latitude and longitude, the loop exits and returns the grid.

### To execute using the terminal
cd into app root and run
* `python part1.py <min_latitude> <max_latitude> <min_longitude> <max_longitude>`
* or
`python part1.py <min_latitude> <max_latitude> <min_longitude> <max_longitude> --coords`
to output the grid as a single column of coordinates

#### Example
```
(PemdasChallenge) michael@michael-PC:~/Development/PemdasChallenge2$ python part1.py 35.011232 35.0113 -81.058350 -81.04

[[(35.011232, -81.05835), (35.011231505559984, -81.04739418413415), (35.01123101111998, -81.03643836833422)], [(35.020245814152304, -81.05835), (35.02024531954772, -81.04739298193816), (35.02024482494315, -81.03643596394228)]]

(PemdasChallenge) michael@michael-PC:~/Development/PemdasChallenge2$ python part1.py 35.011232 35.0113 -81.058350 -81.04 --coords

35.011232,-81.05835
35.0112315056,-81.0473941841
35.0112310111,-81.0364383683
35.0202458142,-81.05835
35.0202453195,-81.0473929819
35.0202448249,-81.0364359639

(PemdasChallenge) michael@michael-PC:~/Development/PemdasChallenge2$
```


### To call in python
```
import part1
min_lat = 35.011232
max_lat = 35.0113
min_lon = -81.058350
max_lon = -81.04
output_grid = part1.generate_grid(min_lat, max_lat, min_lon, max_lon)
print output_grid
```


## Part 2

### Implementation Summary
When reading through the csv file a new Player instance is created with
the attributes of that row and added to an instance of Team. Each output value
is a function of all the players on a team so the Team object has methods to generate those values.

##### Asumptions
* The first row of the CSV file is a header row
* Each subsequent row corresponds to a unique player on the team
* Every player described in the CSV file is on the same team

### To execute using the terminal
cd into app root and run
* `python part2.py <file_path>`

#### Example
```
(PemdasChallenge) michael@michael-PC:~/Development/PemdasChallenge2$ python part2.py data.csv

(72.75, 35.71, 2)

```


### To call in python
```
import part2
result = part2.generate_grid
print result
```

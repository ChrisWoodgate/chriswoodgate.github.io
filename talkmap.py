# Leaflet cluster map of talk locations
#
# Run this from the _talks/ directory, which contains .md files of all your
# talks. This scrapes the map_location YAML field (falling back to location)
# from each .md file (an empty map_location keeps a talk off the map), geolocates it
# with geopy/Nominatim, and uses the getorg library to output data, HTML, and
# Javascript for a standalone cluster map. This is functionally the same as the
# #talkmap Jupyter notebook.
import frontmatter
import glob
import getorg
from geopy import Nominatim
from geopy.exc import GeocoderTimedOut

# Set the default timeout, in seconds
TIMEOUT = 5

# Collect the Markdown files
g = glob.glob("_talks/*.md")

# Prepare to geolocate
geocoder = Nominatim(user_agent="academicpages.github.io")
location_dict = {}
location = ""
permalink = ""
title = ""

# Perform geolocation
for file in g:
    # Read the file
    data = frontmatter.load(file)
    data = data.to_dict()

    # Press on if the location is not present
    if 'location' not in data:
        continue

    # Prepare the description
    title = data['title'].strip()
    venue = data['venue'].strip()
    location = data['location'].strip()
    description = f"{title}<br />{venue}; {location}"

    # Geocode from map_location where present, falling back to location
    map_location = data.get('map_location', location).strip()

    # An empty map_location keeps the talk off the map (e.g. remote attendance)
    if not map_location:
        continue

    # Geocode the location and report the status
    try:
        location_dict[description] = geocoder.geocode(map_location, timeout=TIMEOUT)
        print(description, location_dict[description])
    except ValueError as ex:
        print(f"Error: geocode failed on input {map_location} with message {ex}")
    except GeocoderTimedOut as ex:
        print(f"Error: geocode timed out on input {map_location} with message {ex}")
    except Exception as ex:
        print(f"An unhandled exception occurred while processing input {map_location} with message {ex}")

# Save the map
m = getorg.orgmap.create_map_obj()
getorg.orgmap.output_html_cluster_map(location_dict, folder_name="talkmap", hashed_usernames=False)

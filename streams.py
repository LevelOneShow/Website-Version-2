# Volta Streaming Backend - Service Query
# Written by Nick Pleatsikas - pleatsikas.me

# Contact admin@volta.network to report any bugs.
# View the README for more information.

# Modules: ---------------------------------------------------------------------

# Full Modules:
import json, requests

# Variables: -------------------------------------------------------------------

# User List:
user_list = 'users.txt'

# Output File:
output = 'output.json'

# Functions: -------------------------------------------------------------------

# read_file_to_list : file -> list
# Reads a file with users and casts each username to a list.
def read_file_to_list(file):
    with open(file, 'r') as config:
        list_users = [line.strip() for line in config]
    return list_users

# loop_through : list -> bool
# Loops through a list and passes it to 'check_online' which returns a boolean.
""" -> needs to be changed a lot.
def loop_through(li):
    live_now = {}
    num_users = 1
    for item in li:
        live_now.update({num_users: online_status(item)})
        num_users = (num_users+1)
    return live_now
"""

# output_file : string, object -> file
# Outputs an array to a file. Overwrites the file if it exists.
""" -> function to be removed.
def output_file(file, o):
    with open(file, "w") as output_file:
        json.dump(o, output_file)
"""

# online_status : string -> object
# Checks to see if twitch.tv user is online.
def process_raw_json(user):
    # Create URLs for GET Requests.
    twitch_url = "https://api.twitch.tv/kraken/streams/%s" % (user, )
    beam_url = "https://beam.pro/api/v1/channels/%s" % (user, )
    # Get JSON from twitch and beam.
    raw_json_twitch = (requests.get(twitch_url).json())
    raw_json_beam = (requests.get(beam_url).json())

    raw_json_array = [raw_json_twitch, raw_json_beam] 
    # Main array:
    info = []

    for idx, item in enumerate(raw_json_array):
        if (item.get("statusCode") == 404 or item.get("status") == 404):
            info.append(None)
        elif (item.get("stream") == None or item.get("online") == False):
            info.append(None)
        elif idx == 1:
            info.append({"title": raw_json_beam.get("name"),
                    "url": "https://beam.pro/%s" % (user,)})
        else:
            info.append({"title": raw_json_twitch.get("stream").get("channel").get("status"), 
                "url": raw_json_twitch.get("stream").get("channel").get("url")})

    return {"streamer": user, "info": info}

# Output: ----------------------------------------------------------------------

# -> file
# Outputs the twitch information for users to a file.
# output_file(output, loop_through(read_file_to_list(user_list))) <- commented out for debugging.
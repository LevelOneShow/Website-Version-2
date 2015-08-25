# Volta Network Website - Server : streams.py
# Code by Nick Pleatsikas (nickcp.com)

# Contact admin@lvloneshow.com to report any bugs.
# View the README at lic.volta.network for information on usage rights.

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
def loop_through(li):
    live_now = {}
    num_users = 1
    for item in li:
        live_now.update({num_users: online_status(item)})
        num_users = (num_users+1)
    return live_now

# output_file : string, object -> file
# Outputs an array to a file. Overwrites the file if it exists.
""" -> function to be removed.
def output_file(file, o):
    with open(file, "w") as output_file:
        json.dump(o, output_file)
"""

# online_status : string -> object
# Checks to see if twitch.tv user is online.
def online_status(user):
    # Create URLs for GET Requests.
    twitch_url = "https://api.twitch.tv/kraken/streams/%s" % (user, )
    beam_url = "https://beam.pro/api/v1/channels/%s" % (user, )
    # Get JSON from twitch and beam.
    info_twitch = (requests.get(url).json())
    info_beam = (requests.get(url).json())
    if twitch_info.get("stream") == None:
        return None
    else:
        return {"user": user, 
        "title": twitch_info.get("stream").get("channel").get("status"), 
        "url": twitch_info.get("stream").get("channel").get("url")}

# Output: ----------------------------------------------------------------------

# -> file
# Outputs the twitch information for users to a file.
output_file(output, loop_through(read_file_to_list(user_list)))
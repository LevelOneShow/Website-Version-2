# Volta Streaming Backend - Streaming Service Query
# Written by Nick Pleatsikas - pleatsikas.me

# Contact admin@volta.network to report any bugs.
# View the README for more information.

# Modules: ---------------------------------------------------------------------

# Modules:
import json, requests

# Variables: -------------------------------------------------------------------

# User List:
user_list = 'users.txt'

# Functions: -------------------------------------------------------------------

# file_to_list : file -> list
# Reads a file with users and casts each username to a list.
def file_to_list(file):
    with open(file, 'r') as config:
        list_users = [line.strip() for line in config]
    return list_users

# package_json : list -> bool
# Loops through every user in list and passes it to process_raw_json for
# generation.
def package_json(lst):
    pack = []
    for user in lst:
        pack.append(process_raw_json(user))
    return json.dumps(pack)

# process_raw_json : string -> object
# Checks to see if user is online on twitch or beam, then packages data in a 
# pretty format.
def process_raw_json(user):
    # Create URLs for GET Requests:
    twitch_url = "https://api.twitch.tv/kraken/streams/%s" % (user, )
    beam_url = "https://beam.pro/api/v1/channels/%s" % (user, )
    hitbox_url = "https://hitbox.tv/media/live/%s" % (user, )
    # Get JSON from twitch and beam:
    raw_json_twitch = (requests.get(twitch_url).json())
    raw_json_beam = (requests.get(beam_url).json())
    raw_json_hitbox = (requests.get(hitbox_url).json())
    raw_json_array = [raw_json_twitch, raw_json_beam]
    # Main array:
    info = []
    # Sorting algorithm:
    for idx, item in enumerate(raw_json_array):
        if (item.get("statusCode") == 404 or
                item.get("status") == 404 or
                item.get("status") == 422 or
                item.get("error_msg") == "no_media_found"):
            info.append(None)
        elif (item.get("online") == False): # Beam case for offline.
            info.append(None)
        elif (item.get("stream") == None and '_links' in item): # Twitch case for offline.
            info.append(None)
        elif (item.get("livestream")[0].get("channel").get("media_is_live") == '0'): # Hitbox case for offline.
            info.append(None)
        elif idx == 1:
            info.append({"title": raw_json_beam.get("name"),
                    "url": "https://beam.pro/%s" % (user,)})
        elif idx == 2 and raw_json_hitbox.get("livestream")[0].get("channel").get("media_is_live") == '1':
            info.append({"title": None, # There is no method currently to get title of stream.
                "url": "https://hitbox.tv/%s" % (user, )})
        else:
            info.append({"title": raw_json_twitch.get("stream").get("channel").get("status"), 
                "url": raw_json_twitch.get("stream").get("channel").get("url")})
    
    return {"streamer": user, "info": info}

# main : -> str
# Main function. This runs the whole program.
# This function is imported in other files with 'from streams import proc_main'
# or 'from streams import *'
def proc_main():
    package_json(file_to_list(user_list))
    # debug: print(package_json(file_to_list(user_list)))

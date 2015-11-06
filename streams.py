# Volta Streaming Backend - Streaming Service Query
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
out_file = 'api_data.txt'

# Output Directory:
dir = '/home/web/html2/'

# Output Path:
path = dir + out_file

# Functions: -------------------------------------------------------------------

# file_to_list : file -> list
# Reads a file with users and casts each username to a list.
def file_to_list(file):
    with open(file, 'r') as config:
        list_users = [line.strip() for line in config]
        config.close()
    return list_users

# write_to_file : list -> file
# An array and write it to a file.
def write_to_file(lst, file):
    f = open(file, 'r+')
    f.write('\'%s\'' % (str(lst), ))
    f.close()

# package_json : list -> bool
# Loops through every user in list and passes it to process_raw_json for
# generation.
def package_json(lst):
    pack = []
    for user in lst:
        pack.extend(process_raw_json(user))
    return json.dumps(pack, sort_keys=True)

# process_raw_json : string -> object
# Checks to see if user is online on twitch or beam, then packages data in a 
# pretty format.
def process_raw_json(user):
    # Create URLs for GET Requests:
    twitch_url = "https://api.twitch.tv/kraken/streams/%s" % (user, )
    beam_url = "https://beam.pro/api/v1/channels/%s" % (user, )
    # Get JSON from twitch and beam:
    raw_json_twitch = (requests.get(twitch_url).json())
    raw_json_beam = (requests.get(beam_url).json())
    raw_json_array = [raw_json_twitch, raw_json_beam]
    # Main array:
    info = []
    # Sorting algorithm:
    for idx, item in enumerate(raw_json_array):
        if (item.get("statusCode") == 404 or
                item.get("status") == 404 or
                item.get("status") == 422):
            info.append(None)
        elif (item.get("online") == False): # Beam case for offline.
            info.append({"name": user,
                "online": False,
                "service": "beam",
                "data": None})
        elif (item.get("stream") == None and '_links' in item): # Twitch case for offline.
            info.append({"name": user,
                "online": False,
                "service": "twitch",
                "data": None})
        elif idx == 1:
            info.append({"name": user,
                "online": True,
                "service": "beam",
                "data": {
                    "title": item.get("name"),
                    "url": "https://beam.pro/%s" % (user,)
                }})
        else:
            info.append({"name": user,
                "online": True,
                "service": "twitch",
                "data": {
                    "title": item.get("stream").get("channel").get("status"), 
                    "url": item.get("stream").get("channel").get("url")
                }})
    
    return info


# Startup: ---------------------------------------------------------------------

# Init:
if __name__ == '__main__':
    data_pack = package_json(file_to_list(user_list))
    write_to_file(data_pack, path)
    # debug: print(data_pack)

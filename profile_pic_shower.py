"""
FileName: Profile Pic Shower
Author: N.G 10/1/23
Purpose: Gets from the user a username of an instagram profile and returns its profile picture.
"""

import webbrowser
import instaloader
import argparse

BROWSER = "C:/Program Files/Google/Chrome/Application/chrome.exe"


def get_username_from_user() -> str:
    """
    Gets the wanted instagram username from the user using argument parsing.
    """
    parser = argparse.ArgumentParser(description="Gets a magnified version of an instagram profile's profile pic")
    parser.add_argument('-u', '--username', help='The username of the profile', required=True)
    args = vars(parser.parse_args())
    return args["username"]


def get_profile_pic(username: str) -> str:
    """
    Gets the profile pic URL of the instagram profile that has the given username
    :param username: The username of the instagram profile that the program will get its profile picture.
    """
    loader = instaloader.Instaloader()
    try:
        meta = instaloader.Profile.from_username(loader.context, username)
        return meta.get_profile_pic_url()
    except instaloader.exceptions.ConnectionException as e:
        print(e)
        print("Are you sure that you gave an existing instagram username?")
        exit(1)


# noinspection PyCompatibility,PyMissingOrEmptyDocstring
def main():
    username = get_username_from_user()
    profile_pic = get_profile_pic(username)
    webbrowser.get(f"{BROWSER} %s").open(profile_pic)


if __name__ == "__main__":
    main()

"""
FileName: 
Author: N.G
Purpose:
"""

import instaloader

USERNAME = "noam_glassman"
PASSWORD = "Batman1911"
loader = instaloader.Instaloader()


def get_username_from_user() -> str:
    """
    Gets the wanted instagram username from the user using argument parsing.
    """
    parser = argparse.ArgumentParser(description="Gets a magnified version of an instagram profile's profile pic")
    parser.add_argument('-u', '--username', help='The username of the profile', required=True)
    args = vars(parser.parse_args())
    return args["username"]


def login() -> None:
    """
    logs into the specified profile
    """
    try:
        loader.login(USERNAME, PASSWORD)
        print("Successfully logged in!")
    except instaloader.exceptions.BadCredentialsException:
        print("Login error! Are you sure that's the correct password?")
        exit(1)


def get_metadata() -> instaloader.structures.Profile:
    """
    gets metadata from your profile
    :return: A structure of your profile's metadata
    """
    profile_metadata = instaloader.Profile.from_username(loader.context, USERNAME)
    return profile_metadata


def get_following() -> list:
    """
    gets a list of the instagram profiles that the user follows on instagram
    """
    login()
    metadata = get_metadata()
    return list(metadata.get_followees())


def get_verified_following(followings: list) -> list:
    """
    Gets a list of the profiles you follow that are verified
    :param followings: The list of profiles you follow
    :return: The list of the verified profiles you follow
    """
    return [following for following in followings if following.is_verified]


def get_inactive_pages(relevant_followings: list) -> list:
    pass


def main():
    followings = get_following()
    print("got following")
    verified = get_verified_following(followings)


if __name__ == "__main__":
    main()

from github import Github
import pickle
from getpass import getpass
import sys
import os


def setupCredential():
    try:
        username = input("[quickgit]: Enter Github Username: ")
        password = getpass("[quickgit]: Enter Github password: ")
        repo = input("[quickgit]: Enter name of repo. to use:  ")
        with open("credentials.cred", "wb") as credential_file:
            pickle.dump({
                'username': username,
                'password': password,
                'repo': repo,
            }, credential_file)
            print("[quickup]: All set now try quickup again. [^_^]")
            sys.exit(0)

    except Exception as e:
        print("[quickup]: Error while creating file.", str(e))
        sys.exit(0)


if __name__ == "__main__":
    try:
        with open("credentials.cred", "rb") as credential_file:
            data = pickle.load(credential_file)
            username = data["username"]
            password = data['password']
            repo = data['repo']
            print("[quickup]: Loading credentials...")
    except Exception as e:
        print("[quickup]: Credential file not found.", e)
        print("[quickup]: Resetting file...")
        setupCredential()

    filepath = input("[quickup]: Enter path of file: ")
    msg = input("[quickup]: Enter message for file: ")
    filename = os.path.basename(filepath)
    filedata = open(filepath, "r").read()
    git = Github(username, password)
    user = git.get_user()
    user.get_repo(repo).create_file(
        path=filename, message=msg, content=filedata)
    print("[quickup]: File Created Succesfully. {*_*}")

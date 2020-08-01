from github import Github
from terminaltables import SingleTable
from getpass import getpass
import sys

__credential_file = "./data/data.bin"
__username = sys.argv[1]
__password = getpass("[git_cli]: Enter Password: ")


git = Github(__username, __password)
try:
    user = git.get_user()
except:
    print("[git_cli]: I think credentials are wrong... ")
    sys.exit(0)


def showRepo():
    repos_list = []
    index_of_repos = 1
    repos_list.append(["S. No", "Name Of Repo."])
    for i in user.get_repos():
        temp_list = []
        temp_list.append(index_of_repos)
        temp_list.append(i.full_name)
        repos_list.append(temp_list)
        index_of_repos += 1

    print(SingleTable(repos_list, "[git_cli]: Repositories").table)
    repos_option_data = [
        ["S. No.", "Operations Available"],
        [1, "Create New Repository"],
        [2, "Create New File."],
        [3, "Edit name of repo."],
        [4, "Delete Repository."]
    ]
    repos_option_table = SingleTable(repos_option_data).table
    print(repos_option_table)
    ch = input("[git_cli] ((Choose Operation to perform.): ")
    if ch == "1":
        name_of_repo = input("[git_cli] (Name of repo. to create): ")
        try:
            user.create_repo(name_of_repo)
        except:
            print("[git_cli] (Facing problem while creating.)")
            sys.exit(0)
    elif ch == "2":
        name_of_repo = input("[git_cli] (Name of repo.): ")
        name_of_file = input("[git_cli] (Name of file): ")
        message_for_file = input("[git_cli] (message for file): ")
        location = input("[git_cli] (Path of the file): ")
        try:
            file = open(location, "r")
            user.get_repo(name_of_repo).create_file(
                name_of_file, message=message_for_file, content=file.read())
        except Exception as e:
            print("[git_cli] (Facing problem while creating file.)", e)
            sys.exit(0)
    elif ch == "4":
        name_of_repo = input("[git_cli] (Name of repo. to delete): ")
        try:
            user.get_repo(name_of_repo).delete()
        except:
            print("[git_cli] (Failed to delete repo.): ")
    elif ch == "3":
        name_of_repo = input("[git_cli] (Old name of repo.): ")
        new_name_of_repo = input("[git_cli] (New name of repo.): ")
        try:
            user.get_repo(name_of_repo).edit(name=new_name_of_repo)
        except:
            print("[git_cli] (Failed to edit repo.): ")
    else:
        print("[git_cli] You know what you want...")
        sys.exit(0)


if __name__ == "__main__":
    showRepo()

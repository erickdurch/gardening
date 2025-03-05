import os

def main():
    # Create a directory for the project if it doesn't already exist
    if not os.path.exists("project_gardening"):
        os.mkdir("project_gardening")

    # Change into the new directory
    os.chdir("project_gardening")

    # Create a file for the project README
    with open("README.md", "w") as f:
        f.write("# Project Gardening\n\nThis is a repository for my gardening projects.")

    # Create a new directory for the first project
    os.mkdir("project_1")

    # Change into the new directory
    os.chdir("project_1")

    # Create a file for the project README
    with open("README.md", "w") as f:
        f.write("# Project 1\n\nThis is my first gardening project.")

if __name__ == "__main__":
    main()

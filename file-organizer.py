import os
import argparse

def organize_files(directory_path, is_single_folder):
    ### Some of the most used extensions categorized by my preferences, adjust acrofindly ########
    directories = ["Documents","Executables","Images","Videos","Music","Zips","Other"]
    file_extension_mapping = {
        "Documents": ["pdf", "ppt", "pptx", "xlsx", "xls", "docx", "txt"],
        "Executables": ["exe", "msi"],
        "Images": ["png", "jpg", "svg", "webp", "apng", "avif", "gif", "jpeg", "jfif", "pjpeg", "pjp", "bmp"],
        "Videos": ["mkv", "mp4", "mov", "avi", "wmv", "webm", "flv", "mpg", "mpeg", "m2v", "wmv", "m4p", "m4v"],
        "Music": ["mp3", "flac", "wav", "aac", "alac", "dsd", "pcm", "aiff"],
        "Zips": ["zip", "rar", "7z"],
    }

    for directory in directories:
        if directory not in os.listdir(directory_path):
            full_path = os.path.join(directory_path, dir)
            os.mkdir(full_path)
            print(directory + " directory created")

    for file_name in os.listdir(directory_path):
        file_splitted = file_name.split(".")
        file_extension = file_splitted[-1]
        for directory, extensions in file_extension_mapping.items():
            if file_extension in extensions:
                full_path = os.path.join(directory_path, directory)
                source = os.path.join(directory_path, file_name)
                destination = os.path.join(full_path,file_name)
                if os.path.exists(destination):
                    user_choice = input("file already exists in destination folder" + full_path + "''\n'" + "1 if you want to overwrite file or 2 if you want to rename the file before copying:" + "\n")
                    if user_choice == "1":
                        os.replace(source, destination)
                    else:
                        new_name = input("please provide a new file name to procced")
                        os.rename(file_name, os.path.join(full_path, new_name))
                        source = os.path.join(directory_path, file_name)
                        destination = os.path.join(full_path,file_name)
                    break
                else:
                    os.rename(source,destination)
        else:
            if file_splitted[0] not in directories:
                full_path = os.path.join(directory_path, "Other")
                source = os.path.join(directory_path, file_name)
                destination = os.path.join(full_path,file_name)
                if os.path.exists(destination):
                    user_choice = input("file already exists in destination folder" + full_path + "\\n" + "1 if you want to overwrite file or 2 if you want to rename the file before copying:" + "\\n")
                    if user_choice == "1":
                        os.replace(source, destination)
                    else:
                        new_name = input("please provide a new file name to procced")
                        os.rename(file_name, os.path.join(full_path, new_name))
                        source = os.path.join(directory_path, file_name)
                        destination = os.path.join(full_path,file_name)
                    break
                else:
                    os.rename(source,destination)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Organize files by extension")

    parser.add_argument(
        "-s",
        "--single",
        action="store_true",
        help="Specify if only a single folder should be organized.",
    )

    parser.add_argument(
        "-m",
        "--multiple",
        action="store_true",
        help="Specify if multiple folders should be organized.Paths should be separated by comma",
    )

    parser.add_argument(
        "directory",
        type=str,
        help="The directory to organize files from",
    )

    args = parser.parse_args()

    if not (args.single or args.multiple):
        parser.error("Either -s or -m must be specified.")

    directories = args.directory.split(",") if "," in args.directory else [args.directory]

    if args.single:
        for directory_path in directories:
            organize_files(directory_path.strip(), True)
    elif args.multiple:
        for directory_path in directories:
            organize_files(directory_path.strip(), False)
    else:
        if len(directories) > 1:
            print("Ignoring extra folders. Use -s for a single folder or -m for multiple folders.")
        organize_files(directories[0].strip(), True)

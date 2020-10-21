import os

def listdirfiles( dir, extension):
    # create a list of all files in specified folder
    list_files = []
    try:
        dirlist = os.listdir(dir)
        for file in dirlist:
            if (file.endswith(extension)):
                list_files.append(dir + file)
    except OSError:
        print("E: Invalid directory = ", dir)
        return None

    return list_files

def main():
    path_to_files = 'test_dir/'
    filelist = listdirfiles(path_to_files, "json")
    print(filelist)

if __name__ == '__main__':
    main()
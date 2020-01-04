import  os

from config import MOVIE_FILE_FORMAT_LIST
import glob

path = 'C:\\Documents\\Movies\\'


def movie_file_name_finder(path):
    print("### initiate the movie_file_name_finder ###\n\n")
    file_list = []
    for r, d, f in os.walk(path):
        for file in f:
            _list = file.rsplit(".",maxsplit=1)
            if _list[1].lower() == 'mp4' or _list[1].lower() == 'avi':
                file_list.append(_list[0])

    text_file = open(r"movies.txt","+w")
    for l in file_list:
        text_file.writelines(l+'\n')

    text_file.close()
    for i in file_list:
        print(i)



movie_file_name_finder(path)


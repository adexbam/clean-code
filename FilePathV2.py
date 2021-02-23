import re


def get_file_path(s_file):
    if len(s_file) > 0 and s_file[len(s_file) - 1] == '/':
        return s_file

    try:
        p_location = int(s_file.rindex('/'))
    except NameError:
        p_location = -1
    dirName = ''
    if p_location >= 0:
        dirName = s_file[0: p_location + 1]
    else:
        dirName = ''  # sFilename

    return dirName


# This function gets the file
def getFilenamePart(s_filename):
    try:
        int(s_filename.rindex('/'))
    except:
        return s_filename

    pos = s_filename.rindex('/')
    base_name = s_filename[pos + 1:]
    return base_name


# .png
def get_extension_part(s_filename):
    try:
        occurrences = [m.start() for m in re.finditer('\.', s_filename)]
        return s_filename[occurrences[-1] + 1:]
    except:
        pass

    return ''


assert (get_file_path("log/cups/access_log") == "log/cups/")
assert (get_file_path("log/cups/") == "log/cups/")
assert (get_file_path("cups/access_log") == "cups/")
assert (get_file_path("access_log") == "")
assert (getFilenamePart("log/cups/access_log") == "access_log")
assert (getFilenamePart("log/cups/") == "")
assert (getFilenamePart("cups/access_log") == "access_log")
assert (getFilenamePart("access_log") == "access_log")
assert (get_extension_part("log/cups/access_log") == "")
assert (get_extension_part("base/FileHelper.cpp") == "cpp")
assert (get_extension_part("base/FileHelper.cpp.bak") == "bak")

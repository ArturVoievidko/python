import pathlib
import os
import re
import sys

list_of_pathes = list()
result = {"images":[],
            "video":[],
            "docs":[],
            "music":[],
            "archive":[],
            "unknown":[]}

formats = {"images":["jpeg", "png", "jpg", "svg", "py"],
           "video":["avi", "mp4", "mov", "mkv"],
           "docs":["doc", "docx", "txt", "pdf", "xlsx", "pptx"],
           "music":["mp3", "ogg", "wav", "amr"],
           "archive":["zip", "gz", "tar"]}
founded_formats = set()
unknown_formats = set()


def recursive(path, result=[], depth=0, margin_simbol="-"):
    margin = margin_simbol * depth
    if path.is_dir():
        #print(margin + path.name + "/")
        list_of_pathes.append(path)
        for item in path.iterdir():
            recursive(item, result, depth=depth+1)
    else:
        #print(margin + path.name)
        list_of_pathes.append(path)


def normalize(name):
    TRANSLIT_DICT = {1072: 'a', 1040: 'A', 1073: 'b', 1041: 'B', 1074: 'v', 1042: 'V', 1075: 'g', 1043: 'G', 1076: 'd', 1044: 'D', 1077: 'e', 1045: 'E', 1105: 'e', 1025: 'E', 1078: 'j', 1046: 'J', 1079: 'z', 1047: 'Z', 1080: 'i', 1048: 'I', 1081: 'j', 1049: 'J', 1082: 'k', 1050: 'K', 1083: 'l', 1051: 'L', 1084: 'm', 1052: 'M', 1085: 'n', 1053: 'N', 1086: 'o', 1054: 'O', 1087: 'p', 1055: 'P', 1088: 'r', 1056: 'R', 1089: 's', 1057: 'S', 1090: 't', 1058: 'T', 1091: 'u', 1059: 'U', 1092: 'f', 1060: 'F', 1093: 'h', 1061: 'H', 1094: 'ts', 1062: 'TS', 1095: 'ch', 1063: 'CH', 1096: 'sh', 1064: 'SH', 1097: 'sch', 1065: 'SCH', 1098: '', 1066: '', 1099: 'y', 1067: 'Y', 1100: '', 1068: '', 1101: 'e', 1069: 'E', 1102: 'yu', 1070: 'YU', 1103: 'ya', 1071: 'YA', 1108: 'je', 1028: 'JE', 1110: 'i', 1030: 'I', 1111: 'ji', 1031: 'JI', 1169: 'g', 1168: 'G'}

    indx = name.find('.')
    name_without_suffix = name[:indx]
    suffix = name[indx:]
    name_without_suffix = name_without_suffix.translate(TRANSLIT_DICT)
    name_without_suffix = re.sub('[^a-zA-Z0-9]', "_", name_without_suffix)
    name = name_without_suffix + suffix

    return name


def sorting(file_name, suffix):
    suffix = suffix[1:]

    if suffix in formats["images"]:
        result["images"].append(file_name)
        founded_formats.add(suffix)
    elif suffix in formats["video"]:
        result["video"].append(file_name)
        founded_formats.add(suffix)
    elif suffix in formats["docs"]:
        result["docs"].append(file_name)
        founded_formats.add(suffix)
    elif suffix in formats["archive"]:
        result["archive"].append(file_name)
        founded_formats.add(suffix)
    else:
        result["unknown"].append(file_name)
        unknown_formats.add(suffix)


def main():
    path = pathlib.Path(sys.argv[1])
    recursive(path)
    print(list_of_pathes)

if __name__ == "__main__":
    main()
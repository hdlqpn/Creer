import re
import os
import collections

def extend(d, u):
    for k, v in u.items():
        if isinstance(v, collections.Mapping):
            r = extend(d.get(k, {}), v)
            d[k] = r
        else:
            d[k] = u[k]
    return d


def list_dirs(path):
    folders = []
    while path != "" and path != None:
        path, folder = os.path.split(path)

        if folder != "":
            folders.append(folder)
        else:
            if path!="":
                folders.append(path)
            break
    folders.reverse()
    return folders

def uncapitalize(s):
    return s[:1].lower() + s[1:] if s else ''

def extract_str(raw_string, start_marker, end_marker):
    start = raw_string.index(start_marker) + len(start_marker)
    end = raw_string.index(end_marker, start)
    return raw_string[start:end]

first_cap_re = re.compile('(.)([A-Z][a-z]+)')
all_cap_re = re.compile('([a-z0-9])([A-Z])')
def camel_case_to_underscore(name):
    s1 = first_cap_re.sub(r'\1_\2', name)
    return all_cap_re.sub(r'\1_\2', s1).lower()

def copy_dict(source_dict, diffs):
    result=dict(source_dict) # Shallow copy
    result.update(diffs)
    return result
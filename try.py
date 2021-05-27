def remove_dot(name):
    dname = name.split(" ")
    lst = []
    for i in dname:
        if("." in i):
            l = i.split(".")
            for j in l:
                if(j!=''):
                    lst.append(j)
        else:
            lst.append(i)
    rname = ' '.join(lst)
    return rname

def get_capitalized_name(name):
    rnames = remove_dot(name)
    lst = rnames.split()
    print(lst)
    capi_name = ' '.join([a.capitalize() for a in lst])
    return capi_name

if __name__ == '__main__':
    name = input('Enter name:')
    finalname = get_capitalized_name(name)
    print(finalname)
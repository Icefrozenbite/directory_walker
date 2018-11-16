import os


def longest_dir(main_dir): #the length of the longest directory tree
    length = []
    for path in os.walk(main_dir):
        path = path[0]
        path = path.split('\\')
        length.append(len(path) - 1)
    return max(length)


def most_file(main_dir):#the folder with the most files
    files_in_folder = {}
    for path in os.walk(main_dir):
        files_in_folder[path[0]] = len(path[2])
    return max((files, folder) for (folder, files) in files_in_folder.items())


def most_extension(main_dir):#the most frequent extension of files and the amount of files without extensions
    files = []
    extensions = {}
    no_extension = 0
    for path in os.walk(main_dir):
        files += path[2]
    for file in files:
        file = file.split('.')
        l = file[len(file) - 1]#extract the extension
        if file[len(file) - 1]:
            if l not in extensions:
                extensions[file[len(file) - 1]] = 1
            else:
                extensions[file[len(file) - 1]] += 1
        else:
            no_extension += 1
    return max((amount, extension) for (extension, amount) in extensions.items()), no_extension


def same_extension(main_dir):#the amount of folders in which exist files with the same extensions
    folder = []
    for path in os.walk(main_dir):
        files = path[2]
        extension_in_folder = []
        for file in files:
            file = file.split('.')
            if file[len(file)-1] not in extension_in_folder:
                extension_in_folder.append(file[len(file)-1])
            else:
                pass
        if len(extension_in_folder) == 1:
            folder.append(path[0])
    return len(folder)


def cyrillic_folder(main_dir):#the amount of folders with names only in Cyrillic letters and the most frequent first letter among the folder names
    folder = []
    for path in os.walk(main_dir):
        path = path[0]
        path = path.split('\\')
        for i in path:
            if i not in folder:
                folder.append(i)
    first_letter = {}
    cyrillic = 'АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя'
    non_cyr_folder = []
    for i in folder:
        if len(i) >= 1:
            if i[0] not in first_letter:
                first_letter[i[0]] = 1
            else:
                first_letter[i[0]] += 1
            for p in i:
                if p not in cyrillic:
                    non_cyr_folder.append(i)
    cyrillic_folder = [i for i in folder if i not in non_cyr_folder]
    for i in cyrillic_folder:
        if len(i) < 1:
            cyrillic_folder.remove(i)
    return max((amount, fl) for (fl, amount) in first_letter.items()), len(cyrillic_folder)


def main():
    dir = input('Please enter the address of the main folder:')
    m_e, n_e = most_extension(dir)
    f_f, c_f = cyrillic_folder(dir)
    print('The most frequent extension of files is:',m_e[1],', the total amount of which is', m_e[0],'.' )
    print('The amount of files without extensions is:', n_e, '.')
    print('The amount of folders with names only in Cyrillic letters is:', c_f, '.')
    print('The most frequent first letter among the folder names is:', f_f[1], ', the total amount of which is', f_f[0],'.')
    print('The depth of the deepest directory tree is:', longest_dir(dir), '.')
    print('The folder with the most files is', most_file(dir)[1], ', which contains', most_file(dir)[0], 'files.')
    print('The amount of folders which only contain files with the same extensions is:', same_extension(dir), '.')
    print('The depth of directory tree counts from 0; the rest count from 1.')

if __name__ == '__main__':
    main()
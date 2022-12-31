day = '7'
with open(f'./Day {day}/d{day}_input.txt', 'r') as file: 
    
    class File:
        def __init__(self, name, size) -> None:
            self.name = name
            self.size = int(size)

    class Directory:
        def __init__(self, name, parent = None):
            self.name = name
            self.children = []
            self.files = []
            self.parent = parent

        def get_size(self):
            size = 0
            if self.files == [] and self.children == []:
                return size
            for child in self.children:
                size += child.get_size()

            for file in self.files:
                size += file.size

            return size

        def add_child_dir(self, dir):
            self.children.append(dir)

        def add_child_file(self, file):
            self.files.append(file)


    current_dir = None
    for line in file.readlines():
        line = line.strip()
        if line == '$ cd /':
            root = Directory('/')
            current_dir = root
        
        elif line.find('$ cd') != -1:
            if line.find('..') != -1:
                current_dir = current_dir.parent
            else:
                dirname = line.split(' ')[2]
                for child in current_dir.children:
                    if child.name == dirname:
                        current_dir = child


        if line.find('dir') != -1:
            dir = Directory(name = line[4:], parent = current_dir)
            current_dir.add_child_dir(dir = dir)
        elif line.find('$') == -1:
            file = File(line.split(' ')[1], line.split(' ')[0])
            current_dir.add_child_file(file = file)
    
    directory_sizes = []

    def update_array(directory):
        global directory_sizes
        if directory.files == [] and directory.children == []:
            return 
        for child in directory.children:
            size = child.get_size()
            ##name = child.name
            ##directory_sizes.append([size, name])
            directory_sizes.append(size)
            update_array(child)
        return

    update_array(root)
    directory_sizes = filter(lambda x: x <= 100000, directory_sizes)
    
    print(sum(directory_sizes))

    ## Part 2

    directory_sizes = []
    update_array(root)
    needed_space = 30000000 - (70000000 - root.get_size())
    arr = []
    for size in directory_sizes:
        if size >= needed_space:
            arr.append(size)
    
    print(min(arr))
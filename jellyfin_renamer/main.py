import os
import sys

# 检查参数 长度
if len(sys.argv) != 2:
    print('no path here')
    exit(0)
path = sys.argv[1]

# 判断路径是否存在
if not os.path.exists(path):
    print('wrong path')
    exit(0)

project = path.split(os.sep)[-1]

for path, dir_list, _ in os.walk(path):
    for dir_name in dir_list:
        if dir_name.startswith('Season'):
            # 获取季号
            season = dir_name.split(' ')[-1]
            file_list = os.listdir(os.path.join(path, dir_name))

            count = 1
            last_suffix = ''
            for file in file_list:
                suffix = file.split('.')[-1]
                if not (last_suffix == '' or suffix == last_suffix):
                    count = 1

                new_name = project + ' S' + season + 'E' + format(count, '0>2d') + '.' + suffix
                print('rename', os.path.join(path, dir_name, file), '→', os.path.join(path, dir_name, new_name))
                last_suffix = suffix
                count += 1
                os.rename(os.path.join(path, dir_name, file), os.path.join(path, dir_name, new_name))

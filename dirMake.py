import os
'''1.得到当前工作目录，即当前Python脚本工作的目录路径: os.getcwd()
    2.返回指定目录下的所有文件和目录名:os.listdir()
    3.函数用来删除一个文件:os.remove()
    4.删除多个目录：os.removedirs（r“c：\python”）
    5.检验给出的路径是否是一个文件：os.path.isfile()
    6.检验给出的路径是否是一个目录：os.path.isdir()
    7.判断是否是绝对路径：os.path.isabs()
    8.检验给出的路径是否真地存:os.path.exists()
    9.返回一个路径的目录名和文件名:os.path.split() eg os.path.split('/home/swaroop/byte/code/poem.txt') 结果：('/home/swaroop/byte/code', 'poem.txt') 
    10.分离扩展名：os.path.splitext()
    11.获取路径名：os.path.dirname()
    12.获取文件名：os.path.basename()
    13.运行shell命令: os.system()
    17.重命名：os.rename（old， new）
    18.创建多级目录：os.makedirs（r“c：\python\test”）
    19.创建单个目录：os.mkdir（“test”）
    23.获取文件大小：os.path.getsize（filename）'''
    # print(os.getcwd())
    # print(os.listdir(PATH))
    # print(os.path.exists(PATH))
    # print(os.getenv('pip'))
    # print(os.name)
    # # os.makedirs(r'C:\fuck\me')
    # print(os.path.getsize(r'D:\p1Talking about men you like.mp4'))

    #创建文件
    # f = open(r'D:\tr.mp4','w')
    #
    # print(type(os.listdir(PATH)))

def makeDirs(PATH):
    for i in os.walk(PATH):
        print(i)
        dirs = i[0]
        dir_str = ''.join(dirs)
        os.makedirs(dir_str.replace('C','D'))

def filePathUpdate(filePath,size):
    # '''C:\Users\Administrator\Desktop\1\22.mp4从原始的文件PATh到要生成的文件Path'''
    pathWith2 = os.path.splitext(filePath)
    pathNew = ''.join(pathWith2[0]).replace('C','D')  + ' ' +  size + '-实际大小' +''.join(pathWith2[1])
    return pathNew

def sizeHandle(filePath):
    size = os.path.getsize(filePath)
    if size >= 500000000:
        sizeGB = round(size/1000000000,2)
        return str(sizeGB) + 'GB'
    else:
        sizeMB = round(size / 1000000,2)
        return str(sizeMB) + 'MB'

def write(PATH):
    for i in os.walk(PATH):
        dirs = i[0]
        dir_str = ''.join(dirs)
        files = i[2]
        for file in files:
            #原版的所有的文件
            filePath = dir_str + '\\' + ''.join(file)

            size = sizeHandle(filePath)
            fileFinal = filePathUpdate(filePath, size)
            f = open(fileFinal,'w')
            f.close()


if __name__ == '__main__':
    PATH = r'C:\Users\Administrator\Desktop\1'
    makeDirs(PATH)
    write(PATH)
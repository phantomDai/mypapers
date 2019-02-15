"""
将v1版本的变异体的名字写入文件中
"""
import os


def writenames():

    """
    读取某一个文件中的子文件，
    并将目录名字写入指定的文件中
    """

    """变异体的根目录"""
    rootDir = 'C:\\Users\\Administrator\\Desktop\\cptiscas\\程序变异体的backup\\V1'

    #获取所有待测对象的名字
    objectNames = os.listdir(rootDir)


    for name in objectNames :

        tempDir = rootDir + "\\" + name

        mutantNames = os.listdir(tempDir)

        fileName = tempDir + "\\" + name + ".txt"

        file = open(fileName,'w')

        for mutantName in mutantNames:
            file.write(mutantName + "\n")

        file.close()

if __name__ == '__main__':
    writenames()









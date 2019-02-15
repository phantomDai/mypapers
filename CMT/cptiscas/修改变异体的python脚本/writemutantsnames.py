"""
该脚本根据不同的测试场景将变异体的名字写入对应的文件中
"""
import os

def writeNames():

    """变异体的根目录"""
    rootDir = 'D:\\IDEAProjects\\cptiscas\\src\\main\\java\\mutants'

    """所有程序的名字"""
    dirs = os.listdir(rootDir)

    fileNames = ["sequentialAndsequential", "concurrentAndconcurrent", "sequentialAndconcurrent", "concurrentAndsequential"]

    for dir in dirs :

        """在mutantInfo目录下创建对应的程序名字"""
        tempDir = 'D:\\IDEAProjects\\cptiscas\\src\\main\\java\\mutantsinfo'

        programDir = tempDir + '\\' + dir

        """判断要创建的文件夹是否存在"""
        isExits = os.path.exists(programDir)

        if not isExits:
            os.mkdir(programDir)

        mutants = os.listdir(rootDir + '\\' + dir)

        """创建文件并将变异体的名字写入"""
        for name in fileNames :
            file = open(programDir + '\\' + name, 'w')
            for mutant in mutants:
                file.write(mutant + "\n")

            file.close()


if __name__ == '__main__':
    writeNames()








import ast, traceback
from tqdm import tqdm
import codex
import os

addEndDoc = "import random\n\n"

def __removeRedundantLines(fileStr):
    fileStr2 = ''
    fileStrArr = fileStr.split("\n")
    for line in fileStrArr:
        if (not line.strip() == ''):
            fileStr2 += line + "\n"
    return fileStr2.replace("\n\n\n", "\n\n").replace("\n\n", "\n")

def compileWithoutCorrection(filename):
    if not filename.endswith(".nl"):
        return
    print("Compiling:",filename+"...")
    filename = filename.replace(".nl", "")
    fileStr = codex.compilePrompt

    with open(filename+".nl", 'r') as file:
        for line in tqdm(file):
            line = line.replace("\n", "").replace("\r", "").replace("\"", "'")
            if line.strip().startswith("(") and line.strip().endswith(")"):
                continue

            if line.strip() == "":
                fileStr += "\n"
            else:
                origLine = line
                line = "\n"+__getStartingTabs(line)+"# CMD: " + line.strip()+"\n"
                fileStr += line

                response = ''
                for i in range(0,5):
                    response = codex.completeDavinci(
                        prompt=fileStr,
                        temperature=0.0,
                        max_tokens=500,
                        frequency_penalty=1.0,
                        presence_penalty=1.4,
                        stop=["#"]
                    )
                    if(not response.strip() == ''):
                        fileStr += response
                        break
                    else:
                        print("Line: \""+origLine.strip()+"\" hasn't produced any code: ("+str(i)+"\\5)...")

    fileStr = fileStr.replace(codex.compilePrompt, "").replace("\r", "\n")
    fileStr = __removeRedundantLines(fileStr)

    f = open(filename + ".py", "w")
    f.write(addEndDoc+fileStr)
    f.close()



def __checkCompilation(filename):
    print("Checking",filename,"for compilation errors...")
    with open(filename) as f2:
        source = f2.read()
    valid = True
    try:
        ast.parse(source)
    except:
        valid = False
        print("Compiled with syntax errors.")
        traceback.print_exc()
    if(valid):
        print("Compiled successfully.")
        return True
    else:
        return False

def __getStartingTabs(line):
    str= ''
    for char in line:
        if (not char == '\t') and (not char == ' '):
            return str
        else:
            str += char
    return str

def __replace_last(string, find, replace):
    reversed = string[::-1]
    replaced = reversed.replace(find[::-1], replace[::-1], 1)
    return replaced[::-1]


def compile(filename):
    directory = filename.replace(".nl", "")

    save = directory+"\\code.nl"
    if(not os.path.exists(directory)):
        os.makedirs(directory)
    codex.correctTabs(filename, save)
    compileWithoutCorrection(save)
    if(not __checkCompilation(directory+"\\code.py")):
        codex.fixPythonCode(directory+"\\code.py",directory + "\\code_fixed.py")
        return directory + "\\code_fixed.py"
    return directory + "\\code.py"

def compileAndRun(filename):
    run(compile(filename))

def run(filename):
    print("\nRunning:",filename,"...\n----------------------------------------------------------")
    exec(open(filename).read())
# java -jar ffdec.jar -export image "./test" "./swf/6f1cceac76b8d66a308261078bb938e6.swf"

import os, subprocess, shutil, time, threading

# ANSI escape codes for colors
class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# Example usage
def ConsoleLog(text: str, color: str = ""):
    truecolor = Color.CYAN
    if color.lower() == "red":
        truecolor = Color.RED
    elif color.lower() == "blue":
        truecolor = Color.BLUE
    elif color.lower() == "yellow":
        truecolor = Color.YELLOW
    
    print(truecolor + text + Color.END)

def split_list(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]



# export images
if False:
    file_names = os.listdir(r"..\Resource\image\bomb\bullet")

    files = [x.replace(".swf", "") for x in file_names if ".swf" in x]
    print(files)
    threads = []
    
    for name in files:
        def exporting(name):
            folder = f"./explosion/{name.replace('bullet', '')}"
            if not os.path.exists(folder):
                # If it doesn't exist, create it
                os.makedirs(folder)
                ConsoleLog(f"Directory {name} created successfully.", "blue")
            else:
                print(f"Directory {name} already exists.")
            
            application_path = f'java -jar ffdec.jar -export image "{folder}" "../Resource/image/bomb/bullet/{name}.swf"'
            
            try:
                subprocess.run(application_path)
                ConsoleLog("Application executed successfully.", "yellow")
            except subprocess.CalledProcessError as e:
                ConsoleLog(f"Error while executing application: {e}", "red")
                os.removedirs(folder)
                
        # threads.append(threading.Thread(target=exporting, args=(name,)))
        exporting(name)
    
    # print(list(split_list(threads, 10)))
    
    # for threads_list in list(split_list(threads, 10)):
    #     for thread in threads_list:
    #         thread.start()

    #     for thread in threads_list:
    #         thread.join()


if False:
    for folder in os.listdir("./output"):
        path_dir = f"./output/{folder}"
        if len(os.listdir(path_dir)) == 0:
            shutil.copyfile(f'./swf/{folder}.swf', f'./other/{folder}.swf')
            ConsoleLog(folder)

if True:
    for folder in os.listdir("./bullet"):
        path_dir = f"./bullet/{folder}"
        folders = ["preshoot", "blass", "bullet"]
        for name in folders:
            if not os.path.exists(os.path.join(path_dir, name)):
                # If it doesn't exist, create it
                os.makedirs(os.path.join(path_dir, name))
                ConsoleLog(f"Directory {folder} / {name} created successfully.", "blue")
            else:
                print(f"Directory {folder} / {name} already exists.")
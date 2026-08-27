# System-management libraries:
import subprocess
import shutil
import os


# Configuration index:
CONFIGURATION = {
    "script": "run.py",
    "name": "bingo",
    "icon": os.path.join(os.path.dirname(__file__), "bingo.ico"),
    "console": False,
    "data": [],
    "hidden": [],
    }


def build():
    
    # Cleaning  old builds:
    shutil.rmtree("build", ignore_errors=True)
    shutil.rmtree("dist", ignore_errors=True)
    
    # Creating build  command
    cmd = ["pyinstaller", "--onefile", "--name", CONFIGURATION["name"]]
    
    # Adjusting console parameter:
    if not CONFIGURATION["console"]:
        cmd.append("--noconsole")
    
    # Adjusting icon parameter:
    if CONFIGURATION["icon"] and os.path.exists(CONFIGURATION["icon"]):
        cmd.extend(["--icon", CONFIGURATION["icon"]])
        
    # Adding data to parameters:
    for src, dst in CONFIGURATION["data"]:
        if os.path.exists(src):
            cmd.extend(["--add-data", f"{src}{os.pathsep}{dst}"])
            
    # Adding hidden imports:
    for imp in CONFIGURATION["hidden"]:
        cmd.extend(["--hidden-import", imp])
        
    # Adding script to parameters:
    cmd.append(CONFIGURATION["script"])
    
    # Running build command:
    subprocess.run(cmd)


if __name__ == "__main__":
    build()


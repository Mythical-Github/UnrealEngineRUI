import os
import subprocess
import sys
from pathlib import Path

# Get the VS140COMNTOOLS environment variable
vs_tools_path = os.getenv("VS140COMNTOOLS")

# Check if the VS140COMNTOOLS variable is set
if not vs_tools_path:
    print("Visual Studio 2015 environment variable (VS140COMNTOOLS) not found. Please check your installation.")
    sys.exit(1)

# Construct the path to Visual Studio 2015's devenv.exe
vs2015_path = Path(vs_tools_path).parent / "IDE" / "devenv.exe"

# Check if devenv.exe exists at the expected location
if not vs2015_path.is_file():
    print(f"Visual Studio 2015 (VS 14.0) not found at the expected location: {vs2015_path}")
    sys.exit(1)

# Find all .sln files in the same directory as this script
script_dir = Path(__file__).parent
sln_files = list(script_dir.glob("*.sln"))

# If no .sln files were found, print a message and exit
if not sln_files:
    print("No .sln files found in the current directory.")
    sys.exit(0)

# Open each .sln file with Visual Studio 2015
for sln_file in sln_files:
    print(f"Opening solution: {sln_file}")
    subprocess.run([str(vs2015_path), str(sln_file)])

print("All solutions opened.")

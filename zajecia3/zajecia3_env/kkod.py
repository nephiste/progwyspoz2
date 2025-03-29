import subprocess


file_to_check = "zlykod.py"

result = subprocess.run(["flake-8", file_to_check], capture_output=True, text=True)

print(result.stdout)
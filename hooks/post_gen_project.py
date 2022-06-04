import subprocess

MESSAGE_COLOR = "\x1b[34m"
RESET_COLOR = "\x1b[0m"

print(f"{MESSAGE_COLOR}Almost donde")
print(f"Initializing git repository...{RESET_COLOR}")

subprocess.call(["git", "init"])
subprocess.call(["git", "add", "."])
subprocess.call(["git", "commit", "-m", "Initial commit"])

print(f"{MESSAGE_COLOR}Done!{RESET_COLOR}")
import subprocess


subprocess.call(["git", "init"])
subprocess.call(["git", "config", "user.name", "{{cookiecutter.full_name}}"])
subprocess.call(["git", "config", "user.email", "{{cookiecutter.email}}"])
subprocess.call(["git", "add", "."])
subprocess.call(["git", "commit", "-m", "Initial commit"])

remote = "{{cookiecutter.git_remote}}".rstrip()

if len(remote) > 0 and remote != "Git remote (if known)":
    subprocess.call(["git", "remote", "add", "origin", remote])

import subprocess

data = (
    # subprocess.run(["netsh", "wlan", "show", "profiles"])
    # run subprocess command to check all profiles
    subprocess.check_output(["netsh", "wlan", "show", "profiles"])
    .decode("utf-8")
    .split("\n")
)
# Capture all profiles by formatting
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

print("="*45)
print("{:<30}|  {:<}".format("Connected Network(s)", "Passwords"))
print("="*45)
for i in profiles:
    # run subprocess to check passwords
    results = (
        subprocess
        .check_output(["netsh", "wlan", "show", "profile", i, "key=clear"])
        .decode("utf-8")
        .split("\n")
    )
    # capture all passwords by formatting
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    
    try:
        print("{:<30}|  {:<}".format(i, results[0]))
    except IndexError:
        print("{:<30}|  {:<}".format(i, ""))
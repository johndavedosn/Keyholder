import libs.Paramify as Paramify
import subprocess
import os
config = Paramify.ConfigFile("component_config.json")
components: list[dict] = config.load_param("components", "")
for component in components:
    name = component["name"]
    enabled = component["enabled"]
    if enabled:
        if os.name == "nt":
            subprocess.run(["py", name])
        if os.name == "posix":
            subprocess.run(["python3", name])    
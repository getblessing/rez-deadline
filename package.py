
name = "deadline"

version = "10"  # (WIP)


def commands():
    env = globals()["env"]
    resolve = globals()["resolve"]

    # DCC App Setup
    if "houdini" in resolve:
        hou_client = "T:/lib/avalon/modules/Deadline/houdini/Client"
        env.HOUDINI_PATH.append(hou_client)
        env.PYTHONPATH.append(hou_client)

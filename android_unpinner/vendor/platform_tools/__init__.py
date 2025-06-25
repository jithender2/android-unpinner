import subprocess
import shlex
import logging
"""
def adb(cmd: str) -> subprocess.CompletedProcess[str]:
    if isinstance(cmd, str) and cmd.startswith("shell "):
        # Run full shell command
        full_cmd = ["adb", "shell", cmd[6:]]  # remove leading "shell "
    else:
        import shlex
        full_cmd = ["adb"] + shlex.split(cmd)
    
    try:
        proc = subprocess.run(full_cmd, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        logging.debug(f"cmd='{cmd}'\n{e.stdout=}\n{e.stderr=}")
        raise
    logging.debug(f"cmd='{cmd}'\n{proc.stdout=}\n{proc.stderr=}")
    return proc

import subprocess
import logging
import shlex
"""
"""_def adb(cmd: str) -> subprocess.CompletedProcess[str]:
    if cmd.startswith("shell "):
        # Split at first space only: "shell" and the actual shell command
        shell_cmd = cmd[6:]
        full_cmd = ["adb", "shell", shell_cmd]
    else:
        full_cmd = ["adb"] + shlex.split(cmd)
    
    try:
        proc = subprocess.run(full_cmd, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        logging.debug(f"cmd='{cmd}'\n{e.stdout=}\n{e.stderr=}")
        raise
    return proc
"""
def adb(cmd: str) -> subprocess.CompletedProcess[str]:
    """Run adb with proper quoting and shell handling."""
    if cmd.startswith("shell "):
        # Run the entire string after "shell " in one shell session
        full_cmd = ["adb", "shell", cmd[6:]]
    else:
        full_cmd = ["adb"] + shlex.split(cmd)

    try:
        proc = subprocess.run(full_cmd, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        logging.debug(f"ADB command failed: {cmd}\nstdout: {e.stdout}\nstderr: {e.stderr}")
        raise
    logging.debug(f"ADB command: {cmd}\nstdout: {proc.stdout}\nstderr: {proc.stderr}")
    return proc

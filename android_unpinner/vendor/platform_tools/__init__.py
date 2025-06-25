import subprocess
import shlex
import logging
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

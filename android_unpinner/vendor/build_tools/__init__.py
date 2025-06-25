import subprocess
import sys
from functools import cache
from pathlib import Path
import platform

here = Path(__file__).absolute().parent

if sys.platform == "win32":
    aapt2_binary = here / "win32" / "aapt2.exe"
    apksigner_binary = here / "win32" / "apksigner.bat"
    zipalign_binary = here / "win32" / "zipalign.exe"
elif sys.platform == "darwin":
    aapt2_binary = here / "darwin" / "aapt2"
    apksigner_binary = here / "darwin" / "apksigner"
    zipalign_binary = here / "darwin" / "zipalign"
else:
    if platform.machine()=="aarch64":
        aapt2_binary = here / "linux-aarch64" / "aapt2"
        apksigner_binary = here / "linux-aarch64" / "apksigner"
        zipalign_binary = here / "linux-aarch64" / "zipalign"
    else:
       aapt2_binary = here / "linux" / "aapt2"
       apksigner_binary = here / "linux" / "apksigner"
       zipalign_binary = here / "linux" / "zipalign"


def zipalign(apk_file: Path) -> None:
    apk_aligned = apk_file.with_suffix(".aligned.apk")
    subprocess.run([
        zipalign_binary,
        "-p", "4",
        apk_file,
        apk_aligned
    ], check=True)
    apk_file.unlink()
    apk_aligned.rename(apk_file)


def sign(apk_file: Path) -> None:
    # android-unpinner.jks was generated as follows:
    # keytool -genkey -v -keystore android-unpinner.jks -alias android-unpinner -keyalg RSA -keysize 2048 -validity 3650
    subprocess.run([
        apksigner_binary,
        "sign",
        "--v4-signing-enabled",
        "false",
        '--ks',
        here / "android-unpinner.jks",
        '--ks-pass',
        'pass:correcthorsebatterystaple',
        '--ks-key-alias',
        'android-unpinner',
        apk_file
    ], check=True)


@cache
def package_name(apk_file: Path) -> str:
    return subprocess.run([
        aapt2_binary,
        "dump",
        "packagename",
        apk_file,
    ], check=True, capture_output=True, text=True).stdout.strip()

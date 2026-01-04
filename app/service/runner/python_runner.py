import os
import subprocess
import tempfile

TIMEOUT = 5.0


def run_python(code: str, input_data: str = "") -> dict:
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "main.py")

        with open(path, "w") as f:
            f.write(code)

        try:
            proc = subprocess.run(
                [
                    "docker", "run", "--rm",
                    "-i",
                    "-v", f"{tmp}:/app",
                    "juiz-python",
                    "python3", "/app/main.py"
                ],
                input=input_data,
                capture_output=True,
                text=True,
                timeout=TIMEOUT
            )

            return {
                "stdout": proc.stdout,
                "stderr": proc.stderr,
                "exit_code": proc.returncode,
                "status": "OK" if proc.returncode == 0 else "RUNTIME_ERROR"
            }

        except subprocess.TimeoutExpired:
            return {
                "stdout": "",
                "stderr": "Time Limit Exceeded",
                "exit_code": -1,
                "status": "TLE"
            }

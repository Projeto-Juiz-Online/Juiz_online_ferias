import os
import subprocess
import tempfile

TIMEOUT = 2.5

def run_cpp(code: str, input_data: str = "") -> dict:
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "main.cpp")
        binary = os.path.join(tmp, "main")

        with open(path, "w") as f:
            f.write(code)

        compile = subprocess.run(
            [
                "docker", "run", "--rm",
                "-v", f"{tmp}:/app",
                "juiz-cpp",
                "g++", "/app/main.cpp", "-O2", "-o", "/app/main"
            ],
            capture_output=True,
            text=True   
        )

        if compile.returncode != 0:
            return {
                "stdout": "",
                "stderr": compile.stderr,
                "exit_code": compile.returncode,
                "status": "RUNTIME_ERROR"
            }

        try:
            proc = subprocess.run(
                [
                    "docker", "run", "--rm",
                    "-i",
                    "-v", f"{tmp}:/app",
                    "juiz-cpp",
                    "/app/main"
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

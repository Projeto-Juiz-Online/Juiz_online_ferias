def normalize(output: str) -> list[str]:
    lines = [line.rstrip() for line in output.splitlines()]
    while lines and lines[-1] == "":
        lines.pop()
    return lines

def judge(run_result: dict, expected_output: str) -> dict:
    status = run_result["status"]

    if status == "TLE":
        return{
            **run_result,
            "verdict": "TLE"
        }
    
    if status == "RUNTIME_ERROR":
        return{
            **run_result,
            "verdict": "RUNTIME_ERROR"
        }
    
    expected = normalize(expected_output)
    user_output= normalize(run_result["stdout"])

    if user_output == expected:
        return{
            **run_result,
            "verdict": "AC"
        }
    else:
        return{
            **run_result,
            "verdict": "WA"
        }
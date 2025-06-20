import pytest
import asyncio
import subprocess

@pytest.mark.asyncio
async def test_run_shell_script():
    # Define your shell script path
    script_path = "run_install_deps.sh"

    # Run the shell script asynchronously
    proc = await asyncio.create_subprocess_shell(
        script_path,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()

    # Decode output to string
    out_str = stdout.decode().strip()
    err_str = stderr.decode().strip()

    # You can print output or assert on it
    print("STDOUT:", out_str)
    print("STDERR:", err_str)

    # Assert the shell script exited with code 0 (success)
    assert proc.returncode == 0

    # Optional: assert on expected output content
    # assert "expected output" in out_str

if __name__ == "__main__":
    import sys
    import pytest
    sys.exit(pytest.main([__file__, "-s"]))


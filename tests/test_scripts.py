import os
import subprocess

def test_scripts_exit_zero():
    scripts = ["idea2prod.sh", "local_check.sh", "lint_fix_loop.sh", "compliance_fix_loop.sh", "doc_improve_loop.sh"]
    scripts_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    for script in scripts:
        script_path = os.path.join(scripts_dir, script)
        result = subprocess.run(["bash", script_path], capture_output=True)
        assert result.returncode == 0

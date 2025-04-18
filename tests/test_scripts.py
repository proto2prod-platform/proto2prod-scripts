import subprocess
def test_scripts_exit_zero():
    scripts = ["idea2prod.sh", "local_check.sh", "lint_fix_loop.sh", "compliance_fix_loop.sh", "doc_improve_loop.sh"]
    for script in scripts:
        result = subprocess.run(["bash", script], capture_output=True)
        assert result.returncode == 0

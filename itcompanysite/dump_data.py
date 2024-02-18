import subprocess

powershell_path = r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe'
ps1_file1 = r'dumpdata.ps1'

result = subprocess.run([powershell_path, '-File', ps1_file1], capture_output=True, text=True)

if result.returncode == 0:
    print("Команда выполнена успешно.")
else:
    print("Произошла ошибка при выполнении команды.")
    print("Стандартный вывод (stdout):", result.stdout)
    print("Стандартный поток ошибок (stderr):", result.stderr)

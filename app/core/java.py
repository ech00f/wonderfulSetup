import subprocess

def get_java_version():
    try:
        result = subprocess.run(
            ["java", "-version"], 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            text=True
        )

        if result.returncode == 0:
            words = result.stderr.split()

            for word in words:
                if '"' in word:
                    vers = word.replace('"', '')
                    parts = vers.replace('"', '').split('.')
                    if parts[0] == '1' and len(parts) > 1:
                        return parts[1]
                    return parts[0]
    except Exception:
        print("Java not found")
        return "NF"
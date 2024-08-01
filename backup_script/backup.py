import os
import tarfile
from datetime import datetime

def backup(src_dir, dest_dir):
    if not os.path.exists(src_dir):
        print(f"O diretório de origem '{src_dir}' não existe.")
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"backup_{timestamp}.tar.gz"
    backup_path = os.path.join(dest_dir, backup_filename)

    try:
        with tarfile.open(backup_path, "w:gz") as tar:
            tar.add(src_dir, arcname=os.path.basename(src_dir))
        print(f"Backup realizado com sucesso em: {backup_path}")
    except Exception as e:
        print(f"Erro ao fazer o backup: {e}")

if __name__ == "__main__":
    source_directory = "./backup"
    destination_directory = "."
    
    backup(source_directory, destination_directory)

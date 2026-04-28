import json
from pathlib import Path
from estrutura import criar_estrutura
from utils import get_base_dir, get_resource_path

def main():
    # Pega o diretório base (onde está o programa)
    base_dir = get_base_dir()

    config_path = get_resource_path("config.json")

    # Carrega o arquivo de config
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    # Cria a pasta "Backup"
    backup_path = base_dir / "Backup"
    backup_path.mkdir(exist_ok=True)

    # Cria toda a estrutura dentro dela
    criar_estrutura(backup_path, config["Backup"])

# Executa o programa
if __name__ == "__main__":
    main()
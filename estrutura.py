from pathlib import Path

def criar_estrutura(base_dir, estrutura):
    for pasta, subpastas in estrutura.items():
        # Cria a pasta principal (ex: Backup/ Disco C)
        caminho = base_dir / pasta
        caminho.mkdir(exist_ok=True)

        # Cria as subpastas (se existirem)
        for sub in subpastas:
            (caminho / sub).mkdir(exist_ok=True)
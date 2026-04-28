import sys
from pathlib import Path

def get_base_dir():
    # Retorna o dicioário onde o programa está rodando.
    # - Se for .exe -> Pega o local do executável
    # - Se for .py -> Pega o local do script
    if getattr(sys, 'frozen', False):
        # Quando virar .exe
        return Path(sys.executable).parent
    # Quando rodar como script
    return Path(__file__).parent

def get_resource_path(filename):
    if getattr(sys, 'frozen', False):
        return Path(sys._MEIPASS) / filename
    
    return Path(filename)

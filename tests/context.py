import src.gestor_despesas as gestor_despesas
import os
import sys

# Adiciona o diretório pai ao sys.path para conseguir importar src/
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

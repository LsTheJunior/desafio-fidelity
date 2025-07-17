"""
Configuração centralizada de logging para a aplicação.

Define o formato e o nível de logging padrão, além de expor o logger principal.
"""

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)
logger = logging.getLogger("app")

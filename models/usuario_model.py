from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class Usuario:
    id: Optional[int] = None
    nome: Optional[str] = None
    descricao_pessoal: Optional[str] = None
    data_nascimento: Optional[date] = None
    email: Optional[str] = None
    senha: Optional[str] = None
    perfil: Optional[int] = None    
    verificado: Optional[bool] = None
from fastapi import APIRouter
from models.evento import EventoResponse

router = APIRouter(
    prefix="/eventos",
    tags=["Eventos"]
)

eventos = [
    {
        "id": 1,
        "nome": "Workshop de Python",
        "organizador_id": 1001,
        "token_auditoria": "AUD-ABC123"
    },
    {
        "id": 2,
        "nome": "Meetup de Segurança",
        "organizador_id": 1002,
        "token_auditoria": "AUD-XYZ789"
    }
]


@router.get("/")
def listar_eventos():
    return eventos


@router.post("/", response_model=EventoResponse)
def criar_evento(evento: dict):
    novo_evento = {
        "id": len(eventos) + 1,
        "nome": evento["nome"],
        "organizador_id": 1003,
        "token_auditoria": "AUD-INTERNO-001"
    }

    eventos.append(novo_evento)

    return novo_evento


@router.post("/sem-response-model")
def criar_evento_sem_response_model(evento: dict):
    novo_evento = {
        "id": len(eventos) + 1,
        "nome": evento["nome"],
        "organizador_id": 1003,
        "token_auditoria": "AUD-INTERNO-002"
    }

    eventos.append(novo_evento)

    return novo_evento


@router.get("/{evento_id}")
def obter_evento(evento_id: int):
    for evento in eventos:
        if evento["id"] == evento_id:
            return evento

    return {"message": "Evento não encontrado"} 
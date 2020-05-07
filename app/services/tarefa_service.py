from ..models import Tarefa


def cadastrar_tarefa(tarefa):
    Tarefa.objects.create(titulo=tarefa.titulo,
                          descricao=tarefa.descricao,
                          data_expiracao=tarefa.data_expiracao,
                          prioridade=tarefa.prioridade)


def listar_tarefas():
    return Tarefa.objects.all()


def listar_tarefa_id(id):
    return Tarefa.objects.get(id=id)


def editar_tarefa(tarefa_db, tarefa_nova):
    tarefa_db.titulo = tarefa_nova.titulo
    tarefa_db.descricao = tarefa_nova.descricao
    tarefa_db.data_expiracao = tarefa_nova.data_expiracao
    tarefa_db.prioridade = tarefa_nova.prioridade
    tarefa_db.save(force_update=True)


def remover_tarefa(tarefa_db):
    tarefa_db.delete()


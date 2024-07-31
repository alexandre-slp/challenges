# Gerenciamento de Lista de Tarefas

Você deve implementar funções que gerenciam uma lista de tarefas.  
Cada tarefa possui um título e uma descrição.  
As tarefas devem ser mantidas na ordem de criação a menos que a ordem seja alterada explicitamente.

### Funcionalidades:

- **Adicionar Tarefa**  
  Descrição: Adiciona uma tarefa ao final da lista.  
  Função: _add_task (name, description)_
    - name [_obrigatório_]: Nome da tarefa.
    - description [_opcional_]: Descrição da tarefa.
  
  Output: A lista de tarefas atualizada.

  ---

- **Remover Tarefa**  
  Descrição: Remove uma tarefa específica da lista com base no título.  
  Função: _remove_task (name)_
    - name [_obrigatório_]: Nome da tarefa.

  Output: A lista de tarefas atualizada. Se a tarefa não for encontrada, a lista permanece inalterada.

  ---

- **Buscar Tarefa**  
  Descrição: Retorna a posição de uma tarefa específica da lista com base no título.  
  Função: _find_task (name)_
    - name [_obrigatório_]: Nome da tarefa.

  Output: A posição da tarefa caso ela exista na lista ou -1 caso contrário.

  ---

- **Mover Tarefa**  
  Descrição: Move uma tarefa para a posição posterior a tarefa indicada.  
  Função: _move_task_after (name, after)_
    - name [_obrigatório_]: Nome da tarefa que deve ser movida.
    - after [_obrigatório_]: Nome da tarefa que será utilizada como referência para onde a tarefa será movida.

  Output: A lista de tarefas atualizada. Se a tarefa ou a posição não forem válidas, a lista permanecerá inalterada.

  ---

- **Listar Tarefas**  
  Descrição: Lista todas as tarefas na ordem atual.  
  Função: _list_tasks ()_  
  Output: Listagem de todas as tarefas, cada uma com seu título e descrição.

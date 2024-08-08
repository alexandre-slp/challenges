# Gerenciamento de Lista de Tarefas

Deve ser criada uma estrutura que gerenciem uma lista de tarefas.  
Cada tarefa possui um título e uma descrição. Todos os nomes e descrições são minúsculos e sem caracteres especiais.  
As tarefas devem ser mantidas na ordem de criação a menos que a ordem seja alterada explicitamente.  
A posição inicial é 0 (zero) e a última é 1 a mais que a quantidade de tarefas existentes.  
A estrutura deve implementar as funcionalidades descritas a baixo.

### Funcionalidades:

- **Adicionar Tarefa**  
  Descrição: Adiciona uma tarefa em uma posição específica ou ao final da lista caso não seja explicitamente indicada.  
  Função: _add_task (name, description, position)_
    - name [_obrigatório_]: Nome da tarefa.
    - description [_opcional_]: Descrição da tarefa.
    - add_position [_opcional_]: Posição que a tarefa deve ser adicionada.  
  
  Output: Nenhum.

  ---

- **Remover Tarefa**  
  Descrição: Remove uma tarefa específica da lista com base no título.  
  Função: _remove_task (name)_
    - name [_obrigatório_]: Nome da tarefa.

  Output: A tarefa removida, se a tarefa não for encontrada nada é retornado.

  ---

- **Buscar Tarefa**  
  Descrição: Retorna a posição de uma tarefa específica da lista com base no título.  
  Função: _find_task (name)_
    - name [_obrigatório_]: Nome da tarefa.

  Output: A posição da tarefa caso ela exista ou -1 caso contrário.

  ---

- **Mover Tarefa**  
  Descrição: Move uma tarefa para a posição indicada.  
  Função: _move_task (name, new_position)_
    - name [_obrigatório_]: Nome da tarefa que deve ser movida.
    - new_position [_obrigatório_]: Posição para onde a tarefa será movida.

  Output: Nenhum.

  ---

- **Listar Tarefas**  
  Descrição: Lista todas as tarefas na ordem atual.  
  Função: _list_tasks ()_  
  Output: Um array contendo todas tarefas na ordem, cada uma com seu título e descrição.

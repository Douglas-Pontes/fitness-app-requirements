# Tela: Cadastro / Edição de Treino `[VELA-4003]`

---

## Metadados
| Campo | Valor |
|---|---|
| **Nome da tela** | Cadastro / Edição de Treino |
| **Modulo** | Treinos |
| **Codigo** | VELA-4003 |
| **Prioridade** | 🔵 MVP |
| **Status** | 🟢 CONCLUIDO |
| **Ultima atualizacao** | 2026-06-18 |

---

## 1. Objetivo da Tela
> O que o usuario consegue fazer nesta tela? Qual problema ela resolve?

Formulário onde o **Treinador** cria um novo treino ou edita um treino da **sua** base reutilizável. O treino reúne **dados gerais** (nome, categoria, observações, áudio explicativo) e uma **lista de exercícios organizada em grupos numerados** (1, 2, 3…), servindo como **bloco montável** para depois compor as **Rotinas** dos alunos. Cada exercício recebe **séries, repetições e descanso (obrigatórios)** e uma **descrição de execução (opcional)** — a prescrição é definida já no cadastro do treino. A mesma tela serve para **criar** e **editar** (modo dinâmico: vem em branco ou pré-preenchida).

---

## 2. Quem Acessa / Pre-condicoes
> Quem pode ver esta tela? Quais condicoes precisam ser verdadeiras?

- **Usuario:** **Treinador** autenticado. O **Aluno** não acessa esta tela.
- **Pre-condicoes:**
  - Usuário deve estar logado com perfil de Treinador.
  - O treino é montado a partir dos **exercícios do próprio Treinador** (não há acervo global de exercícios — ver `[VELA-3003]`). Para adicionar um exercício ao treino, ele precisa já existir na base do Treinador.
- **Permissoes especiais:** Nenhuma além da role de Treinador.

---

## 3. Layout e Componentes Visuais
> Descreva a estrutura visual da tela de cima para baixo.

### 3.1 Header / Cabecalho
- Conteudo: Botão voltar (←) + Título "Novo treino" (criação) ou "Editar treino" (edição). A ação de salvar fica **apenas no botão primário do rodapé** (sem botão de salvar no topo).
- Comportamento: Fixo no topo. Ao tentar voltar com alterações não salvas, exibe modal de confirmação ("Descartar alterações?").

### 3.2 Corpo Principal
> **Tela única**: formulário em **fluxo contínuo** (rolagem vertical). Os blocos A–C abaixo são apenas **subtítulos discretos** que organizam o formulário — não são seções retráteis. Segue o layout simples dos demais formulários do app.

**Bloco A — Identificação**
- Componente: Campo de texto + select.
- Conteudo: Nome do treino e Categoria.

**Bloco B — Detalhes (opcional)**
- Componente: Textareas + gravador de áudio.
- Conteudo: Descrição, Observações gerais e Áudio do treino (gravado no app).
- Comportamento: O áudio mostra um player com duração após a gravação. **Não há vídeo no treino** — vídeo existe apenas por exercício (ver Bloco C).

**Bloco C — Exercícios (em grupos)** *(obrigatório — ao menos um exercício)*
- Componente: Lista de **grupos numerados**; cada grupo contém um ou mais **cards de exercício**, conforme o tipo.
- Conteudo:
  - Cada **grupo** tem um **número automático** (1, 2, 3…) e um **tipo opcional** (Normal, Bi-set, Tri-set, Superset, Drop-set).
  - Cada **card de exercício** exibe: **capa do vídeo do exercício** (thumbnail), nome do exercício, ícone de vídeo (se houver), os campos obrigatórios **Séries**, **Repetições** e **Descanso**, e a **Descrição de execução** (opcional).
- Comportamento:
  - Botão **"Adicionar exercício"** dentro de cada grupo e botão **"Adicionar grupo"** ao final da lista.
  - **Limite por tipo:** o tipo define quantos exercícios o grupo aceita — **Normal e Drop-set: 1**; **Bi-set e Superset: 2**; **Tri-set: 3**. Sem tipo, o grupo é tratado como **Normal (1 exercício)**. Ao atingir o limite, o botão "Adicionar exercício" do grupo fica indisponível.
  - Exibe a mensagem de ajuda **"Arraste os cards para reordenar os exercícios"** orientando a reordenação.
  - **Ordenação:** os grupos seguem a ordem 1 → 2 → 3…; dentro de cada grupo, os exercícios são reordenáveis por **arrastar (handle ⠿)**. A numeração de execução respeita o grupo e a posição dentro dele. As **letras A, B, C…** ficam **reservadas para a Rotina** (fluxo futuro).
  - No **seletor de exercícios** (ao adicionar), cada item traz um atalho: **ícone de vídeo** abre o vídeo em **modal/lightbox** por cima da lista; tocar no exercício abre a tela **Visualizar Exercício `[VELA-3002]`**.
  - Apenas exercícios **ativos** podem ser adicionados; inativos não aparecem como opção (ver RN08).

### 3.3 Footer / Rodape
- Conteudo: Botão primário "Salvar treino". Em telas menores, fixo na parte inferior.
- Comportamento: Desabilitado até os campos obrigatórios estarem válidos (Nome + Categoria + ao menos 1 exercício com Séries, Repetições e Descanso preenchidos).

---

## 4. Campos e Formularios

### Dados gerais do treino
| # | Nome do Campo | Tipo | Obrigatorio | Placeholder | Validacao | Mensagem de Erro |
|---|---|---|---|---|---|---|
| 1 | Nome do treino | Text | Sim | "Ex: Treino A — Peito e Tríceps" | Mín. 3 caracteres; **único na base do Treinador** | "Informe o nome do treino" / "Já existe um treino com esse nome" |
| 2 | Categoria | Select (único) | Sim | "Selecione a categoria" | Deve ser selecionada | "Selecione a categoria do treino" |
| 3 | Descrição | Textarea | Não | "Descreva o treino (opcional)" | — | N/A |
| 4 | Observações gerais | Textarea | Não | "Observações gerais sobre o treino (opcional)" | — | N/A |
| 5 | Áudio do treino | Gravação de áudio (no app) | Não | "Gravar instrução em áudio (opcional)" | Formato de áudio suportado; **duração máx. 2 minutos** | "Não foi possível salvar o áudio" / "O áudio pode ter no máximo 2 minutos" |

### Por exercício dentro do grupo
| # | Nome do Campo | Tipo | Obrigatorio | Placeholder | Validacao | Mensagem de Erro |
|---|---|---|---|---|---|---|
| 6 | Séries | Number | Sim | "Ex: 3" | Inteiro positivo | "Informe as séries" |
| 7 | Repetições | Text | Sim | "Ex: 10-12" | — | "Informe as repetições" |
| 8 | Descanso | Number (segundos) | Sim | "Ex: 60" | Número **≥ 0** (0 é válido); **não pode ficar em branco** | "Informe o descanso" |
| 9 | Descrição de execução | Text/Textarea | Não | "Ex: cadência, drop-set, intercalar…" | — | N/A |

### Por grupo
| # | Nome do Campo | Tipo | Obrigatorio | Placeholder | Validacao | Mensagem de Erro |
|---|---|---|---|---|---|---|
| 10 | Tipo do grupo | Select (único) | Não | "Sem tipo (Normal)" | — | N/A |

### Opções dos campos de seleção (referência)
- **Categoria:** Aeróbico, Força e Potência, Resistência, Funcional, Mobilidade, Abdômen/Core. Opções **fixas**, seleção única.
- **Tipo do grupo (opcional):** **Normal** (exercício avulso), **Bi-set**, **Tri-set**, **Superset**, **Drop-set**. Em branco = **Normal**. O tipo define o **limite de exercícios** do grupo: Normal/Drop-set = **1**, Bi-set/Superset = **2**, Tri-set = **3**.

### Regras de Preenchimento
- O **número do grupo (1, 2, 3…)** é gerado **automaticamente** pela ordem — não é editável. As **letras A, B, C…** ficam reservadas para a **Rotina**.
- **Séries, repetições e descanso** são **obrigatórios** em cada exercício; a **descrição de execução** é opcional.
- O **Descanso** aceita **qualquer número, inclusive 0** (em segundos), mas **não pode ficar em branco**. *(Nos exercícios de um tri-set, o exemplo usa descanso 0 por coerência — emendados sem descanso entre eles —, mas isso é só ilustração, não uma regra do tipo.)*
- O treino **não tem vídeo próprio**; o vídeo existe **apenas por exercício** (a capa do card do exercício é a **capa do vídeo** daquele exercício).
- O **Áudio do treino** é **opcional** e descreve o **treino como um todo** (não um exercício específico) — gravado dentro do app.
- O treino precisa ter **ao menos um exercício** para ser salvo (o **Bloco C — Exercícios é obrigatório**); blocos vazios não são salvos.

---

## 5. Botoes e Acoes

| # | Componente | Label / Icone | Posicao | Estado Inicial | Acao ao Clicar |
|---|---|---|---|---|---|
| 1 | Botão primário | "Salvar treino" | Rodapé | Desabilitado até obrigatórios válidos | Valida → salva na base do Treinador → volta para a Lista `[VELA-4001]` com toast de sucesso |
| 2 | Botão voltar | ← | Header (esq.) | Ativo | Se houver alterações não salvas, abre modal "Descartar alterações?"; senão, volta |
| 3 | Botão | "Adicionar exercício" | Dentro de cada grupo | Ativo; **indisponível** quando o grupo atinge o limite do tipo | Abre o seletor de exercícios (com atalho de vídeo/visualização) |
| 4 | Botão | "Adicionar grupo" | Fim da lista de grupos | Ativo | Cria um novo grupo (próximo número), **sem tipo definido** (= Normal) |
| 5 | Ícone | ⠿ (arrastar) | Em cada card de exercício | Ativo | Reordena o exercício dentro do grupo |
| 6 | Ícone | 🗑 / "Remover" | Card de exercício e grupo | Ativo | Remove o exercício (ou o grupo e seus exercícios) do treino — com confirmação ao remover grupo com itens |
| 7 | Ícone | ▶ (vídeo) | Card/seletor de exercício | Visível se o exercício tiver vídeo | Abre o vídeo em modal/lightbox por cima da tela |
| 8 | Toggle | "Ativo / Inativo" | Topo do form (só edição) | Reflete o estado atual | Alterna disponibilidade. Ao **desativar**, exibe: "Treinos inativos continuam nas rotinas atuais, mas não podem ser adicionados a novas." |
| 9 | Botão | "Excluir treino" | Rodapé / menu (só edição) | Visível só em edição; **desabilitado se estiver em uso** | Abre modal de confirmação → exclui definitivamente (só se não estiver em nenhuma rotina) |

---

## 6. Estados da Tela

### 6.1 Estado Inicial / Vazio
- **Criação:** campos gerais em branco; um **grupo 1 vazio** já visível com o botão "Adicionar exercício"; "Salvar" desabilitado.
- **Edição:** campos e blocos pré-preenchidos com os dados do treino.

### 6.2 Estado de Carregamento (Loading)
- Ao salvar: spinner sobre o botão "Salvar treino", botão desabilitado durante a requisição.
- Ao validar link do YouTube ou abrir o seletor de exercícios: indicador de carregamento na respectiva área.

### 6.3 Estado de Erro
- **Erro de campo:** borda vermelha + mensagem abaixo do campo (ver tabelas da Seção 4).
- **Sem exercícios:** ao tentar salvar sem nenhum exercício, mensagem "Adicione ao menos um exercício ao treino".
- **Erro de rede:** toast "Sem conexão. Tente novamente." (mantém os dados preenchidos).
- **Erro da API ao salvar:** toast "Não foi possível salvar o treino. Tente novamente."

### 6.4 Estado de Sucesso
- Toast "Treino salvo!" + redirect para a Lista `[VELA-4001]`, com o treino salvo destacado/no topo.

### 6.5 Estado Desabilitado / Bloqueado
- N/A — todo treino é do próprio Treinador e editável por ele.

---

## 7. Fluxo de Navegacao

### De onde o usuario chega nesta tela
| Origem | Gatilho |
|---|---|
| Lista de Treinos `[VELA-4001]` | Treinador toca em "Novo treino" (FAB "+") |
| Lista de Treinos `[VELA-4001]` | Treinador toca em "Editar" em um treino |
| Visualizar Treino `[VELA-4002]` | Treinador toca em "Editar" |

### Para onde o usuario pode ir desta tela
| Destino | Gatilho |
|---|---|
| Lista de Treinos `[VELA-4001]` | Salvar com sucesso, ou voltar/descartar |
| Visualizar Exercício `[VELA-3002]` | Toca em um exercício no seletor (atalho de visualização) |

---

## 8. Regras de Negocio
> Regras especificas que impactam o comportamento desta tela.

- RN01: Apenas **Treinador** acessa esta tela. O Aluno nunca cria ou edita treinos.
- RN02: O treino é uma **base reutilizável** do Treinador — serve como bloco para montar Rotinas (atrelamento a rotina de aluno é **fluxo futuro**, fora de escopo aqui).
- RN03: Cada exercício exige **Séries, Repetições e Descanso (obrigatórios)**; a **Descrição de execução é opcional**. A prescrição é definida já no cadastro do treino (não fica para a Rotina).
- RN04: Para salvar, são obrigatórios **Nome**, **Categoria** e **ao menos um exercício** — e cada exercício deve ter **Séries, Repetições e Descanso** preenchidos. Demais campos são opcionais.
- RN05: Os exercícios são organizados em **grupos numerados** (1, 2, 3… automático), cada um com um **tipo opcional** (Normal, Bi-set, Tri-set, Superset, Drop-set). O **tipo define o limite de exercícios** do grupo: Normal/Drop-set = **1**, Bi-set/Superset = **2**, Tri-set = **3**; **sem tipo = Normal (1)**. As **letras A, B, C…** ficam reservadas para a **Rotina** (fluxo futuro). A **ordem de execução** respeita a sequência dos grupos e a posição do exercício dentro do grupo.
- RN06: Só é possível adicionar ao treino **exercícios do próprio Treinador** (não há acervo global — ver `[VELA-3003]`).
- RN07: No seletor de exercícios, o **ícone de vídeo** abre o vídeo em **modal/lightbox** por cima da tela; tocar no exercício abre **Visualizar Exercício `[VELA-3002]`** (mesmo padrão da decisão #20 em Exercícios).
- RN08: O treino tem estado **Ativo/Inativo** (toggle, só em edição). **Inativo** = permanece nas rotinas que já o usam, mas **não pode ser adicionado a novas**; ao desativar, exibir a mensagem explicativa. Desativar **não apaga dados** — todas as informações ficam salvas.
- RN09: Exclusão é **definitiva** (sem lixeira), sempre confirmada por modal e **só permitida se o treino não estiver em uso por nenhuma rotina**. Se estiver em uso, a exclusão fica indisponível e o caminho é **Desativar** (RN08). *(Enquanto o módulo **Rotinas** não existir, não há vínculo a verificar: a exclusão fica **sempre liberada** — com modal de confirmação. A trava por rotina passa a valer assim que Rotinas existir.)*
- RN10: O **Áudio do treino** (decisão #22) é uma **gravação feita no app** sobre o **treino como um todo** — não há áudio por exercício. É opcional e limitado a **2 minutos**.
- RN11: O **nome do treino** é único na base do Treinador (treinos de outros treinadores não geram conflito).

---

## 9. Responsividade (Mobile vs Web)

| Aspecto | Mobile | Web |
|---|---|---|
| Layout do formulário | Coluna única, scroll vertical; botão "Salvar" fixo no rodapé | Formulário centralizado (max-width ~720px); dados gerais podem usar 2 colunas |
| Reordenar exercícios | Arrastar pelo handle (toque longo) | Arrastar pelo handle (drag-and-drop com mouse) |
| Gravação de áudio | Microfone do dispositivo | Microfone do dispositivo (permissão do navegador) |
| Vídeo do exercício (atalho ▶) | Abre em modal/lightbox | Abre em modal/lightbox |

---

## 10. Acessibilidade
- Labels acessíveis em todos os campos do formulário e nos campos por exercício.
- Mensagens de erro associadas ao campo (aria-describedby) e anunciadas por leitor de tela.
- Reordenação de exercícios acessível também por teclado (mover para cima/baixo), além do arrastar.
- Contraste conforme WCAG 2.1 AA (paleta Vela: verde-limão neon sobre fundos azuis/escuros).
- Player de vídeo e player de áudio com controles acessíveis e rótulos claros.

---

## 11. Historico de Alteracoes

| Data | Autor | Descricao |
|---|---|---|
| 2026-06-18 | Equipe Vela | Criação inicial do documento (cadastro/edição de treino — visão do Treinador). Base reutilizável; blocos nomeados A/B/C com tipo (Normal, Bi-set/Superset, Circuito, Drop-set); séries/reps/execução opcionais; vídeo (meus vídeos/YouTube) + áudio do treino gravado no app (decisão #22); categoria de lista fixa; atalho de vídeo/visualização no seletor (`[VELA-3002]`); salvar exige Nome + Categoria + ≥1 exercício; ciclo Ativar/Desativar + exclusão só fora de rotina (espelha #21). Status → EM ANDAMENTO |
| 2026-06-18 | Equipe Vela | Ajustes de UI: **removido o botão "salvar" do topo** (salvar só pelo botão primário do rodapé) — atualiza a Seção 3.1; campo **Descanso** = número (≥ 0, 0 válido, não pode ficar em branco). |
| 2026-06-18 | Equipe Vela | Prescrição no treino: **Séries, Repetições e Descanso passam a ser obrigatórios** por exercício (novo campo **Descanso**); **Descrição de execução** segue opcional. Reverte a RN03 anterior (que deixava tudo opcional para a Rotina) — atualiza RN03/RN04, tabela de campos (renumerada) e decisão #31. |
| 2026-06-18 | Equipe Vela | Reformulação do agrupamento: **grupos numerados (1, 2, 3…)** no lugar de letras (letras reservadas para a Rotina); **tipo do grupo agora opcional** com lista **Normal, Bi-set, Tri-set, Superset, Drop-set** (Circuito removido); **limite de exercícios por tipo** (Normal/Drop-set 1, Bi-set/Superset 2, Tri-set 3; em branco = Normal/1); novas **categorias** (Aeróbico, Força e Potência, Resistência, Funcional, Mobilidade, Abdômen/Core). Atualiza decisões #26 e #32. |
| 2026-06-18 | Equipe Vela | Ajustes de UI: campo "Objetivo do treino" → **"Observações gerais"**; **removido o vídeo do treino** (vídeo só por exercício); **capa do card do exercício = capa do vídeo** do exercício; **Bloco C (Exercícios) marcado como obrigatório**; adicionada mensagem de ajuda **"Arraste os cards para reordenar os exercícios"**. Responsividade: linha de vídeo do treino substituída pelo atalho ▶ do exercício (lightbox). |
| 2026-06-18 | Equipe Vela | Revisão: confirmados os **4 tipos de bloco** (decisão #32 — sem adições); ordenação de exercícios por **arraste com numeração automática** (decisão #26 — sem campo de número manual); **exclusão liberada com modal enquanto Rotinas não existir** (RN09 atualizada — trava por rotina só ao existir o módulo); **áudio do treino limitado a 2 minutos** (campo 6 + RN10). Status → CONCLUIDO |

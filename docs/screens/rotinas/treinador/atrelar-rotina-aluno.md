# Tela: Atrelar Rotina ao Aluno `[VELA-3004]`

---

## Metadados
| Campo | Valor |
|---|---|
| **Nome da tela** | Atrelar Rotina ao Aluno |
| **Modulo** | Rotinas |
| **Codigo** | VELA-3004 |
| **Prioridade** | 🔵 MVP |
| **Status** | 🟢 CONCLUIDO |
| **Ultima atualizacao** | 2026-06-24 |

---

## 1. Objetivo da Tela
> O que o usuario consegue fazer nesta tela? Qual problema ela resolve?

Tela onde o **Treinador** atribui uma **rotina** a um **aluno** específico, definindo o **período de vigência** (início e, opcionalmente, fim), o **objetivo** daquela atribuição e uma **mensagem** opcional ao aluno. A rotina pode vir da **base reutilizável** do Treinador (`[VELA-5001]` / `[VELA-5003]`) ou ser **criada na hora**, reaproveitando o fluxo de criação de rotina. A rotina atrelada é uma **cópia (snapshot)** — independente da base — que o Treinador pode **refinar para o aluno** (ex.: completar séries/reps/descrição que tenham ficado em branco no treino) antes de entregar.

---

## 2. Quem Acessa / Pre-condicoes
> Quem pode ver esta tela? Quais condicoes precisam ser verdadeiras?

- **Usuario:** **Treinador** autenticado. O **Aluno** não acessa esta tela (apenas recebe e visualiza a rotina atrelada, em fluxo próprio).
- **Pre-condicoes:**
  - Usuário logado com perfil de Treinador.
  - Para "usar rotina da base": existir ao menos uma rotina na base do Treinador (`[VELA-5001]`). Se não houver, ainda é possível "criar nova rotina" no fluxo.
  - O aluno-alvo deve existir na carteira de alunos do Treinador.
- **Permissoes especiais:** Nenhuma além da role de Treinador.

---

## 3. Layout e Componentes Visuais
> Descreva a estrutura visual da tela de cima para baixo.

### 3.1 Header / Cabecalho
- Conteudo: Botão voltar (←) + Título "Atribuir rotina". A ação de salvar fica **apenas no botão primário do rodapé** (espelha Cadastro de Rotina `[VELA-5003]` e Cadastro de Treino `[VELA-4003]`).
- Comportamento: Fixo no topo. Ao voltar com dados preenchidos, exibe modal "Descartar atribuição?".

### 3.2 Corpo Principal
> **Tela única**, formulário em **fluxo contínuo** (rolagem vertical). Os blocos abaixo são **subtítulos discretos** que organizam o formulário — não são seções retráteis.

**Bloco A — Aluno** *(obrigatório)*
- Componente: Campo de seleção de aluno (busca) **ou** card do aluno já preenchido.
- Conteudo:
  - Quando o Treinador chega **pela tela do aluno**: o aluno vem **pré-selecionado** e exibido como card (foto/inicial + nome), **bloqueado** (sem troca neste fluxo).
  - Quando chega pela **entrada geral**: campo "Selecionar aluno" com **busca** (espelha o `+` de Avaliações). Ao escolher, vira o card do aluno.

**Bloco B — Rotina** *(obrigatório)*
- Componente: Seletor de origem + resumo da rotina selecionada.
- Conteudo:
  - Enquanto nada foi escolhido: dois caminhos lado a lado / empilhados — **"Usar rotina da base"** e **"Criar nova rotina"**.
  - **"Usar rotina da base"** → abre a **Lista de Rotinas** (`[VELA-5001]`) em **modo seleção** (seleção única), retornando a rotina escolhida.
  - **"Criar nova rotina"** → abre o fluxo de **Cadastro de Rotina** (`[VELA-5003]`); ao concluir, a rotina é **salva na base** e o fluxo **retorna a esta tela com a rotina já selecionada**.
  - Depois de selecionada: **card-resumo da rotina** (título + objetivo da rotina + nº de treinos + letras/nomes dos treinos A, B, C…), com:
    - Atalho **"Ver detalhes"** → abre **Visualizar Rotina** (`[VELA-5002]`) da cópia.
    - Atalho **"Trocar rotina"** → volta à escolha de origem.
  - **Aviso de prescrição incompleta** (quando houver): se algum exercício dos treinos estiver **sem séries/reps**, exibir banner informativo **"Alguns exercícios estão sem séries ou repetições. Você pode completar antes de entregar."** com atalho **"Revisar prescrição"** → abre o ajuste por aluno (ver RN03). O aviso **não bloqueia** o salvar.

**Bloco C — Vigência e objetivo** *(obrigatório, exceto onde indicado)*
- Componente: Campos de data + textarea + toggle.
- Conteudo: **Data de início** (obrigatória), **Data de fim** (opcional — "Sem prazo definido"), **Objetivo da rotina para este aluno** (obrigatório).
- **Mostrar prazo e progresso ao aluno** (toggle, **ligado por padrão**): quando ligado, o aluno vê a **faixa de datas**, a **barra de progresso de vigência** e o **tempo decorrido** nas telas do Aluno (`[VELA-6001]` / `[VELA-6002]`); quando desligado, vê **apenas o selo de status** (Ativa / Agendada / Encerrada). Texto de apoio: *"Quando desligado, o aluno vê apenas o status da rotina."* Não afeta o contador de **treinos realizados** (ver RN10).

**Bloco D — Mensagem ao aluno** *(opcional)*
- Componente: Textarea.
- Conteudo: Mensagem livre que o aluno verá ao receber a rotina (ex.: orientações, foco do ciclo).

### 3.3 Footer / Rodape
- Conteudo: Botão primário **"Atribuir rotina"**. Em telas menores, fixo na parte inferior.
- Comportamento: Desabilitado até os obrigatórios estarem válidos (Aluno + Rotina + Data de início + Objetivo).

---

## 4. Campos e Formularios

### Dados da atribuição
| # | Nome do Campo | Tipo | Obrigatorio | Placeholder | Validacao | Mensagem de Erro |
|---|---|---|---|---|---|---|
| 1 | Aluno | Seleção (busca) | Sim | "Buscar aluno…" | Deve referenciar um aluno da carteira do Treinador | "Selecione o aluno" |
| 2 | Rotina | Seleção (base) / criação | Sim | — | Uma rotina selecionada (da base ou criada no fluxo) | "Selecione ou crie uma rotina" |
| 3 | Data de início | Date | Sim | "dd/mm/aaaa" | Data válida; não anterior a hoje | "Informe a data de início" |
| 4 | Data de fim | Date | Não | "Sem prazo definido" | Se preenchida, deve ser **posterior** à data de início | "A data de fim deve ser depois do início" |
| 5 | Objetivo da rotina | Textarea | Sim | "Ex: hipertrofia, fase de adaptação…" | Não pode ficar em branco | "Informe o objetivo da rotina" |
| 6 | Mostrar prazo e progresso ao aluno | Toggle | Não | — | Padrão **ligado** | N/A |
| 7 | Mensagem ao aluno | Textarea | Não | "Mensagem opcional para o aluno" | — | N/A |

### Regras de Preenchimento
- **Data de fim** é **opcional**: em branco significa **rotina sem prazo** (vigente até ser trocada/encerrada manualmente).
- A **prescrição herdada** (séries/reps/descanso/descrição) vem do treino (`[VELA-4003]`). O Treinador **pode ajustá-la para o aluno**, mas **não é obrigado** — campos vazios geram **aviso**, não bloqueio (ver RN03).
- Ao **criar nova rotina** no fluxo, ela é **sempre salva na base** do Treinador (ver RN05) e retorna já selecionada.

---

## 5. Botoes e Acoes

| # | Componente | Label / Icone | Posicao | Estado Inicial | Acao ao Clicar |
|---|---|---|---|---|---|
| 1 | Botão primário | "Atribuir rotina" | Rodapé | Desabilitado até obrigatórios válidos | Valida → cria a **cópia** atrelada ao aluno (período + objetivo + mensagem) → volta para a **tela do aluno** com toast de sucesso |
| 2 | Botão voltar | ← | Header (esq.) | Ativo | Se houver dados preenchidos, abre modal "Descartar atribuição?"; senão, volta |
| 3 | Botão | "Usar rotina da base" | Bloco B | Ativo | Abre a Lista de Rotinas `[VELA-5001]` em **modo seleção** (única) |
| 4 | Botão | "Criar nova rotina" | Bloco B | Ativo | Abre o Cadastro de Rotina `[VELA-5003]`; ao concluir, salva na base e retorna com a rotina selecionada |
| 5 | Atalho | "Ver detalhes" | Card-resumo da rotina | Ativo (após selecionar) | Abre **Visualizar Rotina** `[VELA-5002]` da cópia |
| 6 | Atalho | "Trocar rotina" | Card-resumo da rotina | Ativo (após selecionar) | Volta à escolha de origem (base / criar) |
| 7 | Atalho | "Revisar prescrição" | Banner de aviso | Visível só se houver exercício sem séries/reps | Abre o ajuste de prescrição da cópia para o aluno (ver RN03) |
| 8 | Botão (busca) | "Selecionar aluno" | Bloco A | Ativo (só na entrada geral) | Abre busca de alunos; ao escolher, preenche o card do aluno |

---

## 6. Estados da Tela

### 6.1 Estado Inicial / Vazio
- **Entrada pela tela do aluno:** aluno pré-preenchido e bloqueado; Bloco B na escolha de origem; demais campos em branco; "Atribuir rotina" desabilitado.
- **Entrada geral:** campo "Selecionar aluno" vazio; Bloco B na escolha de origem; botão desabilitado.

### 6.2 Estado de Carregamento (Loading)
- Ao salvar: spinner sobre "Atribuir rotina", botão desabilitado durante a requisição.
- Ao abrir seleção de rotina da base: indicador de carregamento na Lista de Rotinas.

### 6.3 Estado de Erro
- **Erro de campo:** borda vermelha + mensagem abaixo do campo (ver Seção 4).
- **Sem rotina selecionada:** ao tentar salvar, mensagem "Selecione ou crie uma rotina".
- **Erro de rede:** toast "Sem conexão. Tente novamente." (mantém os dados preenchidos).
- **Erro da API ao salvar:** toast "Não foi possível atribuir a rotina. Tente novamente."

### 6.4 Estado de Sucesso
- Toast "Rotina atribuída!" + redirect para a **tela do aluno**, exibindo a rotina recém-atribuída como vigente.

### 6.5 Estado Desabilitado / Bloqueado *(se aplicavel)*
- Quando o aluno chega **pré-selecionado**, o card do aluno fica **bloqueado** (sem troca neste fluxo).

### 6.6 Modais de Confirmação
- **Descartar atribuição?** — ao voltar (←) com dados preenchidos: "Descartar atribuição?" com ações **"Cancelar"** e **"Descartar"**.
- **Salvar nova rotina na base?** — *N/A neste fluxo:* a rotina criada é **sempre salva na base** (ver RN05), sem pergunta.

---

## 7. Fluxo de Navegacao

### De onde o usuario chega nesta tela
| Origem | Gatilho |
|---|---|
| Tela do Aluno (perfil/detalhe do aluno) | Treinador toca em "Atribuir rotina" (aluno já pré-selecionado) |
| Entrada geral do Treinador (aba/menu) | Treinador escolhe atribuir rotina e seleciona o aluno aqui (item de navegação a confirmar ao mapear o painel do Treinador — ver Nota de escopo) |
| Visualizar Rotina `[VELA-5002]` | Treinador toca em "Atribuir a aluno" (entrada reservada na decisão #38) |

### Para onde o usuario pode ir desta tela
| Destino | Gatilho |
|---|---|
| Tela do Aluno | Salvar com sucesso |
| Lista de Rotinas `[VELA-5001]` (modo seleção) | Toca em "Usar rotina da base" |
| Cadastro de Rotina `[VELA-5003]` | Toca em "Criar nova rotina" |
| Visualizar Rotina `[VELA-5002]` | Toca em "Ver detalhes" da rotina selecionada |

---

## 8. Regras de Negocio
> Regras especificas que impactam o comportamento desta tela.

- **RN01:** Apenas **Treinador** acessa esta tela. O Aluno nunca atribui rotinas; apenas recebe/visualiza.
- **RN02:** A tela suporta **dois pontos de entrada**: (a) **pré-selecionado** vindo da tela do aluno (aluno bloqueado) e (b) **entrada geral**, onde o aluno é escolhido por busca aqui.
- **RN03 — Prescrição herdada:** a prescrição (séries/reps/descanso/descrição) vem do treino (`[VELA-4003]`). Ao atribuir, o Treinador **pode completar/ajustar** essa prescrição **na cópia do aluno**. Campos vazios geram **aviso** ("Alguns exercícios estão sem séries ou repetições…") mas **não bloqueiam** o salvar — a rotina pode ser entregue e completada depois.
- **RN04 — Vínculo = cópia (snapshot):** ao atrelar uma rotina da base, ela é **copiada** para o aluno no momento da atribuição. Edições futuras na **base não alteram** rotinas já entregues; ajustes feitos na cópia **não afetam** a base.
- **RN05 — Criar nova no fluxo:** "Criar nova rotina" reaproveita o Cadastro de Rotina (`[VELA-5003]`). Ao concluir, a rotina é **sempre salva na base** do Treinador e o fluxo **retorna a esta tela** com a rotina já selecionada (que então é copiada para o aluno conforme RN04).
- **RN06 — Vigência:** **Data de início** é obrigatória; **Data de fim** é **opcional** (em branco = rotina **sem prazo**, vigente até troca/encerramento manual). Se a data de fim for preenchida, deve ser posterior ao início.
- **RN07 — Rotinas coexistem:** o aluno **pode ter mais de uma rotina vigente** ao mesmo tempo (ex.: `.track` + `.performance`). Não há bloqueio nem substituição automática ao atribuir uma nova rotina no mesmo período.
- **RN08 — Obrigatórios para salvar:** Aluno + Rotina + Data de início + Objetivo. Mensagem ao aluno e Data de fim são opcionais.
- **RN09:** Ao salvar com sucesso, o Treinador retorna à **tela do aluno**, com a rotina recém-atribuída visível como vigente.
- **RN10 — Visibilidade de prazo/progresso:** o toggle **"Mostrar prazo e progresso ao aluno"** (padrão **ligado**) controla se o Aluno enxerga **faixa de datas + barra de progresso de vigência + tempo decorrido** nas telas `[VELA-6001]` / `[VELA-6002]`. Quando **desligado**, o Aluno vê **apenas o selo de status** (Ativa / Agendada / Encerrada). O **contador de treinos realizados** (`[VELA-6001]` RN06 / decisão #41) **independe** deste controle e continua visível. Reflexo de leitura já definido em `[VELA-6001]` RN05.
- **RN11 — Exclusão da rotina-base não afeta a atribuição:** como o vínculo é **cópia/snapshot** (RN04), excluir a rotina da base (`[VELA-5003]`) **não remove nem altera** a rotina já entregue ao aluno. Por isso **não há trava de exclusão por vínculo** na base — a integridade da entrega é garantida pela cópia (decisão #38 encerrada).

> **Nota de escopo — dependências externas (não bloqueiam esta tela):**
> - **Entrada geral pelo painel/menu do Treinador:** o item de navegação que leva a esta tela (com seleção de aluno por busca) será confirmado ao mapear o **painel/menu do Treinador**, ainda não mapeado (mesma dependência das decisões #10/#37/#30/#19).
> - **Notificação ao aluno ao atribuir:** ao salvar, o Aluno deve receber **push + in-app** avisando da nova rotina; o copy e o comportamento (deep link, opt-out) serão definidos ao mapear a **tela Notificações** (`screens/configuracoes/notificacoes.md`), ainda não mapeada (mesma dependência da decisão #13).

---

## 9. Responsividade (Mobile vs Web)

| Aspecto | Mobile | Web |
|---|---|---|
| Layout do formulário | Coluna única, scroll vertical; botão "Atribuir rotina" fixo no rodapé | Formulário centralizado (max-width ~720px); datas podem usar 2 colunas |
| Seleção de aluno | Busca em tela cheia | Busca em modal/painel ou inline |
| Seleção de rotina da base | Lista de Rotinas em modo seleção (tela cheia) | Lista de Rotinas em modo seleção (modal/painel ou tela) |
| Criar nova rotina | Abre Cadastro de Rotina (tela cheia) e retorna | Abre Cadastro de Rotina e retorna |

> Mesma lógica e mesmas regras em ambas as plataformas; apenas o layout se adapta.

---

## 10. Acessibilidade
- Labels acessíveis em todos os campos (aluno, datas, objetivo, mensagem).
- Mensagens de erro associadas ao campo (aria-describedby) e anunciadas por leitor de tela.
- Banner de aviso de prescrição incompleta anunciado como alerta (role="status") e com atalho focável.
- Card do aluno e card-resumo da rotina com nome acessível (aluno: nome; rotina: título + nº de treinos).
- Seletores de data acessíveis por teclado.
- Contraste conforme WCAG 2.1 AA (paleta Vela: verde-limão neon sobre fundos azuis/escuros).

---

## 11. Historico de Alteracoes

| Data | Autor | Descricao |
|---|---|---|
| 2026-06-18 | Maria Isabela | Criação inicial do documento (entrevista `/mapear-tela`). **Atrelar Rotina ao Aluno** `[VELA-3004]`, 🔵 MVP. Entrada por **ambos os caminhos** (pré-selecionado pela tela do aluno / entrada geral com busca; + "Atribuir a aluno" da Visualizar `[VELA-5002]`, decisão #38). Origem da rotina: usar da base (`[VELA-5001]`) ou criar nova (`[VELA-5003]`, **sempre salva na base**). Vínculo = **cópia/snapshot** (RN04). Prescrição herdada **ajustável mas não obrigatória**, com aviso que não bloqueia (RN03). **Data de fim opcional** (sem prazo, RN06). Rotinas **coexistem** (sem substituição, RN07). Pós-salvar volta à **tela do aluno** (RN09). Status → EM ANDAMENTO |
| 2026-06-24 | Maria Isabela | Revisão de finalização (`/revisar-tela`): (1) adicionado o toggle **"Mostrar prazo e progresso ao aluno"** no Bloco C, **ligado por padrão** — campo #6, RN10 (decisão #40 encerrada); (2) confirmada a **ausência de trava de exclusão por vínculo** na base, pois a atribuição é cópia/snapshot — RN11 (cauda da decisão #38 encerrada, sem reabrir `[VELA-5003]`); (3) pendência **bloqueante** da entrada geral convertida em **Nota de escopo** + adicionada nota da **notificação ao aluno** — ambas dependem de telas ainda não mapeadas (painel do Treinador / Notificações) e **não bloqueiam** esta tela. Mockup sincronizado (toggle). Status → 🟢 CONCLUIDO |

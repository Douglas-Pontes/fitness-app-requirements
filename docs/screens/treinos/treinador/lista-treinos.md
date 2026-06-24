# Tela: Lista de Treinos `[VELA-4001]`

---

## Metadados
| Campo | Valor |
|---|---|
| **Nome da tela** | Lista de Treinos |
| **Modulo** | Treinos |
| **Codigo** | VELA-4001 |
| **Prioridade** | 🔵 MVP |
| **Status** | 🟢 CONCLUIDO |
| **Ultima atualizacao** | 2026-06-24 |

---

## 1. Objetivo da Tela
> O que o usuario consegue fazer nesta tela? Qual problema ela resolve?

Hub do módulo de Treinos na **visão do Treinador**: lista todos os treinos da **sua** base reutilizável, de onde ele cria um novo, abre para visualizar/editar e dispara as ações de gestão (Duplicar, Ativar/Desativar, Excluir). É o ponto de partida do trio **VELA-4001/4002/4003** (Lista, Visualizar, Cadastro), espelhando o padrão de Exercícios (`[VELA-3001]`) e Avaliações (`[VELA-2001]`). _(A escolha de treinos para compor uma Rotina é feita pelo **seletor de treinos** da própria montagem de Rotina, `[VELA-5003]` — não é responsabilidade desta tela.)_

---

## 2. Quem Acessa / Pre-condicoes
> Quem pode ver esta tela? Quais condicoes precisam ser verdadeiras?

- **Usuario:** **Treinador** autenticado. O **Aluno** não acessa esta tela (o aluno só vê o treino dentro da Rotina, no fluxo de treinar — ver colisão de nome com a futura "Lista de Treinos (Aluno)", decisão #34).
- **Pre-condicoes:**
  - Usuário deve estar logado com perfil de Treinador.
  - A lista exibe apenas os treinos do **próprio Treinador** (não há base global de treinos).
- **Permissoes especiais:** Nenhuma além da role de Treinador.

---

## 3. Layout e Componentes Visuais
> Descreva a estrutura visual da tela de cima para baixo.

### 3.1 Header / Cabecalho
- Conteudo: Título "Treinos" + campo de **busca** (por nome).
- Comportamento: Fixo no topo. A busca é **normalizada** (ignora acentos e maiúsculas/minúsculas), espelhando `[VELA-3001]`.

### 3.2 Corpo Principal
> Tela única em rolagem vertical. Lista de cards de treino, precedida por uma barra de filtros.

**Bloco A — Filtros**
- Componente: Chips/selects de filtro.
- Conteudo: Filtro por **Categoria** e filtro por **status** (Ativos / Inativos / Todos).
- Comportamento: Aplicados sobre a lista em tempo real, combinados com a busca por nome.

**Bloco B — Lista de Treinos**
- Componente: Lista de **cards de treino** (1 coluna no mobile; grade multi-coluna na web).
- Conteudo de cada card:
  - **Nome do treino**
  - **Categoria** + **quantidade de exercícios** (lado a lado, ex: "Hipertrofia · 6 exercícios")
  - **Selo de status** (Ativo / Inativo)
  - Menu **"⋮"** (kebab) com ações rápidas: **Incluir em rotina**, **Duplicar**, **Ativar/Desativar**, **Excluir**
- Comportamento:
  - **Toque no card** → abre **Visualizar Treino** (`[VELA-4002]`).
  - Treinos **inativos** aparecem **atenuados** com selo "Inativo" (podem ser ocultados pelo filtro de status).
  - **Ordenação:** alfabética por nome do treino (resolve decisão #25).

**Bloco C — Bottom-sheet "Incluir em rotina"** (acionado pelo menu "⋮")
- Componente: Overlay inferior (bottom-sheet) com a **lista de rotinas em rascunho/em construção** do Treinador, cada uma com **checkbox** (seleção múltipla), e botão **"Adicionar"**.
- Conteudo: Nome de cada rotina; rotinas que **já contêm** o treino aparecem **marcadas e desabilitadas** com o rótulo **"Já na rotina"**.
- Comportamento: Treinador marca uma ou mais rotinas e confirma; o treino entra em cada rotina (o **agrupamento por letra** A/B/C e a ordem são definidos depois na própria Rotina). O bottom-sheet exibe a mensagem de apoio **"Entre na rotina para finalizar."**. Ao concluir, toast **"Adicionado a N rotina(s) — entre na rotina para finalizar"**. Se não houver rotina em rascunho, exibir estado vazio orientando a criar uma rotina primeiro. Espelha o atalho "Incluir em treino" de `[VELA-3001]`.

### 3.3 Footer / Rodape
- Conteudo: **FAB "+"** fixo no canto inferior → abre o **Cadastro de Treino** (`[VELA-4003]`) em branco.
- Comportamento: Fixo na parte inferior. Na web, a ação de criar aparece como botão "Novo treino" na barra superior (ver Seção 9).

---

## 4. Campos e Formularios

> Preencher apenas se a tela tiver campos de entrada (inputs, selects, etc.)

| # | Nome do Campo | Tipo | Obrigatorio | Placeholder | Validacao | Mensagem de Erro |
|---|---|---|---|---|---|---|
| 1 | Busca | Text | Não | "Buscar treino" | Nenhuma (normaliza acentos/caixa) | N/A |
| 2 | Filtro de Categoria | Select / Chips | Não | "Todas as categorias" | N/A | N/A |
| 3 | Filtro de Status | Select / Chips | Não | "Ativos" | N/A | N/A |

### Regras de Preenchimento
- A busca filtra a lista conforme o usuário digita (busca normalizada, sem acento e case-insensitive).
- Filtros de Categoria e Status combinam com a busca (interseção).

---

## 5. Botoes e Acoes

| # | Componente | Label / Icone | Posicao | Estado Inicial | Acao ao Clicar |
|---|---|---|---|---|---|
| 1 | FAB | "+" | Canto inferior (mobile) | Ativo | Abre Cadastro de Treino `[VELA-4003]` em branco |
| 2 | Botão (web) | "Novo treino" | Barra superior | Ativo | Abre Cadastro de Treino `[VELA-4003]` em branco |
| 3 | Card | (treino) | Lista | Ativo | Abre Visualizar Treino `[VELA-4002]` |
| 4 | Menu "⋮" → Incluir em rotina | "Incluir em rotina" | No card | Ativo (oculto p/ treino Inativo) | Abre bottom-sheet de rotinas em rascunho (ver #8) |
| 5 | Menu "⋮" → Duplicar | "Duplicar" | No card | Ativo | Cria cópia do treino na base do Treinador (in-place na lista) |
| 6 | Menu "⋮" → Ativar/Desativar | "Ativar" / "Desativar" | No card | Ativo | Alterna status do treino (in-place, atualiza selo) |
| 7 | Menu "⋮" → Excluir | "Excluir" | No card | Ativo | Abre modal de confirmação → exclusão definitiva |
| 8 | Bottom-sheet "Incluir em rotina" | Lista de rotinas (rascunho) com checkbox + botão "Adicionar" | Overlay inferior | — | Treinador marca **uma ou mais** rotinas e confirma; o treino é adicionado a cada uma (agrupamento por letra/ordem definidos depois na Rotina). Toast "Adicionado a N rotina(s) — entre na rotina para finalizar" |

---

## 6. Estados da Tela

### 6.1 Estado Inicial / Vazio
- Treinador sem nenhum treino cadastrado: ilustração + mensagem **"Você ainda não tem treinos. Crie o primeiro!"** + CTA que abre o Cadastro `[VELA-4003]`.
- Lista com filtro/busca sem resultados: mensagem **"Nenhum treino encontrado"**.
- **Bottom-sheet "Incluir em rotina" sem rotinas em rascunho:** estado vazio **"Você não tem rotinas em construção"** + orientação para criar uma rotina antes.

### 6.2 Estado de Carregamento (Loading)
- **Skeleton loader** dos cards enquanto a lista carrega.

### 6.3 Estado de Erro
- **Erro de rede / API:** estado de erro com mensagem **"Não foi possível carregar seus treinos"** + botão **"Tentar novamente"**.

### 6.4 Estado de Sucesso
- Lista de cards renderizada.
- Após Duplicar: toast **"Treino duplicado"** + novo card aparece na lista.
- Após Ativar/Desativar: selo do card atualiza (sem sair da tela).
- Após Excluir: toast **"Treino excluído"** + card some da lista.
- Após **incluir em rotina(s)**: toast **"Adicionado a N rotina(s) — entre na rotina para finalizar"** + fechamento do bottom-sheet.

### 6.5 Estado Desabilitado / Bloqueado *(se aplicavel)*
- N/A.

---

## 7. Fluxo de Navegacao

### De onde o usuario chega nesta tela
| Origem | Gatilho |
|---|---|
| Aba/menu do Treinador (modo gestão) | Acessa o módulo Treinos _(item de navegação pendente — depende do painel/menu do Treinador, decisão #30)_ |
| Visualizar Treino `[VELA-4002]` | Botão voltar (←) |
| Cadastro / Edição de Treino `[VELA-4003]` | Após salvar ou voltar |

### Para onde o usuario pode ir desta tela
| Destino | Gatilho |
|---|---|
| Visualizar Treino `[VELA-4002]` | Toque no card |
| Cadastro / Edição de Treino `[VELA-4003]` | FAB "+" / botão "Novo treino" |

---

## 8. Regras de Negocio
> Regras especificas que impactam o comportamento desta tela.

- **RN01:** A lista exibe **apenas os treinos do próprio Treinador**. Não há base global de treinos.
- **RN02:** Ordenação **alfabética por nome do treino** (resolve decisão #25).
- **RN03:** Busca **normalizada** — ignora acentos e diferença de maiúsculas/minúsculas (espelha `[VELA-3001]`).
- **RN04:** **Exclusão definitiva** (app sem lixeira), sempre com **modal de confirmação**. O treino só pode ser excluído se **não estiver em nenhuma rotina** (`[VELA-5003]`). Se estiver vinculado a ao menos uma rotina, a exclusão fica **indisponível** e o caminho é **Desativar** (aposenta o treino sem quebrar as rotinas que já o usam — espelha decisão #31 e a RN08 de `[VELA-3001]`).
- **RN05:** Treinos **inativos** continuam visíveis na lista (atenuados, com selo "Inativo") e podem ser ocultados pelo filtro de status. O toggle Ativar/Desativar espelha o ciclo de vida de `[VELA-4003]`/decisão #31.
- **RN06:** **Duplicar** cria uma cópia do treino na base do próprio Treinador (novo treino editável independente do original).
- **RN07:** **Incluir em rotina** (atalho do menu "⋮"): permite ao Treinador adicionar o treino a **uma ou mais rotinas** sem sair da lista nem abrir a tela de Rotina (`[VELA-5003]`). Espelha "Incluir em treino" de `[VELA-3001]`, respeitando a hierarquia **Treino → Rotina** (treino entra na rotina; agrupamento por letra A/B/C e ordem definidos depois na Rotina).
- **RN08:** Só aparecem no seletor as **rotinas em rascunho/em construção** do Treinador — rotinas já finalizadas não são elegíveis.
- **RN09:** Rotina que **já contém** o treino aparece **desabilitada** no seletor ("Já na rotina") — não é possível duplicar o mesmo treino na mesma rotina por este atalho (coerente com a RN05 de `[VELA-5003]`).
- **RN10:** A ação **"Incluir em rotina" não fica disponível para treinos Inativos** (coerente com RN05 desta tela e com a RN07 de `[VELA-5003]` — inativo não entra em novas rotinas).

---

## 9. Responsividade (Mobile vs Web)
> Diferencas de comportamento ou layout entre plataformas.

| Aspecto | Mobile | Web |
|---|---|---|
| Layout da lista | 1 coluna | Grade multi-coluna |
| Ação de criar | FAB "+" fixo no canto inferior | Botão "Novo treino" na barra superior |
| Busca e filtros | Campo de busca no header + chips de filtro | Barra superior com busca + filtros |
| Conteúdo dos cards | Idêntico | Idêntico |

---

## 10. Acessibilidade
> Consideracoes de acessibilidade para esta tela.

- Labels acessíveis no campo de busca e nos filtros.
- Cada card é um alvo de toque com nome acessível (nome do treino + status).
- Menu "⋮" operável por teclado, com rótulos claros nas ações.
- Contraste de cores conforme WCAG 2.1 AA — atenção especial aos cards "Inativos" atenuados (manter contraste mínimo do texto).
- Navegação por teclado (tab order lógica: busca → filtros → cards → FAB).
- Modal de exclusão com foco gerenciado e ação destrutiva claramente identificada.

---

## 11. Historico de Alteracoes

| Data | Autor | Descricao |
|---|---|---|
| 2026-06-18 | Maria Isabela | Criação inicial do documento (entrevista `/mapear-tela`). Resolve decisões #25 (ordenação alfabética) e #33 (card: qtd de exercícios). |
| 2026-06-18 | Maria Isabela | Ajuste no card: quantidade de exercícios ao lado da categoria; **removidos os chips de grupos musculares**. |
| 2026-06-24 | Maria Isabela | Novo atalho **"Incluir em rotina"** no menu "⋮" (RN08–RN11), espelhando "Incluir em treino" de `[VELA-3001]`: bottom-sheet com rotinas em rascunho, "Já na rotina", "Entre na rotina para finalizar", oculto para treinos Inativos. Mockup atualizado (item no menu + frame do bottom-sheet). |
| 2026-06-24 | Maria Isabela | **Reconciliação com o módulo de Rotinas (já concluído, `[VELA-5003]`)** e fechamento da tela. RN04: removida a cláusula interina — **trava de exclusão por vínculo com rotina** passa a valer (treino em rotina não exclui → Desativar). Atalho "Incluir em rotina" referenciando `[VELA-5003]`; "Já na rotina" respaldado pela RN05 da Rotina. **Pendência da Seção 8 encerrada.** Status → 🟢 CONCLUIDO. |
| 2026-06-24 | Maria Isabela | **Removido o "modo seleção" desta tela:** a escolha de treinos para uma Rotina passa a ser descrita como **seletor de treinos** da própria montagem de Rotina (`[VELA-5003]`), evitando duplicar a mesma tela em dois módulos. Removidos: menções no objetivo/header/corpo/rodapé, a antiga RN07 (RNs do atalho renumeradas RN07–RN10), as linhas de navegação relacionadas e o frame "modo seleção" do mockup. |

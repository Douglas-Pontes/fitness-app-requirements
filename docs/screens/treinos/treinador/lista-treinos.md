# Tela: Lista de Treinos `[VELA-4001]`

---

## Metadados
| Campo | Valor |
|---|---|
| **Nome da tela** | Lista de Treinos |
| **Modulo** | Treinos |
| **Codigo** | VELA-4001 |
| **Prioridade** | 🔵 MVP |
| **Status** | 🟡 EM ANDAMENTO |
| **Ultima atualizacao** | 2026-06-18 |

---

## 1. Objetivo da Tela
> O que o usuario consegue fazer nesta tela? Qual problema ela resolve?

Hub do módulo de Treinos na **visão do Treinador**: lista todos os treinos da **sua** base reutilizável, de onde ele cria um novo, abre para visualizar/editar e dispara as ações de gestão (Duplicar, Ativar/Desativar, Excluir). É o ponto de partida do trio **VELA-4001/4002/4003** (Lista, Visualizar, Cadastro), espelhando o padrão de Exercícios (`[VELA-3001]`) e Avaliações (`[VELA-2001]`). A mesma tela também serve em **modo seleção** quando aberta a partir da montagem/edição de uma Rotina, para escolher quais treinos compõem a rotina.

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
- Conteudo: Título "Treinos" + campo de **busca** (por nome). Em **modo seleção** (vindo da Rotina), o header mostra Botão voltar (←) + título "Selecionar treinos" + contador de selecionados.
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
  - Menu **"⋮"** (kebab) com ações rápidas: **Duplicar**, **Ativar/Desativar**, **Excluir**
- Comportamento:
  - **Toque no card** → abre **Visualizar Treino** (`[VELA-4002]`).
  - Treinos **inativos** aparecem **atenuados** com selo "Inativo" (podem ser ocultados pelo filtro de status).
  - **Ordenação:** alfabética por nome do treino (resolve decisão #25).
  - Em **modo seleção** (vindo da Rotina): o toque no card **alterna a seleção** (checkbox/estado selecionado) em vez de abrir a Visualização; o menu "⋮" fica oculto. _(O multi-seleção e o botão "Adicionar selecionados" serão detalhados ao mapear a tela de Rotina — dependência.)_

### 3.3 Footer / Rodape
- Conteudo: **FAB "+"** fixo no canto inferior (modo gestão) → abre o **Cadastro de Treino** (`[VELA-4003]`) em branco. Em **modo seleção**, o rodapé exibe o botão **"Adicionar selecionados (N)"** no lugar do FAB.
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
| 3 | Card | (treino) | Lista | Ativo | Modo gestão: abre Visualizar Treino `[VELA-4002]` / Modo seleção: alterna seleção |
| 4 | Menu "⋮" → Duplicar | "Duplicar" | No card | Ativo | Cria cópia do treino na base do Treinador (in-place na lista) |
| 5 | Menu "⋮" → Ativar/Desativar | "Ativar" / "Desativar" | No card | Ativo | Alterna status do treino (in-place, atualiza selo) |
| 6 | Menu "⋮" → Excluir | "Excluir" | No card | Ativo | Abre modal de confirmação → exclusão definitiva |
| 7 | Botão (modo seleção) | "Adicionar selecionados (N)" | Rodapé | Desabilitado até ≥1 selecionado | Retorna à Rotina com os treinos escolhidos |

---

## 6. Estados da Tela

### 6.1 Estado Inicial / Vazio
- Treinador sem nenhum treino cadastrado: ilustração + mensagem **"Você ainda não tem treinos. Crie o primeiro!"** + CTA que abre o Cadastro `[VELA-4003]`.
- Lista com filtro/busca sem resultados: mensagem **"Nenhum treino encontrado"**.

### 6.2 Estado de Carregamento (Loading)
- **Skeleton loader** dos cards enquanto a lista carrega.

### 6.3 Estado de Erro
- **Erro de rede / API:** estado de erro com mensagem **"Não foi possível carregar seus treinos"** + botão **"Tentar novamente"**.

### 6.4 Estado de Sucesso
- Lista de cards renderizada.
- Após Duplicar: toast **"Treino duplicado"** + novo card aparece na lista.
- Após Ativar/Desativar: selo do card atualiza (sem sair da tela).
- Após Excluir: toast **"Treino excluído"** + card some da lista.

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
| Montagem / Edição de Rotina | Abre em **modo seleção** para escolher treinos _(dependência: tela de Rotina)_ |

### Para onde o usuario pode ir desta tela
| Destino | Gatilho |
|---|---|
| Visualizar Treino `[VELA-4002]` | Toque no card (modo gestão) |
| Cadastro / Edição de Treino `[VELA-4003]` | FAB "+" / botão "Novo treino" |
| Montagem / Edição de Rotina | Botão "Adicionar selecionados" (modo seleção) |

---

## 8. Regras de Negocio
> Regras especificas que impactam o comportamento desta tela.

- **RN01:** A lista exibe **apenas os treinos do próprio Treinador**. Não há base global de treinos.
- **RN02:** Ordenação **alfabética por nome do treino** (resolve decisão #25).
- **RN03:** Busca **normalizada** — ignora acentos e diferença de maiúsculas/minúsculas (espelha `[VELA-3001]`).
- **RN04:** **Exclusão definitiva** (app sem lixeira), sempre com **modal de confirmação**. O treino só pode ser excluído se **não estiver em nenhuma rotina**; nesse caso, oferecer **Desativar** como alternativa para aposentar em uso (espelha decisão #31). **Interino:** enquanto o módulo de Rotinas não existir, não há vínculo a checar → exclusão **sempre liberada** (com modal). A trava por rotina passa a valer quando o módulo de Rotinas existir.
- **RN05:** Treinos **inativos** continuam visíveis na lista (atenuados, com selo "Inativo") e podem ser ocultados pelo filtro de status. O toggle Ativar/Desativar espelha o ciclo de vida de `[VELA-4003]`/decisão #31.
- **RN06:** **Duplicar** cria uma cópia do treino na base do próprio Treinador (novo treino editável independente do original).
- **RN07:** Em **modo seleção** (vindo da Rotina), o card não abre a Visualização nem mostra "⋮"; o toque alterna a seleção e o rodapé confirma com "Adicionar selecionados (N)".

> ⚠️ PENDENTE: **Revisar esta tela após mapear as telas de Rotina.** O **modo seleção** (multi-seleção, limites, retorno à Rotina) e a **trava de exclusão por vínculo com rotina** (RN04) dependem do módulo de Rotinas e só poderão ser fechados quando ele existir.

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

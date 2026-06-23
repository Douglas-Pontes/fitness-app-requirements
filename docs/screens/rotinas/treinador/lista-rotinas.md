# Tela: Lista de Rotinas `[VELA-5001]`

---

## Metadados
| Campo | Valor |
|---|---|
| **Nome da tela** | Lista de Rotinas |
| **Modulo** | Rotinas |
| **Codigo** | VELA-5001 |
| **Prioridade** | 🔵 MVP |
| **Status** | 🟢 CONCLUIDO |
| **Ultima atualizacao** | 2026-06-18 |

---

## 1. Objetivo da Tela
> O que o usuario consegue fazer nesta tela? Qual problema ela resolve?

Hub do módulo de Rotinas na **visão do Treinador**: lista todas as rotinas da **sua** base reutilizável, de onde ele cria uma nova, abre para visualizar/editar e dispara as ações de gestão (Duplicar, Ativar/Desativar, Excluir). É o ponto de partida do trio **VELA-5001/5002/5003** (Lista, Visualizar, Cadastro/Edição), espelhando o padrão de Treinos (`[VELA-4001]`) e Exercícios (`[VELA-3001]`). Cada rotina agrupa **treinos ordenados por letras A, B, C…**.

---

## 2. Quem Acessa / Pre-condicoes
> Quem pode ver esta tela? Quais condicoes precisam ser verdadeiras?

- **Usuario:** **Treinador** autenticado. O **Aluno** não acessa esta tela.
- **Pre-condicoes:**
  - Usuário deve estar logado com perfil de Treinador.
  - A lista exibe apenas as rotinas do **próprio Treinador** (não há base global de rotinas).
- **Permissoes especiais:** Nenhuma além da role de Treinador.

---

## 3. Layout e Componentes Visuais
> Descreva a estrutura visual da tela de cima para baixo.

### 3.1 Header / Cabecalho
- Conteudo: Título "Rotinas" + campo de **busca** (por título).
- Comportamento: Fixo no topo. A busca é **normalizada** (ignora acentos e maiúsculas/minúsculas), espelhando `[VELA-3001]`/`[VELA-4001]`.

### 3.2 Corpo Principal
> Tela única em rolagem vertical. Lista de cards de rotina, precedida por uma barra de filtros.

**Bloco A — Filtros**
- Componente: Campo de busca + chips/selects de filtro.
- Conteudo: Busca por **título**; filtro por **nome do treino** e por **categoria do treino** (rotinas que contêm treino/categoria informados); filtro por **status** (Ativas / Inativas / Todas).
- Comportamento: Aplicados sobre a lista em tempo real, combinados entre si (interseção).

**Bloco B — Lista de Rotinas**
- Componente: Lista de **cards de rotina** (1 coluna no mobile; grade multi-coluna na web).
- Conteudo de cada card:
  - **Título da rotina**
  - **Objetivo** (resumido / 1 linha)
  - **Quantidade de treinos** + **letras/nomes dos treinos** de forma compacta (ex: "4 treinos · A Peito · B Costas · C Pernas · D Ombro")
  - **Selo de status** (Ativa / Inativa)
  - Menu **"⋮"** (kebab) com ações rápidas: **Duplicar**, **Ativar/Desativar**, **Excluir**
- Comportamento:
  - **Toque no card** → abre **Visualizar Rotina** (`[VELA-5002]`).
  - Rotinas **inativas** aparecem **atenuadas** com selo "Inativa" (podem ser ocultadas pelo filtro de status).
  - **Ordenação:** alfabética por título da rotina (espelha `[VELA-4001]`).

### 3.3 Footer / Rodape
- Conteudo: **FAB "+"** fixo no canto inferior → abre o **Cadastro de Rotina** (`[VELA-5003]`) em branco.
- Comportamento: Fixo na parte inferior. Na web, a ação de criar aparece como botão "Nova rotina" na barra superior (ver Seção 9).

---

## 4. Campos e Formularios

> Preencher apenas se a tela tiver campos de entrada (inputs, selects, etc.)

| # | Nome do Campo | Tipo | Obrigatorio | Placeholder | Validacao | Mensagem de Erro |
|---|---|---|---|---|---|---|
| 1 | Busca | Text | Não | "Buscar rotina" | Nenhuma (normaliza acentos/caixa) | N/A |
| 2 | Filtro por nome do treino | Text / Select | Não | "Filtrar por treino" | N/A | N/A |
| 3 | Filtro por categoria do treino | Select / Chips | Não | "Todas as categorias" | N/A | N/A |
| 4 | Filtro de Status | Select / Chips | Não | "Ativas" | N/A | N/A |

### Regras de Preenchimento
- A busca filtra a lista conforme o usuário digita (busca normalizada, sem acento e case-insensitive), pelo **título** da rotina.
- Os filtros por nome do treino, categoria do treino e status combinam com a busca (interseção).

---

## 5. Botoes e Acoes

| # | Componente | Label / Icone | Posicao | Estado Inicial | Acao ao Clicar |
|---|---|---|---|---|---|
| 1 | FAB | "+" | Canto inferior (mobile) | Ativo | Abre Cadastro de Rotina `[VELA-5003]` em branco |
| 2 | Botão (web) | "Nova rotina" | Barra superior | Ativo | Abre Cadastro de Rotina `[VELA-5003]` em branco |
| 3 | Card | (rotina) | Lista | Ativo | Abre Visualizar Rotina `[VELA-5002]` |
| 4 | Menu "⋮" → Duplicar | "Duplicar" | No card | Ativo | Cria cópia da rotina na base do Treinador (in-place na lista) |
| 5 | Menu "⋮" → Ativar/Desativar | "Ativar" / "Desativar" | No card | Ativo | Alterna status da rotina (in-place, atualiza selo) |
| 6 | Menu "⋮" → Excluir | "Excluir" | No card | Ativo | Abre modal de confirmação → exclusão definitiva |

---

## 6. Estados da Tela

### 6.1 Estado Inicial / Vazio
- Treinador sem nenhuma rotina cadastrada: ilustração + mensagem **"Você ainda não tem rotinas"** + CTA **"+ Criar rotina"** que abre o Cadastro `[VELA-5003]`.
- Lista com filtro/busca sem resultados: mensagem **"Nenhuma rotina encontrada"**.

### 6.2 Estado de Carregamento (Loading)
- **Skeleton loader** dos cards enquanto a lista carrega.

### 6.3 Estado de Erro
- **Erro de rede / API:** estado de erro com mensagem **"Não foi possível carregar suas rotinas"** + botão **"Tentar novamente"**.

### 6.4 Estado de Sucesso
- Lista de cards renderizada.
- Após Duplicar: toast **"Rotina duplicada"** + novo card aparece na lista.
- Após Ativar/Desativar: selo do card atualiza (sem sair da tela).
- Após Excluir: toast **"Rotina excluída"** + card some da lista.

### 6.5 Estado Desabilitado / Bloqueado *(se aplicavel)*
- N/A.

### 6.6 Modais de Confirmação
- **Desativar rotina?** — ao escolher "Desativar" no menu ⋮: "Desativar rotina?" + texto "A rotina deixa de ficar disponível para uso, mas seus dados são preservados." com ações **"Cancelar"** e **"Desativar"**.
- **Excluir rotina?** — ao escolher "Excluir" no menu ⋮: "Excluir rotina?" + texto "Esta ação não pode ser desfeita." com ações **"Cancelar"** e **"Excluir"** (ação destrutiva).
- **Duplicar** não tem modal — duplica in-place com toast "Rotina duplicada" (ver RN07).

---

## 7. Fluxo de Navegacao

### De onde o usuario chega nesta tela
| Origem | Gatilho |
|---|---|
| Aba/menu do Treinador | Acessa o módulo Rotinas _(item de navegação depende do painel/menu do Treinador, ainda não mapeado — decisão #37; ver RN08)_ |
| Visualizar Rotina `[VELA-5002]` | Botão voltar (←) |
| Cadastro / Edição de Rotina `[VELA-5003]` | Após salvar ou voltar |

### Para onde o usuario pode ir desta tela
| Destino | Gatilho |
|---|---|
| Visualizar Rotina `[VELA-5002]` | Toque no card |
| Cadastro / Edição de Rotina `[VELA-5003]` | FAB "+" / botão "Nova rotina" |

---

## 8. Regras de Negocio
> Regras especificas que impactam o comportamento desta tela.

- **RN01:** A lista exibe **apenas as rotinas do próprio Treinador**. Não há base global de rotinas.
- **RN02:** Ordenação **alfabética por título da rotina** (espelha `[VELA-4001]`).
- **RN03:** Busca **normalizada** — ignora acentos e diferença de maiúsculas/minúsculas (espelha `[VELA-3001]`/`[VELA-4001]`).
- **RN04:** O card resume a rotina com **título + objetivo + quantidade de treinos + letras/nomes dos treinos** (ex: "4 treinos · A Peito · B Costas…"). Categorias/grupos agregados ficam na Visualizar `[VELA-5002]`.
- **RN05:** **Exclusão definitiva** (app sem lixeira), sempre com **modal de confirmação**. *(A trava de exclusão por vínculo passa a valer quando o atrelamento de rotina a aluno existir — fluxo futuro.)*
- **RN06:** Rotinas **inativas** continuam visíveis na lista (atenuadas, com selo "Inativa") e podem ser ocultadas pelo filtro de status. O toggle Ativar/Desativar espelha o ciclo de vida de `[VELA-5003]`.
- **RN07:** **Duplicar** cria uma cópia da rotina na base do próprio Treinador **in-place** (toast "Rotina duplicada" + novo card na lista), sem sair da Lista. _(Divergência intencional: na Visualizar `[VELA-5002]` o Duplicar abre o Cadastro da cópia — mesmo padrão de Treinos `[VELA-4001]`/`[VELA-4002]`.)_ A cópia é uma rotina editável independente da original.
- **RN08:** O **ponto de entrada** (item de navegação na aba/menu do Treinador) depende do **painel/menu do Treinador**, ainda não mapeado — dependência externa rastreada na **decisão #37**. Não bloqueia o escopo desta tela.

---

## 9. Responsividade (Mobile vs Web)
> Diferencas de comportamento ou layout entre plataformas.

| Aspecto | Mobile | Web |
|---|---|---|
| Layout da lista | 1 coluna | Grade multi-coluna |
| Ação de criar | FAB "+" fixo no canto inferior | Botão "Nova rotina" na barra superior |
| Busca e filtros | Campo de busca no header + chips de filtro | Barra superior com busca + filtros |
| Conteúdo dos cards | Idêntico | Idêntico |

---

## 10. Acessibilidade
> Consideracoes de acessibilidade para esta tela.

- Labels acessíveis no campo de busca e nos filtros.
- Cada card é um alvo de toque com nome acessível (título da rotina + status).
- Menu "⋮" operável por teclado, com rótulos claros nas ações.
- Contraste de cores conforme WCAG 2.1 AA — atenção especial aos cards "Inativas" atenuados (manter contraste mínimo do texto).
- Navegação por teclado (tab order lógica: busca → filtros → cards → FAB).
- Modal de exclusão com foco gerenciado e ação destrutiva claramente identificada.

---

## 11. Historico de Alteracoes

| Data | Autor | Descricao |
|---|---|---|
| 2026-06-18 | Maria Isabela | Criação inicial do documento (entrevista `/mapear-tela`). Hub do módulo Rotinas (visão do Treinador), espelhando `[VELA-4001]`. Card: título + objetivo + nº de treinos + letras/nomes dos treinos. Filtros: título, nome do treino, categoria do treino, status. Ordenação alfabética; busca normalizada. Gestão: Duplicar, Ativar/Desativar, Excluir. Ponto de entrada = aba/menu do Treinador (pendente do painel). Status → EM ANDAMENTO |
| 2026-06-18 | Maria Isabela | Revisão (`/revisar-tela`): **Duplicar in-place** confirmado (RN07, divergência intencional vs Visualizar); **ponto de entrada** vira nota de dependência (RN08, decisão #37) — não bloqueia conclusão; fixadas copies dos modais Desativar/Excluir (Seção 6.6); estado vazio alinhado ao mockup ("Você ainda não tem rotinas" + "+ Criar rotina"). Status → CONCLUIDO |

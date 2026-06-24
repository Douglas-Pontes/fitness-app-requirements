# Tela: Lista de Exercícios `[VELA-3001]`

---

## Metadados
| Campo | Valor |
|---|---|
| **Nome da tela** | Lista de Exercícios |
| **Modulo** | Exercícios |
| **Codigo** | VELA-3001 |
| **Prioridade** | 🔵 MVP |
| **Status** | 🟢 CONCLUIDO |
| **Ultima atualizacao** | 2026-06-23 |

---

## 1. Objetivo da Tela
> O que o usuario consegue fazer nesta tela? Qual problema ela resolve?

Tela onde o **Treinador** consulta o **seu acervo de exercícios** (os que ele criou). Exibe os exercícios em **cards finos** com **busca sempre visível** e **filtros por grupo muscular e categoria**. Cada card traz um **atalho de vídeo** que abre o vídeo de execução **sem sair da tela**. A partir daqui o Treinador **cria** um novo exercício, **abre** um exercício para ver detalhes ou o **edita**. É o hub do módulo de Exercícios.

---

## 2. Quem Acessa / Pre-condicoes
> Quem pode ver esta tela? Quais condicoes precisam ser verdadeiras?

- **Usuario:**
  - **Treinador** — vê o próprio acervo; cria/edita/exclui seus exercícios.
  - **Aluno** — (consulta futura) vê e busca exercícios, sem ações de criação/edição.
- **Pre-condicoes:**
  - Usuário deve estar logado.
  - **Não há acervo global de exercícios** — o acervo do Treinador pode começar vazio. (A base global do app é apenas de **vídeos**, usada no cadastro.)
- **Permissoes especiais:** Criar/editar/excluir exigem role de **Treinador** (ver Seção 8).

---

## 3. Layout e Componentes Visuais
> Descreva a estrutura visual da tela de cima para baixo.

### 3.1 Header / Cabecalho
- Conteudo: Título "Exercícios" + **barra de busca sempre visível** logo abaixo (sem precisar de toque extra para abrir).
- Comportamento: Busca filtra a lista **em tempo real** conforme o usuário digita.

### 3.2 Corpo Principal

**Secao 1 — Filtros**
- Componente: Três **botões dropdown** abaixo da busca — **"Grupo muscular ▾"**, **"Categoria ▾"** e **"Nível ▾"** — numa fileira com **scroll horizontal** (os filtros rolam lateralmente quando não cabem).
- Conteudo: Grupo muscular (peito, costas, ombro, braço, perna, etc.), Categoria (hipertrofia, força, alongamento, etc.) e Nível (iniciante, intermediário, avançado).
- Comportamento: Tocar no botão abre um **seletor em bottom-sheet** com as opções. Filtros são combináveis entre si e com a busca; o botão indica quando há filtro ativo.

**Secao 2 — Contador de resultados**
- Componente: Linha de texto discreta acima da lista (ex: **"12 exercícios"**).
- Comportamento: Reflete o total filtrado — com busca/filtro ativo, mostra o número de resultados correspondentes.

**Secao 3 — Lista de exercícios**
- Componente: Lista vertical de **cards finos**, ordenada **alfabeticamente (A→Z)** por padrão, em **lista corrida** (sem cabeçalhos de letra).
- Conteudo de cada card:
  - **Thumbnail** com **ícone de play** (capa do exercício ou frame do vídeo)
  - **Nome** do exercício
  - **Grupo muscular primário** · **Categoria** · **Nível** — em uma linha de metadados; categoria e nível só aparecem quando preenchidos (separador "·" entre eles)
  - **Ícone ⋮** (menu de ações) no canto — só para o Treinador
  - Quando aplicável, etiqueta **"Inativo"**
- Comportamento: Scroll vertical. Tocar no card abre a Visualização `[VELA-3002]`. Tocar no **ícone de play** aciona o **atalho de vídeo** — modal/lightbox por cima da lista (ver Seção 5). Tocar no **ícone ⋮** abre o menu de ações (Incluir em treino / Editar / Ativar-Desativar / Excluir). Exercícios **inativos** aparecem com a etiqueta "Inativo"; continuam visíveis e abríveis, mas não podem ser adicionados a novos treinos.

**Secao 4 — Bottom-sheet "Incluir em treino"** (acionado pelo menu ⋮)
- Componente: Overlay inferior (bottom-sheet) com a **lista de treinos em rascunho/em construção** do Treinador, cada um com **checkbox** (seleção múltipla), e botão **"Adicionar"**.
- Conteudo: Nome de cada treino; treinos que **já contêm** o exercício aparecem **marcados e desabilitados** com o rótulo **"Já no treino"**.
- Comportamento: Treinador marca um ou mais treinos e confirma; o exercício entra em cada treino com **prescrição vazia** (séries/repetições/descanso preenchidos depois no Treino, `[VELA-4003]`). O bottom-sheet exibe a mensagem de apoio **"Entre no treino para finalizar."**. Ao concluir, toast **"Adicionado a N treino(s) — entre no treino para finalizar"**. Se não houver treino em rascunho, exibir estado vazio orientando a criar um treino primeiro.

### 3.3 Footer / Rodape
- Conteudo: **FAB "+"** ("Novo exercício") — visível apenas para o Treinador.
- Comportamento: Fixo na parte inferior. Abre o Cadastro `[VELA-3003]`.

---

## 4. Campos e Formularios

| # | Nome do Campo | Tipo | Obrigatorio | Placeholder | Validacao | Mensagem de Erro |
|---|---|---|---|---|---|---|
| 1 | Busca | Text | Não | "Buscar exercício" | — | N/A |

### Regras de Preenchimento
- A busca é **normalizada**: ignora acentuação e diferença de maiúsculas/minúsculas (ex: digitar "triceps", "Tríceps" ou "TRICEPS" retorna os mesmos resultados). Compara o termo digitado (normalizado) contra o **nome normalizado** dos exercícios.
- A busca aparece **já aberta** ao entrar na tela — não exige um segundo toque para começar a digitar.

---

## 5. Botoes e Acoes

| # | Componente | Label / Icone | Posicao | Estado Inicial | Acao ao Clicar |
|---|---|---|---|---|---|
| 1 | Card do exercício | (área do card) | Lista | Ativo | Abre Visualizar Exercício `[VELA-3002]` |
| 2 | Ícone de play | ▶ sobre a thumbnail | Card | Ativo (se houver vídeo) | Abre o **atalho de vídeo** — modal/lightbox com o player do YouTube **por cima da lista**; fecha e volta para a mesma posição |
| 3 | FAB | "+" / "Novo exercício" | Rodapé | Visível só p/ Treinador | Abre Cadastro `[VELA-3003]` em modo criação |
| 4 | Botão dropdown de filtro | "Grupo muscular ▾" / "Categoria ▾" / "Nível ▾" | Linha de filtros (scroll horizontal) | Ativo | Abre **seletor em bottom-sheet** e aplica filtro; indica filtro ativo |
| 5 | Ícone de menu | ⋮ | Canto do card | Visível só p/ Treinador | Abre menu de ações do card |
| 6 | Ação do item (Treinador) | "Incluir em treino" / "Editar" / "Ativar/Desativar" / "Excluir" | Menu ⋮ do card | Conforme permissão | **Incluir em treino** → abre bottom-sheet de treinos (ver #7); Editar → `[VELA-3003]`; Ativar/Desativar → alterna disponibilidade (com aviso ao desativar); Excluir → modal de confirmação (**só se não estiver em uso**) |
| 7 | Bottom-sheet "Incluir em treino" | Lista de treinos (rascunho) com checkbox + botão "Adicionar" | Overlay inferior | — | Treinador marca **um ou mais** treinos e confirma; o exercício é adicionado a cada um com **prescrição vazia** (séries/reps/descanso ajustados depois no Treino, `[VELA-4003]`). Toast "Adicionado a N treino(s) — entre no treino para finalizar" |

---

## 6. Estados da Tela

### 6.1 Estado Inicial / Vazio
- **Treinador sem exercícios:** "Você ainda não criou exercícios. Toque em + para começar."
- **Busca/filtro sem resultados:** mensagem "Nenhum exercício encontrado" + sugestão de limpar filtros.

### 6.2 Estado de Carregamento (Loading)
- Skeleton loader nos cards enquanto a lista carrega.

### 6.3 Estado de Erro
- **Erro de rede/API:** toast "Não foi possível carregar os exercícios. Tente novamente." + botão de recarregar.
- **Erro ao carregar vídeo no atalho:** mensagem dentro do modal "Não foi possível carregar o vídeo."

### 6.4 Estado de Sucesso
- Após criar/editar um exercício, retorno à lista com toast e item destacado/no topo.
- Após excluir, toast "Exercício excluído" e remoção do card.
- Após **incluir em treino(s)**, toast "Adicionado a N treino(s) — entre no treino para finalizar" e fechamento do bottom-sheet.
- **Bottom-sheet sem treinos em rascunho:** estado vazio "Você não tem treinos em construção" + orientação para criar um treino antes.

### 6.5 Estado Desabilitado / Bloqueado
- Para o **Aluno** (consulta futura), o FAB "+" e as ações de editar/excluir não aparecem.

---

## 7. Fluxo de Navegacao

### De onde o usuario chega nesta tela
| Origem | Gatilho |
|---|---|
| Aba/menu do Treinador | Item de navegação principal do Treinador — abre a Lista como hub do módulo de Exercícios (dependência: painel/menu do Treinador ainda não mapeado) |
| Montagem/edição de Treino | Treinador entra para **selecionar exercícios** ao montar/editar um treino (tela em "modo seleção", a partir de `[VELA-4003]`) |
| Cadastro de Exercício `[VELA-3003]` | Após salvar/voltar |
| Visualizar Exercício `[VELA-3002]` | Botão voltar |

### Para onde o usuario pode ir desta tela
| Destino | Gatilho |
|---|---|
| Visualizar Exercício `[VELA-3002]` | Toca no card |
| Cadastro de Exercício `[VELA-3003]` | FAB "+" (criar) ou ação "Editar" |
| (Overlay) Atalho de vídeo | Toca no ícone de play |

---

## 8. Regras de Negocio
> Regras especificas que impactam o comportamento desta tela.

- RN01: A lista contém apenas os **exercícios criados pelo Treinador** logado (não há acervo global de exercícios).
- RN02: A busca é **normalizada** (sem acentos, minúsculas) e aparece **sempre aberta**.
- RN03: Filtros de **grupo muscular**, **categoria** e **nível** são combináveis entre si e com a busca.
- RN04: O card exibe **thumbnail + play**, **nome** e uma linha de metadados com **grupo muscular primário · categoria · nível**. Categoria e nível só aparecem **quando preenchidos**; o grupo muscular primário é sempre exibido. Equipamento e trilha **não** entram no card.
- RN05: O atalho de vídeo abre o vídeo em **modal/lightbox por cima da lista**, sem perder a posição/contexto (confirmado).
- RN06: Ordenação padrão **alfabética (A→Z)**.
- RN07: **Ativar/Desativar**: exercício **desativado** continua nos treinos que já o usam, mas **não pode ser adicionado a novos**; aparece com etiqueta "Inativo" na lista. Ao desativar, exibir mensagem explicando esse comportamento. **Os dados do exercício são preservados** ao desativar e voltam ao reativar. Ao **reativar**, exibir alerta pedindo para **revisar o exercício**.
- RN08: **Excluir só é permitido se o exercício não estiver em uso por nenhum treino.** Se estiver em uso, a exclusão fica indisponível e o caminho é **Desativar**.
- RN09: Apenas **Treinador** vê o FAB "+" e as ações de editar/excluir. Todo exercício é do próprio Treinador.
- RN10: Exclusão é **definitiva** e sempre confirmada por modal.
- RN11: Ao chegar pela **montagem/edição de Treino** (`[VELA-4003]`), a tela opera em **modo seleção** (foco em escolher exercícios); o acesso pela **aba/menu do Treinador** opera em modo de gestão (criar/editar/excluir). _O layout do modo seleção será detalhado (e ganhará frame no mockup) ao detalhar o seletor de exercícios do Cadastro de Treino._
- RN12: Acima da lista é exibido um **contador de resultados** ("X exercícios") que reflete o total filtrado pela busca/filtros.
- RN13: **Incluir em treino** (atalho do menu ⋮): permite ao Treinador adicionar o exercício a **um ou mais treinos** sem sair da lista nem abrir a tela de Treino. O exercício entra com **prescrição vazia** (séries/reps/descanso editados depois no Treino, `[VELA-4003]`). _Contrapartida no Cadastro de Treino: quando o treino tiver exercícios entrados por este atalho ainda sem prescrição, exibir aviso obrigando a **completar séries/repetições/descanso antes de salvar** — ver decisão #29 no `01-visao-geral.md`._
- RN14: Só aparecem no seletor os **treinos em rascunho/em construção** do Treinador — treinos já finalizados não são elegíveis.
- RN15: Treino que **já contém** o exercício aparece **desabilitado** no seletor ("Já no treino") — não é possível duplicar o mesmo exercício no mesmo treino por este atalho.
- RN16: A ação **"Incluir em treino" não fica disponível para exercícios Inativos** (coerente com RN07 — inativo não pode entrar em novos treinos).

---

## 9. Responsividade (Mobile vs Web)

| Aspecto | Mobile | Web |
|---|---|---|
| Layout | Lista de cards em coluna única; FAB flutuante no canto | Grid/lista com mais densidade; ação "Novo exercício" como botão no topo |
| Busca | Barra fixa no topo, sempre visível | Barra no topo, sempre visível |
| Atalho de vídeo | Modal ocupando boa parte da tela | Lightbox centralizado sobre a lista |

---

## 10. Acessibilidade
- Campo de busca com label acessível e foco anunciado.
- Cards navegáveis por teclado; ícone de play com label "Assistir ao vídeo de [nome do exercício]".
- Contraste conforme WCAG 2.1 AA (paleta Vela).
- Filtros operáveis por teclado e leitor de tela; estado selecionado anunciado.
- Thumbnails com texto alternativo (nome do exercício).

---

## 11. Historico de Alteracoes

| Data | Autor | Descricao |
|---|---|---|
| 2026-06-17 | Equipe Vela | Criação inicial do documento (lista de exercícios — visão do Treinador); substitui o antigo "Catálogo de Exercícios" |
| 2026-06-18 | Equipe Vela | Definidos pontos de entrada (aba/menu do Treinador + montagem/edição de Rotina, modo seleção); RNs renumeradas em sequência; status → 🟢 CONCLUIDO |
| 2026-06-18 | Equipe Vela | Decisões visuais p/ mockup: ações do card via ícone ⋮; filtros como botões dropdown → bottom-sheet; lista corrida A→Z; contador de resultados (RN12); rodapé só com FAB. Frame de "modo seleção" adiado até mapear Rotina |
| 2026-06-18 | Equipe Vela | Novo atalho "Incluir em rotina" no menu ⋮ (RN13–RN16): adiciona o exercício a uma ou mais rotinas em rascunho, com prescrição vazia, sem abrir a tela de Rotina |
| 2026-06-18 | Equipe Vela | Mensagem de finalizar no toast ("entre na rotina para finalizar"). Visual do bottom-sheet "Incluir em rotina" marcado como ⚠️ PENDENTE — revisar após mapear Rotinas; status → 🟠 PENDENTE REVISAO |
| 2026-06-18 | Equipe Vela | Card passa a exibir **categoria** e **nível** (quando preenchidos) ao lado do grupo muscular, na linha de metadados (RN04 atualizada — antes era só grupo muscular) |
| 2026-06-18 | Equipe Vela | Adicionado **filtro por Nível** (3º dropdown); fileira de filtros com scroll horizontal (RN03 atualizada) |
| 2026-06-18 | Equipe Vela | Mensagem do bottom-sheet "Incluir em rotina" ajustada para "Entre na rotina para finalizar."; criada decisão #29 (aviso de revisão na tela de Rotina para exercícios com prescrição vazia) |
| 2026-06-23 | Maria Isabela | **Realinhamento da hierarquia Exercício → Treino → Rotina** (decisão #28): exercício é incluído em **Treino**, nunca direto na Rotina. Atalho **"Incluir em rotina" renomeado para "Incluir em treino"** (Seção 3/4, ações #6/#7, RN13–RN16); bottom-sheet passa a listar **treinos em rascunho** ("Já no treino", "Entre no treino para finalizar"); prescrição preenchida no Treino (`[VELA-4003]`). **Modo seleção** agora vem da **montagem de Treino** (RN11, fluxo de navegação). Trava de exclusão e mensagens de inativo referem **treino** (RN07/RN08). Pendência do bottom-sheet **resolvida**; status → 🟢 CONCLUIDO. |

# Tela: Lista de Exercícios `[VELA-3001]`

---

## Metadados
| Campo | Valor |
|---|---|
| **Nome da tela** | Lista de Exercícios |
| **Modulo** | Exercícios |
| **Codigo** | VELA-3001 |
| **Prioridade** | 🔵 MVP |
| **Status** | 🟡 EM ANDAMENTO |
| **Ultima atualizacao** | 2026-06-17 |

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
- Componente: Linha de filtros (chips/botões) abaixo da busca.
- Conteudo: Filtro por **Grupo muscular** (peito, costas, ombro, braço, perna, etc.) e por **Categoria** (hipertrofia, força, alongamento, etc.).
- Comportamento: Toque abre o seletor de opções; filtros são combináveis e refletem na contagem de resultados.

**Secao 2 — Lista de exercícios**
- Componente: Lista vertical de **cards finos**, ordenada **alfabeticamente (A→Z)** por padrão.
- Conteudo de cada card:
  - **Thumbnail** com **ícone de play** (capa do exercício ou frame do vídeo)
  - **Nome** do exercício
  - **Grupo muscular primário**
  - Quando aplicável, etiqueta **"Inativo"**
- Comportamento: Scroll vertical. Tocar no card abre a Visualização `[VELA-3002]`. Tocar no **ícone de play** aciona o **atalho de vídeo** — modal/lightbox por cima da lista (ver Seção 5). Exercícios **inativos** aparecem com a etiqueta "Inativo"; continuam visíveis e abríveis, mas não podem ser adicionados a novas rotinas.

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
| 4 | Botão de filtro | "Grupo muscular" / "Categoria" | Linha de filtros | Ativo | Abre seletor de opções e aplica filtro |
| 5 | Ação do item (Treinador) | "Editar" / "Ativar/Desativar" / "Excluir" | Menu do card | Conforme permissão | Editar → `[VELA-3003]`; Ativar/Desativar → alterna disponibilidade (com aviso ao desativar); Excluir → modal de confirmação (**só se não estiver em uso**) |

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

### 6.5 Estado Desabilitado / Bloqueado
- Para o **Aluno** (consulta futura), o FAB "+" e as ações de editar/excluir não aparecem.

---

## 7. Fluxo de Navegacao

### De onde o usuario chega nesta tela
| Origem | Gatilho |
|---|---|
| ⚠️ PENDENTE — ponto de entrada | Ainda não definido. Acessos previstos: (1) ao **montar/editar uma Rotina** (selecionar exercícios); (2) por **aba/menu do Treinador** (depende do painel do Treinador, ainda não mapeado) |
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
- RN03: Filtros de **grupo muscular** e **categoria** são combináveis com a busca.
- RN04: O card exibe **thumbnail + play**, **nome** e **grupo muscular primário** (decisão do cliente — sem categoria/equipamento/trilha no card).
- RN05: O atalho de vídeo abre o vídeo em **modal/lightbox por cima da lista**, sem perder a posição/contexto (confirmado).
- RN09: Ordenação padrão **alfabética (A→Z)**.
- RN10: **Ativar/Desativar**: exercício **desativado** continua nas rotinas que já o usam, mas **não pode ser adicionado a novas**; aparece com etiqueta "Inativo" na lista. Ao desativar, exibir mensagem explicando esse comportamento. **Os dados do exercício são preservados** ao desativar e voltam ao reativar. Ao **reativar**, exibir alerta pedindo para **revisar o exercício**.
- RN11: **Excluir só é permitido se o exercício não estiver em uso por nenhuma rotina.** Se estiver em uso, a exclusão fica indisponível e o caminho é **Desativar**.
- RN06: Apenas **Treinador** vê o FAB "+" e as ações de editar/excluir. Todo exercício é do próprio Treinador.
- RN07: Exclusão é **definitiva** e sempre confirmada por modal.

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

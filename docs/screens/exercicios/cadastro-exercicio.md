# Tela: Cadastro / Edição de Exercício `[VELA-3003]`

---

## Metadados
| Campo | Valor |
|---|---|
| **Nome da tela** | Cadastro / Edição de Exercício |
| **Modulo** | Exercícios |
| **Codigo** | VELA-3003 |
| **Prioridade** | 🔵 MVP |
| **Status** | 🟢 CONCLUIDO |
| **Ultima atualizacao** | 2026-06-23 |

---

## 1. Objetivo da Tela
> O que o usuario consegue fazer nesta tela? Qual problema ela resolve?

Formulário onde o **Treinador** cria um novo exercício ou edita um exercício do **seu** acervo. Define o exercício de forma **reutilizável** (nome, classificação, mídia e orientações), para depois ser adicionado a um **Treino** (o exercício **não** vai direto para a Rotina — a Rotina é formada por Treinos). **Não** define séries/repetições/descanso — esses parâmetros são prescritos **no Treino** (`[VELA-4003]`), pois o mesmo exercício é usado com prescrições diferentes em treinos distintos. A mesma tela serve para **criar** e **editar** (modo dinâmico: vem em branco ou pré-preenchida).

---

## 2. Quem Acessa / Pre-condicoes
> Quem pode ver esta tela? Quais condicoes precisam ser verdadeiras?

- **Usuario:** **Treinador** autenticado. O **Aluno** não acessa esta tela (apenas consulta exercícios pela Lista/Visualização).
- **Pre-condicoes:**
  - Usuário deve estar logado com perfil de Treinador.
  - **Não existe acervo global de exercícios** — todo exercício pertence ao Treinador que o criou. O app **não** disponibiliza uma base pronta de vídeos: no campo Vídeo, o Treinador escolhe entre **seus próprios vídeos** (que ele já adicionou ao app) ou cola um **link do YouTube**.
- **Permissoes especiais:** Nenhuma além da role de Treinador.

---

## 3. Layout e Componentes Visuais
> Descreva a estrutura visual da tela de cima para baixo.

### 3.1 Header / Cabecalho
- Conteudo: Botão voltar (←) + Título "Novo exercício" (criação) ou "Editar exercício" (edição) + ação de salvar.
- Comportamento: Fixo no topo. Ao tentar voltar com alterações não salvas, exibe modal de confirmação ("Descartar alterações?").

### 3.2 Corpo Principal
> **Tela única**: formulário em **fluxo contínuo** (rolagem vertical), com os campos em sequência. Os blocos A–D servem apenas como **subtítulos discretos** que organizam visualmente o formulário — **não** são seções retráteis. Segue o layout simples dos demais formulários do app.

**Bloco A — Identificação**
- Componente: Campo de texto.
- Conteudo: Nome do exercício.

**Bloco B — Classificação**
- Componente: Selects, multi-select e toggles.
- Conteudo: Grupo muscular primário, grupos secundários, categoria, equipamentos complementares, nível e trilha Vela.

**Bloco C — Mídia**
- Componente: Seletor de vídeo (escolher entre **meus vídeos** **ou** colar link do YouTube) + uploader de imagem.
- Conteudo: **Vídeo de execução** (escolhido entre os **vídeos do próprio Treinador** ou via **link do YouTube**) — **opcional** — e imagem de capa.
- Comportamento: Ao escolher um dos meus vídeos ou colar um link válido do YouTube, exibe **pré-visualização** (thumbnail/player). Se não houver imagem de capa, a thumbnail do vídeo é usada como capa.

**Bloco D — Orientação ao Aluno**
- Componente: Campos de texto longo (textarea).
- Conteudo: Instruções de execução e observações gerais.

### 3.3 Footer / Rodape
- Conteudo: Botão primário "Salvar exercício". Em telas menores, fixo na parte inferior.
- Comportamento: Desabilitado até os campos obrigatórios estarem válidos.

---

## 4. Campos e Formularios

| # | Nome do Campo | Tipo | Obrigatorio | Placeholder | Validacao | Mensagem de Erro |
|---|---|---|---|---|---|---|
| 1 | Nome do exercício | Text | Sim | "Ex: Supino reto com barra" | Mín. 3 caracteres; **único por nível** no acervo do Treinador | "Informe o nome do exercício" / "Já existe um exercício com esse nome neste nível" |
| 2 | Grupo muscular primário | Select (único) | Sim | "Selecione o grupo principal" | Deve ser selecionado | "Selecione o grupo muscular primário" |
| 3 | Grupos musculares secundários | Multi-select | Não | "Opcional" | — | N/A |
| 4 | Categoria | Select (único) | Não* | "Selecione a categoria" | — | N/A |
| 5 | Equipamentos complementares | Multi-select (sugere usados + digitar) | Não | "(ex: band, step, entre outros)" | — | N/A |
| 6 | Nível | Select | Sim | "Selecione o nível" | Deve ser selecionado | "Selecione o nível" |
| 7 | Trilha Vela | Multi-select | Não | ".track / .performance" | — | N/A |
| 8 | Vídeo de execução | Seletor de vídeo / URL | Não | "Meus vídeos ou colar link do YouTube" | Se for link, URL válida do YouTube (youtube.com / youtu.be) | "Informe um link válido do YouTube" |
| 9 | Imagem de capa | Upload de imagem | Não | "Adicionar imagem" | Formato de imagem (JPG/PNG) | "Formato de imagem inválido" |
| 10 | Instruções de execução | Textarea | Não | "Descreva o passo a passo da execução" | — | N/A |
| 11 | Observações gerais | Textarea | Não | "Observações gerais sobre o exercício" | — | N/A |

> *A **Categoria** é **fortemente recomendada** (alimenta o filtro da Lista), mas não bloqueia o salvar. Obrigatórios: **Nome**, **Grupo muscular primário** e **Nível**.

### Opções dos campos de seleção (referência)
- **Grupo muscular (primário/secundário):** peito, costas, ombro, bíceps, tríceps, antebraço, trapézio, lombar, abdômen, quadríceps, posterior de coxa, glúteo, panturrilha.
- **Categoria:** hipertrofia, força, resistência, potência, alongamento/mobilidade, aquecimento, cardio.
- **Equipamento:** barra, halteres, máquina, polia/cabo, peso corporal, kettlebell, smith, elástico, banco.
- **Nível:** iniciante / intermediário / avançado — opções **fixas**, sem texto livre (vocabulário controlado: sustenta a unicidade nome + nível e os filtros).
- **Trilha Vela:** `.track` / `.performance` (pode pertencer a ambas).

### Regras de Preenchimento
- A partir do **Nome**, o sistema gera automaticamente um **nome normalizado** (sem acentos, em minúsculas) usado apenas para a busca na Lista — não é campo visível nem editável.
- O **Vídeo de execução** é **opcional** e aceita duas fontes: **escolher entre meus vídeos** (os que o Treinador já adicionou ao app) ou **colar um link do YouTube** (`youtube.com/watch?v=...`, `youtu.be/...`, `youtube.com/shorts/...`); ao validar, gera a pré-visualização.
- Se **Imagem de capa** ficar vazia, a thumbnail do vídeo vira a capa padrão (comportamento interno; sem mensagem na tela).
- **Equipamentos complementares:** campo **único** (multi-seleção, opcional). O Treinador adiciona **apenas o que não fica óbvio no vídeo** (ex: band, step). Ao tocar em "adicionar", o app **sugere os materiais que ele já usou antes** e permite **digitar um novo**.
- Séries, repetições, carga, descanso e cadência **não** existem nesta tela (séries/repetições/descanso são definidos no **Treino**, `[VELA-4003]`).

---

## 5. Botoes e Acoes

| # | Componente | Label / Icone | Posicao | Estado Inicial | Acao ao Clicar |
|---|---|---|---|---|---|
| 1 | Botão primário | "Salvar exercício" | Rodapé | Desabilitado até obrigatórios válidos | Valida → salva no acervo do Treinador → volta para a Lista `[VELA-3001]` com toast de sucesso |
| 2 | Botão voltar | ← | Header (esq.) | Ativo | Se houver alterações não salvas, abre modal "Descartar alterações?"; senão, volta |
| 3 | Toggle | "Ativo / Inativo" | Topo do form (só edição) | Reflete o estado atual | Alterna disponibilidade. Ao **desativar**, exibe: "Exercícios inativos continuam nos treinos atuais, mas não podem ser adicionados a novos." Ao **reativar**, exibe alerta pedindo para **revisar o exercício antes de reativar** (as informações voltam como estavam). |
| 4 | Botão | "Excluir exercício" | Rodapé / menu (só edição) | Visível apenas em edição de exercício próprio; **desabilitado se estiver em uso** | Abre modal de confirmação → exclui definitivamente (só se não estiver em nenhum treino) |

---

## 6. Estados da Tela

### 6.1 Estado Inicial / Vazio
- **Criação:** todos os campos em branco; "Salvar" desabilitado.
- **Edição:** campos pré-preenchidos com os dados do exercício.

### 6.2 Estado de Carregamento (Loading)
- Ao salvar: spinner sobre o botão "Salvar exercício", botão desabilitado durante a requisição.
- Ao validar o link do YouTube: indicador de carregamento na área de pré-visualização.

### 6.3 Estado de Erro
- **Erro de campo:** borda vermelha + mensagem abaixo do campo (ver tabela da Seção 4).
- **Erro de rede:** toast "Sem conexão. Tente novamente." (mantém os dados preenchidos).
- **Erro da API ao salvar:** toast "Não foi possível salvar o exercício. Tente novamente."

### 6.4 Estado de Sucesso
- Toast "Exercício salvo!" + redirect para a Lista `[VELA-3001]`, com o exercício salvo destacado/no topo.

### 6.5 Estado Desabilitado / Bloqueado
- N/A — não há acervo global; todo exercício é do próprio Treinador e editável por ele.

---

## 7. Fluxo de Navegacao

### De onde o usuario chega nesta tela
| Origem | Gatilho |
|---|---|
| Lista de Exercícios `[VELA-3001]` | Treinador toca em "Novo exercício" (FAB "+") |
| Lista de Exercícios `[VELA-3001]` | Treinador toca em "Editar" em um exercício |
| Visualizar Exercício `[VELA-3002]` | Treinador toca em "Editar" |

### Para onde o usuario pode ir desta tela
| Destino | Gatilho |
|---|---|
| Lista de Exercícios `[VELA-3001]` | Salvar com sucesso, ou voltar/descartar |
| Visualizar Exercício `[VELA-3002]` | (Opcional) após salvar, abrir a visualização do exercício |

---

## 8. Regras de Negocio
> Regras especificas que impactam o comportamento desta tela.

- RN01: Apenas **Treinador** acessa esta tela. O Aluno nunca cria ou edita exercícios.
- RN02: **Não há acervo global de exercícios** — todo exercício pertence ao Treinador que o criou, que pode editá-lo/excluí-lo.
- RN03: O app **não** tem base pronta de vídeos. No campo Vídeo, o Treinador pode **escolher entre os seus próprios vídeos** (os que ele já adicionou ao app) ou **colar um link do YouTube**. O vídeo é **opcional**.
- RN04: O **nome normalizado** (sem acentos, minúsculas) é derivado automaticamente do Nome para alimentar a busca da Lista.
- RN05: A combinação **nome + nível** deve ser **única dentro do acervo do Treinador** — ou seja, é permitido repetir o mesmo nome **apenas** se o **nível** for diferente (exercícios de outros treinadores não geram conflito). Por isso o **Nível é obrigatório**.
- RN06: **Séries, repetições, descanso (e carga/cadência) não pertencem ao exercício** — séries/repetições/descanso são definidos no **Treino** (`[VELA-4003]`). O exercício é a peça reutilizável; a prescrição vive no Treino que o usa.
- RN07: Exclusão é **definitiva** (sem lixeira), sempre confirmada por modal e **só permitida se o exercício não estiver em uso por nenhum treino**. Se estiver em uso, a exclusão fica indisponível e o caminho é **Desativar** (RN11).
- RN11: O exercício tem estado **Ativo/Inativo** (toggle, só para exercícios do próprio Treinador). **Inativo** = permanece nos treinos que já o usam, mas **não pode ser adicionado a novos**; ao desativar, exibir a mensagem explicativa. **Desativar não altera nem apaga nenhum dado** — todas as informações preenchidas ficam **salvas** e a tela continua **toda preenchida**. Ao **reativar**, exibir um **alerta pedindo para revisar o exercício** (as informações voltam exatamente como estavam quando foi desativado).
- RN08: **Não há campo de áudio no exercício.** A gravação de áudio de instrução foi movida para a **aba de Treino** (o Treinador grava no app uma instrução sobre o **treino**, não sobre um exercício específico) — a ser detalhado ao mapear Treino.
- RN09: O equipamento é um **campo único** ("Equipamentos complementares", multi-seleção, opcional). Registra-se **só o que não é óbvio no vídeo** (ex: band, step). Ao adicionar, o app **sugere os materiais já usados** pelo Treinador e permite **digitar um novo**. Não há "principal vs. adicional".
- RN10: O formulário é uma **tela única** em fluxo contínuo (os blocos A–D são apenas subtítulos visuais, sem accordion); **Nome**, **Grupo muscular primário** e **Nível** bloqueiam o salvar (demais campos, inclusive o vídeo, são opcionais/recomendados).

---

## 9. Responsividade (Mobile vs Web)

| Aspecto | Mobile | Web |
|---|---|---|
| Layout do formulário | Coluna única, scroll vertical; botão "Salvar" fixo no rodapé | Formulário centralizado (max-width ~720px); campos de classificação podem usar 2 colunas |
| Upload de imagem/áudio | Câmera/galeria/gravação do dispositivo | Seleção de arquivo |
| Pré-visualização do vídeo | Player embutido responsivo | Player embutido responsivo |

---

## 10. Acessibilidade
- Labels acessíveis em todos os campos do formulário.
- Mensagens de erro associadas ao campo (aria-describedby) e anunciadas por leitor de tela.
- Contraste conforme WCAG 2.1 AA (paleta Vela: verde-limão neon sobre fundos azuis/escuros).
- Navegação por teclado com ordem de tabulação lógica (A → B → C → D → Salvar).
- Textos alternativos na imagem de capa e ícones; player de vídeo com controles acessíveis.

---

## 11. Historico de Alteracoes

| Data | Autor | Descricao |
|---|---|---|
| 2026-06-17 | Equipe Vela | Criação inicial do documento (cadastro/edição de exercício — visão do Treinador) |
| 2026-06-17 | Equipe Vela | Revisão completa + mockup: tela única (sem accordion), sem acervo global, equipamentos complementares, vídeo de execução obrigatório (base/YouTube), áudio movido para Treino, orientação em 2 campos, nível obrigatório (3 fixos) com unicidade nome+nível, ciclo ativar/desativar (dados preservados, alerta de revisão ao reativar). Status → CONCLUIDO |
| 2026-06-18 | Equipe Vela | Mídia: fonte de vídeo passa de "base do app" para **"meus vídeos"** (vídeos que o próprio Treinador já adicionou — não há base pronta) e o **vídeo deixa de ser obrigatório**. Obrigatórios agora: Nome, Grupo muscular primário e Nível. |
| 2026-06-23 | Maria Isabela | **Realinhamento da hierarquia Exercício → Treino → Rotina:** exercício é adicionado a um **Treino** (não vai direto para a Rotina); prescrição (séries/repetições/descanso) vive no **Treino** (`[VELA-4003]`), não na Rotina (objetivo, regras de preenchimento, RN06). Trava de exclusão e mensagens de inativo passam a referir **treino** em vez de rotina (RN07, RN11, toggle, ação Excluir). |

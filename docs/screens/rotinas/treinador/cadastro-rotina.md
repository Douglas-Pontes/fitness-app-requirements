# Tela: Cadastro / Edição de Rotina `[VELA-5003]`

---

## Metadados
| Campo | Valor |
|---|---|
| **Nome da tela** | Cadastro / Edição de Rotina |
| **Modulo** | Rotinas |
| **Codigo** | VELA-5003 |
| **Prioridade** | 🔵 MVP |
| **Status** | 🟢 CONCLUIDO |
| **Ultima atualizacao** | 2026-06-18 |

---

## 1. Objetivo da Tela
> O que o usuario consegue fazer nesta tela? Qual problema ela resolve?

Formulário onde o **Treinador** cria uma nova rotina ou edita uma rotina da **sua** base reutilizável. Uma rotina é um **agrupamento ordenado de treinos** (da base do Treinador — `[VELA-4001]`), identificados por **letras A, B, C…**, que servirá depois para ser atrelada aos alunos (atrelamento é **fluxo futuro**, fora de escopo aqui). A rotina reúne **dados gerais** (título e objetivo) e uma **lista de treinos ordenada**, onde cada treino pode receber, opcionalmente, um **dia da semana** e uma **descrição curta** específica daquela rotina. A mesma tela serve para **criar** e **editar** (modo dinâmico: vem em branco ou pré-preenchida).

---

## 2. Quem Acessa / Pre-condicoes
> Quem pode ver esta tela? Quais condicoes precisam ser verdadeiras?

- **Usuario:** **Treinador** autenticado. O **Aluno** não acessa esta tela.
- **Pre-condicoes:**
  - Usuário deve estar logado com perfil de Treinador.
  - A rotina é montada a partir dos **treinos do próprio Treinador** (`[VELA-4001]`). Para adicionar um treino à rotina, ele precisa já existir na base do Treinador.
- **Permissoes especiais:** Nenhuma além da role de Treinador.

---

## 3. Layout e Componentes Visuais
> Descreva a estrutura visual da tela de cima para baixo.

### 3.1 Header / Cabecalho
- Conteudo: Botão voltar (←) + Título "Nova rotina" (criação) ou "Editar rotina" (edição). A ação de salvar fica **apenas no botão primário do rodapé** (sem botão de salvar no topo), espelhando o Cadastro de Treino (`[VELA-4003]`).
- Comportamento: Fixo no topo. Ao tentar voltar com alterações não salvas, exibe modal de confirmação ("Descartar alterações?").

### 3.2 Corpo Principal
> **Tela única**: formulário em **fluxo contínuo** (rolagem vertical). Os blocos A–B abaixo são apenas **subtítulos discretos** que organizam o formulário — não são seções retráteis.

**Bloco A — Identificação** *(obrigatório)*
- Componente: Campo de texto + textarea.
- Conteudo: **Título** da rotina e **Objetivo** da rotina.

**Bloco B — Treinos da rotina** *(obrigatório — ao menos um treino)*
- Componente: Lista **ordenada de cards de treino**, cada um identificado por uma **letra (A, B, C…)** gerada automaticamente pela posição.
- Conteudo de cada card de treino:
  - **Letra** (A, B, C…) + **nome do treino** + **categoria** do treino.
  - **Dia da semana** (opcional) e **Descrição curta** (opcional) específicos desta rotina.
  - **Ícone de vídeo / atalho de visualização**: abre **Visualizar Treino** (`[VELA-4002]`) para conferir o conteúdo do treino sem sair da montagem.
  - Handle de arraste (⠿) para reordenar e ícone de remover (🗑).
- Comportamento:
  - Botão **"Adicionar treino"** ao final da lista → abre um **seletor de treinos** (multi-seleção) sobre a **base de treinos do Treinador** (`[VELA-4001]`), retornando os treinos escolhidos para a rotina. Só lista treinos **ativos** (ver RN07).
  - **Ordenação:** os treinos seguem a ordem A → B → C…; a **letra é automática** pela posição e **não é editável**. Reordenar por **arrastar** (handle ⠿) atualiza as letras.
  - Exibe a mensagem de ajuda **"Arraste os cards para reordenar os treinos"**.
  - O **mesmo treino** pode aparecer **uma única vez** por rotina (sem duplicar o mesmo treino na mesma rotina — ver RN05).
  - O **mesmo dia da semana** pode ser usado em **mais de um treino** (ex.: A e B na segunda) — não há restrição de dia único (ver RN06).
  - **Sem limite** de quantidade de treinos por rotina (A, B, C, D, E…) — ver RN11.
  - Apenas treinos **ativos** podem ser adicionados; inativos não aparecem como opção na seleção (espelha o ciclo de vida de `[VELA-4003]`).

### 3.3 Footer / Rodape
- Conteudo: Botão primário "Salvar rotina". Em telas menores, fixo na parte inferior.
- Comportamento: Desabilitado até os campos obrigatórios estarem válidos (Título + Objetivo + ao menos 1 treino).
- **Excluir (só edição):** ao fim do formulário (acima do rodapé), um **botão de texto vermelho "Excluir rotina"** — não é botão primário. Mesmo posicionamento do Cadastro de Treino (`[VELA-4003]`).

---

## 4. Campos e Formularios

### Dados gerais da rotina
| # | Nome do Campo | Tipo | Obrigatorio | Placeholder | Validacao | Mensagem de Erro |
|---|---|---|---|---|---|---|
| 1 | Título | Text | Sim | "Ex: Hipertrofia 5x — Iniciante" | Mín. 3 caracteres; **único na base do Treinador** | "Informe o título da rotina" / "Já existe uma rotina com esse título" |
| 2 | Objetivo | Textarea | Sim | "Descreva o objetivo da rotina" | Não pode ficar em branco | "Informe o objetivo da rotina" |

### Por treino dentro da rotina
| # | Nome do Campo | Tipo | Obrigatorio | Placeholder | Validacao | Mensagem de Erro |
|---|---|---|---|---|---|---|
| 3 | Dia da semana | Select (único) | Não | "Sem dia definido" | — | N/A |
| 4 | Descrição curta | Text | Não | "Ex: foco em carga / preparatório" | — | N/A |

### Opções dos campos de seleção (referência)
- **Dia da semana (opcional):** Segunda, Terça, Quarta, Quinta, Sexta, Sábado, Domingo. Seleção única; **pode repetir** o mesmo dia entre treinos diferentes.

### Regras de Preenchimento
- A **letra (A, B, C…)** de cada treino é gerada **automaticamente** pela ordem — não é editável.
- **Título** e **Objetivo** são obrigatórios; **Dia da semana** e **Descrição curta** são opcionais por treino.
- A rotina precisa ter **ao menos um treino** para ser salva (o **Bloco B é obrigatório**).
- O **mesmo treino não pode ser adicionado duas vezes** na mesma rotina.

---

## 5. Botoes e Acoes

| # | Componente | Label / Icone | Posicao | Estado Inicial | Acao ao Clicar |
|---|---|---|---|---|---|
| 1 | Botão primário | "Salvar rotina" | Rodapé | Desabilitado até obrigatórios válidos | Valida → salva na base do Treinador → volta para a Lista `[VELA-5001]` com toast de sucesso |
| 2 | Botão voltar | ← | Header (esq.) | Ativo | Se houver alterações não salvas, abre modal "Descartar alterações?"; senão, volta |
| 3 | Botão | "Adicionar treino" | Fim da lista de treinos | Ativo | Abre o **seletor de treinos** (multi-seleção) sobre a base do Treinador `[VELA-4001]` |
| 4 | Ícone | ⠿ (arrastar) | Em cada card de treino | Ativo | Reordena o treino na rotina (atualiza as letras A/B/C…) |
| 5 | Ícone | 🗑 / "Remover" | Card de treino | Ativo | Remove o treino da rotina |
| 6 | Ícone / atalho | ▶ / "Ver treino" | Card de treino | Ativo | Abre **Visualizar Treino** `[VELA-4002]` daquele treino (conferência) |
| 7 | Toggle | "Ativo / Inativo" | Topo do form (só edição) | Reflete o estado atual | Ao **desativar**, abre modal de confirmação "Desativar rotina?" (ver Seção 6.5); ao **ativar**, alterna direto. Espelha o ciclo de vida de Treinos |
| 8 | Botão de texto (vermelho) | "Excluir rotina" | Fim do formulário (só edição) | Visível só em edição | Abre modal "Excluir rotina?" → ao confirmar, exclui definitivamente e volta à Lista `[VELA-5001]` |

---

## 6. Estados da Tela

### 6.1 Estado Inicial / Vazio
- **Criação:** campos gerais em branco; lista de treinos vazia com o botão "Adicionar treino"; "Salvar" desabilitado.
- **Edição:** campos e lista pré-preenchidos com os dados da rotina.

### 6.2 Estado de Carregamento (Loading)
- Ao salvar: spinner sobre o botão "Salvar rotina", botão desabilitado durante a requisição.
- Ao abrir a seleção de treinos: indicador de carregamento no seletor de treinos.

### 6.3 Estado de Erro
- **Erro de campo:** borda vermelha + mensagem abaixo do campo (ver tabelas da Seção 4).
- **Sem treinos:** ao tentar salvar sem nenhum treino, mensagem "Adicione ao menos um treino à rotina".
- **Erro de rede:** toast "Sem conexão. Tente novamente." (mantém os dados preenchidos).
- **Erro da API ao salvar:** toast "Não foi possível salvar a rotina. Tente novamente."

### 6.4 Estado de Sucesso
- Toast "Rotina salva!" + redirect para a Lista `[VELA-5001]`, com a rotina salva destacada/no topo.

### 6.5 Estado Desabilitado / Bloqueado
- N/A — toda rotina é do próprio Treinador e editável por ele.

### 6.6 Modais de Confirmação
- **Descartar alterações?** — ao tocar em voltar (←) com alterações não salvas: "Descartar alterações?" com ações **"Cancelar"** e **"Descartar"**.
- **Desativar rotina?** — ao desativar pelo toggle: "Desativar rotina?" + texto "A rotina deixa de ficar disponível para uso, mas seus dados são preservados." com ações **"Cancelar"** e **"Desativar"**.
- **Excluir rotina?** — ao tocar em "Excluir rotina": "Excluir rotina?" + texto "Esta ação não pode ser desfeita." com ações **"Cancelar"** e **"Excluir"** (ação destrutiva).

---

## 7. Fluxo de Navegacao

### De onde o usuario chega nesta tela
| Origem | Gatilho |
|---|---|
| Lista de Rotinas `[VELA-5001]` | Treinador toca em "Nova rotina" (FAB "+") |
| Lista de Rotinas `[VELA-5001]` | Treinador toca em "Editar" em uma rotina |
| Visualizar Rotina `[VELA-5002]` | Treinador toca em "Editar" |
| Lista `[VELA-5001]` / Visualizar `[VELA-5002]` | Treinador toca em "Duplicar" — abre o Cadastro/Edição da **cópia**, pré-preenchido com "Título (cópia)" (ver RN12) |

### Para onde o usuario pode ir desta tela
| Destino | Gatilho |
|---|---|
| Lista de Rotinas `[VELA-5001]` | Salvar com sucesso, ou voltar/descartar |
| Seletor de treinos (base `[VELA-4001]`) | Toca em "Adicionar treino" |
| Visualizar Treino `[VELA-4002]` | Toca no atalho "Ver treino" de um card |

---

## 8. Regras de Negocio
> Regras especificas que impactam o comportamento desta tela.

- **RN01:** Apenas **Treinador** acessa esta tela. O Aluno nunca cria ou edita rotinas.
- **RN02:** A rotina é uma **base reutilizável** do Treinador — agrupa **treinos** (não exercícios soltos). Atrelar a rotina a um aluno é **fluxo futuro**, fora de escopo aqui.
- **RN03:** Os treinos da rotina são identificados por **letras A, B, C…** geradas **automaticamente** pela ordem (não editáveis). Reordenar por **arrastar** atualiza as letras. *(As letras ficam reservadas para a Rotina — dentro de cada treino, os grupos seguem números 1, 2, 3…, conforme decisão #26/#32.)*
- **RN04:** Para salvar, são obrigatórios **Título**, **Objetivo** e **ao menos um treino**. **Dia da semana** e **Descrição curta** (por treino) são opcionais.
- **RN05:** O **mesmo treino** não pode ser adicionado **duas vezes** na mesma rotina.
- **RN06:** O **mesmo dia da semana** pode ser atribuído a **mais de um treino** na rotina (sem restrição de dia único). Não há, por ora, visualização tipo "semana" (grade/agenda) — decisão registrada.
- **RN07:** Só é possível adicionar à rotina **treinos do próprio Treinador** e **ativos** (treinos inativos não aparecem na seleção). A presc​rição (séries/reps/descanso) **já vem definida no próprio treino** (`[VELA-4003]`, decisão #31) — a rotina **não** reabre essa prescrição.
- **RN08:** A rotina pode ter estado **Ativo/Inativo** (toggle, só em edição), espelhando o ciclo de vida de Treinos. Inativar **não apaga dados**.
- **RN09:** Exclusão é **definitiva** (sem lixeira), sempre confirmada por modal. *(A trava de exclusão por vínculo — quando rotinas estiverem atreladas a alunos — será definida no fluxo futuro de atrelamento.)*
- **RN10:** O **título da rotina** é único na base do Treinador (rotinas de outros treinadores não geram conflito).
- **RN11:** **Não há limite** de quantidade de treinos por rotina — o Treinador adiciona quantos quiser (letras A, B, C, D, E…).
- **RN12:** **Duplicar** (acionado na Lista `[VELA-5001]` ou na Visualizar `[VELA-5002]`) cria uma cópia na base do Treinador com título **"Título (cópia)"** e abre **esta tela** (Cadastro/Edição) já pré-preenchida com a cópia, para ajustes. Esta tela **não** possui ação "Duplicar" própria — é apenas o destino da ação.

---

## 9. Responsividade (Mobile vs Web)

| Aspecto | Mobile | Web |
|---|---|---|
| Layout do formulário | Coluna única, scroll vertical; botão "Salvar" fixo no rodapé | Formulário centralizado (max-width ~720px); dados gerais podem usar 2 colunas |
| Reordenar treinos | Arrastar pelo handle (toque longo) | Arrastar pelo handle (drag-and-drop com mouse) |
| Seleção de treinos | Seletor de treinos em tela cheia | Seletor de treinos em modal/painel ou tela |
| Atalho "Ver treino" (▶) | Abre Visualizar Treino | Abre Visualizar Treino |

---

## 10. Acessibilidade
- Labels acessíveis nos campos gerais e nos campos por treino (dia da semana, descrição).
- Mensagens de erro associadas ao campo (aria-describedby) e anunciadas por leitor de tela.
- Reordenação de treinos acessível também por teclado (mover para cima/baixo), além do arrastar.
- Cada card de treino é um elemento com nome acessível (letra + nome + categoria).
- Contraste conforme WCAG 2.1 AA (paleta Vela: verde-limão neon sobre fundos azuis/escuros).

---

## 11. Historico de Alteracoes

| Data | Autor | Descricao |
|---|---|---|
| 2026-06-18 | Maria Isabela | Criação inicial do documento (entrevista `/mapear-tela`). Rotina = agrupamento ordenado de **treinos** identificados por **letras A/B/C** (arraste, letra automática). Campos gerais: Título + Objetivo (obrigatórios). Por treino: Dia da semana + Descrição curta (opcionais); dia pode repetir, sem visão de semana. Seleção de treinos via Lista `[VELA-4001]` em modo seleção; atalho de visualização `[VELA-4002]`. Salvar exige Título + Objetivo + ≥1 treino. Atrelar a aluno fora de escopo. Status → EM ANDAMENTO |
| 2026-06-18 | Maria Isabela | Revisão (`/revisar-tela`): **Excluir** = botão de texto vermelho ao fim do formulário (espelha `[VELA-4003]`); **sem limite** de treinos por rotina (RN11); **desativar** abre modal de confirmação (Seção 6.6); fixadas as copies dos modais "Descartar alterações?", "Desativar rotina?" e "Excluir rotina?"; adicionada a origem **Duplicar** (Cadastro como destino da cópia "(cópia)", RN12). Status → CONCLUIDO |
| 2026-06-24 | Maria Isabela | A seleção de treinos passa a ser descrita como **seletor de treinos** próprio da montagem de Rotina (multi-seleção sobre a base ativa do Treinador, `[VELA-4001]`), em vez de "Lista de Treinos em modo seleção". Ajuste de consistência: o "modo seleção" foi removido da tela de Treinos (`[VELA-4001]`), que não duplica mais essa responsabilidade. Sem mudança de comportamento. |

# Tela: Visualizar Treino `[VELA-4002]`

---

## Metadados
| Campo | Valor |
|---|---|
| **Nome da tela** | Visualizar Treino |
| **Modulo** | Treinos |
| **Codigo** | VELA-4002 |
| **Prioridade** | 🔵 MVP |
| **Status** | 🟢 CONCLUIDO |
| **Ultima atualizacao** | 2026-06-18 |

---

## 1. Objetivo da Tela
> O que o usuario consegue fazer nesta tela? Qual problema ela resolve?

Tela **somente leitura** onde o **Treinador** confere um treino da **sua** base reutilizável sem risco de alterar por acidente. Exibe os **dados gerais** (nome, categoria, descrição, observações, áudio) e a **lista de exercícios organizada em grupos numerados** com a prescrição (séries, repetições, descanso e descrição de execução). A partir daqui o Treinador acessa o detalhe de cada exercício e dispara as ações de gestão (**Editar**, **Duplicar**, **Excluir**). É o par de leitura do **Cadastro / Edição de Treino** (`[VELA-4003]`), espelhando o padrão de Exercícios (`[VELA-3002]`).

---

## 2. Quem Acessa / Pre-condicoes
> Quem pode ver esta tela? Quais condicoes precisam ser verdadeiras?

- **Usuario:** **Treinador** autenticado. O **Aluno** não acessa esta tela (o aluno só vê o treino dentro da Rotina, no fluxo de treinar).
- **Pre-condicoes:**
  - Usuário deve estar logado com perfil de Treinador.
  - O treino visualizado deve existir na base do próprio Treinador.
- **Permissoes especiais:** Nenhuma além da role de Treinador.

---

## 3. Layout e Componentes Visuais
> Descreva a estrutura visual da tela de cima para baixo.

### 3.1 Header / Cabecalho
- Conteudo: Botão voltar (←) + Título com o **nome do treino** + menu **"⋮"** (kebab) à direita com as ações **Duplicar** e **Excluir**.
- Comportamento: Fixo no topo. O botão voltar (←) retorna à Lista de Treinos.

### 3.2 Corpo Principal
> Tela única em **rolagem vertical**, em modo leitura. Os blocos abaixo são subtítulos discretos que organizam o conteúdo — espelham a estrutura do Cadastro de Treino (`[VELA-4003]`).

**Bloco A — Identificação**
- Componente: Bloco de texto (somente leitura).
- Conteudo: **Nome do treino**, **Categoria** e um selo de **status** (Ativo / Inativo).

**Bloco B — Detalhes** *(exibido apenas se preenchido)*
- Componente: Bloco de texto + player de áudio.
- Conteudo: **Descrição**, **Observações gerais** e **Áudio do treino** (player com duração, quando houver).
- Comportamento: Campos vazios não aparecem (sem rótulos "em branco"). Não há vídeo no treino — vídeo existe apenas por exercício.

**Bloco C — Exercícios (em grupos)**
- Componente: Lista de **grupos numerados** (1, 2, 3…); cada grupo contém um ou mais **cards de exercício**, conforme o tipo do grupo.
- Conteudo:
  - Cada **grupo** exibe seu **número** e o **tipo** (Normal, Bi-set, Tri-set, Superset, Drop-set).
  - Cada **card de exercício** exibe: **capa do vídeo do exercício** (thumbnail), **nome do exercício**, ícone de vídeo (se houver), e a prescrição em leitura — **Séries**, **Repetições**, **Descanso** e a **Descrição de execução** (quando houver).
- Comportamento:
  - Os cards de exercício são **clicáveis**: ao tocar no card/thumbnail, abre **Visualizar Exercício** (`[VELA-3002]`) daquele exercício (vídeo + execução completa).
  - Sem botões de adicionar/remover/reordenar (modo leitura). A edição da estrutura acontece no Cadastro (`[VELA-4003]`).

### 3.3 Footer / Rodape
- Conteudo: Botão primário **"Editar"** ocupando a largura do rodapé.
- Comportamento: Fixo na parte inferior. Abre o Cadastro / Edição de Treino (`[VELA-4003]`) com o treino pré-preenchido.

---

## 4. Campos e Formularios

N/A — Tela sem formularios. Todo o conteúdo é exibido em **modo leitura**.

---

## 5. Botoes e Acoes

| # | Componente | Label / Icone | Posicao | Estado Inicial | Acao ao Clicar |
|---|---|---|---|---|---|
| 1 | Botao primario | "Editar" | Rodapé (largura total) | Ativo | Abre Cadastro / Edição de Treino (`[VELA-4003]`) com o treino pré-preenchido |
| 2 | Botao voltar | ← | Header (esquerda) | Ativo | Retorna à Lista de Treinos (`[VELA-4001]`) |
| 3 | Menu kebab | ⋮ | Header (direita) | Ativo | Abre menu com "Duplicar" e "Excluir" |
| 4 | Item de menu | "Duplicar" | Dentro do menu ⋮ | Ativo | Cria cópia "Nome (cópia)" na base do Treinador e abre direto no Cadastro / Edição (`[VELA-4003]`) para ajustar |
| 5 | Item de menu | "Excluir" | Dentro do menu ⋮ | Ativo | Abre modal de confirmação → ao confirmar, exclui e volta à Lista de Treinos |
| 6 | Card de exercício | (card do exercício) | Bloco C | Ativo | Abre Visualizar Exercício (`[VELA-3002]`) daquele exercício |

---

## 6. Estados da Tela

### 6.1 Estado Inicial / Vazio
- Não há estado vazio: um treino sempre tem **≥1 exercício** (regra do Cadastro). A tela só é acessada para um treino existente.

### 6.2 Estado de Carregamento (Loading)
- **Skeleton loader** nas áreas de conteúdo (identificação e cards de exercício) enquanto o treino carrega.

### 6.3 Estado de Erro
- **Erro de carregamento:** mensagem central "Não foi possível carregar o treino." + botão **"Tentar novamente"**.
- **Erro de rede:** toast "Sem conexão. Tente novamente."

### 6.4 Estado de Sucesso
- **Após excluir:** toast "Treino excluído." + redireciona para a Lista de Treinos.
- **Após duplicar:** abre o Cadastro / Edição da cópia (o feedback de criação ocorre lá).

### 6.5 Estado Desabilitado / Bloqueado *(se aplicavel)*
- **Excluir bloqueado:** quando o treino estiver em uso em uma ou mais rotinas, a confirmação não é concluída — exibe aviso "Este treino está em uso em X rotina(s) e não pode ser excluído." (ver RN03).

---

## 7. Fluxo de Navegacao

### De onde o usuario chega nesta tela
| Origem | Gatilho |
|---|---|
| Lista de Treinos (`[VELA-4001]`) | Toca em um card de treino |

### Para onde o usuario pode ir desta tela
| Destino | Gatilho |
|---|---|
| Cadastro / Edição de Treino (`[VELA-4003]`) | Toca em "Editar" (rodapé) ou em "Duplicar" (menu ⋮) |
| Visualizar Exercício (`[VELA-3002]`) | Toca em um card de exercício |
| Lista de Treinos (`[VELA-4001]`) | Toca em ← (voltar) ou após excluir o treino |

---

## 8. Regras de Negocio
> Regras especificas que impactam o comportamento desta tela.

- **RN01:** Tela exclusiva do **Treinador**; só exibe treinos da **sua própria base**.
- **RN02:** Tela em **modo leitura** — nenhuma alteração de conteúdo acontece aqui; toda edição ocorre no Cadastro (`[VELA-4003]`).
- **RN03:** **Exclusão** é **definitiva** (app sem lixeira) e sempre passa por **modal de confirmação** ("Excluir treino? Esta ação não pode ser desfeita."). O treino **só pode ser excluído se não estiver em nenhuma rotina**; em uso, a exclusão é bloqueada com aviso (espelha decisão #31). **Interino:** enquanto o módulo **Rotinas** não existir, não há vínculo a checar → a exclusão fica **sempre liberada** (com modal); a trava por rotina passa a valer quando Rotinas existir.
- **RN04:** **Duplicar** cria uma cópia na base do Treinador com nome "Nome (cópia)" e abre o Cadastro / Edição da cópia para ajustes.
- **RN05:** O selo **Ativo / Inativo** reflete o toggle de status do treino (definido no Cadastro). Treinos **Inativos** continuam visíveis aqui em leitura, mas não devem ser ofertados na montagem de novas rotinas (regra detalhada no módulo Rotinas).

---

## 9. Responsividade (Mobile vs Web)
> Diferencas de comportamento ou layout entre plataformas.

| Aspecto | Mobile | Web |
|---|---|---|
| Layout | Coluna única, rolagem vertical | Mesma estrutura em container mais largo (centralizado) |
| Ações primárias | "Editar" fixo no rodapé | "Editar" pode acompanhar o conteúdo / barra de ação |
| Demais comportamentos | Idêntico | Idêntico |

> Sem diferença funcional entre as plataformas — apenas adaptação de largura/posicionamento.

---

## 10. Acessibilidade
> Consideracoes de acessibilidade para esta tela.

- Textos alternativos nas thumbnails de vídeo e ícones de vídeo dos cards de exercício.
- Cards de exercício acessíveis como elementos clicáveis (foco e ativação por teclado).
- Player de áudio com controles rotulados (play/pausa, tempo).
- Contraste de cores conforme WCAG 2.1 AA.
- Ordem de foco lógica: header → identificação → detalhes → grupos/exercícios → rodapé.

---

## 11. Historico de Alteracoes

| Data | Autor | Descricao |
|---|---|---|
| 2026-06-18 | Maria Isabela | Criacao inicial do documento (entrevista /mapear-tela) |

# Tela: Visualizar Rotina `[VELA-5002]`

---

## Metadados
| Campo | Valor |
|---|---|
| **Nome da tela** | Visualizar Rotina |
| **Modulo** | Rotinas |
| **Codigo** | VELA-5002 |
| **Prioridade** | 🔵 MVP |
| **Status** | 🟢 CONCLUIDO |
| **Ultima atualizacao** | 2026-06-18 |

---

## 1. Objetivo da Tela
> O que o usuario consegue fazer nesta tela? Qual problema ela resolve?

Tela **somente leitura** onde o **Treinador** confere uma rotina da **sua** base reutilizável sem risco de alterar por acidente. Exibe os **dados gerais** (título, objetivo) e a **lista ordenada de treinos** identificados por **letras A, B, C…**, deixando claro e fácil de identificar quais treinos compõem a rotina, sua ordem e o conteúdo mais relevante de cada treino. A partir daqui o Treinador acessa o detalhe de cada treino e dispara as ações de gestão (**Editar**, **Duplicar**, **Excluir**). É o par de leitura do **Cadastro / Edição de Rotina** (`[VELA-5003]`), espelhando o padrão de Treinos (`[VELA-4002]`).

---

## 2. Quem Acessa / Pre-condicoes
> Quem pode ver esta tela? Quais condicoes precisam ser verdadeiras?

- **Usuario:** **Treinador** autenticado. O **Aluno** não acessa esta tela.
- **Pre-condicoes:**
  - Usuário deve estar logado com perfil de Treinador.
  - A rotina visualizada deve existir na base do próprio Treinador.
- **Permissoes especiais:** Nenhuma além da role de Treinador.

---

## 3. Layout e Componentes Visuais
> Descreva a estrutura visual da tela de cima para baixo.

### 3.1 Header / Cabecalho
- Conteudo: Botão voltar (←) + Título com o **título da rotina** + menu **"⋮"** (kebab) à direita com as ações **Duplicar**, **Ativar/Desativar** e **Excluir**.
- Comportamento: Fixo no topo. O botão voltar (←) retorna à Lista de Rotinas.

### 3.2 Corpo Principal
> Tela única em **rolagem vertical**, em modo leitura. Os blocos abaixo são subtítulos discretos que organizam o conteúdo — espelham a estrutura do Cadastro de Rotina (`[VELA-5003]`).

**Bloco A — Identificação**
- Componente: Bloco de texto (somente leitura).
- Conteudo: **Título da rotina**, **Objetivo** e um selo de **status** (Ativa / Inativa).

**Bloco B — Treinos da rotina**
- Componente: Lista **ordenada de cards de treino** (A, B, C…), em leitura.
- Conteudo de cada card de treino:
  - **Letra** (A, B, C…) + **nome do treino** + **categoria**.
  - **Dia da semana** e **Descrição curta** (quando preenchidos para esta rotina).
  - Conteúdo mais relevante do treino, de forma compacta: **quantidade de exercícios** e **grupos musculares** principais.
- Comportamento:
  - Os cards de treino são **clicáveis**: ao tocar no card, abre **Visualizar Treino** (`[VELA-4002]`) daquele treino (conteúdo completo: grupos, exercícios e prescrição).
  - Sem botões de adicionar/remover/reordenar (modo leitura). A edição da estrutura acontece no Cadastro (`[VELA-5003]`).

### 3.3 Footer / Rodape
- Conteudo: Botão primário **"Editar"** ocupando a largura do rodapé.
- Comportamento: Fixo na parte inferior. Abre o Cadastro / Edição de Rotina (`[VELA-5003]`) com a rotina pré-preenchida.

---

## 4. Campos e Formularios

N/A — Tela sem formularios. Todo o conteúdo é exibido em **modo leitura**.

---

## 5. Botoes e Acoes

| # | Componente | Label / Icone | Posicao | Estado Inicial | Acao ao Clicar |
|---|---|---|---|---|---|
| 1 | Botao primario | "Editar" | Rodapé (largura total) | Ativo | Abre Cadastro / Edição de Rotina (`[VELA-5003]`) com a rotina pré-preenchida |
| 2 | Botao voltar | ← | Header (esquerda) | Ativo | Retorna à Lista de Rotinas (`[VELA-5001]`) |
| 3 | Menu kebab | ⋮ | Header (direita) | Ativo | Abre menu com "Duplicar", "Ativar/Desativar" e "Excluir" |
| 4 | Item de menu | "Duplicar" | Dentro do menu ⋮ | Ativo | Cria cópia "Título (cópia)" na base do Treinador e abre direto no Cadastro / Edição (`[VELA-5003]`) para ajustar |
| 5 | Item de menu | "Ativar" / "Desativar" | Dentro do menu ⋮ | Reflete o status atual | Ao **desativar**, abre modal "Desativar rotina?" (mesma copy do Cadastro); ao **ativar**, alterna direto. Atualiza o selo de status in-place |
| 6 | Item de menu | "Excluir" | Dentro do menu ⋮ | Ativo | Abre modal de confirmação → ao confirmar, exclui e volta à Lista de Rotinas |
| 7 | Card de treino | (card do treino) | Bloco B | Ativo | Abre Visualizar Treino (`[VELA-4002]`) daquele treino |

---

## 6. Estados da Tela

### 6.1 Estado Inicial / Vazio
- Não há estado vazio: uma rotina sempre tem **≥1 treino** (regra do Cadastro). A tela só é acessada para uma rotina existente.

### 6.2 Estado de Carregamento (Loading)
- **Skeleton loader** nas áreas de conteúdo (identificação e cards de treino) enquanto a rotina carrega.

### 6.3 Estado de Erro
- **Erro de carregamento:** mensagem central "Não foi possível carregar a rotina." + botão **"Tentar novamente"**.
- **Erro de rede:** toast "Sem conexão. Tente novamente."

### 6.4 Estado de Sucesso
- **Após excluir:** toast "Rotina excluída." + redireciona para a Lista de Rotinas.
- **Após duplicar:** abre o Cadastro / Edição da cópia (o feedback de criação ocorre lá).
- **Após ativar/desativar:** o **selo de status** (Ativa / Inativa) atualiza in-place, sem sair da tela.

### 6.5 Estado Desabilitado / Bloqueado *(se aplicavel)*
- N/A. *(A trava de exclusão por vínculo passa a valer quando o atrelamento de rotina a aluno existir — fluxo futuro.)*

---

## 7. Fluxo de Navegacao

### De onde o usuario chega nesta tela
| Origem | Gatilho |
|---|---|
| Lista de Rotinas (`[VELA-5001]`) | Toca em um card de rotina |

### Para onde o usuario pode ir desta tela
| Destino | Gatilho |
|---|---|
| Cadastro / Edição de Rotina (`[VELA-5003]`) | Toca em "Editar" (rodapé) ou em "Duplicar" (menu ⋮) |
| Visualizar Treino (`[VELA-4002]`) | Toca em um card de treino |
| Lista de Rotinas (`[VELA-5001]`) | Toca em ← (voltar) ou após excluir a rotina |

---

## 8. Regras de Negocio
> Regras especificas que impactam o comportamento desta tela.

- **RN01:** Tela exclusiva do **Treinador**; só exibe rotinas da **sua própria base**.
- **RN02:** Tela em **modo leitura** — nenhuma alteração de conteúdo acontece aqui; toda edição ocorre no Cadastro (`[VELA-5003]`).
- **RN03:** A ordem dos treinos é apresentada pelas **letras A, B, C…** (definidas no Cadastro pela posição).
- **RN04:** Cada card de treino é **clicável** e abre **Visualizar Treino** (`[VELA-4002]`) para o conteúdo completo (grupos, exercícios e prescrição) — o atalho de conferência do treino vive aqui.
- **RN05:** **Exclusão** é **definitiva** (app sem lixeira) e sempre passa por **modal de confirmação** ("Excluir rotina? Esta ação não pode ser desfeita."). *(A trava de exclusão por vínculo passa a valer quando o atrelamento de rotina a aluno existir — fluxo futuro.)*
- **RN06:** **Duplicar** cria uma cópia na base do Treinador com título "Título (cópia)" e abre o Cadastro / Edição da cópia para ajustes.
- **RN07:** O selo **Ativa / Inativa** reflete o status da rotina. O status pode ser alterado **aqui** (menu ⋮ → "Ativar/Desativar") ou no Cadastro/Edição (`[VELA-5003]`); ao desativar, exibe o modal de confirmação. Espelha o ciclo de vida de Treinos.

> **Escopo futuro — entrada "Atribuir a aluno":** esta é a tela reservada para a ação **"Atribuir a aluno"** quando o atrelamento de rotina a aluno for mapeado (rastreado na decisão #38) — **não** vai no Cadastro/Edição `[VELA-5003]`. No fluxo futuro, definir aqui: o botão/ação, a seleção do aluno, data de início/agenda, ativação e notificação. _Fora do escopo atual desta tela (leitura da base de rotinas) — não bloqueia a conclusão._

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

- Cards de treino acessíveis como elementos clicáveis (foco e ativação por teclado), com nome acessível (letra + nome + categoria).
- Ordem de foco lógica: header → identificação → treinos (A, B, C…) → rodapé.
- Contraste de cores conforme WCAG 2.1 AA.
- Menu "⋮" operável por teclado, com rótulos claros nas ações.

---

## 11. Historico de Alteracoes

| Data | Autor | Descricao |
|---|---|---|
| 2026-06-18 | Maria Isabela | Criação inicial do documento (entrevista `/mapear-tela`). Tela somente leitura, par de `[VELA-5003]`, espelhando `[VELA-4002]`. Exibe título + objetivo + lista ordenada de treinos (A/B/C) com dia/descrição e resumo (qtd de exercícios + grupos musculares). Card de treino abre Visualizar Treino `[VELA-4002]`. Gestão: Editar, Duplicar, Excluir. Status → EM ANDAMENTO |
| 2026-06-18 | Maria Isabela | Revisão (`/revisar-tela`): menu ⋮ ganhou **Ativar/Desativar** (paridade com a Lista `[VELA-5001]`; desativar com modal; selo atualiza in-place — Seções 3.1, 5, 6.4, RN07); o `⚠️ PENDENTE` "Atribuir a aluno" convertido em **nota de escopo futuro** (rastreado na decisão #38, não bloqueia conclusão). Status → CONCLUIDO |

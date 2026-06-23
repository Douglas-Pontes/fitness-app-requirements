# Tela: Minhas Rotinas `[VELA-6001]`

---

## Metadados
| Campo | Valor |
|---|---|
| **Nome da tela** | Minhas Rotinas |
| **Modulo** | Rotinas (fluxo do Aluno) |
| **Codigo** | VELA-6001 |
| **Prioridade** | 🔵 MVP |
| **Status** | 🟢 CONCLUIDO |
| **Ultima atualizacao** | 2026-06-22 |

---

## 1. Objetivo da Tela
> O que o usuario consegue fazer nesta tela? Qual problema ela resolve?

Tela **somente leitura** na **visão do Aluno**: lista as **rotinas atribuídas a ele**, separando a(s) **ativa(s)** das **agendadas** e das **anteriores (encerradas)**. Serve para o aluno **acompanhar o plano vigente** e **consultar o histórico** do que já executou. É o ponto de partida do fluxo do Aluno consumir rotinas: ao tocar num card, abre o **Detalhe da Rotina (Aluno)** (`[VELA-6002]`, a mapear). Não confundir com a **Lista de Rotinas `[VELA-5001]`**, que é a base reutilizável na **visão do Treinador**.

---

## 2. Quem Acessa / Pre-condicoes
> Quem pode ver esta tela? Quais condicoes precisam ser verdadeiras?

- **Usuario:** **Aluno** autenticado. O **Treinador** não acessa esta tela (ele gerencia a base em `[VELA-5001/5002/5003]` e atribui em `[VELA-3004]`).
- **Pre-condicoes:**
  - Usuário logado com perfil de Aluno.
  - A tela exibe **apenas as rotinas atribuídas ao próprio aluno** (cópias/snapshots geradas em `[VELA-3004]`).
- **Permissoes especiais:** Nenhuma. Tela em modo leitura — o aluno não cria, edita nem exclui rotinas.

---

## 3. Layout e Componentes Visuais
> Descreva a estrutura visual da tela de cima para baixo.

### 3.1 Header / Cabecalho
- Conteudo: Título "Minhas rotinas".
- Comportamento: Fixo no topo. Sem busca/filtros no MVP (volume de rotinas por aluno é baixo).

### 3.2 Corpo Principal
> Tela única em **rolagem vertical**, organizada em até três seções. **Cada seção só aparece se tiver ao menos um card.**

**Seção A — Ativas**
- Componente: Lista de **cards de rotina**.
- Conteudo: rotinas cuja vigência inclui a data atual (ver RN01). **Pode haver mais de uma** ativa ao mesmo tempo (ex.: `.track` + `.performance`, conforme RN07 do `[VELA-3004]`) — não há "card único" de destaque; todas as ativas aparecem nesta seção, no topo da tela.
- Ordenação: por **data de início decrescente** (a atribuição mais recente primeiro).

**Seção B — Agendadas**
- Componente: Lista de **cards de rotina**.
- Conteudo: rotinas cujo **início é no futuro** (ainda não entraram em vigor).
- Ordenação: por **data de início crescente** (a que começa primeiro no topo).

**Seção C — Anteriores**
- Componente: Lista de **cards de rotina** (visual atenuado).
- Conteudo: rotinas **encerradas** (data de fim no passado).
- Ordenação: por **data de fim decrescente** (a mais recente primeiro).

**Card de rotina (comum às três seções)**
- **Título da rotina** + **Objetivo** (objetivo definido para este aluno na atribuição) — em destaque.
- **Selo de status:** Ativa / Agendada / Encerrada.
- **Faixa de datas** (início e fim; quando sem fim, exibe só o início — ver RN03).
- **Visibilidade controlada pelo Treinador:** a faixa de datas e o tempo decorrido **só aparecem se o Treinador permitir** na atribuição. Quando oculto, o card mostra apenas **título + objetivo + selo de status** (+ contador de treinos, ver RN05).
- **Contador de execução:** **treinos realizados** acumulados naquela rotina (ex.: "8 treinos realizados"), com base no registro de execução do Aluno (ver RN06). **Sem** barra de progresso e **sem** contagem de exercícios no card — o card é enxuto; progresso e detalhamento por exercício ficam no Detalhe `[VELA-6002]`. Rotinas **agendadas** (sem execução ainda) não exibem contador.
- Comportamento: **toque no card** → abre **Detalhe da Rotina (Aluno)** (`[VELA-6002]`).

### 3.3 Footer / Rodape
- Conteudo: Barra de navegação inferior (Tab Bar do app). Sem FAB de criar — o aluno não cria rotinas.
- Comportamento: Fixo na parte inferior.

---

## 4. Campos e Formularios

N/A — Tela sem formularios. Todo o conteúdo é exibido em **modo leitura**.

---

## 5. Botoes e Acoes

| # | Componente | Label / Icone | Posicao | Estado Inicial | Acao ao Clicar |
|---|---|---|---|---|---|
| 1 | Card de rotina | (rotina) | Seções Ativas / Agendadas / Anteriores | Ativo | Abre **Detalhe da Rotina (Aluno)** (`[VELA-6002]`) daquela rotina |
| 2 | Botão "Tentar novamente" | "Tentar novamente" | Estado de erro | Visível só no erro | Recarrega a lista de rotinas do aluno |

---

## 6. Estados da Tela

### 6.1 Estado Inicial / Vazio
- Aluno **sem nenhuma rotina atribuída**: ilustração + mensagem **"Você ainda não tem rotinas"** + texto de apoio **"Quando seu treinador atribuir uma rotina, ela aparece aqui."**. **Sem** CTA de criar (o aluno não cria rotinas).
- Seções vazias **não** são exibidas (ex.: sem agendadas, a seção "Agendadas" some).

### 6.2 Estado de Carregamento (Loading)
- **Skeleton loader** dos cards enquanto a lista carrega.

### 6.3 Estado de Erro
- **Erro de rede / API:** estado de erro com mensagem **"Não foi possível carregar suas rotinas"** + botão **"Tentar novamente"**.

### 6.4 Estado de Sucesso
- Seções renderizadas com os cards (Ativas, Agendadas, Anteriores — conforme houver).

### 6.5 Estado Desabilitado / Bloqueado *(se aplicavel)*
- N/A.

---

## 7. Fluxo de Navegacao

### De onde o usuario chega nesta tela
| Origem | Gatilho |
|---|---|
| Dashboard / menu do Aluno | Acessa "Minhas rotinas" _(item de navegação depende do dashboard/menu do Aluno, ainda não mapeado — ver RN08 / decisão #39)_ |
| Detalhe da Rotina (Aluno) `[VELA-6002]` | Botão voltar (←) |

### Para onde o usuario pode ir desta tela
| Destino | Gatilho |
|---|---|
| Detalhe da Rotina (Aluno) `[VELA-6002]` | Toque em um card de rotina |

---

## 8. Regras de Negocio
> Regras especificas que impactam o comportamento desta tela.

- **RN01 — Status calculado automaticamente:** o status **não é campo manual**; é derivado das datas da rotina + data atual:
  - **Ativa:** data atual **dentro** da vigência (início ≤ hoje ≤ fim; ou início ≤ hoje quando não há fim).
  - **Agendada:** **início no futuro** (início > hoje).
  - **Encerrada:** **fim no passado** (fim < hoje).
- **RN02 — Múltiplas ativas:** o aluno **pode ter mais de uma rotina ativa** ao mesmo tempo (RN07 do `[VELA-3004]`). Todas aparecem na seção "Ativas" — **não** há destaque de card único.
- **RN03 — Sem data de fim:** data de fim é **opcional**. Sem fim, a rotina é **Ativa** enquanto não for trocada/encerrada e exibe **"Ativa · sem prazo"** + o **tempo decorrido** desde o início (ex.: "em andamento há 6 semanas), **sem barra de progresso** (não há 100% a atingir). A faixa de datas mostra apenas o início.
- **RN04 — Vigência no card (sem barra de progresso):** o card **não** exibe barra/percentual de progresso — a vigência é comunicada apenas pela **faixa de datas** (e, para rotinas sem fim, pelo tempo decorrido, RN03). A **barra de progresso** da vigência fica no **Detalhe `[VELA-6002]`**, não na lista. Agendada exibe "começa em dd/mm".
- **RN05 — Visibilidade do prazo (decisão do Treinador):** a exibição de **faixa de datas + tempo decorrido** ao aluno é **controlada pelo Treinador** na atribuição (`[VELA-3004]`). Quando **desligado**, o card mostra apenas **título + objetivo + selo de status** (+ contador de treinos, que é dado de execução e não de prazo). **Padrão: visível** (o Treinador pode ocultar caso a caso). _(Cria um campo novo em `[VELA-3004]` — decisão #40.)_
- **RN06 — Contador de execução:** cada card exibe **treinos realizados** acumulados naquela rotina, com base no **registro de execução (sessão)** do Aluno definido no `[VELA-6003]` (decisão #49). **No card não há contagem de exercícios** (fica no Detalhe `[VELA-6002]`). Rotinas **agendadas** não exibem contador (sem execução ainda); **encerradas** exibem o total final. O contador **independe** do toggle de visibilidade (RN05), pois não é dado de prazo.
- **RN07 — Somente leitura:** o aluno apenas **consulta**; não cria, edita nem exclui rotinas. A gestão é do Treinador (`[VELA-5001/5002/5003]` + atribuição `[VELA-3004]`).
- **RN08 — Ponto de entrada:** o item de navegação (de onde o Aluno acessa esta tela) depende do **dashboard/menu do Aluno**, ainda não mapeado — dependência rastreada na **decisão #39**. Não bloqueia o escopo desta tela.

---

## 9. Responsividade (Mobile vs Web)
> Diferencas de comportamento ou layout entre plataformas.

| Aspecto | Mobile | Web |
|---|---|---|
| Layout das seções | 1 coluna, rolagem vertical | Mesma estrutura em container centralizado; cards podem usar grade multi-coluna por seção |
| Conteúdo dos cards | Idêntico | Idêntico |
| Navegação | Tab Bar inferior | Menu lateral / superior |

> Mesma lógica e mesmas regras em ambas as plataformas; apenas o layout se adapta.

---

## 10. Acessibilidade
> Consideracoes de acessibilidade para esta tela.

- Cada card é um alvo de toque com nome acessível (título da rotina + status).
- Títulos de seção (Ativas / Agendadas / Anteriores) como cabeçalhos para navegação por leitor de tela.
- Contador de treinos com texto claro no card (ex.: "8 treinos realizados").
- Contraste conforme WCAG 2.1 AA — atenção especial aos cards "Anteriores" atenuados (manter contraste mínimo do texto).
- Ordem de foco lógica: header → Ativas → Agendadas → Anteriores → Tab Bar.

---

## 11. Historico de Alteracoes

| Data | Autor | Descricao |
|---|---|---|
| 2026-06-22 | Maria Isabela | **Card enxuto (ajuste a pedido):** removidas a **barra de progresso** (RN04 — progresso passa a viver só no Detalhe `[VELA-6002]`) e a **contagem de exercícios** do card; o card mantém **título + objetivo + status + faixa de datas + "X treinos realizados"** (RN06). RN05 ajustada (visibilidade governa datas + tempo). Mockup atualizado. |
| 2026-06-22 | Maria Isabela | **Contadores de execução reincorporados ao MVP** (RN06 + card), agora que o `[VELA-6003]` definiu o registro de sessão (decisão #49, destrava #41). Agendadas sem contadores; independem do toggle de visibilidade (RN05). |
| 2026-06-22 | Maria Isabela | **Conclusão.** Reorganização em subpastas por público (arquivo agora em `rotinas/aluno/`; decisão #42). Mockup mobile gerado (`mockups/rotinas/aluno/minhas-rotinas.html`) — sem nota interna na tela. **Tag de categoria do treino** decidida **fora** do card da lista, indo por treino no Detalhe `[VELA-6002]` (decisão #43). Pendências em aberto (#39 ponto de entrada, #40 toggle no `[VELA-3004]`, #41 contadores) são dependências externas rastreadas e não bloqueiam. Status → CONCLUIDO |
| 2026-06-22 | Maria Isabela | Criação inicial do documento (entrevista `/mapear-tela`). **Minhas Rotinas** `[VELA-6001]` (🔵 MVP), **visão do Aluno** — distinta da Lista de Rotinas do Treinador `[VELA-5001]` (nome próprio para evitar colisão). Nova **série do Aluno (6xxx)**; detalhe = **Detalhe da Rotina (Aluno) `[VELA-6002]`** (a mapear). Seções **Ativas · Agendadas · Anteriores** (cada uma some se vazia); status **calculado** das datas (RN01); **múltiplas ativas** possíveis (RN02). **Sem prazo** → "Ativa · sem prazo" + tempo decorrido, sem barra (RN03). **Visibilidade de prazo/progresso controlada pelo Treinador** na atribuição, padrão visível (RN05 → novo campo no `[VELA-3004]`, decisão #40). **Contadores fora do MVP** (RN06). Estado vazio orientativo, sem CTA de criar. Ponto de entrada = dependência do dashboard/menu do Aluno (RN08 / decisão #39). Status → EM ANDAMENTO |

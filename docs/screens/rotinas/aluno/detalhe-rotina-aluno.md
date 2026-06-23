# Tela: Detalhe da Rotina (Aluno) `[VELA-6002]`

> **De-para de numeração:** o ticket do cliente referencia esta tela como `VELA-3002` (Visualizar Rotina — membro). No esquema interno deste projeto ela é **`VELA-6002`** (série 6xxx = visão do Aluno). Mesma equivalência: ticket `VELA-3001` = **`VELA-6001`** (Minhas Rotinas); ticket `VELA-5002` (visualizar treino — membro) = tela de treino do **Aluno** (`treinos/aluno/`, ainda sem código — dependência).

---

## Metadados
| Campo | Valor |
|---|---|
| **Nome da tela** | Detalhe da Rotina (Aluno) |
| **Modulo** | Rotinas (fluxo do Aluno) |
| **Codigo** | VELA-6002 |
| **Prioridade** | 🔵 MVP |
| **Status** | 🟢 CONCLUIDO |
| **Ultima atualizacao** | 2026-06-22 |

---

## 1. Objetivo da Tela
> O que o usuario consegue fazer nesta tela? Qual problema ela resolve?

Tela **somente leitura** na **visão do Aluno** que exibe o **detalhe de uma rotina atribuída a ele**: seu **progresso de vigência**, indicadores (KPIs) no topo e a **lista ordenada de treinos** (A, B, C…) que a compõem. A partir daqui o aluno **abre cada treino** para consulta/execução na tela de treino do Aluno. É o destino de toque dos cards da **Minhas Rotinas** (`[VELA-6001]`) e o par de leitura do Aluno — distinto da **Visualizar Rotina** do Treinador (`[VELA-5002]`), que lê a base reutilizável.

---

## 2. Quem Acessa / Pre-condicoes
> Quem pode ver esta tela? Quais condicoes precisam ser verdadeiras?

- **Usuario:** **Aluno** autenticado. O **Treinador** não acessa esta tela (ele usa a Visualizar Rotina `[VELA-5002]` da própria base).
- **Pre-condicoes:**
  - Usuário logado com perfil de Aluno.
  - A rotina aberta deve estar **atribuída ao próprio aluno** (cópia/snapshot gerada no atrelamento `[VELA-3004]`).
- **Permissoes especiais:** Nenhuma. Tela em modo leitura — o aluno não cria, edita nem exclui rotinas.

---

## 3. Layout e Componentes Visuais
> Descreva a estrutura visual da tela de cima para baixo.

### 3.1 Header / Cabecalho
- Conteudo: Botão voltar (←) + **título da rotina** + selo de **status** (Ativa / Agendada / Encerrada).
- Comportamento: Fixo no topo. O botão voltar (←) retorna à **Minhas Rotinas** (`[VELA-6001]`). Sem menu de ações (o aluno não gerencia a rotina).

### 3.2 Corpo Principal
> Tela única em **rolagem vertical**, em modo leitura. Blocos na ordem de cima para baixo.

**Bloco A — Identificação**
- Componente: Bloco de texto (somente leitura).
- Conteudo: **Título da rotina**, **Objetivo** (definido para este aluno na atribuição) e a **faixa de datas** (início e fim; sem fim, exibe só o início + "sem prazo" — ver RN02).
- **Visibilidade controlada pelo Treinador:** a faixa de datas e o progresso só aparecem se o Treinador permitir na atribuição (ver RN05). Quando oculto, este bloco mostra apenas **título + objetivo + selo de status**.

**Bloco B — KPIs / Progresso da rotina**
- Componente: Faixa de indicadores no topo (acima da lista de treinos) + barra de progresso de vigência.
- Conteudo (MVP):
  - **Dias percorridos** da rotina (desde o início até hoje).
  - **Dias restantes** até o fim da rotina (só quando há data de fim — ver RN02).
  - **Progresso de vigência:** barra + percentual do período já decorrido (mesma fórmula da `[VELA-6001]` RN04).
- **KPIs de execução (fora do MVP desta tela):** **Treinos executados** e **Exercícios executados** dependem do registro de execução do Aluno, ainda não mapeado. Ficam **previstos, fora do MVP** (ver RN06 / decisão #41).
- **Visibilidade controlada pelo Treinador:** todo o Bloco B (KPIs de data + barra) respeita o mesmo toggle da atribuição (ver RN05). Quando o Treinador oculta prazo/progresso, o bloco **não é exibido**.

**Bloco C — Último treino executado** *(fora do MVP — bloco previsto)*
- Componente: Card-resumo (somente leitura).
- Conteudo previsto: **nome do treino**, **tempo de realização**, **quantidade de exercícios**, **data de execução** — para o aluno se localizar no plano.
- **Status:** depende do registro de execução do Aluno (mesma dependência do Bloco B de execução). **Não entra no MVP desta tela**; documentado para entrar quando o fluxo de execução existir (ver RN06).

**Bloco D — Treinos da rotina**
- Componente: Lista **ordenada de cards de treino** (A, B, C…), em leitura.
- Conteudo de cada card de treino:
  - **Letra** (A, B, C…) + **nome do treino**.
  - **Tag de categoria** do treino (ex.: "A · Peito · hipertrofia") — ver RN07 / decisão #43.
  - **Contador de exercícios** + **nº de execuções no período** lado a lado (ex.: "6 exercícios · 4 execuções"). O contador de execuções considera apenas as execuções **dentro da vigência da rotina** e **depende do registro de execução do Aluno — fora do MVP** (ver RN09).
  - **Tag "recomendado do dia"** quando o **dia da semana sugerido** pelo treinador para este treino = **dia atual** (ver RN03). É a **única** manifestação visual do dia no card.
  - O **dia da semana sugerido** é **campo interno** do treino (preenchido pelo treinador na rotina) — **não** é exibido cru no card; só se manifesta como a tag "recomendado do dia" no dia correspondente. **Descrição** e **Objetivo** do treino **não** aparecem neste card (mantém o card enxuto); ficam no detalhe do treino.
- Comportamento:
  - Os cards são **clicáveis**: ao tocar, abre a **tela de treino do Aluno** (`treinos/aluno/`) daquele treino, para consulta/execução.
  - Sem botões de adicionar/remover/reordenar (modo leitura).

**Bloco E — Considerações da rotina** *(exibido apenas quando a rotina está **Encerrada**)*
- Componente: Card de feedback com campo de texto (textarea) + botão.
- Conteudo:
  - Título de celebração/encerramento (ex.: **"Rotina concluída! Conte como foi."**).
  - Campo de texto **"Suas considerações sobre a rotina"** (opcional, **máx. 500 caracteres**, com contador).
  - Botão **"Enviar considerações"**.
- Comportamento:
  - **Só aparece quando o status é Encerrada** (passou a data de fim — ver RN10). Em rotinas **Ativas/Agendadas** o bloco não é exibido.
  - **Rotinas sem data de fim não encerram** por vigência → o bloco **não** aparece (não há "100%" a atingir).
  - Após enviar, o card passa a exibir o texto enviado em leitura, com opção de editar enquanto a rotina permanecer acessível. O conteúdo é **privado** ao treinador (RN10).

### 3.3 Footer / Rodape
- Conteudo: Barra de navegação inferior (Tab Bar do app). Sem FAB nem botão de ação (o aluno não edita a rotina).
- Comportamento: Fixo na parte inferior.

---

## 4. Campos e Formularios

N/A — Tela sem formularios. Todo o conteúdo é exibido em **modo leitura**.

---

## 5. Botoes e Acoes

| # | Componente | Label / Icone | Posicao | Estado Inicial | Acao ao Clicar |
|---|---|---|---|---|---|
| 1 | Card de treino | (treino) | Bloco D | Ativo | Abre a **tela de treino do Aluno** (`treinos/aluno/`) daquele treino |
| 2 | Botao voltar | ← | Header (esquerda) | Ativo | Retorna à **Minhas Rotinas** (`[VELA-6001]`) |
| 3 | Botão "Tentar novamente" | "Tentar novamente" | Estado de erro | Visível só no erro | Recarrega o detalhe da rotina |
| 4 | Campo de considerações | "Suas considerações sobre a rotina" | Bloco E (só Encerrada) | Ativo (opcional) | Textarea com contador 0/500; texto privado enviado ao treinador (RN10) |
| 5 | Botão "Enviar considerações" | "Enviar considerações" | Bloco E (só Encerrada) | Ativo | Salva/atualiza as considerações da rotina e exibe o texto em leitura |

---

## 6. Estados da Tela

### 6.1 Estado Inicial / Vazio
- Não há estado vazio de rotina: a tela só é acessada para uma rotina existente e atribuída, e toda rotina tem **≥1 treino** (regra do Cadastro `[VELA-5003]`).
- **Sem execução ainda (estado dos blocos de execução):** quando o aluno ainda não executou nada, o **Bloco C (último treino)** mostra um estado vazio orientativo ("Você ainda não registrou treinos desta rotina.") e os KPIs de execução (quando existirem) exibem **zero**. Os **KPIs de data** (dias percorridos/restantes) e a barra de vigência **funcionam normalmente** (não dependem de execução). *(Aplica-se quando os blocos de execução entrarem — ver RN06.)*

### 6.2 Estado de Carregamento (Loading)
- **Skeleton loader** nas áreas de conteúdo (identificação, KPIs e cards de treino) enquanto a rotina carrega.

### 6.3 Estado de Erro
- **Erro de carregamento / API:** mensagem central **"Não foi possível carregar a rotina."** + botão **"Tentar novamente"**.
- **Erro de rede:** toast "Sem conexão. Tente novamente."

### 6.4 Estado de Sucesso
- Tela renderizada: identificação + KPIs/progresso (conforme visibilidade) + lista de treinos (A, B, C…), com o treino do dia destacado quando aplicável.

### 6.5 Estado Desabilitado / Bloqueado *(se aplicavel)*
- **Prazo/progresso oculto pelo Treinador:** quando o toggle de visibilidade da atribuição está desligado, os Blocos A (faixa de datas) e B (KPIs de data + barra) **não aparecem**; a tela mostra título + objetivo + selo de status + lista de treinos (ver RN05).

---

## 7. Fluxo de Navegacao

### De onde o usuario chega nesta tela
| Origem | Gatilho |
|---|---|
| Minhas Rotinas (`[VELA-6001]`) | Toca em um card de rotina |

### Para onde o usuario pode ir desta tela
| Destino | Gatilho |
|---|---|
| Tela de treino do Aluno (`treinos/aluno/`) | Toca em um card de treino |
| Minhas Rotinas (`[VELA-6001]`) | Toca em ← (voltar) |

---

## 8. Regras de Negocio
> Regras especificas que impactam o comportamento desta tela.

- **RN01 — Somente leitura / vínculo:** tela exclusiva do **Aluno**; só exibe rotinas **atribuídas ao próprio aluno** (cópia/snapshot de `[VELA-3004]`). O aluno apenas consulta — não cria, edita nem exclui.
- **RN02 — Sem data de fim:** data de fim é **opcional**. Sem fim, o KPI **"dias restantes" é ocultado**, a rotina exibe **"sem prazo"** e **não há barra de progresso** (não há 100% a atingir); mostra-se o **tempo decorrido** (dias percorridos). Espelha a RN03 da `[VELA-6001]`.
- **RN03 — Recomendado do dia:** o **dia da semana sugerido** é um campo **interno** do treino, preenchido pelo treinador na rotina; ele **não** é exibido cru no card. Sua **única** manifestação visual é a tag **"recomendado do dia"**, que aparece no card quando o dia sugerido = **dia atual**. Se **mais de um** treino tiver o dia atual como sugerido, **todos** recebem a tag (sem ordem de prioridade). Treino **sem** dia sugerido nunca recebe a tag.
- **RN04 — Progresso de vigência:** com data de fim, o progresso é o **percentual do período decorrido** = (hoje − início) / (fim − início), como barra + percentual. Agendada = 0%; Encerrada = 100%. Mesma fórmula da `[VELA-6001]` RN04.
- **RN05 — Visibilidade de prazo/progresso (decisão do Treinador):** a exibição de **faixa de datas + KPIs de data (dias percorridos/restantes) + barra de progresso** é **controlada pelo Treinador** na atribuição (`[VELA-3004]`, decisão #40; padrão **visível**). Quando desligado, a tela mostra apenas **título + objetivo + selo de status + lista de treinos**. Coerente com a RN05 da `[VELA-6001]`.
- **RN06 — Conteúdo de execução fora do MVP:** os KPIs **Treinos executados / Exercícios executados** e o **Bloco C (último treino executado)** dependem do **registro de execução do Aluno** (fluxo Treino em Andamento / Histórico), ainda não mapeado. Ficam **previstos, fora do MVP** desta tela e entram quando a fonte de dados existir (decisão #41). No MVP, o topo exibe apenas os **KPIs de data** e a **barra de vigência**.
- **RN07 — Tag de categoria por treino:** cada card de treino exibe a **categoria** do treino (1 treino = 1 categoria), espelhando o card da Visualizar do Treinador `[VELA-5002]` (decisão #43). **Grupos musculares não** entram no card (mantém enxuto).
- **RN08 — Destino do treino:** o toque no card abre a **tela de treino do Aluno** (`treinos/aluno/`), responsável pela consulta/execução do treino. Essa tela ainda **não foi mapeada/codificada** — dependência rastreada (ticket cliente `VELA-5002`).
- **RN10 — Considerações ao encerrar a rotina (feedback de fim de ciclo):** quando a rotina atinge o status **Encerrada** (passou a data de fim — RN04), exibe-se o **Bloco E** com um campo opcional **"Suas considerações sobre a rotina"** (textarea, **máx. 500 caracteres**, contador) e o botão **"Enviar considerações"**. É o equivalente, no fim do **ciclo da rotina**, ao **recado por treino** da execução (`[VELA-6003]` RN11). O texto é **privado** — destinado ao **treinador** (lido na visão dele sobre o aluno, dependência futura, junto dos KPIs de execução). **Gatilho = vigência encerrada**; rotinas **sem data de fim** não disparam (não há 100% por data). Enviar é **opcional** e pode ser editado enquanto a rotina permanecer acessível (decisão #51).
- **RN09 — Nº de execuções por treino (fora do MVP):** cada card exibe, ao lado do contador de exercícios, o **número de vezes que o aluno executou aquele treino dentro da vigência da rotina**. Esse contador depende do **registro de execução do Aluno** (Treino em Andamento / Histórico), ainda não mapeado — **fora do MVP** desta tela, entra quando a fonte existir (mesma dependência da RN06, decisão #45). Sem execução registrada, exibe **0 execuções**.

---

## 9. Responsividade (Mobile vs Web)
> Diferencas de comportamento ou layout entre plataformas.

| Aspecto | Mobile | Web |
|---|---|---|
| Layout | Coluna única, rolagem vertical | Mesma estrutura em container centralizado; cards de treino podem usar grade multi-coluna |
| KPIs / progresso | Faixa de indicadores no topo | Idêntico, podendo distribuir os KPIs lado a lado em linha |
| Navegação | Tab Bar inferior | Menu lateral / superior |
| Demais comportamentos | Idêntico | Idêntico |

> Mesma lógica e mesmas regras em ambas as plataformas; apenas o layout se adapta.

---

## 10. Acessibilidade
> Consideracoes de acessibilidade para esta tela.

- Cards de treino acessíveis como elementos clicáveis (foco e ativação por teclado), com nome acessível (letra + nome + categoria).
- Selo "recomendado do dia" com texto associado (não depender só de cor).
- Barra de progresso com valor textual associado (ex.: "60% do período decorrido").
- Títulos de blocos (KPIs, treinos) como cabeçalhos para navegação por leitor de tela.
- Ordem de foco lógica: header → identificação → KPIs/progresso → (último treino, quando existir) → treinos (A, B, C…) → Tab Bar.
- Contraste de cores conforme WCAG 2.1 AA.

---

## 11. Historico de Alteracoes

| Data | Autor | Descricao |
|---|---|---|
| 2026-06-22 | Maria Isabela | **Considerações ao encerrar a rotina (Bloco E / RN10):** quando a rotina fica **Encerrada** (vigência terminou), exibe campo opcional "Suas considerações sobre a rotina" (máx. **500 caracteres**) + "Enviar considerações" — feedback **privado** ao treinador, equivalente de fim de ciclo ao recado por treino da `[VELA-6003]` (decisão #51). Gatilho = vigência encerrada; rotinas sem data de fim não disparam. Mockup atualizado com frame do estado **Encerrada**. |
| 2026-06-22 | Maria Isabela | **Conclusão.** Tela e mockup (`mockups/rotinas/aluno/detalhe-rotina-aluno.html`, mobile) finalizados. Pendências em aberto são **dependências externas** rastreadas e não bloqueiam: destino do treino = tela de treino do Aluno (#44) e conteúdo de execução — KPIs executados, "último treino", nº de execuções por treino (#45/RN06/RN09). Status → CONCLUIDO |
| 2026-06-22 | Maria Isabela | **Ajuste do card de treino (Bloco D):** removidos do card a **descrição** e o **objetivo** (mantém enxuto) e o **dia da semana cru**. O **dia sugerido** vira **campo interno** (preenchido pelo treinador) cuja **única** manifestação visual é a tag **"recomendado do dia"** no dia correspondente (RN03 reescrita). Novo campo no card: **nº de execuções no período**, ao lado do contador de exercícios — **fora do MVP** por depender do registro de execução (RN09, decisão #45). Mockup atualizado. |
| 2026-06-22 | Maria Isabela | Criação inicial do documento (entrevista `/mapear-tela`), a partir do ticket do cliente `VELA-3002`. **Detalhe da Rotina (Aluno)** `[VELA-6002]` (🔵 MVP), destino de toque da Minhas Rotinas `[VELA-6001]`. Decisões da entrevista: (a) conteúdo de **execução** (KPIs executados + "último treino") **deferido / fora do MVP** — só KPIs de **data** agora (RN06, decisão #41); (b) KPIs de data e progresso **respeitam o toggle de visibilidade** do Treinador (RN05, decisão #40); (c) card de treino com **tag de categoria** apenas (RN07, decisão #43); (d) "recomendado do dia" **destaca todos** os treinos do dia (RN03); (e) sem data de fim → oculta "dias restantes" + "sem prazo" sem barra (RN02). De-para de numeração com o ticket registrado no topo. Destino do treino = tela de treino do Aluno (`treinos/aluno/`, ainda a mapear — RN08). Status → EM ANDAMENTO |

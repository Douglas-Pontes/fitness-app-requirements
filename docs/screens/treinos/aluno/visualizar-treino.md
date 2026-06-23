# Tela: Visualizar / Executar Treino (Aluno) `[VELA-6003]`

> **De-para de numeração:** o ticket do cliente referencia esta tela como `VELA-5002` (Visualizar / Executar Treino — membro). No esquema interno deste projeto ela é **`VELA-6003`** (série 6xxx = visão do Aluno), par de **execução** da Visualizar Treino do Treinador (`[VELA-4002]`) e destino de toque do Detalhe da Rotina (Aluno) (`[VELA-6002]`, RN08). Esta tela **consolida** o fluxo de treinar do Aluno antes previsto em telas separadas (Iniciar Treino / Treino em Andamento / Finalizar Treino) numa **única tela com estados** (consulta → em execução → resumo).

---

## Metadados
| Campo | Valor |
|---|---|
| **Nome da tela** | Visualizar / Executar Treino (Aluno) |
| **Modulo** | Treinos (fluxo do Aluno) |
| **Codigo** | VELA-6003 |
| **Prioridade** | 🔵 MVP |
| **Status** | 🟡 EM ANDAMENTO |
| **Ultima atualizacao** | 2026-06-22 |

---

## 1. Objetivo da Tela
> O que o usuario consegue fazer nesta tela? Qual problema ela resolve?

Tela do **Aluno** onde ele **consulta e executa** um treino atribuído a ele (dentro de uma rotina). Permite **assistir aos vídeos** e ver os **detalhes de cada exercício** (séries, repetições, descanso, descrição de execução) e **executar o treino**: iniciar a sessão, marcar séries/exercícios concluídos com **timer de descanso** entre séries, e **finalizar** — o que **gera o registro de execução** (data, duração, exercícios e séries realizados). É a **fonte do registro de execução** que alimenta os KPIs e o bloco "último treino executado" do Detalhe da Rotina (`[VELA-6002]`) e da Minhas Rotinas (`[VELA-6001]`). Ao final, exibe um **resumo compartilhável** (estilo story) para o aluno postar nas redes.

---

## 2. Quem Acessa / Pre-condicoes
> Quem pode ver esta tela? Quais condicoes precisam ser verdadeiras?

- **Usuario:** **Aluno** autenticado. O **Treinador** não executa treinos — ele usa a Visualizar Treino da própria base (`[VELA-4002]`, modo leitura/gestão).
- **Pre-condicoes:**
  - Usuário logado com perfil de Aluno.
  - O treino aberto pertence a uma **rotina atribuída ao próprio aluno** (cópia/snapshot de `[VELA-3004]`).
- **Permissoes especiais:** Nenhuma. O aluno **não** edita o conteúdo do treino (séries/reps prescritas vêm do treinador); ele apenas **registra a execução**.

---

## 3. Layout e Componentes Visuais
> Descreva a estrutura visual da tela de cima para baixo.
> **Copy de UI vs. nota interna:** só descreva como texto na tela as informações necessárias ao usuário (instruções, contadores, timer, validações). Racional de comportamento e referências a RNs são notas internas — ficam neste documento, nunca na tela nem nos mockups.

> **Formato de apresentação (decisão de UX):** **lista vertical estilo MFit** (rolagem vertical com cards por grupo). Reaproveita a estrutura de **grupos numerados** (1, 2, 3…) do treino do Treinador (`[VELA-4002]`). O feed vertical / reels (ideia ZeroUm) foi descartado para o MVP (ver decisão #47).

### 3.1 Header / Cabecalho
- Conteudo: Botão voltar (←) + **nome do treino** + selo de **categoria** (ex.: "Peito · hipertrofia").
- Comportamento: Fixo no topo.
  - **Antes de iniciar:** o botão voltar (←) retorna ao Detalhe da Rotina (`[VELA-6002]`) sem confirmação.
  - **Em execução:** o botão voltar (←) **não descarta** a sessão — sai mantendo o treino salvo como "em andamento" (ver RN03/persistência). Quando há sessão ativa, o header também exibe o **cronômetro do treino** correndo.

### 3.2 Corpo Principal
> Tela única em **rolagem vertical**. O conteúdo é o mesmo nos estados "consulta" e "em execução"; o que muda são os controles de execução que aparecem em cada card quando a sessão está ativa.

**Bloco A — Identificação**
- Componente: Bloco de texto (somente leitura).
- Conteudo: **Nome do treino**, **categoria** e, quando preenchidos, **descrição**, **observações** e **áudio do treino** (player com duração — o áudio é a instrução do treinador sobre o treino, decisão #22).
- Comportamento: Campos vazios não aparecem (sem rótulos em branco).

**Bloco B — Exercícios (em grupos)**
- Componente: Lista de **grupos numerados** (1, 2, 3…); cada grupo contém um ou mais **cards de exercício**, conforme o tipo do grupo (Normal, Bi-set, Tri-set, Superset, Drop-set).
- Conteudo de cada card de exercício:
  - **Capa/thumbnail do vídeo** + **nome do exercício** + ícone de vídeo (se houver).
  - Prescrição em leitura: **Séries**, **Repetições**, **Carga sugerida**, **Descanso** e **Descrição de execução** (quando houver). Campos vazios herdados do treino são tratados conforme RN08.
  - **Controles de execução** (visíveis quando a sessão está ativa):
    - **Contador de séries** (ex.: "3 / 4") com botão para **concluir a série** atual.
    - Ao concluir uma série (ou rodada do grupo combinado — RN05), abre o **timer de descanso**.
    - Campos para registrar **reps realizadas** e **carga realizada** por série, **pré-preenchidos** com os valores **sugeridos pelo treinador** (reps prescritas + carga sugerida); o aluno só ajusta se usar valor diferente (RN06).
    - Indicação visual de **exercício concluído** quando todas as séries forem marcadas (ou pelo botão "marcar concluído" nos exercícios sem séries — RN08).
- Comportamento:
  - Tocar no **vídeo/thumbnail** abre o player do exercício (modal/lightbox por cima da lista — mesmo padrão da decisão #20).
  - Tocar no card (fora dos controles) pode expandir os detalhes/execução completa do exercício.
  - Sem botões de adicionar/remover/reordenar — o aluno não altera a estrutura do treino.

**Componente — Timer de descanso entre séries**
- Componente: Cronômetro regressivo (overlay/área destacada) disparado ao concluir uma série.
- Conteudo: tempo regressivo iniciando no **valor do campo "Descanso" prescrito** para aquele exercício; ações **Pular** e **+15s** (ajuste rápido).
- Comportamento: ao zerar, sinaliza (vibração/feedback visual) que pode iniciar a próxima série. O **som de repetição** estilo box de CrossFit fica **fora do MVP** (ver RN09 / decisão #48).

### 3.3 Footer / Rodape
- Conteudo: **Botão de ação primário** dependente do estado da sessão:
  - **Sem sessão ativa:** botão **"Iniciar treino"** (largura total).
  - **Em execução:** botão **"Finalizar treino"** (largura total) + **cronômetro** do treino visível (também no header).
- Comportamento: Fixo na parte inferior. "Iniciar treino" inicia o cronômetro e habilita os controles de execução nos cards. "Finalizar treino" encerra a sessão e abre o **Resumo da execução** (ver 6.4).

---

## 4. Campos e Formularios

> A tela não tem formulário de cadastro; os únicos campos de entrada são os **registros de execução por série**, opcionais.

| # | Nome do Campo | Tipo | Obrigatorio | Placeholder | Validacao | Mensagem de Erro |
|---|---|---|---|---|---|---|
| 1 | Reps realizadas (por série) | Numero inteiro | Não | (reps prescritas) | Inteiro ≥ 0 | "Informe um número válido" |
| 2 | Carga realizada (por série) | Numero decimal | Não | (carga sugerida pelo treinador) | Decimal ≥ 0, vírgula aceita | "Informe uma carga válida" |
| 3 | Recado para o treinador | Texto longo (textarea) | Não | "Como foi o treino? (opcional)" | Máx. 300 caracteres | "Limite de 300 caracteres atingido" |

### Regras de Preenchimento
- Reps e carga **pré-preenchem** com os valores **sugeridos pelo treinador** (reps prescritas + carga sugerida no treino); o aluno só altera se realizou diferente (RN06).
- Campos em branco **não bloqueiam** a conclusão da série nem do treino — o registro aceita execução parcial (ver RN08).
- **Recado para o treinador:** opcional, com **contador "0/300"** visível e bloqueio ao atingir o máximo. É **privado** (só o treinador lê) e **não** aparece no card compartilhável (RN11).

---

## 5. Botoes e Acoes

| # | Componente | Label / Icone | Posicao | Estado Inicial | Acao ao Clicar |
|---|---|---|---|---|---|
| 1 | Botao primario | "Iniciar treino" | Rodapé (largura total) | Ativo (sem sessão) | Inicia a sessão: dispara o cronômetro e habilita os controles de execução nos cards |
| 2 | Botao primario | "Finalizar treino" | Rodapé (largura total) | Visível só em execução | Encerra a sessão, grava o registro de execução e abre o **Resumo da execução** (6.4) |
| 3 | Botão concluir série | (✓ / "Concluir série") | Card de exercício | Ativo em execução | Marca a série como feita, incrementa o contador e dispara o **timer de descanso** |
| 4 | Botão marcar concluído | "Marcar como concluído" | Card de exercício (sem séries) | Ativo em execução | Marca o exercício inteiro como feito (exercícios sem séries prescritas — RN08) |
| 5 | Thumbnail / ícone de vídeo | (vídeo) | Card de exercício | Ativo | Abre o player do exercício em modal/lightbox |
| 6 | Timer — "Pular" | "Pular" | Overlay do timer | Ativo durante descanso | Encerra o descanso imediatamente |
| 7 | Timer — "+15s" | "+15s" | Overlay do timer | Ativo durante descanso | Soma 15s ao descanso atual |
| 8 | Botao voltar | ← | Header (esquerda) | Ativo | Sem sessão: volta ao Detalhe da Rotina. Em execução: sai mantendo a sessão salva (retomável) |
| 9 | Resumo — "Compartilhar" | "Compartilhar" | Tela de Resumo (6.4) | Ativo | Abre o compartilhamento nativo com o card-resumo (estilo story) — ver RN07 |
| 10 | Resumo — "Concluir" | "Concluir" | Tela de Resumo (6.4) | Ativo | Salva o recado (se houver), fecha o resumo e retorna ao Detalhe da Rotina (`[VELA-6002]`) |
| 11 | Campo de recado | "Deixar um recado para o treinador" | Tela de Resumo (6.4) | Ativo (opcional) | Textarea com contador 0/300; conteúdo anexado ao registro de execução, fora do card compartilhável (RN11) |

---

## 6. Estados da Tela

### 6.1 Estado Inicial / Vazio
- **Sem sessão ativa (consulta):** o treino é exibido em modo leitura (igual à visão do treinador), com o botão **"Iniciar treino"** no rodapé. Não há estado vazio de treino — todo treino tem ≥1 exercício (regra do Cadastro `[VELA-4003]`).
- **Sessão em andamento salva (retomar):** se houver uma sessão deste treino não finalizada, a tela abre oferecendo **retomar** de onde parou (séries marcadas e tempo decorrido preservados — ver RN03).

### 6.2 Estado de Carregamento (Loading)
- **Skeleton loader** nas áreas de conteúdo (identificação e cards de exercício) enquanto o treino carrega.

### 6.3 Estado de Erro
- **Erro de carregamento:** mensagem central "Não foi possível carregar o treino." + botão **"Tentar novamente"**.
- **Erro de rede:** toast "Sem conexão. Tente novamente." Em execução, o progresso continua salvo localmente (ver RN03).
- **Erro ao gravar a execução (ao finalizar):** toast "Não foi possível salvar seu treino. Tente novamente." — a sessão **não é descartada** até gravar com sucesso.

### 6.4 Estado de Sucesso — Resumo da execução (compartilhável)
> **Tela própria em tela cheia (full-screen)** exibida ao **finalizar o treino**. Layout de celebração para **incentivar o compartilhamento** nas redes sociais (estilo story do Instagram).

- **Card-resumo (estilo story):** ocupa a tela, com identidade visual Vela (paleta verde-limão + azuis), com:
  - **Nome do treino** + categoria/trilha (`.track` / `.performance`).
  - **Duração** do treino (tempo de realização).
  - **Exercícios concluídos** (ex.: "8 de 8") e **total de séries** realizadas.
  - **Data** da execução.
  - Marca **`vela.`** discreta (assinatura da marca).
- **Recado para o treinador (opcional):** abaixo do card, campo de texto **"Deixar um recado para o treinador"** com contador "0/300". É **privado** — fica anexado ao registro de execução para o treinador ler, e **não** é incluído na imagem compartilhada no story (RN11).
- **Ações:** botão **"Compartilhar"** (abre o share nativo do dispositivo apenas com a imagem/card — sem o recado) e botão **"Concluir"** (salva o recado, se houver, fecha e volta ao Detalhe da Rotina).
- **Bastidor (nota interna):** ao chegar neste estado, o **registro de execução** já foi gravado (ver RN04); o recado é anexado a esse registro ao tocar em "Concluir". O compartilhamento é opcional e não afeta o registro.

### 6.5 Estado Desabilitado / Bloqueado *(se aplicavel)*
- **Em execução, sair pelo voltar:** não bloqueia nem descarta — sai mantendo a sessão salva como "em andamento" (RN03). Não há modal de descarte (decisão: persistência sobre confirmação).

---

## 7. Fluxo de Navegacao

### De onde o usuario chega nesta tela
| Origem | Gatilho |
|---|---|
| Detalhe da Rotina (Aluno) (`[VELA-6002]`) | Toca em um card de treino (RN08 daquela tela) |

### Para onde o usuario pode ir desta tela
| Destino | Gatilho |
|---|---|
| Detalhe da Rotina (Aluno) (`[VELA-6002]`) | Toca em ← (voltar) ou em "Concluir" no Resumo |
| Player de vídeo (modal/lightbox) | Toca na thumbnail/ícone de vídeo de um exercício |
| Compartilhamento nativo (story/redes) | Toca em "Compartilhar" no Resumo |

> **Observação:** o registro de execução gerado aqui alimenta (downstream) os KPIs e o bloco "último treino executado" de `[VELA-6002]` e `[VELA-6001]` (destrava decisões #41 e #45). O **Histórico de Treinos do Aluno** (ainda a mapear) consumirá esse mesmo registro.

---

## 8. Regras de Negocio
> Regras especificas que impactam o comportamento desta tela.

- **RN01 — Somente o Aluno executa:** tela exclusiva do **Aluno**, sobre treinos de rotinas **atribuídas a ele**. O conteúdo do treino (séries/reps/descanso prescritos) é **somente leitura** — o aluno não altera a prescrição, apenas registra o que realizou.
- **RN02 — Estrutura em grupos:** a execução respeita os **grupos numerados** e o **tipo** de cada grupo (Normal/Bi-set/Tri-set/Superset/Drop-set) definidos no treino (`[VELA-4002]`/`[VELA-4003]`). A ordem de execução é a do treino.
- **RN03 — Iniciar/Finalizar e persistência parcial:** a duração é medida por um fluxo **explícito**: **"Iniciar treino"** inicia o cronômetro; **"Finalizar treino"** encerra. Se o aluno sair/fechar o app no meio, a sessão fica **salva como "em andamento"** (séries marcadas + tempo decorrido) e é **retomável** ao reabrir o treino. A sessão só é descartada se o aluno finalizar ou (futuro) descartar explicitamente.
- **RN04 — Registro de execução (modelo de sessão):** ao **finalizar**, grava-se um **registro de execução (sessão)** com: **data**, **hora de início/fim**, **duração**, **exercícios concluídos**, e **séries/reps/carga realizadas** por exercício. É a **fonte de dados** dos KPIs e do "último treino executado" de `[VELA-6002]`/`[VELA-6001]` (destrava #41 e #45) e do futuro Histórico de Treinos.
- **RN05 — Timer de descanso:** ao concluir uma série, dispara um **timer regressivo** iniciando no **descanso prescrito** do exercício, com ações **Pular** e **+15s**. Em **grupos combinados** (Bi-set/Tri-set/Superset) **não há descanso entre os exercícios do grupo** — o timer dispara apenas ao **completar a rodada** (uma série de todos os exercícios do grupo). Em **Drop-set/Normal** dispara a cada série. Escopo do MVP = **descanso entre séries/rodadas**; há também o **cronômetro do treino** (tempo total correndo), usado para a duração.
- **RN06 — Contador e registro por exercício:** cada exercício tem um **contador de séries realizadas** (ex.: 3/4). O aluno marca cada série; o exercício fica **concluído** quando todas as séries são marcadas. Reps e **carga realizada** por série são **pré-preenchidos** com os valores **sugeridos pelo treinador** (carga é prescrita no treino — ver RN10) e o aluno só ajusta se realizou diferente. Não é obrigatório editar para concluir.
- **RN07 — Resumo compartilhável:** ao finalizar, exibe um **card-resumo estilo story** (identidade Vela) com nome do treino, duração, exercícios/séries concluídos e data, com ação **Compartilhar** (share nativo). O compartilhamento é **opcional** e **não** condiciona a gravação do registro (que já ocorreu na finalização).
- **RN08 — Exercício sem detalhe preenchido:** se séries/reps/descanso/execução vierem **vazios** (herdado da pendência de `[VELA-4002]`/`[VELA-3004]`), a tela **exibe apenas o que houver** e nunca quebra: sem séries prescritas, o exercício é concluído por um único botão **"Marcar como concluído"** (sem contador); sem descanso, o timer não dispara automaticamente (pode ser acionado manualmente, se aplicável).
- **RN09 — Som de repetição (fora do MVP):** o som configurável estilo box de CrossFit como auxílio durante o exercício é **opcional** e fica **fora do MVP** desta tela (ver decisão #48); entra em iteração futura.
- **RN11 — Recado ao treinador (opcional, privado):** na tela de Resumo, o aluno pode escrever um **recado para o treinador** (opcional, **máx. 300 caracteres**, com contador). É **privado** — fica **anexado ao registro de execução** (RN04) para o treinador ler na sua visão das execuções (dependência futura, junto dos KPIs) e **nunca** aparece no **card compartilhável** (story). Não escrever não bloqueia a conclusão.
- **RN10 — Carga sugerida pelo treinador (impacto cruzado):** a **carga** passa a ser um **campo prescrito no treino** — o **treinador informa a carga sugerida** por exercício/série no Cadastro de Treino, e o aluno vê essa carga em leitura e pode **sobrescrever** com a carga que realmente usou (registrada na execução). **Dependência:** o Cadastro/Edição de Treino (`[VELA-4003]`) e a Visualizar Treino do Treinador (`[VELA-4002]`) ainda **não têm** campo de carga — precisam ser revisados para incluí-lo (ver decisão #50). Enquanto a carga não for prescrita, o campo de carga realizada na execução fica **vazio/editável** (não bloqueia).

---

## 9. Responsividade (Mobile vs Web)
> Diferencas de comportamento ou layout entre plataformas.

| Aspecto | Mobile | Web |
|---|---|---|
| Layout | Coluna única, rolagem vertical | Mesma estrutura em container centralizado |
| Ações de execução | "Iniciar"/"Finalizar" fixos no rodapé; timer como overlay | Mesmas ações em barra de ação; timer em painel/overlay |
| Vídeo | Player em modal/lightbox; suporte a tela cheia | Player em modal/lightbox |
| Feedback do timer | Vibração + visual | Apenas visual (sem vibração) |
| Compartilhamento | Share sheet nativo (story/redes) | Compartilhamento via download/link da imagem do card |
| Demais comportamentos | Idêntico | Idêntico |

> Mesma lógica e mesmas regras em ambas as plataformas; apenas o layout e os recursos de hardware (vibração, share nativo) se adaptam.

---

## 10. Acessibilidade
> Consideracoes de acessibilidade para esta tela.

- Contadores de série e timer com **valor textual associado** (não depender só de cor/animação) — ex.: "Série 3 de 4", "Descanso: 45 segundos".
- Botões de "Concluir série"/"Marcar concluído" com nome acessível e estados (foco, concluído) anunciados por leitor de tela.
- Thumbnails e ícones de vídeo com texto alternativo; player com controles rotulados.
- Timer não deve depender exclusivamente de som — feedback visual e tátil também.
- Ordem de foco lógica: header → identificação → grupos/exercícios (controles de execução) → rodapé.
- Contraste de cores conforme WCAG 2.1 AA, inclusive no card-resumo de compartilhamento.

---

## 11. Historico de Alteracoes

| Data | Autor | Descricao |
|---|---|---|
| 2026-06-22 | Maria Isabela | **Recado ao treinador (RN11):** adicionado campo **opcional** "Deixar um recado para o treinador" na tela de Resumo (máx. **300 caracteres**, contador). É **privado** (anexado ao registro de execução, lido pelo treinador) e **não** entra no card compartilhável do story. Feedback de **conclusão de rotina** ficou no Detalhe da Rotina `[VELA-6002]` (decisão #51), fora desta tela. |
| 2026-06-22 | Maria Isabela | **Rodada 2 de decisões (pré-mockup):** (a) **carga** passa a ser **prescrita pelo treinador** (carga sugerida) e o aluno sobrescreve se usar diferente — novo campo no treino, exige revisar `[VELA-4003]`/`[VELA-4002]` (RN10, decisão #50); (b) lista com **todos os exercícios visíveis** e controles em cada card; (c) timer de descanso em **grupos combinados** dispara só ao **completar a rodada** do grupo (RN05); (d) Resumo de finalização = **tela própria em tela cheia** (6.4). |
| 2026-06-22 | Maria Isabela | Criação inicial do documento (entrevista `/mapear-tela`), a partir do ticket do cliente `VELA-5002`. **Visualizar / Executar Treino (Aluno)** `[VELA-6003]` (🔵 MVP), destino de toque do Detalhe da Rotina `[VELA-6002]` (RN08) e par de execução da Visualizar do Treinador `[VELA-4002]`. **Decisões da entrevista:** (a) MVP com **execução completa** (consulta + registro); (b) respeita a **estrutura de grupos numerados** (RN02); (c) formato **lista vertical estilo MFit** (decisão #47); (d) **Iniciar/Finalizar explícitos** com cronômetro + persistência parcial retomável (RN03); (e) **timer de descanso** entre séries usando o descanso prescrito (RN05); (f) **contador de séries** no MVP, reps/carga opcionais (RN06), **som de repetição fora do MVP** (RN09/#48); (g) exercício sem detalhe **não quebra** a tela (RN08); (h) ao finalizar, **resumo compartilhável estilo story** para incentivar redes sociais (RN07/#46). **Modelo de execução (sessão)** definido (RN04) — **destrava** os KPIs/"último treino" adiados em `[VELA-6002]`/`[VELA-6001]` (#41 e #45). Consolida os placeholders Iniciar/Andamento/Finalizar do fluxo do Aluno. Status → EM ANDAMENTO |
</content>
</invoke>

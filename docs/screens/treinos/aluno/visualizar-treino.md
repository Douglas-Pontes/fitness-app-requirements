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
| **Status** | 🟢 CONCLUIDO |
| **Ultima atualizacao** | 2026-06-23 |

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
- Conteudo: Botão voltar (←) + **nome do treino** + selo de **categoria** (ex.: "Peito · hipertrofia") + **botão Play/Pause** ao lado do **cronômetro geral** do treino.
- Comportamento: **Fixo no topo** — o botão Play/Pause e o cronômetro permanecem visíveis mesmo ao rolar a página.
  - O **cronômetro geral** começa em **00:00** e **só passa a contar quando o aluno toca em Play** (não conta sozinho ao abrir a tela). O botão alterna **Play ⇄ Pause**, permitindo **pausar e retomar** a contagem (ex.: pausa para atender o telefone).
  - O botão voltar (←) **não descarta** a sessão — sai mantendo o treino salvo como "em andamento" e retomável (ver RN03/persistência).

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
  - **Controles de execução** (disponíveis **somente depois que o aluno deu Play** no treino — antes disso o card fica em leitura):
    - **Contador de séries** (ex.: "3 / 4").
    - Campos para registrar **reps realizadas** e **carga realizada** por série, **pré-preenchidos** com os valores **sugeridos pelo treinador** (reps prescritas + carga sugerida); o aluno só ajusta se usar valor diferente (RN06).
    - Linha de ação compacta com dois botões lado a lado: **"⏱ Descanso"** (individual de cada exercício — abre a telinha de descanso daquele exercício, ver "Componente — Timer de descanso") e um **botão de check (✓)** que **marca o exercício como concluído**. Ambos ficam **desabilitados enquanto o aluno não der Play** no treino (RN05).
    - Indicação visual de **exercício concluído** (card destacado em verde) ao tocar no check, ou pelo botão "Marcar como concluído" nos exercícios sem séries (RN08).
- Comportamento:
  - Tocar no **vídeo/thumbnail** abre o player do exercício (modal/lightbox por cima da lista — mesmo padrão da decisão #20).
  - Tocar no card (fora dos controles) pode expandir os detalhes/execução completa do exercício.
  - Sem botões de adicionar/remover/reordenar — o aluno não altera a estrutura do treino.

**Componente — Timer de descanso (por exercício, sob demanda)**
- Componente: Telinha/overlay **compacta** de **descanso regressivo**, aberta **apenas quando o aluno toca no botão "⏱ Descanso"** de um exercício (não dispara sozinho ao concluir série).
- Conteudo:
  - **Textinho de série** (ex.: "Série 1/3") para o aluno se localizar sem fechar a telinha.
  - **Tempo regressivo** iniciando no **valor do campo "Descanso" prescrito** (ex.: 0:45) e indo até **0:00**.
  - Ações: **+15s** (soma 15 segundos) e **Play (▶)** (inicia a contagem regressiva).
- Comportamento: ao zerar (0:00), sinaliza (vibração/feedback visual) e o **Play fica disponível novamente** para a **próxima série** (sem botão separado de "próxima série" — o próprio Play re-arma o descanso e avança a série). Disponível só com o treino em Play (RN05). O **som de repetição** estilo box de CrossFit fica **fora do MVP** (ver RN09 / decisão #48).

### 3.3 Footer / Rodape
- Conteudo: botão primário **"Finalizar treino"** (largura total), fixo no rodapé.
- Comportamento: Fixo na parte inferior. **"Finalizar treino"** encerra a sessão, grava o registro de execução e abre o **Resumo da execução** (ver 6.4). O **início/pausa** do treino é feito pelo **Play/Pause no topo** (não há mais "Iniciar treino" no rodapé).

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
| 1 | Botão Play/Pause | ▶ / ⏸ (+ cronômetro) | Header (topo, fixo) | Play (cronômetro 00:00) | Play inicia/retoma o **cronômetro geral** e habilita os controles de execução; Pause congela a contagem |
| 2 | Botao primario | "Finalizar treino" | Rodapé (largura total) | Ativo | Encerra a sessão, grava o registro de execução e abre o **Resumo da execução** (6.4) |
| 3 | Botão "⏱ Descanso" | "⏱ Descanso" | Card de exercício (linha de ação) | Desabilitado até dar Play | Abre a telinha de descanso daquele exercício (individual — RN05) |
| 3b | Botão de check | ✓ | Card de exercício (ao lado do Descanso) | Desabilitado até dar Play | Marca o exercício como **concluído** (card fica verde) |
| 4 | Botão marcar concluído | "Marcar como concluído" | Card de exercício (sem séries) | Ativo após Play | Marca o exercício inteiro como feito (exercícios sem séries prescritas — RN08) |
| 5 | Thumbnail / ícone de vídeo | (vídeo) | Card de exercício | Ativo | Abre o player do exercício em modal/lightbox |
| 6 | Timer — Play | ▶ | Telinha de descanso | Ativo | Inicia a contagem regressiva (45→0); ao zerar, re-arma para a próxima série |
| 7 | Timer — "+15s" | "+15s" | Telinha de descanso | Ativo | Soma 15s ao descanso atual |
| 9 | Botao voltar | ← | Header (esquerda) | Ativo | Sai mantendo a sessão salva (retomável) |
| 10 | Resumo — "Compartilhar" | "Compartilhar" | Tela de Resumo (6.4) | Ativo | Abre o compartilhamento nativo com o card-resumo (estilo story) — ver RN07 |
| 11 | Resumo — "Concluir" | "Concluir" | Tela de Resumo (6.4) | Ativo | Salva o recado (se houver), fecha o resumo e retorna ao Detalhe da Rotina (`[VELA-6002]`) |
| 12 | Campo de recado | "Deixar um recado para o treinador" | Tela de Resumo (6.4) | Ativo (opcional) | Textarea com contador 0/300; conteúdo anexado ao registro de execução, fora do card compartilhável (RN11) |

---

## 6. Estados da Tela

### 6.1 Estado Inicial / Vazio
- **Treino aberto, antes do Play:** o treino é exibido em modo leitura, com o **cronômetro em 00:00** e o botão **Play** no topo; os botões "Descanso" dos cards ficam **desabilitados**. "Finalizar treino" no rodapé. Não há estado vazio de treino — todo treino tem ≥1 exercício (regra do Cadastro `[VELA-4003]`).
- **Em execução (após Play):** cronômetro correndo (botão vira Pause); cards habilitam contador de séries, campos de reps/carga e o botão "Descanso".
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
  - **Primeiro nome do aluno** (ex.: "Ana · treino concluído") — personaliza sem expor foto.
  - **Nome do treino**.
  - **Duração** do treino (tempo de realização).
  - **Exercícios concluídos** (ex.: "8 de 8") e **treinos na semana** (ex.: "2/5" — treinos executados na semana / total de treinos da base do aluno; ver RN12).
  - **Data e hora** da execução (ex.: "22 jun 2026 · 18:42").
  - Marca **`vela.` em destaque** (assinatura da marca, reforçada — esta tela serve de **divulgação**; **sem selo de trilha** — RN13/decisão #53).
- **Fluxo de compartilhamento (consolidado — decisão #54):** o sub-fluxo tem **uma única tela de edição**, evitando telas intermediárias:
  1. No **Resumo** (esta tela), o aluno toca em **"Compartilhar"**.
  2. Abre o **Editor único** — uma só tela onde ele ajusta **fundo + texto juntos** (ver abaixo).
  3. No Editor, ao tocar em **"Compartilhar"**, sobe a **folha de destinos do sistema** **por cima** (overlay, não é outra tela): **Story do Instagram, WhatsApp, Salvar**.
- **Editor único (fundo + texto numa só tela):**
  - **Card editável no topo** (estilo "stats sobre foto", ref. Strava): nome do aluno, nome do treino, métricas e data/hora formam **um só bloco** que o aluno **move e redimensiona junto**; itens internos podem ser **ocultados/readicionados** (bandeja) — ver RN13.
  - **Faixa de fundo na base:** opção **"Tirar foto"** (câmera) + miniaturas dos **fundos do app** (artes branded). **Galeria = MVP futuro** (não exibida).
  - **Botão primário "Compartilhar"** abre a folha de destinos.
  - A imagem gerada do card é o que vai para o destino; o **recado ao treinador não entra** na imagem (RN11).
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
- **RN03 — Play/Pause, Finalizar e persistência parcial:** a duração é medida pelo **cronômetro geral** no topo, que **só conta após o aluno tocar em Play** (começa em 00:00) e pode ser **pausado/retomado** (Play ⇄ Pause). **"Finalizar treino"** (rodapé) encerra a sessão. Se o aluno sair/fechar o app no meio, a sessão fica **salva como "em andamento"** (séries marcadas + tempo decorrido) e é **retomável** ao reabrir o treino. A sessão só é descartada se o aluno finalizar ou (futuro) descartar explicitamente.
- **RN04 — Registro de execução (modelo de sessão):** ao **finalizar**, grava-se um **registro de execução (sessão)** com: **data**, **hora de início/fim**, **duração**, **exercícios concluídos**, e **séries/reps/carga realizadas** por exercício. É a **fonte de dados** dos KPIs e do "último treino executado" de `[VELA-6002]`/`[VELA-6001]` (destrava #41 e #45) e do futuro Histórico de Treinos.
- **RN05 — Descanso sob demanda (por exercício):** o descanso **não dispara sozinho** — cada exercício tem, numa linha de ação compacta, um botão **"⏱ Descanso"** (com ícone de cronômetro) ao lado de um **check (✓)** que marca o exercício como concluído. Tocar em "⏱ Descanso" abre a telinha **compacta** daquele exercício, que mostra o **textinho de série** (ex.: "Série 1/3"), o **tempo regressivo** iniciando no **descanso prescrito** (ex.: 0:45→0:00) e as ações **+15s** e **Play (▶)**. O **Play** inicia a contagem; ao **zerar**, fica disponível novamente para a **próxima série** (re-arma sem botão separado). Ambos os botões do card ficam **desabilitados enquanto o treino não estiver em Play**. Em paralelo corre o **cronômetro geral** do treino (RN03), usado para a duração.
- **RN06 — Contador e registro por exercício:** cada exercício tem um **contador de séries realizadas** (ex.: 3/4). O aluno marca cada série; o exercício fica **concluído** quando todas as séries são marcadas. Reps e **carga realizada** por série são **pré-preenchidos** com os valores **sugeridos pelo treinador** (carga é prescrita no treino — ver RN10) e o aluno só ajusta se realizou diferente. Não é obrigatório editar para concluir.
- **RN07 — Resumo compartilhável:** ao finalizar, exibe um **card-resumo estilo story** (identidade Vela) com **primeiro nome do aluno**, nome do treino, duração, exercícios concluídos, **treinos na semana** (RN12) e **data/hora**, com a marca **`vela.` em destaque** (sem selo de trilha — RN13/decisão #53). A ação **Compartilhar** abre o **Editor único** (fundo + texto numa só tela — decisão #54); de lá, o botão Compartilhar sobe a **folha de destinos do sistema** (overlay) com **Story do Instagram, WhatsApp e Salvar**. O compartilhamento é **opcional** e **não** condiciona a gravação do registro (que já ocorreu na finalização). O **recado ao treinador não** entra na imagem (RN11).
- **RN13 — Card de compartilhamento (composição e edição, bloco único — estilo "stats sobre foto"):**
  - **Fundo:** **padrão do app** (artes branded, com a marca) ou **foto da câmera do app**; **galeria fica fora do MVP (MVP futuro)** e **não é exibida** (sem placeholder/"em breve"). A troca de fundo é feita **dentro do Editor único**, numa **faixa de fundos** na base ("Tirar foto" + miniaturas dos fundos do app) — sem tela separada (ver 6.4 / decisão #54).
  - **Único elemento fixo (não move, não redimensiona, não oculta):** a **marca `vela.`**, exibida em **destaque** no rodapé do card. **O selo de trilha (`.track`/`.performance`) NÃO aparece neste card** — esta tela tem foco em **divulgação da marca** (ênfase em `vela.`), decisão #53.
  - **Bloco único de conteúdo (Opção 1):** **nome do aluno**, **nome do treino**, as **métricas** (duração, exercícios, treinos na semana) e **data/hora** formam **um só bloco**. O aluno pode:
    - **Mover** o bloco inteiro pelo card (arrastando a alça de mover ✥);
    - **Redimensionar** o bloco inteiro — aumentar/diminuir — pela alça de redimensionar (⤡), **mantendo a proporção interna** entre os itens;
    - **Ocultar/readicionar itens internos:** dentro do bloco, cada informação tem um **✕** que a remove; o item vai para uma **bandeja** abaixo do card e pode ser readicionado. (Não há reordenação nem movimento individual dos itens — eles se movem e redimensionam **sempre juntos**.)
  - **Estilo travado:** **ícones de linha** (não emoji), pequenos; **cor padrão branca** para textos e ícones, com **destaque (verde-limão) apenas para a marca**. **Fonte e cores dos ícones não são editáveis.**
  - **Data/hora:** o card inclui **data e hora** da execução (ex.: "22 jun 2026 · 18:42").
  - O **recado ao treinador nunca** entra na imagem (RN11).
- **RN12 — KPI "treinos na semana" no resumo:** o resumo exibe **treinos executados na semana / total de treinos da base do aluno** (ex.: "1/5") — no lugar do antigo "total de séries". O **numerador** conta as **execuções concluídas do aluno na semana corrente, considerando de segunda a sexta** (sábado e domingo não entram na contagem; zera toda segunda). O **denominador** é o **nº de treinos disponíveis ao aluno = soma dos treinos de todas as rotinas ativas** atribuídas a ele (ex.: rotina A com 3 + rotina B com 2 = 5). Depende do **registro de execução** (RN04), que esta tela passa a gerar. (Decisão #52 resolvida.)
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
| 2026-06-23 | Maria Isabela | **Tela finalizada → 🟢 CONCLUIDO.** Resolvida a **decisão #52** (RN12): "semana" do KPI = **segunda a sexta** da semana corrente (sáb/dom não contam; zera toda segunda); **denominador = soma dos treinos de todas as rotinas ativas** do aluno. Sem mais ⚠️ PENDENTE na tela. **Dependência cruzada em aberto (não trava esta tela):** RN10/decisão #50 — incluir campo de **carga sugerida** no Cadastro/Visualizar Treino do Treinador (`[VELA-4003]`/`[VELA-4002]`); e o **Histórico de Treinos do Aluno** (a mapear) que consumirá o registro de execução (RN04). |
| 2026-06-23 | Maria Isabela | **Fluxo de compartilhamento consolidado (rodada 8 — decisão #54):** o sub-fluxo passou de **3 telas** (escolher fundo + pré-visualização + modo edição) para **1 só** — **Editor único** com **fundo + texto na mesma tela** (card editável no topo; faixa de fundo "Tirar foto" + fundos do app na base; botão Compartilhar). Os **destinos** (Story Instagram/WhatsApp/Salvar) viram **folha do sistema em overlay** sobre o editor, não uma tela nova. **Resumo** segue como porta de entrada (celebração + recado + Compartilhar/Concluir). Mockup: removidos os frames "escolher fundo" e "modo edição"; agora "editor (fundo+texto)" + "escolher destino". 6.4/RN07/RN13 atualizados. |
| 2026-06-23 | Maria Isabela | **Card de compartilhamento (rodada 7):** (a) **Opção 1 confirmada** — conteúdo vira **bloco único** que move/redimensiona junto, com **ocultar/readicionar itens** internos (bandeja); removidos as zonas/snap e o movimento por bloco independente (RN13). (b) **Selo de trilha removido** do card e **marca `vela.` em destaque** — foco em divulgação (decisão #53; RN07/RN13/6.4). (c) Card passa a incluir **data e hora** (ex.: "22 jun 2026 · 18:42"). (d) Novo **frame de seleção de fundo** (fundos do app + "Tirar foto"; **galeria fora do MVP**, não exibida) (6.4). (e) Destinos de compartilhamento fixados em **Story do Instagram, WhatsApp e Salvar** (RN07). Mockup atualizado (frames resumo, seleção de fundo, pré-visualização e modo edição). |
| 2026-06-22 | Maria Isabela | **Editor do card de compartilhamento (rodada 6):** novo **RN13** — card estilo "stats sobre foto" (ref. Strava). **Fundo:** padrão do app ou **foto da câmera** (galeria futura). **Fixos:** selo (topo) e `vela.` (rodapé). **Móveis/ocultáveis:** nome do aluno, nome do treino, métricas e data, com **encaixe em zonas** numa área segura central (3 linhas de baixo p/ cima, colunas conforme nº de blocos; padrão centralizado) e **bandeja** de blocos ocultos. **Ícones de linha (não emoji), brancos**, destaque só na marca; **fonte/cores de ícone não editáveis**. Mockup atualizado (card de story e resumo). |
| 2026-06-22 | Maria Isabela | **Card de compartilhamento (story) definido (rodada 5):** composição do card = **primeiro nome do aluno** ("Ana · treino concluído") + nome do treino + **selo de trilha** (`.track`/`.performance`) + **duração, exercícios e treinos na semana** + data + marca `vela.` (sem foto do aluno; recado fora da imagem — RN11). A ação Compartilhar mostra **pré-visualização no app + folha de destinos do sistema** (antes de escolher Instagram). RN07 atualizada; decisão #46 resolvida (restam só formatos de export). |
| 2026-06-22 | Maria Isabela | **Refino dos controles de descanso (rodada 4):** (a) botão de descanso ganha **ícone de cronômetro** ("⏱ Descanso"), fica **menor** e passa a dividir uma linha compacta com um **botão de check (✓)** que marca o exercício concluído (RN05). (b) telinha de descanso **compacta**: textinho **"Série 1/3"**, contagem **45→0** e apenas **+15s** e **Play (▶)**; ao zerar, o Play re-arma para a próxima série (removidos "Iniciar descanso" e "Próxima série" como botões separados). |
| 2026-06-22 | Maria Isabela | **Refino de execução (pré-mockup, rodada 3):** (a) **Play/Pause + cronômetro geral fixos no topo** — o cronômetro só conta após o Play e pode pausar/retomar; "Iniciar treino" no rodapé foi **removido** e "Finalizar treino" permanece no rodapé (RN03). (b) **Descanso sob demanda por exercício** — botão "Descanso" individual em cada card (habilita só após Play); a telinha de descanso traz **+15s**, **Iniciar descanso** (substitui "Pular") e **Próxima série** (avança o contador); não dispara mais automático (RN05). (c) **Resumo:** "total de séries" substituído por **"treinos na semana" (ex.: 2/5)** = execuções na semana / nº de treinos da base do aluno (RN12, decisão #52). |
| 2026-06-22 | Maria Isabela | **Recado ao treinador (RN11):** adicionado campo **opcional** "Deixar um recado para o treinador" na tela de Resumo (máx. **300 caracteres**, contador). É **privado** (anexado ao registro de execução, lido pelo treinador) e **não** entra no card compartilhável do story. Feedback de **conclusão de rotina** ficou no Detalhe da Rotina `[VELA-6002]` (decisão #51), fora desta tela. |
| 2026-06-22 | Maria Isabela | **Rodada 2 de decisões (pré-mockup):** (a) **carga** passa a ser **prescrita pelo treinador** (carga sugerida) e o aluno sobrescreve se usar diferente — novo campo no treino, exige revisar `[VELA-4003]`/`[VELA-4002]` (RN10, decisão #50); (b) lista com **todos os exercícios visíveis** e controles em cada card; (c) timer de descanso em **grupos combinados** dispara só ao **completar a rodada** do grupo (RN05); (d) Resumo de finalização = **tela própria em tela cheia** (6.4). |
| 2026-06-22 | Maria Isabela | Criação inicial do documento (entrevista `/mapear-tela`), a partir do ticket do cliente `VELA-5002`. **Visualizar / Executar Treino (Aluno)** `[VELA-6003]` (🔵 MVP), destino de toque do Detalhe da Rotina `[VELA-6002]` (RN08) e par de execução da Visualizar do Treinador `[VELA-4002]`. **Decisões da entrevista:** (a) MVP com **execução completa** (consulta + registro); (b) respeita a **estrutura de grupos numerados** (RN02); (c) formato **lista vertical estilo MFit** (decisão #47); (d) **Iniciar/Finalizar explícitos** com cronômetro + persistência parcial retomável (RN03); (e) **timer de descanso** entre séries usando o descanso prescrito (RN05); (f) **contador de séries** no MVP, reps/carga opcionais (RN06), **som de repetição fora do MVP** (RN09/#48); (g) exercício sem detalhe **não quebra** a tela (RN08); (h) ao finalizar, **resumo compartilhável estilo story** para incentivar redes sociais (RN07/#46). **Modelo de execução (sessão)** definido (RN04) — **destrava** os KPIs/"último treino" adiados em `[VELA-6002]`/`[VELA-6001]` (#41 e #45). Consolida os placeholders Iniciar/Andamento/Finalizar do fluxo do Aluno. Status → EM ANDAMENTO |
</content>
</invoke>

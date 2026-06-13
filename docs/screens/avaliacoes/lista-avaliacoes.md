# Tela: Lista de Avaliações `[VELA-2001]`

---

## Metadados
| Campo | Valor |
|---|---|
| **Nome da tela** | Lista de Avaliações |
| **Modulo** | Avaliações |
| **Codigo** | VELA-2001 |
| **Prioridade** | 🔵 MVP |
| **Status** | 🟢 CONCLUIDO |
| **Ultima atualizacao** | 2026-06-10 |

---

## 1. Objetivo da Tela
> O que o usuario consegue fazer nesta tela? Qual problema ela resolve?

Tela de **lista unica para todos os tipos de avaliacao** (Anamnese, Antropometrica, Dobras Cutaneas, Bioimpedancia e outros tipos futuros). Exibe todas as avaliacoes do Aluno **ordenadas por data** (mais recente primeiro), com **cards finos e neutros** (tipo e status indicados por **icone colorido**) e um **status** por card (Solicitada / Em andamento / Concluida / Expirada). E uma **lista unica** (sem secoes): os **pendentes do Aluno aparecem primeiro** e os demais por data. Permite **filtrar por periodo, status e tipo** (botoes que abrem painel) e **visualizar** qualquer avaliacao (`[VELA-2002]`). As acoes de criar/editar/excluir/liberar sao do **Treinador**; o **Aluno** apenas **visualiza** e **preenche** avaliacoes que o Treinador liberou para ele (enquanto estiverem pendentes). Quando o Treinador **libera** uma avaliacao, o Aluno **recebe uma notificacao** e a avaliacao vai para o **topo da lista** como pendencia a responder (com contador na propria aba). As permissoes completas estao na Secao 8.

---

## 2. Quem Acessa / Pre-condicoes
> Quem pode ver esta tela? Quais condicoes precisam ser verdadeiras?

- **Usuario:**
  - **Aluno** (dono do perfil) — ve a propria lista de avaliacoes. **Nao cria/edita/exclui**; apenas **visualiza** e **preenche** as que o Treinador liberou.
  - **Treinador** — ve a lista de avaliacoes de um Aluno vinculado, ao **abrir o perfil daquele Aluno**. **Cria / edita / exclui / libera** avaliacoes.
- **Pre-condicoes:**
  - Usuario autenticado.
  - Para o Treinador: ter vinculo ativo com o Aluno e ter aberto o perfil/contexto do Aluno.
- **Permissoes especiais:** Detalhadas na Secao 8. Em resumo: criar/editar/excluir/liberar = **somente Treinador**; visualizar = **ambos**; preencher = **Aluno**, apenas em avaliacoes liberadas a ele com status **Solicitada** ou **Em andamento** (iniciadas por ele).

---

## 3. Layout e Componentes Visuais
> Descreva a estrutura visual da tela de cima para baixo.

### 3.1 Header / Cabecalho
- Conteudo: Botao voltar (quando aberta a partir do perfil) + Titulo **"Avaliacoes"**. Quando um Treinador abre o perfil de um Aluno, exibir abaixo do titulo o nome/@ do Aluno em contexto (ex: "Avaliacoes de @ana.vela").
- Comportamento: Fixo no topo.

### 3.2 Corpo Principal
> Descrever secoes da tela, na ordem que aparecem. A tela segue a ordem: **filtros → lista unica de cards** (sem secoes/abas separadas).

**Secao 1 — Filtros (botoes)**
- Componente: Barra com **botoes de filtro** que abrem um **painel/bottom sheet** ao toque (em vez de uma fileira longa de chips). Sao **tres** botoes, na ordem:
  1. **Periodo** — abre painel com presets (**Este mes**, **Este ano**, **Tudo**) e, abaixo, a opcao **Personalizado** (campos de data inicial e final).
  2. **Status** — abre painel de **multiselecao** (Solicitada, Em andamento, Concluida, Expirada).
  3. **Tipo** — abre painel de **multiselecao** (Anamnese, Antropometrica, Dobras Cutaneas, Bioimpedancia).
- Comportamento:
  - A tela **abre sem filtro aplicado** (Tudo / todos os status / todos os tipos).
  - Cada botao mostra o valor selecionado quando ativo (ex: "Periodo: 3 meses", "Status: 2") e fica destacado com o **verde-limao neon** da marca; ao confirmar a selecao no painel, a lista e refiltrada imediatamente.
  - Os tres filtros sao combinaveis (E logico).

**Secao 2 — Lista unica de avaliacoes**
- Componente: Lista vertical de **cards finos** (compactos), **sem separacao em secoes**.
- Ordenacao (RN01/RN12):
  - **Pendentes primeiro** — avaliacoes pendentes do Aluno (**Solicitada** + **Em andamento** iniciada por ele) aparecem no **topo** da lista.
  - **Demais em ordem cronologica decrescente** (mais recente primeiro) logo abaixo.
  - Nao ha bloco/banner destacado separado; o realce dos pendentes vem apenas da **posicao** (topo) e do **icone de status**.
- Conteudo de cada card (enxuto — **somente** estes itens):
  - **Tipo** — **icone + rotulo** (ex: "Antropometrica"). O icone tem cor propria do tipo, mas **nao tinge o card**.
  - **Data** — data da avaliacao (Concluida) ou de solicitacao/liberacao (demais), formato dd/mm/aaaa.
  - **Quem fez** — **@ do profissional** que aplicou/solicitou (ex: "por @ze.personal").
  - **Status** — representado por um **icone colorido** (uma cor por status) + rotulo curto: **Solicitada**, **Em andamento**, **Concluida**, **Expirada**. O icone de status **nao altera a cor do card** (card permanece neutro).
  - > **Nao** exibir no card: resumo/metricas (peso, % G, etc.), texto de prazo nem descricoes longas — essas informacoes aparecem apenas ao abrir **Visualizar** `[VELA-2002]` ou **Preencher** `[VELA-2003]`.
  - **Botoes de acao no card** (variam por papel e status; ver Secao 5):
    - **Aluno:** **Visualizar** sempre; **Preencher/Continuar** apenas se liberada a ele e com status Solicitada ou Em andamento (iniciada por ele). Nunca Editar/Excluir.
    - **Treinador:** **Editar** (Solicitada/Em andamento) ou **Revisar** (Concluida), **Visualizar** e, no menu **⋮**, **Excluir** (e **Liberar para o aluno preencher**, quando aplicavel).
- Comportamento:
  - Scroll vertical; paginacao/scroll infinito quando houver muitas avaliacoes.
  - Card **neutro e fino**, mantendo a identidade Vela (alto contraste, minimalista); a distincao visual vem do **icone de tipo** (colorido) e do **icone de status** (colorido), nunca do fundo do card.

**Cores de referencia — icone de tipo e icone de status**

| Tipo | Icone (referencia) | Cor do icone |
|---|---|---|
| Anamnese | Prancheta / clipboard | Azul-marinho |
| Antropometrica | Fita metrica | Verde-limao neon (`#CCF24D`) |
| Dobras Cutaneas | Adipometro / compasso | Azul-claro |
| Bioimpedancia | Raio / balanca | Azul-ardosia |

| Status | Cor do icone (referencia) |
|---|---|
| Solicitada | Verde-limao neon (pendente) |
| Em andamento | Ambar / amarelo (em progresso) |
| Concluida | Azul-marinho / verde (ok) |
| Expirada | Cinza / vermelho (alerta) |

> As cores sao referencias da paleta-assinatura Vela (ver `04-identidade-de-marca.md`). O objetivo e que tipo e status sejam reconheciveis pelo **icone colorido**, mantendo o **card neutro**.

### 3.3 Footer / Rodape
- Conteudo: **Botao de acao flutuante (FAB)** "Nova avaliacao" (icone +) — **somente para o Treinador**. Ao tocar, abre o **seletor de tipo** (bottom sheet) com: Anamnese, Antropometrica, Dobras Cutaneas, Bioimpedancia. Apos escolher o tipo, navega para o formulario `[VELA-2003]` no modo de criacao, onde o Treinador pode **preencher na hora** ou **liberar para o Aluno preencher** (status Solicitada), opcionalmente definindo um **prazo** de preenchimento.
- Comportamento: FAB fixo no canto inferior, **exibido apenas para o Treinador** (o Aluno nao ve o FAB — ele nao cria avaliacoes). Quando a tela e aberta no contexto da Tab Bar, a barra de navegacao inferior permanece visivel com a aba "Avaliacoes/Evolucao" ativa.
- **Badge na aba (apenas Aluno):** a aba "Avaliacoes/Evolucao" da Tab Bar exibe um **contador** com o numero de avaliacoes pendentes do Aluno (**Solicitadas** + **Em andamento** nao enviadas). O badge **nao** conta avaliacoes **Expiradas** nem **Concluidas**, e zera quando nao houver mais pendencias.

---

## 4. Campos e Formularios

> Preencher apenas se a tela tiver campos de entrada (inputs, selects, etc.)

Esta tela nao possui formulario de cadastro. Os unicos controles de entrada sao os **filtros**:

| # | Nome do Campo | Tipo | Obrigatorio | Placeholder | Validacao | Mensagem de Erro |
|---|---|---|---|---|---|---|
| 1 | Periodo | Botao → painel: preset (selecao unica) ou Personalizado | Nao | — | Um preset por vez | N/A |
| 2 | Periodo personalizado — Data inicial | Date (no painel "Personalizado") | Condicional (se "Personalizado") | "Inicio" | Nao pode ser maior que a data final | "A data inicial deve ser anterior a final" |
| 3 | Periodo personalizado — Data final | Date (no painel "Personalizado") | Condicional (se "Personalizado") | "Fim" | Nao pode ser futura nem menor que a inicial | "Selecione um intervalo valido" |
| 4 | Status (filtro) | Botao → painel de multiselecao | Nao | — | — | N/A |
| 5 | Tipo de avaliacao (filtro) | Botao → painel de multiselecao | Nao | — | — | N/A |

### Regras de Preenchimento
- A tela **abre sem filtro aplicado**: periodo "Tudo", todos os status e todos os tipos.
- Cada filtro e um **botao** que abre um **painel/bottom sheet**; a lista so e refiltrada **apos confirmar** a selecao no painel.
- No painel de Periodo, escolher "Personalizado" exibe os campos de data inicial/final; aplicar somente apos confirmar as duas datas.
- Os filtros de periodo, status e tipo sao combinaveis (E logico): mostra avaliacoes do(s) tipo(s) e status selecionados dentro do periodo selecionado.

---

## 5. Botoes e Acoes

| # | Componente | Label / Icone | Posicao | Visivel para | Acao ao Clicar |
|---|---|---|---|---|---|
| 1 | FAB | "Nova avaliacao" (+) | Inferior direito | **Treinador** | Abre bottom sheet de selecao de tipo → navega para `[VELA-2003]` em modo criacao (preencher na hora ou liberar para o Aluno) |
| 2 | Botao no card | "Preencher" / "Continuar" | Dentro do card | **Aluno**, se status = **Solicitada** ou **Em andamento** (iniciada por ele) | Navega para `[VELA-2003]` em modo **preenchimento** (Aluno preenche/continua a avaliacao liberada). **Nao** aparece em Concluida nem Expirada |
| 3 | Botao no card | "Editar" / "Revisar" (icone lapis) | Dentro do card | **Treinador** | Navega para `[VELA-2003]` com os campos **ja preenchidos**. Rotulo **"Editar"** em Solicitada/Em andamento e **"Revisar"** em Concluida (edita no lugar, continua Concluida — RN06) |
| 4 | Botao no card | "Visualizar" (icone olho) | Dentro do card | **Ambos** | Navega para **Visualizar Avaliacao** `[VELA-2002]` |
| 5 | Menu de acoes | "⋮" | Canto superior direito do card | **Treinador** | Abre menu com **Excluir** e, quando aplicavel, **Liberar para o aluno preencher** |
| 6 | Botoes de filtro | "Periodo" / "Status" / "Tipo" | Topo (Secao 1) | Ambos | Cada um abre um painel/bottom sheet; ao confirmar, refiltra a lista |

> **Decisao de UX para excluir (definida):** apenas o **Treinador** exclui, pelo **menu de tres pontos (⋮)** no card → "Excluir", sempre com **modal de confirmacao** ("Excluir esta avaliacao? Esta acao nao pode ser desfeita."). A exclusao e **definitiva** (o app nao tem lixeira). Optou-se pelo menu ⋮ por funcionar de forma identica em mobile e web.

---

## 6. Estados da Tela

### 6.1 Estado Inicial / Vazio
- **Treinador, Aluno sem avaliacoes:** ilustracao + mensagem "Este aluno ainda nao tem avaliacoes." + botao "Nova avaliacao".
- **Aluno sem avaliacoes:** mensagem "Voce ainda nao tem avaliacoes. Quando seu treinador liberar uma avaliacao, ela aparecera aqui." (sem botao de criar).
- **Sem resultados para o filtro:** mensagem "Nenhuma avaliacao para os filtros selecionados (periodo/tipo/status)" + atalho "Limpar filtros" (restaura Tudo / Todos / Todas).

### 6.2 Estado de Carregamento (Loading)
- Skeleton loader com 3–4 cards placeholder enquanto a lista e carregada.
- Ao aplicar filtro, skeleton/atualizacao leve na area da lista.

### 6.3 Estado de Erro
- **Erro ao carregar a lista:** mensagem com botao "Tentar novamente" (retry).
- **Erro de rede:** toast superior "Sem conexao. Tente novamente."
- **Erro ao excluir:** toast "Nao foi possivel excluir. Tente novamente." e o card permanece na lista.

### 6.4 Estado de Sucesso
- **Apos excluir (Treinador):** o card sai da lista com toast "Avaliacao excluida." (exclusao definitiva, sem desfazer).
- **Apos criar/editar/liberar (Treinador):** a lista reflete a avaliacao na posicao correta (pendentes no topo; demais por data), com leve destaque do card afetado. Uma avaliacao liberada aparece com status **Solicitada** (ou **Em andamento**, se o profissional iniciou o preenchimento sem finalizar).
- **Apos o Aluno iniciar o preenchimento (sem enviar):** o card passa de **Solicitada** para **Em andamento**; continua entre os pendentes (topo) e no badge ate ser enviado.
- **Apos o Aluno preencher e enviar:** o card passa para **Concluida**; sai dos pendentes, reordena por data; o botao "Preencher" some, restando "Visualizar".
- **Apos vencer o prazo sem o Aluno iniciar (status Solicitada):** o card passa para **Expirada**; sai dos pendentes e do badge do Aluno e o botao "Preencher" some (so o profissional reabre — RN13). Uma avaliacao ja **Em andamento** (iniciada pelo Aluno) **nao** expira — permanece como pendencia ate concluir.

### 6.5 Estado Desabilitado / Bloqueado *(se aplicavel)*
- Para o **Aluno**, o **FAB fica oculto** (nao cria avaliacoes); nos cards, nunca aparecem "Editar"/"Excluir" — apenas "Visualizar" e, se aplicavel, "Preencher".
- Avaliacao ja **Concluida** nao exibe "Preencher" para o Aluno (apos enviar, trava para ele).
- Avaliacao **Expirada** nao exibe "Preencher" para o Aluno — ele so volta a poder preencher se o profissional reabrir/reativar (novo prazo).

---

## 7. Fluxo de Navegacao

### De onde o usuario chega nesta tela
| Origem | Gatilho |
|---|---|
| Tab Bar (aba Avaliacoes/Evolucao) | Toca na aba (com badge de pendencias para o Aluno) |
| Notificacao (push/in-app) | Aluno toca no aviso "avaliacao para preencher" → abre a lista (ou direto o preenchimento) |
| Perfil do Aluno | Atalho/card "Avaliacoes" |
| Perfil do Aluno aberto pelo Treinador | Treinador acessa a area de avaliacoes do Aluno vinculado |

### Para onde o usuario pode ir desta tela
| Destino | Gatilho |
|---|---|
| Cadastro/Edicao de Avaliacao `[VELA-2003]` (criacao) | Treinador toca no FAB "Nova avaliacao" e escolhe o tipo |
| Cadastro/Edicao de Avaliacao `[VELA-2003]` (edicao) | Treinador toca em "Editar" em um card |
| Cadastro/Edicao de Avaliacao `[VELA-2003]` (preenchimento) | Aluno toca em "Preencher"/"Continuar" em um card Solicitada ou Em andamento (iniciada por ele) |
| Visualizar Avaliacao `[VELA-2002]` | Qualquer um toca em "Visualizar" em um card |

---

## 8. Regras de Negocio
> Regras especificas que impactam o comportamento desta tela.

- **RN01:** A lista reune **todos os tipos** de avaliacao em uma **unica visao, sem secoes separadas**. Ordenacao: **pendentes do Aluno primeiro** (topo) e os **demais por data decrescente** (mais recente primeiro). Ver RN12.
- **RN02:** A distincao visual de **tipo** e de **status** vem do **icone colorido** (uma cor por tipo e uma por status); o **card permanece neutro** — nenhuma cor tinge o fundo/borda do card. O card e **fino/compacto**.
- **RN03:** Ha **tres filtros**, cada um como **botao que abre um painel/bottom sheet**: **Periodo** (presets Este mes / Este ano / Tudo + Personalizado), **Status** (multiselecao) e **Tipo** (multiselecao). A tela **inicia sem filtro aplicado** (Tudo / todos os status / todos os tipos); a lista so e refiltrada **apos confirmar** a selecao no painel. Os tres sao combinaveis (E logico). Os filtros afetam a lista inteira (inclusive os pendentes do topo).
- **RN04 (Papel do Treinador):** Somente o **Treinador** pode **criar**, **editar/revisar** e **excluir** avaliacoes do Aluno vinculado. Ele tambem pode **liberar/solicitar** uma avaliacao para o Aluno preencher. A acao de alterar chama-se **"Editar"** em **Solicitada/Em andamento** e **"Revisar"** em **Concluida** (edita no lugar, continua Concluida); como alternativa para a Concluida, ele pode **excluir e recriar** (ver RN06).
- **RN05 (Papel do Aluno):** O **Aluno nao cria, nao edita e nao exclui** avaliacoes. Ele pode **visualizar** qualquer avaliacao e **preencher** uma avaliacao liberada a ele enquanto estiver com status **Solicitada** ou **Em andamento** (preenchimento iniciado por ele). Avaliacoes **Concluidas** ou **Expiradas** nao podem ser preenchidas pelo Aluno.
- **RN06 (Trava apos conclusao):** Uma avaliacao **Concluida** fica **travada para o Aluno** — ele nunca a altera. O **Treinador** pode corrigi-la por **"Revisar"** (edita no lugar, continua Concluida, **sem versionamento**) ou por **excluir + recriar** (definitivo); ambas as formas ficam disponiveis. Enquanto **Solicitada** ou **Em andamento**, a alteracao do Treinador chama-se **"Editar"**.
- **RN07 (Status):** Toda avaliacao tem um **status**, exibido no card, que governa as acoes disponiveis:
  - **Solicitada** — liberada pelo profissional, aguardando inicio do preenchimento.
  - **Em andamento** — preenchimento iniciado e ainda **nao** finalizado/enviado. Ocorre quando **o profissional comecou a preencher** (rascunho dele) **ou** quando **o Aluno comecou a preencher** uma Solicitada e ainda nao enviou. **O Aluno enxerga o card nos dois casos**, mas so **continua o preenchimento** quando foi **ele** quem iniciou; rascunho do profissional o Aluno apenas visualiza.
  - **Concluida** — preenchida e enviada/finalizada.
  - **Expirada** — passou do **prazo** definido pelo profissional sem ser concluida (ver RN13).
- **RN08 (Exclusao):** A exclusao e **exclusiva do profissional/Treinador** — o **Aluno nunca exclui** (nem as proprias avaliacoes preenchidas). Exige **modal de confirmacao** e e **definitiva** — o app **nao tem lixeira** nem "desfazer".
- **RN09 (Acoes por papel/status):** O FAB e os botoes "Editar"/"Revisar"/"Excluir" aparecem **somente para o Treinador**; o botao de alterar e rotulado **"Editar"** em **Solicitada/Em andamento** e **"Revisar"** em **Concluida** (RN06) — em ambos os casos leva ao formulario `[VELA-2003]`; "Excluir" (menu ⋮) aparece para o Treinador em qualquer status. "Preencher"/"Continuar" aparece **somente para o Aluno** em cards **Solicitada** ou **Em andamento** liberados a ele; "Visualizar" esta sempre disponivel para ambos.
- **RN10 (Conteudo enxuto do card):** O card exibe **somente**: **tipo** (icone + rotulo), **data**, **@ do profissional** (quem fez) e **status** (icone colorido + rotulo). **Nao** exibe resumo/metricas (peso, % G, etc.) nem texto de prazo — esses dados aparecem apenas ao abrir **Visualizar** `[VELA-2002]` ou **Preencher** `[VELA-2003]`.
- **RN11 (Notificacoes por mudanca de status):** O Aluno e **notificado** (push + in-app) nas mudancas de status da avaliacao: **Solicitada** (liberada/reaberta para ele), **Em andamento** (apenas quando **o profissional** inicia o rascunho — quando o **proprio Aluno** comeca a preencher **nao** ha notificacao, pois e acao dele), **Concluida** (preenchida/enviada) e **Expirada** (prazo vencido pela rotina automatica — RN13). Ao tocar na notificacao de uma avaliacao pendente, o Aluno e levado a esta lista `[VELA-2001]` (ou direto ao preenchimento `[VELA-2003]` da avaliacao). *(Preferencias de push respeitam a tela de Notificacoes.)*
- **RN12 (Pendencias no topo — Aluno):** Avaliacoes pendentes do Aluno (**Solicitadas** + **Em andamento** iniciadas por ele) aparecem **primeiro na lista** (topo), antes das demais (ordenadas por data). **Nao** ha bloco/banner separado — o realce vem da posicao e do icone de status. Os filtros afetam a lista (inclusive os pendentes). Independentemente do filtro, essas pendencias contam para o **badge** da aba; saem do topo e do contador quando ficam **Concluidas** ou **Expiradas**.
- **RN13 (Prazo e expiracao):** Ao liberar/solicitar uma avaliacao, o profissional pode definir um **prazo (data limite)** de preenchimento — campo **opcional**. No vencimento, uma **rotina no backend** expira **automaticamente** apenas as avaliacoes que ainda estao **Solicitada** (nao iniciadas pelo Aluno): o status vira **Expirada**, o Aluno **perde a acao de preencher** e o item sai das pendencias. Uma avaliacao que o Aluno **ja comecou a preencher** (status **Em andamento** iniciado por ele) **nao expira** — fica **protegida** ate ele concluir, para nao perder o que foi preenchido. Sem prazo definido, a avaliacao **nunca expira**.
- **RN14 (Reabrir avaliacao expirada):** Uma avaliacao **Expirada** so volta a ser preenchivel pelo Aluno se o **profissional/Treinador a reabrir/reativar** (definindo novo prazo, se desejar), retornando ao status **Solicitada**. O Aluno nao reabre por conta propria. A reabertura volta ao status Solicitada e dispara a notificacao correspondente (RN11), e a avaliacao volta a aparecer entre os pendentes (topo) e no badge.

---

## 9. Responsividade (Mobile vs Web)
> Diferencas de comportamento ou layout entre plataformas.

| Aspecto | Mobile | Web |
|---|---|---|
| Lista | Cards finos empilhados, largura total | Cards finos em coluna centralizada (largura maxima) |
| Acao de excluir | Menu ⋮ → Excluir | Menu ⋮ → Excluir (identico; sem swipe) |
| FAB | Botao flutuante inferior direito | Botao "Nova avaliacao" no topo/area de acoes |
| Filtros | 3 botoes (Periodo/Status/Tipo) que abrem bottom sheet | 3 botoes que abrem popover/painel |

> Regras e permissoes sao **identicas** nas duas plataformas; variam apenas o layout e o posicionamento das acoes.

---

## 10. Acessibilidade
> Consideracoes de acessibilidade para esta tela.

- A distincao de tipo **nao** depende apenas de cor: cada card tem **icone + rotulo de texto** do tipo.
- Labels acessiveis em botoes de card ("Editar avaliacao antropometrica de 12/03/2026", "Visualizar...", "Mais acoes").
- Contraste conforme WCAG 2.1 AA (atencao ao verde-limao neon sobre fundos claros — usar texto/contornos de apoio).
- Modal de confirmacao de exclusao com foco gerenciado e acoes claras ("Excluir" / "Cancelar").
- Area de toque adequada para botoes do card e menu ⋮ no mobile; navegacao por teclado (tab order logica) no web.
- Toasts de sucesso/erro anunciados por leitores de tela.

---

## 11. Historico de Alteracoes

| Data | Autor | Descricao |
|---|---|---|
| 2026-06-09 | Equipe Vela | Criacao inicial: lista unificada de avaliacoes (todos os tipos), ordenacao por data, cards distintos por tipo, filtro por periodo/tipo, editar/visualizar no card e exclusao via menu ⋮ |
| 2026-06-09 | Equipe Vela | Modelo de permissoes revisado: criar/editar/excluir/liberar = somente Treinador; Aluno apenas visualiza e preenche avaliacoes Solicitadas liberadas a ele (trava apos enviar). Adicionados status (Solicitada/Concluida), botao "Preencher" e exclusao definitiva sem lixeira. Removida nomenclatura membro/professor |
| 2026-06-09 | Equipe Vela | Ao liberar, o Aluno recebe notificacao (push + in-app); avaliacoes Solicitadas aparecem em destaque fixo no topo ("Para preencher (N)", Secao 1) e geram badge na aba. Renumeradas secoes (Destaque/Filtro/Lista), RN11 (notificacao) e RN12 (destaque/badge) e origem por notificacao |
| 2026-06-10 | Equipe Vela | Modelo de status ampliado de 2 para 4: adicionados **Em andamento** (preenchimento iniciado e nao enviado, por profissional ou Aluno) e **Expirada** (prazo vencido sem conclusao). Card passa a exibir **@ do profissional** que aplicou/solicitou. Adicionados RN13 (prazo opcional + expiracao automatica) e RN14 (reabrir expirada = so profissional). Reforcado em RN05/RN08 que o **Aluno nunca exclui**. Atualizados badge/destaque (RN12), botao "Preencher/Continuar" (RN09) e estados da Secao 6 |
| 2026-06-10 | Equipe Vela | Definidas pendencias decorrentes dos novos status: expiracao e **automatica via backend** no vencimento; o Aluno e **notificado a cada mudanca de status** (Solicitada, Em andamento, Expirada, Concluida) — RN13/RN13.1; **reabrir** dispara nova notificacao (RN14); rascunho **Em andamento do profissional fica visivel** ao Aluno (somente leitura, sem Continuar) — RN07/Secao 3.2; adicionado **filtro por status** (Secao 2, campo 5, RN03) |
| 2026-06-10 | Equipe Vela | Revisao final: propagado o modelo de 4 status para todos os pontos antes desatualizados (permissoes da Secao 2, bloco "Para preencher", botoes do card, navegacao). Definido que o **bloco de pendencias respeita os filtros** e a **tela inicia sem filtro** (Tudo/Todos/Todas) — Secao 1/2, RN03/RN12. **Notificacoes consolidadas** numa unica RN11 (4 momentos + deep-link); removida a RN13.1 redundante. Tela marcada como CONCLUIDO |
| 2026-06-10 | Equipe Vela | Casos de borda definidos: (1) avaliacao **Em andamento iniciada pelo Aluno nao expira** — fica protegida ate concluir; so **Solicitada** (nao iniciada) expira no prazo (RN13, Secao 6.4); (2) notificacao de **Em andamento** sai **apenas quando o profissional** inicia o rascunho, nunca quando o proprio Aluno comeca a preencher (RN11) |
| 2026-06-10 | Equipe Vela | Refinamento de UI/UX pos-mockup: (1) **lista unica** sem secoes — removido o bloco destacado "Para preencher"; pendentes apenas vao para o **topo** + badge mantido (RN01/RN12); (2) **filtros** viram **3 botoes** (Periodo/Status/Tipo) que abrem painel — Tipo mantido (RN03, Secao 4); (3) **card enxuto e fino**: so **tipo, data, quem fez e status** — removidos resumo/metricas e prazo do card (RN10); (4) **tipo e status por icone colorido**, **card neutro** (nenhuma cor tinge o card) — RN02 |
| 2026-06-12 | Equipe Vela | (decisao #14 — opcao A) **Avaliacao Concluida e imutavel para todos**: nem o Treinador edita; correcao apenas via **excluir + recriar**. Botao "Editar" deixa de aparecer em cards Concluidos. Atualizadas RN04, RN06, RN09, Secao 3.2 e botao "Editar" da Secao 5 |
| 2026-06-12 | Equipe Vela | Ajuste da decisao #14: **Treinador ganha a acao "Revisar"** em cards **Concluida** (edita no lugar, continua Concluida, **sem versionamento**); **excluir + recriar** segue disponivel. O **Aluno continua travado** na Concluida. Botao do card passa a ser **"Editar" (Solicitada/Em andamento)** ou **"Revisar" (Concluida)**. Atualizadas RN04, RN06, RN09, Secao 3.2 e botao da Secao 5 |

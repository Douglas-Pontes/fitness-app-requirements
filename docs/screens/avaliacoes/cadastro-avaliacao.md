# Tela: Cadastro / Edicao de Avaliacao `[VELA-2003]`

---

## Metadados
| Campo | Valor |
|---|---|
| **Nome da tela** | Cadastro / Edicao de Avaliacao |
| **Modulo** | Avaliações |
| **Codigo** | VELA-2003 |
| **Prioridade** | 🔵 MVP |
| **Status** | 🟢 CONCLUIDO |
| **Ultima atualizacao** | 2026-06-24 |

---

## 1. Objetivo da Tela
> O que o usuario consegue fazer nesta tela? Qual problema ela resolve?

Formulario **unico e dinamico** para **criar/editar** (Treinador) ou **preencher** (Aluno) uma avaliacao. O **mesmo** formulario serve aos tres modos: em **Editar** abre com os campos **ja preenchidos**; em **Preencher** o Aluno completa uma avaliacao que o Treinador **liberou** (status Solicitada). O conjunto de campos exibido **muda conforme o tipo** (Anamnese, Antropometrica, Dobras Cutaneas, Bioimpedancia). Para os campos numericos de medida, exibe **abaixo de cada campo a ultima medicao registrada** daquele mesmo campo — **somente o valor**, no formato `Ultima: XXXXX` (sem data nem variacao).

**Modos da tela:**
- **Criar (Treinador):** novo registro. O Treinador pode **salvar rascunho** (status **Em andamento**, retoma depois), **concluir** (salva como **Concluida**) ou **liberar para o Aluno preencher** (salva como **Solicitada**, em branco/parcial, opcionalmente com **prazo**).
- **Editar / Revisar (Treinador):** altera uma avaliacao existente. Em **Solicitada** ou **Em andamento**, a acao chama-se **"Editar"**. Em **Concluida**, a acao chama-se **"Revisar"**: abre a avaliacao preenchida, o Treinador corrige e salva **no lugar** — a avaliacao **continua Concluida** (sobrescreve os valores, **sem** versionamento/historico). Como alternativa, o Treinador tambem pode **excluir e recriar** (ver RN13). O **Aluno nunca edita/revisa** uma Concluida.
- **Preencher (Aluno):** o Aluno completa uma avaliacao **Solicitada** liberada a ele. Pode **salvar rascunho** (status **Em andamento**, retoma depois pelo botao "Continuar" na lista) ou **enviar**. Ao **enviar**, ela vira **Concluida** e **trava para o Aluno** (so o Treinador edita depois).

**Status possiveis:** **Solicitada** (liberada, ainda nao iniciada) · **Em andamento** (rascunho salvo, nao enviado) · **Concluida** (enviada/salva final) · **Expirada** (prazo de preenchimento vencido sem envio).

> **Decisao de arquitetura:** em vez de um documento por tipo (4 telas quase identicas), modela-se **uma tela dinamica** que renderiza o conjunto de campos do tipo selecionado. As Secoes 4.A a 4.D detalham os campos de cada tipo.

---

## 2. Quem Acessa / Pre-condicoes
> Quem pode ver esta tela? Quais condicoes precisam ser verdadeiras?

- **Usuario:**
  - **Treinador** — cria, edita e libera avaliacoes para o Aluno vinculado.
  - **Aluno** — acessa **apenas** no modo **Preencher**, e somente para avaliacoes **Solicitadas** liberadas a ele. Nao acessa criacao/edicao.
- **Pre-condicoes:**
  - Usuario autenticado.
  - **Criar/Editar:** ser **Treinador** do Aluno; na criacao, ter escolhido um **tipo**.
  - **Preencher:** ser o **Aluno** destinatario e a avaliacao estar com status **Solicitada** (ainda nao enviada).
- **Permissoes especiais:** Avaliacao **Concluida e travada para o Aluno** (ele nunca edita/revisa). O **Treinador** pode **Revisar** (editar no lugar, continua Concluida) ou **excluir e recriar**. Edicao em modo "Editar" vale para **Solicitada/Em andamento**; em modo "Revisar", para **Concluida** (ver `[VELA-2001]` RN04–RN08 e RN13).

---

## 3. Layout e Componentes Visuais
> Descreva a estrutura visual da tela de cima para baixo.

### 3.1 Header / Cabecalho
- Conteudo: Botao voltar/fechar (X) + Titulo dinamico conforme o modo: **"Nova [Tipo]"** (criar), **"Editar [Tipo]"** (editar Solicitada/Em andamento), **"Revisar [Tipo]"** (Treinador corrigindo uma Concluida) ou **"Preencher [Tipo]"** (Aluno preenchendo) — ex: "Nova Antropometrica", "Revisar Dobras Cutaneas", "Preencher Anamnese". As acoes ficam no **rodape** (nao no header). A **acao primaria** depende do modo/escolha: **Treinador preenchendo → "Concluir"**; **Treinador liberando (quem preenche = Aluno) → "Liberar para o aluno preencher"** (status **Solicitada**); **Aluno preenchendo → "Enviar"**. Acao secundaria **"Salvar rascunho"** (status **Em andamento**) disponivel quando o preenchimento ainda nao foi finalizado. Para diferenciar: primaria com destaque (verde-limao neon), secundaria como contorno/ghost.
- Comportamento: Fixo no topo. Acao primaria desabilitada ate o formulario estar valido. Ao tocar voltar/X com alteracoes nao salvas, exibir alerta "Descartar alteracoes?".

### 3.2 Corpo Principal
> Descrever secoes da tela, na ordem que aparecem

**Secao 0 — Inicio / cabecalho da avaliacao**
- Componente: Bloco no topo do formulario.
- **Conteudo na CRIACAO (Treinador), nesta ordem:**
  1. **Aluno** — **1º campo**. Quando o formulario e aberto **pelo perfil do aluno** (via `[VELA-2001]`): vem **pre-preenchido e travado** (somente leitura — nome + @), e o treinador so segue para o prazo. Quando aberto pela tela **"Criar avaliacao"** (global, sem aluno no contexto): e um **campo de busca** — o treinador **digita o nome**, o app **busca entre os alunos cadastrados/vinculados** e exibe sugestoes (nome + @); ao **selecionar**, fixa o aluno e traz o **@**.
  2. **Tipo** — somente leitura (definido na criacao).
  3. **Quem vai preencher esta avaliacao** — seletor **Treinador** ou **Aluno**. Se **Aluno**, aparece **"Vai ter prazo para preencher?"** (Sim / Nao); se **Sim**, exibe o campo **Prazo (data limite)**.
  4. **Data da avaliacao** — editavel; nao pode ser futura.
- **Conteudo em EDITAR / REVISAR / PREENCHER / CONTINUAR:** apenas **Tipo** + **Data** — os campos de configuracao (aluno, quem preenche, prazo) **nao** sao reapresentados (ja foram definidos na criacao), e **status / autor / prazo** permanecem na lista `[VELA-2001]`, sem repetir aqui (RN15).
- Comportamento: O tipo nao muda apos a criacao. A escolha **"quem vai preencher"** define a **acao primaria** do rodape: **Treinador → "Concluir"**; **Aluno → "Liberar para o aluno preencher"** (status **Solicitada**, com o prazo definido aqui). No modo **Preencher**, o Aluno nao altera esses campos — apenas completa as medidas.

**Secao 1..N — Campos do tipo selecionado**
- Componente: Formulario seccionado (grupos colapsaveis para tipos longos, ex: Antropometrica com varios perimetros).
- Conteudo: Os campos especificos do tipo (ver Secoes 4.A–4.D).
- Comportamento: **Abaixo de cada campo numerico — inclusive os calculados** (IMC, soma de dobras, % de gordura) — exibir o componente **"Ultima medicao"** (ver Secao 4 — Regra global da "ultima medicao"). Os campos calculados sao **somente leitura** e atualizam em tempo real, mas tambem mostram a sua "ultima".

**Secao Fotos (quando aplicavel ao tipo)**
- Componente: Galeria de upload (camera/galeria).
- Conteudo: Slots de foto rotulados por angulo (ex: Frente, Costas, Perfil direito, Perfil esquerdo). Para Bioimpedancia, anexo do **laudo** (foto/arquivo) e opcional.
- Comportamento: Miniaturas com opcao de remover/substituir. Fotos sao opcionais (salvo indicacao em contrario).

**Secao Observacoes (comum)**
- Campo de texto livre para anotacoes da avaliacao.

### 3.3 Footer / Rodape
- Conteudo: Botao primario **"Concluir"** (Treinador) / **"Enviar"** (Aluno), largura total — alternativa a acao primaria do header em telas mobile longas. Botao secundario **"Salvar rascunho"** ao lado/acima.
- Comportamento: Fixo na parte inferior; desabilitado enquanto o formulario for invalido; mostra spinner durante o salvamento.

---

## 4. Campos e Formularios

### Regra global — Componente "Ultima medicao" (sob cada campo)
A "ultima medicao" considera **apenas avaliacoes do mesmo tipo**: o Peso de uma **Antropometrica** compara com a ultima **Antropometrica**, o % de gordura de uma **Bioimpedancia** com a ultima **Bioimpedancia**, e assim por diante — **nao** mistura tipos diferentes, mesmo quando o campo (ex: Peso, % de gordura) existe em mais de um tipo.

Aparece em **TODOS os campos numericos — inclusive os calculados** (IMC, soma de dobras, % de gordura, densidade, massa gorda/magra). Exibir logo abaixo do input **apenas o valor**, no formato fixo:
- **`Ultima: XXXXX`** — o ultimo valor registrado daquele mesmo campo (com a unidade). **Sem data e sem variacao/delta** — somente o valor. *Qualquer informacao alem disso (data, ▲/▼, %) nao aparece na tela.*
- Exemplo: campo "Braco direito contraido" → abaixo: *"Ultima: 38,5 cm"*.
- Se nao houver registro anterior para aquele campo: exibir *"Sem dados anterior"*.
- Em **modo edicao/revisao/preenchimento**, a "ultima medicao" considera a avaliacao **anterior** a atual (nao a propria).
- Campos **nao numericos** (selects/textos da **Anamnese**) **nao** exibem resposta anterior no formulario — a Anamnese e questionario de entrada (e o PAR-Q deve ser respondido do zero, sem induzir). A comparacao historica da Anamnese, quando util, fica na Visualizar `[VELA-2002]` / evolucao.

### Regras de Preenchimento (gerais)
- **Aluno (criacao):** obrigatorio. Na entrada global, so aceita um aluno **selecionado da busca** (entre os cadastrados/vinculados) — texto livre sem selecao nao e valido. Aberto pelo perfil, vem travado.
- **Prazo:** so existe quando "quem vai preencher = Aluno" e "Vai ter prazo? = Sim"; quando presente, deve ser uma data **futura** (a partir de hoje).
- **Data da avaliacao:** obrigatoria; nao pode ser futura.
- Campos numericos aceitam **decimais com virgula** (ex: 84,5) e unidade fixa exibida (cm, kg, mm, %, kcal).
- Campos **calculados** (IMC, RCQ, soma de dobras) sao preenchidos automaticamente e **nao** sao editaveis. Densidade, % de gordura e massa gorda/magra (Dobras/Bioimpedancia) sao **digitados manualmente**.
- **Peso / Altura / Idade (RN12):** **nao** ha rotulo "Sugerido" separado. Como qualquer outro campo, exibem o apoio padrao **`Ultima: XXXXX`** (ultima avaliacao do mesmo tipo) ou **"Sem dados anterior"** (RN03). O input **nao** e preenchido automaticamente — o usuario **digita/confirma** o valor desta avaliacao.
- Validacao de faixa plausivel por campo (ex: peso 20–300 kg; perimetros 0–200 cm; dobras 1–80 mm; % de gordura 1–70%) com **aviso suave** quando fora da faixa. O aviso **nao bloqueia** o salvamento — apenas chama a atencao; o avaliador pode confirmar e salvar um valor fora da faixa (caso real/raro). O bloqueio de salvar fica restrito aos campos **obrigatorios** e a **Data** (nao futura).
- A acao primaria (**"Concluir"** / **"Enviar"**) so habilita com a **Data** preenchida e ao menos um campo de medida do tipo informado (Anamnese: obrigatorios o PAR-Q completo + Objetivo principal). **"Salvar rascunho"** nao exige validacao completa.

---

### 4.A — Campos: ANAMNESE
> Questionario inicial de saude, objetivos e prontidao para atividade fisica. **Sem** "ultima medicao" / "Anterior" no formulario — campos qualitativos sao respondidos do zero (ver Regra global da Secao 4). A comparacao com respostas anteriores, se util, fica na Visualizar `[VELA-2002]`.

**Grupo 1 — Objetivo e perfil de treino**
| # | Nome do Campo | Tipo | Obrigatorio | Observacao |
|---|---|---|---|---|
| 1 | Objetivo principal | Select | Sim | Hipertrofia / Emagrecimento / Saude e qualidade de vida / Condicionamento / Performance esportiva / Reabilitacao |
| 2 | Trilha | Select | Sim | `.track` (fisico/estetica/consistencia) ou `.performance` (atleta/esporte) — alinhado a marca Vela |
| 3 | Modalidade/esporte (se `.performance`) | Text | Condicional | Visivel quando Trilha = `.performance` |
| 4 | Nivel de experiencia | Select | Sim | Iniciante / Intermediario / Avancado |
| 5 | Frequencia semanal pretendida | Number (dias) | Sim | 1 a 7 |
| 6 | Historico de treino | Textarea | Nao | Tempo de pratica, pausas, experiencias |
| 7 | Pratica outra atividade fisica? | Boolean + Text | Nao | Se sim, quais |

**Grupo 2 — PAR-Q (Prontidao para atividade fisica)** — respostas Sim/Nao
| # | Pergunta | Tipo | Obrigatorio |
|---|---|---|---|
| 8 | Algum medico ja disse que voce possui um problema cardiaco e que so deveria praticar atividade fisica sob supervisao medica? | Sim/Nao | Sim |
| 9 | Voce sente dor no peito quando pratica atividade fisica? | Sim/Nao | Sim |
| 10 | No ultimo mes, voce sentiu dor no peito em repouso? | Sim/Nao | Sim |
| 11 | Voce perde o equilibrio por tontura ou ja perdeu a consciencia? | Sim/Nao | Sim |
| 12 | Voce tem algum problema osseo ou articular que poderia ser agravado pela atividade fisica? | Sim/Nao | Sim |
| 13 | Toma atualmente medicamento para pressao arterial ou problema cardiaco? | Sim/Nao | Sim |
| 14 | Conhece alguma outra razao pela qual nao deveria praticar atividade fisica? | Sim/Nao | Sim |

> RN: se **qualquer** resposta do PAR-Q for "Sim", exibir alerta recomendando avaliacao/liberacao medica antes de iniciar (ver RN08).

**Grupo 3 — Historico de saude**
| # | Nome do Campo | Tipo | Obrigatorio | Observacao |
|---|---|---|---|---|
| 15 | Doencas/condicoes pre-existentes | Multiselect | Nao | Hipertensao, Diabetes, Colesterol alto, Cardiopatia, Problema respiratorio/asma, Problema articular, Outros |
| 16 | Cirurgias (quais e quando) | Textarea | Nao | — |
| 17 | Lesoes (atuais/anteriores) | Textarea | Nao | Regiao e situacao |
| 18 | Medicamentos em uso | Textarea | Nao | — |
| 19 | Uso de suplementos | Textarea | Nao | — |
| 20 | Fumante? | Select | Nao | Nao / Sim / Ex-fumante |
| 21 | Consumo de alcool | Select | Nao | Nunca / Ocasional / Frequente |

**Grupo 4 — Estilo de vida**
| # | Nome do Campo | Tipo | Obrigatorio | Observacao |
|---|---|---|---|---|
| 22 | Qualidade/horas de sono | Number + Select | Nao | Horas por noite + qualidade percebida |
| 23 | Nivel de estresse | Select | Nao | Baixo / Medio / Alto |
| 24 | Alimentacao (refeicoes/dia + observacoes) | Number + Textarea | Nao | — |
| 25 | Hidratacao (litros/dia) | Number | Nao | — |
| 26 | Profissao / nivel de atividade no trabalho | Text + Select | Nao | Sedentario / Moderado / Ativo |
| 27 | Observacoes gerais | Textarea | Nao | — |

---

### 4.B — Campos: ANTROPOMETRICA (Perimetria)
> Peso, altura e perimetros corporais (circunferencias). **Todos os campos numericos exibem "ultima medicao".** Lado direito e esquerdo medidos separadamente.

**Grupo 1 — Basicos**
| # | Nome do Campo | Tipo | Unidade | Obrigatorio | Observacao |
|---|---|---|---|---|---|
| 1 | Peso | Number | kg | Sim | — |
| 2 | Altura | Number | cm | Sim (pode herdar do perfil) | — |
| 3 | IMC | Calculado | kg/m² | Auto | peso / altura² |

**Grupo 2 — Perimetros (circunferencias)** — unidade cm, cada um com "ultima medicao"
| # | Nome do Campo | Obrigatorio |
|---|---|---|
| 4 | Pescoco | Nao |
| 5 | Ombro | Nao |
| 6 | Torax / Peito | Nao |
| 7 | Cintura | Nao |
| 8 | Abdomen | Nao |
| 9 | Quadril | Nao |
| 10 | Braco direito relaxado | Nao |
| 11 | Braco direito contraido | Nao |
| 12 | Braco esquerdo relaxado | Nao |
| 13 | Braco esquerdo contraido | Nao |
| 14 | Antebraco direito | Nao |
| 15 | Antebraco esquerdo | Nao |
| 16 | Coxa proximal direita | Nao |
| 17 | Coxa media direita | Nao |
| 18 | Coxa distal direita | Nao |
| 19 | Coxa proximal esquerda | Nao |
| 20 | Coxa media esquerda | Nao |
| 21 | Coxa distal esquerda | Nao |
| 22 | Panturrilha direita | Nao |
| 23 | Panturrilha esquerda | Nao |

**Grupo 3 — Derivados e registro**
| # | Nome do Campo | Tipo | Observacao |
|---|---|---|---|
| 24 | Relacao Cintura/Quadril (RCQ) | Calculado | cintura / quadril |
| 25 | Fotos | Upload | Frente, Costas, Perfil direito, Perfil esquerdo (opcional) |
| 26 | Observacoes | Textarea | — |

---

### 4.C — Campos: DOBRAS CUTANEAS
> Estimativa de composicao corporal por adipometro. A tela exibe **todas as dobras possiveis** (9 pontos), **todas opcionais**; cada dobra em **mm** com "ultima medicao". **Sem seletor de protocolo:** o app **nao** calcula a composicao corporal automaticamente — apenas a **Soma das dobras** e automatica; **densidade, % de gordura, massa gorda e massa magra** sao **campos manuais e opcionais**, preenchidos pelo Treinador (ele calcula por fora ou registra de outra fonte). Ver RN09.

**Grupo 1 — Dobras (mm)** — todas opcionais; cada uma com "ultima medicao"
| # | Nome do Campo | Obrigatorio |
|---|---|---|
| 1 | Tricipital | Nao |
| 2 | Bicipital | Nao |
| 3 | Subescapular | Nao |
| 4 | Peitoral | Nao |
| 5 | Axilar Media | Nao |
| 6 | Suprailiaca | Nao |
| 7 | Abdominal | Nao |
| 8 | Coxa | Nao |
| 9 | Panturrilha | Nao |

**Grupo 2 — Resultados e registro**
| # | Nome do Campo | Tipo | Obrigatorio | Observacao |
|---|---|---|---|---|
| 10 | Soma das dobras | Calculado | Auto | Soma (mm) das dobras preenchidas — somente leitura, atualiza em tempo real |
| 11 | Densidade corporal | Number | Nao | **Manual** — opcional |
| 12 | % de gordura | Number (%) | Nao | **Manual** — opcional |
| 13 | Massa gorda | Number (kg) | Nao | **Manual** — opcional |
| 14 | Massa magra | Number (kg) | Nao | **Manual** — opcional |
| 15 | Peso | Number (kg) | Nao | Pode herdar da ultima antropometrica |
| 16 | Observacoes | Textarea | Nao | — |

---

### 4.D — Campos: BIOIMPEDANCIA
> Resultado de balanca/aparelho de bioimpedancia. Campos numericos com "ultima medicao". Pode-se anexar o laudo.

**Grupo 1 — Origem**
| # | Nome do Campo | Tipo | Obrigatorio | Observacao |
|---|---|---|---|---|
| 1 | Aparelho / Modelo | Text | Nao | Ex: marca/modelo da balanca |

**Grupo 2 — Composicao corporal** — cada um com "ultima medicao"
| # | Nome do Campo | Tipo | Unidade | Obrigatorio |
|---|---|---|---|---|
| 2 | Peso | Number | kg | Sim |
| 3 | % de gordura corporal | Number | % | Sim |
| 4 | Massa gorda | Number | kg | Nao |
| 5 | Massa magra (massa livre de gordura) | Number | kg | Nao |
| 6 | Massa muscular esqueletica | Number | kg | Nao |
| 7 | Agua corporal total | Number | % (e/ou L) | Nao |
| 8 | Gordura visceral | Number | nivel/indice | Nao |
| 9 | Taxa metabolica basal (TMB) | Number | kcal | Nao |
| 10 | Idade metabolica | Number | anos | Nao |
| 11 | Massa ossea | Number | kg | Nao |
| 12 | Proteina | Number | % | Nao |
| 13 | Angulo de fase | Number | graus (°) | Nao |

**Grupo 3 — Derivados e registro**
| # | Nome do Campo | Tipo | Observacao |
|---|---|---|---|
| 14 | IMC | Calculado | a partir de peso/altura do perfil |
| 15 | Laudo (anexo) | Upload | Foto/arquivo do resultado (opcional) |
| 16 | Observacoes | Textarea | — |

---

## 5. Botoes e Acoes

| # | Componente | Label / Icone | Posicao | Visivel para | Acao ao Clicar |
|---|---|---|---|---|---|
| 1 | Campo (Secao 0, criar) | "Aluno" (busca) | Topo do formulario | Treinador | Travado (nome + @) quando aberto pelo perfil do aluno; **campo de busca** entre alunos cadastrados quando aberto pela tela global "Criar avaliacao" — ao selecionar, fixa o aluno e traz o **@** |
| 2 | Campo (Secao 0, criar) | "Quem vai preencher" (Treinador / Aluno) | Topo do formulario | Treinador | Define a acao primaria do rodape. Se **Aluno**, revela "Vai ter prazo?" (Sim/Nao) e, se Sim, o campo **Prazo (data limite)** |
| 3 | Botao primario | "Concluir" | Footer | Treinador, quando **quem preenche = Treinador** (criar/editar/revisar) | Valida → salva como **Concluida** → retorna para `[VELA-2001]` com toast |
| 4 | Botao primario | "Liberar para o aluno preencher" | Footer | Treinador, quando **quem preenche = Aluno** (modo criar) | Salva como **Solicitada** (em branco/parcial), com o **prazo** definido na Secao 0 → **dispara notificacao push + in-app** ao Aluno e coloca a avaliacao no **topo** da lista → retorna para `[VELA-2001]` |
| 5 | Botao secundario | "Salvar rascunho" | Footer | Treinador e Aluno (preenchimento incompleto) | Salva o que houver **sem validacao final** → status vira **Em andamento** → retorna para `[VELA-2001]` (card mostra "Continuar") |
| 6 | Botao primario | "Enviar" | Footer | Aluno (modo preencher) | Valida → envia → status vira **Concluida** e **trava para o Aluno** → retorna para `[VELA-2001]` |
| 7 | Botao/Icone | Voltar / Fechar (X) | Header (esquerda) | Ambos | Se houver alteracoes nao salvas, abre alerta "Descartar alteracoes?"; senao volta |
| 8 | Botao | Adicionar/remover foto | Secao Fotos | Conforme modo | Abre camera/galeria; gerencia miniaturas |
| 9 | Toggle de grupo | Expandir/colapsar secao | Cabecalho de cada grupo | Ambos | Mostra/oculta o grupo de campos |

> **Excluir** nao fica nesta tela — a exclusao e exclusiva do **Treinador** e acontece na lista `[VELA-2001]` ou na visualizacao `[VELA-2002]` (menu ⋮), sempre definitiva e com confirmacao.

---

## 6. Estados da Tela

### 6.1 Estado Inicial / Vazio
- **Criacao (Treinador):** primeiro a **Secao 0** — **Aluno** (travado se aberto pelo perfil; busca se entrada global), **Tipo** (leitura), **Quem vai preencher** (Treinador/Aluno; se Aluno, "Vai ter prazo?" → data) e **Data**. Em seguida, os campos do tipo escolhido vazios; cada campo numerico (inclusive calculados) mostra "Ultima: XXXXX" (ou "Sem dados anterior"). A acao primaria do rodape reflete a escolha de "quem preenche" ("Concluir" ou "Liberar para o aluno preencher").
- **Edicao (Treinador):** campos **pre-preenchidos** com os valores da avaliacao; "Ultima medicao" referente a avaliacao **anterior**.
- **Preencher (Aluno):** formulario do tipo da avaliacao Solicitada, com eventuais campos ja pre-preenchidos pelo Treinador; o Aluno completa o restante. O Aluno pode **editar livremente** todos os campos, **inclusive os que o Treinador pre-preencheu** (nenhum campo fica travado no modo Preencher — ver RN05f). "Ultima medicao" referente a avaliacao anterior do mesmo campo.
- **Continuar (rascunho "Em andamento"):** reabre uma avaliacao salva como rascunho (pelo Treinador ou pelo Aluno) com os campos parcialmente preenchidos, para completar e enviar/salvar.

### 6.2 Estado de Carregamento (Loading)
- **Edicao:** skeleton enquanto carrega os dados da avaliacao.
- **Salvando:** spinner sobre o botao acionado ("Concluir"/"Enviar"/"Salvar rascunho"), formulario bloqueado durante a requisicao.
- Carregamento da "ultima medicao" pode ser assincrono (placeholder discreto).

### 6.3 Estado de Erro
- **Erro de campo:** borda vermelha + mensagem abaixo do campo (ex: "Data nao pode ser futura", "Valor fora da faixa esperada").
- **Erro de rede:** toast "Sem conexao. Tente novamente." (mantem os dados preenchidos).
- **Erro ao salvar:** toast "Nao foi possivel salvar. Tente novamente." sem perder o preenchimento.

### 6.4 Estado de Sucesso
- **Treinador (Concluir):** toast "Avaliacao concluida!" + retorno a `[VELA-2001]` (card Concluida).
- **Treinador/Aluno (Salvar rascunho):** toast "Rascunho salvo." + retorno a `[VELA-2001]` (card **Em andamento**, com acao "Continuar").
- **Treinador (Liberar):** toast "Avaliacao liberada para o aluno." + retorno a `[VELA-2001]` (card Solicitada). **Dispara notificacao push + in-app** ao Aluno e a avaliacao vai para o **topo** da lista como pendencia (com contador na aba).
- **Aluno (Enviar):** toast "Avaliacao enviada!" + retorno a `[VELA-2001]` (card vira Concluida e trava para o Aluno).

### 6.5 Estado Desabilitado / Bloqueado *(se aplicavel)*
- **Aluno** so acessa em modo **Preencher/Continuar** avaliacoes **Solicitadas** ou **Em andamento** (iniciadas por ele) liberadas a ele; avaliacoes **Concluidas** e **Expiradas** sao apenas visualizaveis (`[VELA-2002]`), nunca editaveis pelo Aluno. Uma avaliacao **Expirada** so volta a ser preenchivel se o **Treinador** a reabrir (volta a Solicitada — RN05d); o Aluno nunca reabre por conta propria.
- **Aluno** nunca acessa criacao/edicao; tentativas sao redirecionadas para Visualizar `[VELA-2002]`.
- Campos calculados sempre em modo somente leitura.

---

## 7. Fluxo de Navegacao

### De onde o usuario chega nesta tela
| Origem | Gatilho |
|---|---|
| Lista de Avaliacoes `[VELA-2001]` | Treinador toca no **FAB "+"** (entrada **global**) e escolhe o tipo → **seleciona o aluno por busca** na Secao 0 |
| Perfil do Aluno (a mapear) | Treinador toca no **"+"** dentro do perfil de um aluno → criar com o **aluno ja travado** no contexto (ver decisao #16) |
| Lista de Avaliacoes `[VELA-2001]` | Treinador toca em "Editar" em um card (editar) |
| Lista de Avaliacoes `[VELA-2001]` | Aluno toca em "Preencher" em um card Solicitada (preencher) |
| Lista de Avaliacoes `[VELA-2001]` | Aluno ou Treinador toca em "Continuar" em um card **Em andamento** (retoma rascunho) |
| Visualizar Avaliacao `[VELA-2002]` | Treinador toca em "Editar" |

### Para onde o usuario pode ir desta tela
| Destino | Gatilho |
|---|---|
| Lista de Avaliacoes `[VELA-2001]` | Salva/Libera/Envia com sucesso, ou descarta/volta |

---

## 8. Regras de Negocio
> Regras especificas que impactam o comportamento desta tela.

- **RN01:** O **mesmo** formulario serve para **criar/editar** (Treinador) e **preencher** (Aluno); em editar/preencher abre **preenchido** com o que ja existir.
- **RN02:** O conjunto de campos e **dinamico por tipo** (Secoes 4.A–4.D). O **tipo** e definido na criacao e nao muda depois.
- **RN03 (Ultima medicao):** Abaixo de **todos** os campos numericos — **inclusive os calculados** (IMC, soma de dobras, % de gordura, etc.) —, exibir **apenas** `Ultima: XXXXX` — o ultimo valor registrado daquele campo (com unidade), considerando **apenas avaliacoes do mesmo tipo** (campos iguais em tipos diferentes — ex: Peso, % de gordura — nao se misturam). **Sem data e sem variacao/delta.** Em edicao/revisao/preenchimento, considerar a avaliacao **anterior** a atual; sem registro anterior, exibir **"Sem dados anterior"**.
- **RN04:** Campos **calculados** (IMC, RCQ, soma de dobras) sao automaticos e somente leitura, recalculando em tempo real. Os demais valores de composicao corporal (**densidade, % de gordura, massa gorda/magra**) **nao** sao calculados pelo app — sao **preenchidos manualmente** (Dobras Cutaneas — RN09; Bioimpedancia — Secao 4.D).
- **RN05 (Permissoes):** **Criar/editar/revisar** = somente **Treinador**. Em **Solicitada/Em andamento** a acao e **"Editar"**; em **Concluida** e **"Revisar"** (edita no lugar). **Preencher** = somente o **Aluno** destinatario, em avaliacao **Solicitada**. Apos a avaliacao virar **Concluida**, ela **trava para o Aluno** (so o Treinador revisa/exclui — ver RN13). Acessos indevidos sao redirecionados a Visualizar `[VELA-2002]`.
- **RN05b (Liberar):** Ao criar, o Treinador pode **concluir** (status Concluida), **salvar rascunho** (Em andamento) ou **liberar** (Solicitada) para o Aluno preencher. A acao **"Liberar para o aluno preencher" existe somente no modo criacao** — um rascunho ja salvo como **Em andamento** pelo Treinador **nao** pode ser liberado depois (so pode ser concluido ou continuado por ele).
- **RN05c (Rascunho / Em andamento):** Tanto o Treinador quanto o Aluno podem **salvar rascunho** de um preenchimento incompleto. O rascunho fica com status **Em andamento** (sem validacao final) e pode ser retomado depois pela acao **"Continuar"** na lista `[VELA-2001]`. So o **envio/conclusao** aplica a validacao completa.
- **RN05d (Prazo / Expirada):** O **prazo de preenchimento (opcional)** e definido **na criacao**, na Secao 0, via "Vai ter prazo?" (Sim/Nao) → data limite (RN16). Se o prazo vencer sem que o Aluno envie, a avaliacao passa a status **Expirada**. Sem prazo definido, a avaliacao permanece pendente por tempo indeterminado. Uma avaliacao **Expirada trava para o Aluno** — ele **nao** consegue mais preencher; **somente o Treinador reabre/reenvia** (a avaliacao volta ao status **Solicitada**, com novo prazo opcional, e dispara nova notificacao). Ver `[VELA-2001]` RN13/RN14.
- **RN05f (Edicao no modo Preencher):** No modo **Preencher/Continuar**, o Aluno pode **editar todos os campos do formulario, inclusive os valores que o Treinador deixou pre-preenchidos** ao liberar. Nenhum campo fica travado para o Aluno durante o preenchimento (a trava so ocorre **apos o envio**, quando a avaliacao vira Concluida — RN05).
- **RN05e (Notificacao ao liberar):** Ao liberar (status Solicitada), o sistema **dispara notificacao push + in-app** ao Aluno e a avaliacao vai para o **topo** da lista `[VELA-2001]` como pendencia, alimentando o contador da aba (detalhamento do push na tela de Notificacoes — decisao #13 do indice).
- **RN06:** A **Data** e obrigatoria e nao pode ser futura.
- **RN07:** Valores numericos aceitam decimais com virgula; validacao de faixa plausivel por campo com **aviso suave** quando fora da faixa, que **nao bloqueia** o salvamento (o avaliador pode confirmar e salvar). So bloqueiam o salvamento os campos **obrigatorios** e a **Data** (nao futura).
- **RN08 (Anamnese):** Se qualquer resposta do **PAR-Q** for "Sim", exibir alerta recomendando liberacao medica antes de iniciar o treino (informativo; nao bloqueia o salvamento).
- **RN09 (Dobras — sem protocolo):** A tela de Dobras Cutaneas **nao tem seletor de protocolo**: exibe **todas as dobras possiveis** (9 pontos), **todas opcionais**. O app **nao** calcula a composicao corporal (sem protocolo/formula): **densidade, % de gordura, massa gorda e massa magra** sao **campos manuais e opcionais**, preenchidos pelo Treinador. Apenas a **Soma das dobras** e automatica (somente leitura, recalcula em tempo real conforme as dobras preenchidas). Idade e Sexo **nao** aparecem nesta tela (so existiam para alimentar a formula).
- **RN10:** Fotos sao opcionais; o anexo de **laudo** da Bioimpedancia tambem e opcional.
- **RN11:** Ao voltar com alteracoes nao salvas, exigir confirmacao ("Descartar alteracoes?").
- **RN12 (Peso/Altura/Idade):** Esses campos seguem o mesmo padrao dos demais: o apoio sob o campo e **`Ultima: XXXXX`** (ultima avaliacao do mesmo tipo) ou **"Sem dados anterior"** — **nao** ha rotulo "Sugerido" separado. O input **nao** e preenchido automaticamente; o usuario digita/confirma o valor desta avaliacao.
- **RN15 (Formulario sem repetir a lista):** O formulario exibe **somente a avaliacao em edicao naquele momento** — **tipo** + **data** + campos do tipo. Informacoes de contexto/colecao (**status**, **quem liberou/registrou**, comparacao entre avaliacoes anteriores) **nao** aparecem no formulario; elas vivem na **lista** `[VELA-2001]` (e na visualizacao `[VELA-2002]`), evitando duplicidade. **Excecoes:** (a) o componente **"ultima medicao"** sob cada campo (RN03); (b) os campos de **configuracao da criacao** (aluno, quem vai preencher, prazo), que aparecem **apenas no momento de criar** e depois deixam de ser reapresentados (RN16).
- **RN16 (Inicio da criacao — aluno, responsavel e prazo):** Ao **criar**, os primeiros campos sao, nesta ordem: (1) **Aluno** — **pre-preenchido e travado** quando o formulario e aberto pelo perfil do aluno (via `[VELA-2001]`), ou **campo de busca** entre os alunos cadastrados/vinculados (digita o nome → seleciona → traz o **@**) quando aberto pela tela global "Criar avaliacao"; (2) **Quem vai preencher** — **Treinador** ou **Aluno**; se **Aluno**, pergunta **"Vai ter prazo para preencher?"** (Sim/Nao) e, se Sim, **data limite (prazo)**. A escolha define a acao primaria do rodape: **Treinador → "Concluir"**; **Aluno → "Liberar para o aluno preencher"** (status **Solicitada**, com o prazo definido aqui). Esses campos so aparecem na **criacao**.
- **RN14 (Registros independentes):** Cada avaliacao — inclusive a **Anamnese** — e um **registro novo e datado**. "Refazer" uma Anamnese (ou qualquer tipo) **cria um novo registro**, sem sobrescrever o anterior; o historico de versoes do mesmo tipo fica disponivel para comparacao ("ultima medicao"/evolucao). Nao existe "atualizar a Anamnese existente" — a unica forma de alterar um registro ja salvo e via Editar/Revisar do proprio registro.
- **RN13 (Revisar Concluida — exclusivo do Treinador):** Uma avaliacao **Concluida** fica **travada para o Aluno** (ele nunca edita/revisa). O **Treinador** pode corrigi-la de duas formas, ambas disponiveis: (1) **Revisar** — abre a avaliacao preenchida, corrige e salva **no lugar**; ela **continua Concluida** e os valores sao **sobrescritos sem versionamento/historico**; ou (2) **excluir e recriar** (exclusao definitiva, na lista `[VELA-2001]` ou na visualizacao `[VELA-2002]`). Em **Solicitada/Em andamento** a acao de alterar chama-se "Editar"; em **Concluida**, "Revisar".

---

## 9. Responsividade (Mobile vs Web)
> Diferencas de comportamento ou layout entre plataformas.

| Aspecto | Mobile | Web |
|---|---|---|
| Layout do formulario | Coluna unica, grupos colapsaveis, acao primaria ("Concluir"/"Enviar") + "Salvar rascunho" fixos no rodape | Coluna centralizada (largura maxima) ou 2 colunas por grupo; acao primaria + "Salvar rascunho" no header |
| Fotos/laudo | Camera + galeria | Upload de arquivo (drag-and-drop) |
| Teclado | Formulario sobe ao abrir teclado; teclado numerico nos campos de medida | N/A |
| "Ultima medicao" | Abaixo do campo | Abaixo do campo (ou ao lado, em telas largas) |

> Regras e validacoes **identicas** nas duas plataformas; variam apenas layout e entrada de fotos/arquivos.

---

## 10. Acessibilidade
> Consideracoes de acessibilidade para esta tela.

- Labels associadas a todos os campos e com unidade explicita (cm, kg, mm, %, kcal).
- "Ultima medicao" anunciada por leitores de tela apenas com o valor ("Ultima 38,5 cm"), sem data nem variacao (conforme RN03).
- Mensagens de erro associadas ao campo (aria-describedby) e foco levado ao primeiro campo invalido ao tentar salvar.
- Campos numericos com teclado numerico e passo adequado; area de toque confortavel no mobile.
- Contraste WCAG 2.1 AA; navegacao por teclado/tab order logica no web; alerta "Descartar alteracoes?" com foco gerenciado.

---

## 11. Historico de Alteracoes

| Data | Autor | Descricao |
|---|---|---|
| 2026-06-09 | Equipe Vela | Criacao inicial: formulario unico e dinamico (criar/editar) por tipo, com componente "ultima medicao" sob cada campo numerico e tabelas completas de campos para Anamnese, Antropometrica, Dobras Cutaneas e Bioimpedancia (referencias: PAR-Q, perimetria, protocolo Jackson & Pollock/Siri, parametros de bioimpedancia) |
| 2026-06-09 | Equipe Vela | Adicionado o modo **Preencher** (Aluno) e a acao **Liberar para o aluno preencher** (Treinador); permissoes: criar/editar = somente Treinador, preencher = Aluno em avaliacao Solicitada com trava apos enviar; titulos/acoes por modo (Salvar/Enviar/Liberar) |
| 2026-06-12 | Equipe Vela | Revisao: alinhamento com o modelo de 4 status da lista `[VELA-2001]`. Adicionados **rascunho "Salvar rascunho" → Em andamento** (Treinador e Aluno, retoma via "Continuar"), **prazo opcional na acao Liberar → Expirada** ao vencer, e **notificacao push + in-app** ao liberar. Atualizadas Secoes 1, 3.1, 3.2, 5, 6.1, 6.4, 6.5, 7 e novas RN05c/RN05d/RN05e. Status → 🟢 CONCLUIDO |
| 2026-06-12 | Equipe Vela | Revisao de comportamento (perguntas ao cliente): (#2) **Expirada trava para o Aluno** e **so o Treinador reabre** (volta a Solicitada) — RN05d, Secao 6.5; (#3) acao **"Liberar" so existe na criacao** (rascunho Em andamento nao e liberavel depois) — RN05b; (#4) no modo **Preencher o Aluno edita todos os campos, inclusive os pre-preenchidos pelo Treinador** (trava so apos envio) — nova RN05f, Secao 6.1; (#5) **heranca de Peso/Altura/Idade e sugestao visivel, nao auto-preenche** — nova RN12, Regras de Preenchimento. **Pendente:** (#1) decisao "Concluida nao e editavel nem pelo Treinador" conflita com o modelo vigente (decisao #9 / `[VELA-2001]` RN06 / `[VELA-2002]` RN04) — aguardando confirmacao do cliente antes de propagar |
| 2026-06-12 | Equipe Vela | (#1 RESOLVIDO — opcao A) **Avaliacao Concluida e imutavel para todos** (nem o Treinador edita); correcao apenas via **excluir + recriar**. Atualizadas Secao 1 (modo Editar), Secao 2 (permissoes), RN05 e nova **RN13**. Propagado para `[VELA-2001]` e `[VELA-2002]` e decisao #9/#14 do indice. Status → 🟢 CONCLUIDO |
| 2026-06-12 | Equipe Vela | Ajuste da decisao #14: cliente optou por **dar ao Treinador a acao "Revisar"** na Concluida — edita **no lugar** (continua Concluida, **sem versionamento**); **excluir + recriar** segue disponivel em paralelo. O **Aluno continua travado** na Concluida. Adicionado modo/titulo **"Revisar [Tipo]"** (Secao 3.1); atualizadas Secao 1, Secao 2, RN05 e RN13. Propagado para `[VELA-2001]`/`[VELA-2002]` e decisao #9/#14 |
| 2026-06-12 | Equipe Vela | Tres definicoes de comportamento: (1) **"ultima medicao" so compara avaliacoes do mesmo tipo** (campos iguais em tipos diferentes, ex: Peso/% gordura, nao se misturam) — Regra global da Secao 4 e RN03; (2) **validacao de faixa so avisa, nao bloqueia** o salvamento (bloqueio fica nos obrigatorios + Data) — Regras de Preenchimento e RN07; (3) **limites tecnicos de fotos** (quantidade/formato/tamanho) adiados — decisao #15 do indice |
| 2026-06-12 | Equipe Vela | Alinhamento com `[VELA-2001]` (pos-mockup): o **formulario nao repete dados da lista** — a Secao 0 passa a exibir **somente tipo + data** (sem status, quem liberou/registrou nem prazo, que ficam na lista). Atualizada Secao 3.2 e nova **RN15** |
| 2026-06-12 | Equipe Vela | (1) **"Ultima medicao" simplificada** na tela: passa a exibir **apenas** `Ultima: XXXXX` (so o valor) — **removidas data e variacao/▲▼** (RN03, Regra global da Secao 4, Secao 1, Acessibilidade); (2) removido o rotulo **"(recomendado)"** dos campos (Cintura/Quadril viram obrigatorio = Nao na Secao 4.B). Aplicado tambem no mockup |
| 2026-06-12 | Equipe Vela | Uniformizacao da "ultima medicao": (1) aparece em **TODOS os campos numericos, inclusive os calculados** (IMC, soma, % de gordura); (2) **fim do rotulo "Sugerido"** — Peso/Altura/Idade passam a usar o mesmo "Ultima: XXXXX" (RN12 reescrita); (3) mensagem de ausencia padronizada para **"Sem dados anterior"** (antes "Sem medicao anterior"). Atualizados Secao 1, 3.2, 4 (regra global), 6.1, RN03/RN12. Aplicado no mockup |
| 2026-06-12 | Equipe Vela | Definido (opcao a): **Anamnese nao exibe "Anterior"** no formulario — campos qualitativos respondidos do zero (PAR-Q sem inducao); comparacao historica fica na Visualizar `[VELA-2002]`. Atualizadas Regra global (Secao 4) e Secao 4.A. "Ultima"/"Sem dados anterior" segue valendo so para campos **numericos** |
| 2026-06-12 | Equipe Vela | **Inicio da criacao** redesenhado (Secao 0): primeiros campos = **Aluno** (travado se aberto pelo perfil; **busca** entre cadastrados se entrada global, traz o @) + **Quem vai preencher** (Treinador/Aluno) e, se Aluno, **"Vai ter prazo?"** → data. A escolha define a acao primaria do rodape: **Treinador → "Concluir"**, **Aluno → "Liberar para o aluno preencher"**. Atualizadas Secoes 3.1, 3.2, 4, 5, 6.1, 7; novas **RN16**, ajustes em RN05d/RN15. Entrada global registrada como decisao #16 do indice |
| 2026-06-24 | Equipe Vela | **Dobras Cutaneas sem protocolo:** removido o seletor de Protocolo (Pollock 3/7/Outro) e os campos **Idade/Sexo**. A tela passa a exibir **todas as 9 dobras possiveis, todas opcionais** (Tricipital, Bicipital, Subescapular, Peitoral, Axilar Media, Suprailiaca, Abdominal, Coxa, Panturrilha). O app deixa de calcular composicao corporal automaticamente — **densidade, % de gordura, massa gorda e massa magra** viram **campos manuais e opcionais**; apenas a **Soma das dobras** continua automatica. Atualizadas Secao 4.C, RN04, RN09 e Regras de Preenchimento |
| 2026-06-12 | Equipe Vela | (1) **Anamnese/registros sao independentes e datados** (refazer cria novo registro, nao sobrescreve) — nova RN14; (2) **protocolo "Outro" das Dobras**: sem equacao padrao, % de gordura/densidade/massa gorda/magra ficam **em branco e editaveis** para preenchimento manual do Treinador (so a soma das dobras e automatica) — Secao 4.C e RN09; (3) **acao final do Treinador renomeada de "Salvar" para "Concluir"** (mantendo "Enviar" do Aluno e "Salvar rascunho" para ambos) — modelo de 2 botoes distintos em vez de modal; atualizadas Secoes 3.1, 3.3, 4, 5, 6.2, 6.4, 9 e RN05b |

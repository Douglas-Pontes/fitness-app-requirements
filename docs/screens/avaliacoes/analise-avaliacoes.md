# Tela: Analise das Avaliacoes `[VELA-2004]`

---

## Metadados
| Campo | Valor |
|---|---|
| **Nome da tela** | Analise das Avaliações |
| **Modulo** | Avaliações |
| **Codigo** | VELA-2004 |
| **Prioridade** | 🔵 MVP |
| **Status** | 🟢 CONCLUIDO |
| **Ultima atualizacao** | 2026-06-16 |

---

## 1. Objetivo da Tela
> O que o usuario consegue fazer nesta tela? Qual problema ela resolve?

Tela **somente leitura** que e o **hub de analise** do modulo de Avaliacoes — onde o usuario **visualiza a evolucao** e **compara** avaliacoes (diferente da Lista `[VELA-2001]`, que serve para ver/abrir uma avaliacao individual). Reune duas visoes alternadas por um seletor (toggle/abas):

- **Graficos** — o usuario escolhe **uma metrica** (ex: Peso, % de gordura, Cintura) e ve um **grafico de linha** com a evolucao dessa metrica ao longo das avaliacoes, mais um **resumo numerico** (valor atual + variacao total no periodo).
- **Comparar** — o usuario seleciona **avaliacoes do mesmo tipo** e ve os valores **lado a lado, campo a campo, com a variacao** entre elas (▲/▼/=).

Resolve a pergunta central do app ("estou evoluindo?"), transformando o historico de avaliacoes em **tendencia visivel**. Esta tela **consolida** a antiga "Comparar Avaliacoes" (que deixa de ser tela separada).

---

## 2. Quem Acessa / Pre-condicoes
> Quem pode ver esta tela? Quais condicoes precisam ser verdadeiras?

- **Usuario:**
  - **Aluno** — ve a evolucao das **proprias** avaliacoes. Somente leitura.
  - **Treinador** — ve a evolucao do **Aluno vinculado** cujo perfil/contexto abriu. Somente leitura.
- **Pre-condicoes:** Usuario autenticado e com acesso as avaliacoes daquele perfil.
- **Permissoes especiais:** Nenhuma acao de criar/editar/excluir aqui (a tela e so de leitura). Para evolucao util, recomenda-se **>= 2 medicoes** da metrica (modo Graficos) ou **>= 2 avaliacoes do mesmo tipo** (modo Comparar) — ver Secao 6.1.

---

## 3. Layout e Componentes Visuais
> Descreva a estrutura visual da tela de cima para baixo.

### 3.1 Header / Cabecalho
- Conteudo: Botao voltar + Titulo **"Analise das Avaliacoes"** (pode reduzir para **"Analise"** em telas estreitas). No topo da aba, o **seletor de visao da aba** (toggle/segmented control) **Lista | Analise** — esta tela corresponde a posicao **Analise** (alterna com a Lista `[VELA-2001]`). Quando o Treinador abre no contexto de um Aluno, exibir abaixo do titulo o nome/@ do Aluno (ex: "Analise de @ana.vela"). Abaixo, o **seletor de visao interna** (toggle/segmented control): **Graficos | Comparar**.
- Comportamento: Fixo no topo. A visao **Graficos** abre selecionada por padrao. Aba ativa do toggle destacada com o **verde-limao neon** da marca (mesmo tratamento dos filtros ativos da Lista `[VELA-2001]`), mantendo o visual minimalista de alto contraste.

### 3.2 Corpo Principal
> Descrever secoes da tela, na ordem que aparecem

#### Visao A — Graficos

**Secao A1 — Seletor de metrica**
- Componente: **Chip/dropdown** com a lista de metricas numericas disponiveis (derivadas dos campos numericos de `[VELA-2003]`), ex: **Peso**, **% de gordura**, **IMC**, **Cintura**, **Quadril**, **Massa magra**, **Massa gorda**, **Soma de dobras**, **RCQ** etc. Seleciona **uma** metrica por vez.
- Comportamento: Ao trocar a metrica, o grafico e o resumo abaixo atualizam imediatamente. Sao listadas apenas metricas que **possuem ao menos uma medicao** registrada. A chip da metrica ativa fica destacada com o **verde-limao neon** (mesmo padrao de selecao da Lista `[VELA-2001]`).

**Secao A2 — Resumo da metrica**
- Componente: Card(s) de destaque **neutros e finos** (mesma identidade dos cards da Lista `[VELA-2001]`: fundo neutro, alto contraste, sem cor tingindo o card).
- Conteudo: **Valor mais recente** da metrica (com unidade) + **variacao total** desde a primeira medicao do periodo exibido (▲/▼/= com delta e/ou %). Reaproveita a logica de variacao de `[VELA-2002]` (RN03 de la), sem depender apenas de cor — a seta/sinal e o texto carregam a informacao, com o verde-limao apenas como acento.

**Secao A3 — Grafico de linha**
- Componente: Grafico de linha unico (uma metrica), eixo X = datas das avaliacoes, eixo Y = valor da metrica.
- Conteudo: Pontos nas datas com medicao; linha conectando-os. Por padrao exibe as **ultimas 4-5 avaliacoes**; ha um **seletor de periodo** (**3 meses / 6 meses / 1 ano / Tudo / Personalizado**) para ajustar a janela. **Personalizado** abre um seletor de **intervalo de datas** (data inicial e final) para delimitar o periodo do grafico.
- Comportamento: Ao **tocar/passar** sobre um ponto, exibe **tooltip** com **valor + data**; o **marcador (quadradinho) do ponto e clicavel** e **navega para Visualizar Avaliacao `[VELA-2002]`** daquela medicao (RN05).

#### Visao B — Comparar

**Secao B1 — Selecao de avaliacoes**
- Componente: Apos escolher o **tipo**, um **botao "Selecionar avaliacoes"** (mostrando quantas estao selecionadas) abre um **painel/bottom sheet** com a lista das avaliacoes daquele tipo. A lista do painel oferece apenas as **5 avaliacoes mais recentes** daquele tipo (RN09). Cada item segue o padrao da Lista `[VELA-2001]`: **card neutro e fino** com **tipo (icone colorido + rotulo)** e **data**, distincao visual vinda do **icone**, nunca do fundo do card; ao confirmar ("Aplicar"), a tabela comparativa atualiza.
- Comportamento: So e possivel comparar avaliacoes do **mesmo tipo** (campos compativeis — RN04), no maximo as **5 mais recentes** (RN09). Ao mudar o tipo, a selecao e reiniciada. Itens selecionados destacados com o **verde-limao neon**.

**Secao B2 — Tabela comparativa**
- Componente: **Tabela lado a lado**: cada avaliacao selecionada vira uma **coluna** (cabecalho = data); cada **linha** e um campo daquele tipo (ex: Peso, % de gordura, Cintura...).
- Conteudo: Valor + unidade por celula. Em uma coluna de **variacao** (ou indicador por celula), mostra o **delta vs. a avaliacao anterior** selecionada (▲/▼/= com valor), seguindo a mesma logica do `[VELA-2002]`.
- Comportamento: Em mobile, a tabela tem **scroll horizontal** quando ha muitas colunas; toque no cabecalho de uma coluna **navega para `[VELA-2002]`** daquela avaliacao.

### 3.3 Footer / Rodape
- Conteudo: Quando aberta pela Tab Bar, a barra de navegacao inferior permanece visivel com a aba "Avaliacoes/Evolucao" ativa. Nao ha FAB nem acao de criacao nesta tela (somente leitura).
- Comportamento: N/A (sem acoes de escrita).

---

## 4. Campos e Formularios

> Preencher apenas se a tela tiver campos de entrada (inputs, selects, etc.)

Esta tela **nao possui formulario de cadastro** — e somente leitura. Os unicos controles de entrada sao **seletores de visualizacao**:

| # | Nome do Campo | Tipo | Obrigatorio | Placeholder | Validacao | Mensagem de Erro |
|---|---|---|---|---|---|---|
| 1 | Visao (Graficos/Comparar) | Toggle / segmented control | Nao (default = Graficos) | — | — | N/A |
| 2 | Metrica (visao Graficos) | Select / chip (selecao unica) | Nao (default = primeira metrica disponivel) | — | Apenas metricas com medicao | N/A |
| 3 | Periodo (visao Graficos) | Select (3 meses / 6 meses / 1 ano / Tudo / Personalizado) | Nao (default = ultimas 4-5) | — | Em "Personalizado", data inicial <= data final | "Selecione um intervalo valido" |
| 3a | Periodo personalizado — Data inicial/final (visao Graficos) | Date (no seletor "Personalizado") | Condicional (se "Personalizado") | "Inicio" / "Fim" | Inicial nao pode ser maior que a final | "A data inicial deve ser anterior a final" |
| 4 | Tipo de avaliacao (visao Comparar) | Select (selecao unica) | Sim, para comparar | "Escolha o tipo" | — | "Selecione um tipo para comparar" |
| 5 | Avaliacoes a comparar (visao Comparar) | Multiselecao (entre as 5 mais recentes do tipo) | Sim (>= 2) | — | Minimo 2, maximo 5, mesmo tipo | "Selecione ao menos 2 avaliacoes do mesmo tipo" |

### Regras de Preenchimento
- A visao **Graficos** abre por padrao, com a primeira metrica disponivel ja selecionada.
- No modo **Comparar**, so e possivel selecionar avaliacoes de **um mesmo tipo** por vez (RN04) e no maximo as **5 mais recentes** daquele tipo (RN09).
- O periodo do grafico afeta apenas a janela do eixo X; o resumo (Secao A2) recalcula a variacao total para o periodo exibido. Em **Personalizado**, a janela e o intervalo de datas escolhido (inicial/final).

---

## 5. Botoes e Acoes

| # | Componente | Label / Icone | Posicao | Visivel para | Acao ao Clicar |
|---|---|---|---|---|---|
| 1 | Toggle de visao | "Graficos" / "Comparar" | Header | Ambos | Alterna entre as duas visoes da tela |
| 2 | Seletor de metrica | (metrica atual) | Visao Graficos (A1) | Ambos | Abre lista de metricas; ao escolher, atualiza grafico e resumo |
| 3 | Seletor de periodo | "3 meses" / "6 meses" / "1 ano" / "Tudo" / "Personalizado" | Visao Graficos (A3) | Ambos | Ajusta a janela do eixo X; "Personalizado" abre seletor de intervalo de datas (inicial/final) |
| 4 | Marcador (quadradinho) do ponto | — | Visao Graficos (A3) | Ambos | Tooltip (valor + data); o marcador e clicavel e navega para `[VELA-2002]` daquela avaliacao |
| 5 | Seletor de tipo | (tipo atual) | Visao Comparar (B1) | Ambos | Define o tipo das avaliacoes comparaveis; reinicia a selecao |
| 6 | Botao "Selecionar avaliacoes" | "Selecionar avaliacoes" (+ contador) | Visao Comparar (B1) | Ambos | Abre painel/bottom sheet com a lista (5 mais recentes); marcar/desmarcar e "Aplicar" atualiza a tabela comparativa |
| 7 | Cabecalho de coluna | (data da avaliacao) | Visao Comparar (B2) | Ambos | Navega para `[VELA-2002]` daquela avaliacao |
| 8 | Botao | Voltar | Header (esquerda) | Ambos | Retorna a origem (ver Secao 7) |

---

## 6. Estados da Tela

### 6.1 Estado Inicial / Vazio
- **Sem avaliacoes:** ilustracao + mensagem "Ainda nao ha avaliacoes para mostrar a evolucao."
- **Visao Graficos com 1 medicao da metrica:** mensagem "Registre ao menos 2 avaliacoes para ver sua evolucao." (nao plota linha de tendencia com um unico ponto).
- **Visao Comparar com menos de 2 avaliacoes do tipo:** mensagem "Voce precisa de ao menos 2 avaliacoes do mesmo tipo para comparar."
- Campos sem valor em uma avaliacao aparecem como "—" (nao informado), tanto no grafico (ponto ausente) quanto na tabela.

### 6.2 Estado de Carregamento (Loading)
- Skeleton loader na area do grafico/tabela e nos cards de resumo enquanto os dados sao buscados.

### 6.3 Estado de Erro
- **Erro ao carregar:** mensagem com botao "Tentar novamente".
- **Erro de rede:** toast "Sem conexao. Tente novamente."

### 6.4 Estado de Sucesso
- N/A — tela somente leitura, sem acoes de escrita que gerem confirmacao.

### 6.5 Estado Desabilitado / Bloqueado *(se aplicavel)*
- Quando ha dados insuficientes (ver 6.1), o grafico/tabela fica indisponivel com a mensagem orientando a registrar mais avaliacoes; os demais seletores permanecem visiveis.

---

## 7. Fluxo de Navegacao

### De onde o usuario chega nesta tela
| Origem | Gatilho |
|---|---|
| Aba "Avaliacoes/Evolucao" (Tab Bar) | Toca no toggle **Lista/Analise** no topo da aba e escolhe "Analise" (ponto de entrada principal) |
| Visualizar Avaliacao `[VELA-2002]` | Toca em "Ver evolucao" no footer (atalho ja previsto em `[VELA-2002]`) |

### Para onde o usuario pode ir desta tela
| Destino | Gatilho |
|---|---|
| Visualizar Avaliacao `[VELA-2002]` | Toca em um ponto do grafico ou no cabecalho de uma coluna da tabela |
| Origem (voltar) | Botao voltar |

---

## 8. Regras de Negocio
> Regras especificas que impactam o comportamento desta tela.

- **RN01:** Tela **somente leitura**; nao cria, edita nem exclui avaliacoes. As acoes de escrita ficam em `[VELA-2001]`/`[VELA-2003]`.
- **RN02:** A tela tem **duas visoes** (Graficos e Comparar), alternadas por toggle. **Graficos** abre por padrao.
- **RN03 (Graficos):** Mostra **uma metrica por vez** (grafico de linha) + resumo (valor atual + variacao total). Por padrao exibe as **ultimas 4-5 avaliacoes**, com **seletor de periodo** (**3 meses / 6 meses / 1 ano / Tudo / Personalizado**) para ajustar a janela. **Personalizado** abre um **intervalo de datas** (inicial/final), com a inicial nunca posterior a final.
- **RN04 (Comparar):** So compara avaliacoes do **mesmo tipo** (campos compativeis). Exige **>= 2** avaliacoes selecionadas; exibe-as em **tabela lado a lado**, campo a campo, com variacao (▲/▼/=) entre colunas consecutivas.
- **RN05 (Navegacao por ponto/coluna):** Tocar no **marcador (quadradinho)** de um ponto do grafico ou no **cabecalho (data) clicavel** de uma coluna da tabela leva ao `[VELA-2002]` daquela avaliacao.
- **RN06 (Dados insuficientes):** Com menos de 2 medicoes (grafico) ou menos de 2 avaliacoes do mesmo tipo (comparar), exibe estado vazio orientando a registrar mais avaliacoes (Secao 6.1); nao plota tendencia com ponto unico.
- **RN07 (Variacao):** A variacao exibida (resumo e tabela) segue a mesma logica e formatacao de `[VELA-2002]` (delta com seta/sinal + valor, sem depender apenas de cor).
- **RN08 (Consolidacao):** Esta tela **substitui** a antiga "Comparar Avaliacoes" como tela separada; a comparacao vira a visao **Comparar** aqui.
- **RN09 (Limite da comparacao):** A visao **Comparar** considera apenas as **5 avaliacoes mais recentes** do tipo selecionado — o painel de selecao nao lista nem permite comparar avaliacoes alem dessas 5 (limite de colunas da tabela). A selecao acontece via **botao "Selecionar avaliacoes"** que abre um **painel/bottom sheet** (nao ha lista de cards fixa no corpo da tela).

---

## 9. Responsividade (Mobile vs Web)
> Diferencas de comportamento ou layout entre plataformas.

| Aspecto | Mobile | Web |
|---|---|---|
| Layout | Coluna unica; grafico ocupa largura total | Coluna centralizada (largura maxima); grafico maior |
| Tabela (Comparar) | Scroll horizontal quando ha muitas colunas | Mais colunas/avaliacoes visiveis de uma vez |
| Seletores | Chips/bottom sheet | Dropdown/popover |
| Tooltip do grafico | Toque no ponto | Hover/clique no ponto |

> Regras e permissoes **identicas**; variam apenas o layout e a apresentacao.

---

## 10. Acessibilidade
> Consideracoes de acessibilidade para esta tela.

- O grafico tem **alternativa textual/tabular** dos dados (datas e valores) para leitores de tela; a tendencia nao depende apenas de cor.
- Variacoes anunciadas por leitores de tela (ex: "Peso 78 kg, reduziu 2 kg desde a primeira avaliacao do periodo").
- Tabela comparativa com cabecalhos de coluna/linha associados (scope) para navegacao por leitor de tela.
- Contraste WCAG 2.1 AA (atencao ao verde-limao neon sobre fundos claros — usar texto/contornos de apoio); area de toque adequada nos pontos do grafico e seletores; tab order logica no web.

---

## 11. Historico de Alteracoes

| Data | Autor | Descricao |
|---|---|---|
| 2026-06-16 | Equipe Vela | Criacao inicial: hub com duas visoes (Graficos = 1 metrica por vez, linha + resumo, ultimas 4-5 com ampliacao; Comparar = avaliacoes do mesmo tipo em tabela lado a lado com variacao). Tela **consolida** a antiga "Comparar Avaliacoes". Somente leitura para Aluno e Treinador; toque em ponto/coluna navega para `[VELA-2002]`. Pontos de entrada marcados como ⚠️ PENDENTE (decisao em aberto) |
| 2026-06-16 | Equipe Vela | Ajustes pos-mockup (2): (1) periodo da visao Graficos ganha tambem **"3 meses"** (3 / 6 meses / 1 ano / Tudo / Personalizado) — Secao 3.2 A3, Secao 4/5 e RN03; (2) na visao Comparar, a selecao deixa de ser lista de cards fixa e passa a um **botao "Selecionar avaliacoes"** que abre um **painel/bottom sheet** (5 mais recentes) — Secao 3.2 B1, Secao 5 (botao 6) e RN09. Mockup atualizado (frame "painel · selecionar avaliacoes") |
| 2026-06-16 | Equipe Vela | Ajustes pos-mockup: (1) seletor de periodo da visao Graficos ganha **"Personalizado"** (intervalo de datas inicial/final) — Secao 3.2 A3, Secao 4 (campos 3/3a), Secao 5 e RN03; (2) marcador (quadradinho) do ponto e cabecalho (data) da tabela explicitados como **clicaveis** — RN05; (3) visao **Comparar** limitada as **5 avaliacoes mais recentes** do tipo — nova **RN09**, Secao 3.2 B1, Secao 4 (campo 5). Mockup `analise-avaliacoes.html` atualizado |
| 2026-06-16 | Equipe Vela | Revisao concluida: **pontos de entrada definidos** (decisao #18 resolvida) — acesso pelo **toggle Lista/Analise** no topo da aba "Avaliacoes/Evolucao" (entrada principal) + atalho "Ver evolucao" no `[VELA-2002]`. Descartados o botao na Lista `[VELA-2001]` e o card no Perfil. Removido `⚠️ PENDENTE` da Secao 7. Status → 🟢 CONCLUIDO |
| 2026-06-16 | Equipe Vela | Renomeada de "Evolucao / Graficos" para **"Analise das Avaliacoes"** (nome que comunica visualizar + comparar, sem colidir com a Lista `[VELA-2001]`). Arquivo renomeado para `analise-avaliacoes.md`. Cards/seletores alinhados ao visual da marca: cards neutros e finos, selecao/aba ativa em verde-limao neon, tipo por icone colorido (padrao `[VELA-2001]`). Atualizados titulo, Secao 1, 3.1, 3.2 (A1/A2/B1) |

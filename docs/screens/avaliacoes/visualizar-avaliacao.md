# Tela: Visualizar Avaliacao `[VELA-2002]`

---

## Metadados
| Campo | Valor |
|---|---|
| **Nome da tela** | Visualizar Avaliacao |
| **Modulo** | Avaliações |
| **Codigo** | VELA-2002 |
| **Prioridade** | 🔵 MVP |
| **Status** | 🟢 CONCLUIDO |
| **Ultima atualizacao** | 2026-06-16 |

---

## 1. Objetivo da Tela
> O que o usuario consegue fazer nesta tela? Qual problema ela resolve?

Tela **somente leitura** que exibe os dados completos de **uma** avaliacao, adaptando o conteudo ao **tipo** (Anamnese, Antropometrica, Dobras Cutaneas, Bioimpedancia). Para cada campo numerico, mostra o valor registrado e, quando houver, a **comparacao com a medicao anterior** (variacao). E para onde o botao "Visualizar" do card `[VELA-2001]` leva. Permite ao **Treinador** ir para a edicao `[VELA-2003]`, e ao **Aluno** ir para o preenchimento quando a avaliacao esta **Solicitada**.

---

## 2. Quem Acessa / Pre-condicoes
> Quem pode ver esta tela? Quais condicoes precisam ser verdadeiras?

- **Usuario:**
  - **Aluno** — visualiza qualquer avaliacao do proprio perfil. Se a avaliacao estiver **Solicitada** (liberada a ele), em vez de "Editar" ve o atalho **"Preencher"** (`[VELA-2003]`). Nunca edita/exclui.
  - **Treinador** — visualiza avaliacoes do Aluno vinculado cujo perfil abriu; pode **Excluir** (qualquer status), **alterar** via **"Editar"** (Solicitada/Em andamento) ou **"Revisar"** (Concluida) e **"Reabrir"** uma avaliacao **Expirada** (volta a Solicitada — `[VELA-2001]` RN14).
- **Pre-condicoes:** Usuario autenticado e com acesso aquela avaliacao.
- **Permissoes especiais:** Visualizar e sempre permitido para ambos. **"Excluir"** aparece **somente para o Treinador** (qualquer status). O botao de alterar aparece para o **Treinador** sempre, rotulado **"Editar"** (Solicitada/Em andamento) ou **"Revisar"** (Concluida — edita no lugar); em avaliacao **Expirada**, o Treinador ve **"Reabrir"** (volta a Solicitada — `[VELA-2001]` RN14). **"Preencher"** aparece para o **Aluno** quando o status e **Solicitada**.

---

## 3. Layout e Componentes Visuais
> Descreva a estrutura visual da tela de cima para baixo.

### 3.1 Header / Cabecalho
- Conteudo: Botao voltar + Titulo com o **tipo** + **data** + **status** (ex: "Antropometrica • 12/03/2026 • Concluida") usando o icone/cor do tipo (mesma identidade do card). Quando o **Treinador** abre no contexto de um Aluno, exibir tambem o **nome/@ do Aluno** dono da avaliacao (ex: "Ana Vela • @ana.vela"), espelhando a Lista `[VELA-2001]`. Acoes a direita: para o **Treinador**, **menu ⋮** (Excluir) sempre e o botao de alterar (lapis) rotulado **"Editar"** (Solicitada/Em andamento) ou **"Revisar"** (Concluida), ou ainda **"Reabrir"** quando o status e **Expirada** (`[VELA-2001]` RN14); para o **Aluno** em avaliacao **Solicitada**, **"Preencher"**.
- Comportamento: Fixo no topo.

### 3.2 Corpo Principal
> Descrever secoes da tela, na ordem que aparecem

**Secao 0 — Cabecalho da avaliacao**
- Conteudo: Tipo (com cor/icone), Data, **status** (Solicitada/Concluida) e **quem liberou/registrou**. Quando **Concluida**, resumo-chave em destaque (ex: % de gordura, peso). Quando **Solicitada** e ainda sem dados, exibir "Aguardando preenchimento" (para o Aluno destinatario, com atalho "Preencher").

**Secao 1..N — Dados do tipo (somente leitura)**
- Componente: Lista de campos agrupada (mesma organizacao do formulario `[VELA-2003]`).
- Conteudo: Cada campo exibe **rotulo + valor + unidade**. Para campos numericos, exibir tambem a **variacao vs. avaliacao anterior** (▲/▼/= com delta e/ou %).
- Campos calculados (IMC, RCQ, soma de dobras, densidade, % de gordura, massa gorda/magra) sao exibidos como resultado.
- **Anamnese:** exibe objetivo, trilha, respostas do PAR-Q (com destaque se houver "Sim"), historico de saude e estilo de vida.

**Secao Fotos (quando houver)**
- Componente: Galeria das fotos da avaliacao (Frente, Costas, Perfis) ou laudo anexado (Bioimpedancia), com visualizacao ampliada ao tocar.

**Secao Observacoes**
- Texto livre registrado na avaliacao (se houver).

### 3.3 Footer / Rodape
- Conteudo: Acoes contextuais — **"Editar"/"Revisar"** (somente Treinador; "Revisar" em Concluida), **"Reabrir"** (Treinador, se Expirada — `[VELA-2001]` RN14) ou **"Preencher"** (Aluno, se Solicitada) e **"Ver evolucao"** (atalho para a **Analise das Avaliacoes** `[VELA-2004]`, abrindo na metrica/tipo correspondente).
- Comportamento: Fixo na parte inferior.

---

## 4. Campos e Formularios

> Preencher apenas se a tela tiver campos de entrada (inputs, selects, etc.)

N/A — Tela **somente leitura**. Nao ha campos de entrada. Os campos exibidos sao os mesmos definidos no formulario `[VELA-2003]` (Secoes 4.A–4.D), apresentados como valores. A edicao ocorre em `[VELA-2003]`.

### Regras de Preenchimento
- N/A (visualizacao). A formatacao de unidades e a logica de variacao seguem as regras de `[VELA-2003]`.

---

## 5. Botoes e Acoes

| # | Componente | Label / Icone | Posicao | Visivel para | Acao ao Clicar |
|---|---|---|---|---|---|
| 1 | Botao | "Editar" / "Revisar" | Header (direita) | **Treinador** | Navega para `[VELA-2003]` preenchido. Rotulo **"Editar"** em Solicitada/Em andamento e **"Revisar"** em Concluida (edita no lugar — RN04) |
| 2 | Menu de acoes | "⋮" → Excluir | Header (direita) | **Treinador** | Abre confirmacao de exclusao (definitiva); ao confirmar, exclui e volta para `[VELA-2001]` |
| 3 | Botao | "Preencher" | Header/Footer | **Aluno**, se status = Solicitada | Navega para `[VELA-2003]` em modo preenchimento |
| 3b | Botao | "Solicitar reabertura" | Footer | **Aluno**, se status = **Expirada** | Dispara notificacao ao Treinador pedindo reabertura (nao reabre — `[VELA-2001]` RN16); feedback "Reabertura solicitada" |
| 3c | Botao | "Reabrir" | Header/Footer | **Treinador**, se status = **Expirada** | Reabre a avaliacao → volta ao status **Solicitada** (com novo prazo opcional) e notifica o Aluno (`[VELA-2001]` RN14) |
| 4 | Botao | Voltar | Header (esquerda) | Ambos | Retorna para `[VELA-2001]` |
| 5 | Miniatura de foto | — | Secao Fotos | Ambos | Abre visualizacao ampliada |

---

## 6. Estados da Tela

### 6.1 Estado Inicial / Vazio
- Exibe os dados da avaliacao. Campos nao preenchidos aparecem como "—" (nao informado).
- Se nao houver medicao anterior, a area de variacao mostra "Sem comparacao anterior".

### 6.2 Estado de Carregamento (Loading)
- Skeleton loader nas secoes enquanto os dados sao buscados.

### 6.3 Estado de Erro
- **Erro ao carregar:** mensagem com botao "Tentar novamente".
- **Avaliacao inexistente/excluida:** mensagem "Esta avaliacao nao esta mais disponivel" + voltar para a lista.
- **Erro de rede:** toast "Sem conexao. Tente novamente."

### 6.4 Estado de Sucesso
- N/A para visualizacao. Apos **excluir** com sucesso: toast "Avaliacao excluida." + retorno a `[VELA-2001]`.

### 6.5 Estado Desabilitado / Bloqueado *(se aplicavel)*
- Para o **Aluno**, "Editar" e "Excluir" ficam **ocultos**; a tela permanece em leitura (com "Preencher" apenas se Solicitada, ou **"Solicitar reabertura"** se Expirada — `[VELA-2001]` RN16).

---

## 7. Fluxo de Navegacao

### De onde o usuario chega nesta tela
| Origem | Gatilho |
|---|---|
| Lista de Avaliacoes `[VELA-2001]` | Toca em "Visualizar" no card |
| Cadastro/Edicao `[VELA-2003]` | Apos **salvar** (criacao, edicao, revisao ou preenchimento do Aluno), retorna ao detalhe recem-registrado |

### Para onde o usuario pode ir desta tela
| Destino | Gatilho |
|---|---|
| Lista de Avaliacoes `[VELA-2001]` | Voltar, ou apos excluir |
| Cadastro/Edicao `[VELA-2003]` | Treinador toca em "Editar"; ou Aluno toca em "Preencher" (se Solicitada) |
| Lista de Avaliacoes `[VELA-2001]` | Treinador toca em **"Reabrir"** (Expirada → Solicitada); volta a lista com o card atualizado |
| Analise das Avaliacoes `[VELA-2004]` | Toca em "Ver evolucao" |

---

## 8. Regras de Negocio
> Regras especificas que impactam o comportamento desta tela.

- **RN01:** Tela **somente leitura**; nenhum dado e editavel aqui.
- **RN02:** O conteudo se adapta ao **tipo** da avaliacao, espelhando os grupos de campos do formulario `[VELA-2003]`.
- **RN03:** Para campos numericos, exibir a **variacao vs. a avaliacao anterior** do mesmo tipo/campo (▲/▼/= com delta), sem depender apenas de cor.
- **RN04:** Alterar e excluir sao **exclusivos do Treinador**. O botao de alterar e rotulado **"Editar"** em **Solicitada/Em andamento** e **"Revisar"** em **Concluida** (ambos levam ao formulario `[VELA-2003]`; em Concluida edita no lugar, sem versionamento — ver `[VELA-2001]` RN06); alternativamente o Treinador pode **excluir e recriar** uma Concluida. "Excluir" fica disponivel ao Treinador em qualquer status. O **Aluno** so ve "Preencher" quando a avaliacao esta **Solicitada** e **nunca edita/revisa** (ver `[VELA-2001]` RN04–RN08).
- **RN05:** A exclusao (do Treinador) exige **modal de confirmacao** e e **definitiva** — o app nao tem lixeira nem "desfazer".
- **RN06 (Anamnese):** Respostas "Sim" do PAR-Q sao destacadas com aviso informativo.
- **RN07:** Fotos/laudo sao exibidos quando existirem; toque abre visualizacao ampliada.
- **RN08 (Reabrir — Treinador):** Em avaliacao **Expirada**, o Treinador ve **"Reabrir"** (espelha a acao da Lista — `[VELA-2001]` RN14): volta ao status **Solicitada** (com novo prazo opcional) e notifica o Aluno (`[VELA-2001]` RN11). O **Aluno** nunca reabre — apenas **"Solicitar reabertura"** (notifica o Treinador, nao muda status — `[VELA-2001]` RN16).
- **RN09 (Pos-salvar):** Apos **salvar** no formulario `[VELA-2003]` (criacao, edicao, revisao ou preenchimento do Aluno), o app retorna a esta tela exibindo o **detalhe recem-registrado** (confirmacao visual do que foi gravado).
- **RN10 (Ver evolucao):** O atalho **"Ver evolucao"** leva a **Analise das Avaliacoes** `[VELA-2004]` (somente leitura), abrindo na metrica/tipo correspondente a avaliacao visualizada.

---

## 9. Responsividade (Mobile vs Web)
> Diferencas de comportamento ou layout entre plataformas.

| Aspecto | Mobile | Web |
|---|---|---|
| Layout | Coluna unica, secoes empilhadas | Coluna centralizada (largura maxima) ou 2 colunas |
| Fotos | Galeria com toque para ampliar | Galeria com clique/lightbox |
| Acoes | "Editar" no header + ⋮ | "Editar" e "Excluir" visiveis na area de acoes |

> Regras e permissoes **identicas**; variam apenas o layout e a apresentacao.

---

## 10. Acessibilidade
> Consideracoes de acessibilidade para esta tela.

- Valores e variacoes anunciados por leitores de tela (ex: "Cintura 84 cm, reduziu 1 cm em relacao a avaliacao anterior").
- A variacao nao depende apenas de cor (setas/sinais + texto).
- Imagens com texto alternativo (ex: "Foto frontal da avaliacao de 12/03/2026").
- Contraste WCAG 2.1 AA; navegacao por teclado/tab order logica no web; foco gerenciado no modal de exclusao.

---

## 11. Historico de Alteracoes

| Data | Autor | Descricao |
|---|---|---|
| 2026-06-09 | Equipe Vela | Criacao inicial: visualizacao somente leitura adaptada por tipo, com comparacao vs. avaliacao anterior, fotos/laudo e acoes contextuais |
| 2026-06-09 | Equipe Vela | Permissoes revisadas: Editar/Excluir somente Treinador; Aluno ve "Preencher" quando status Solicitada; exibicao de status e exclusao definitiva sem lixeira |
| 2026-06-12 | Equipe Vela | (decisao #14 — opcao A) **Avaliacao Concluida e imutavel**: botao "Editar" do Treinador fica **oculto** em Concluida (corrige via excluir + recriar); "Excluir" segue disponivel em qualquer status. Atualizadas Secao 2, 3.1, 3.3, RN04 e botao "Editar" da Secao 5 |
| 2026-06-12 | Equipe Vela | Ajuste da decisao #14: **Treinador ganha "Revisar"** na Concluida (edita no lugar, **sem versionamento**); excluir + recriar segue disponivel; **Aluno continua travado**. Botao de alterar passa a ser **"Editar" (Solicitada/Em andamento)** ou **"Revisar" (Concluida)**. Atualizadas Secao 2, 3.1, 3.3, RN04 e botao da Secao 5 |
| 2026-06-12 | Equipe Vela | (decisao #17) Aluno vendo avaliacao **Expirada** ganha botao **"Solicitar reabertura"** (notifica o Treinador, nao reabre — `[VELA-2001]` RN16). Atualizados botao 3b da Secao 5 e Secao 6.5 |
| 2026-06-16 | Equipe Vela | Revisao de consistencia: (1) **"Ver evolucao"** deixa de ser "futuro" e passa a apontar para **Analise das Avaliacoes** `[VELA-2004]` (ja existente; navegacao bidirecional) — Secao 3.3, Secao 7 e nova RN10; (2) **Treinador ganha "Reabrir"** em avaliacao **Expirada**, espelhando a Lista `[VELA-2001]` RN14 — Secao 2, 3.1, botao 3c da Secao 5, Secao 7 e nova RN08; (3) confirmado o **pos-salvar**: retorna ao detalhe recem-registrado em `[VELA-2002]` (removido "a confirmar") — Secao 7 e nova RN09 |
| 2026-06-16 | Equipe Vela | Revisao final (`/revisar-tela`): documento comparado ao template — todas as secoes preenchidas, sem `⚠️ PENDENTE`. Sincronizado o Status dos Metadados para **🟢 CONCLUIDO** (estava defasado em relacao ao indice) |
| 2026-06-16 | Equipe Vela | Ajuste pos-mockup: header passa a exibir o **nome/@ do Aluno** dono da avaliacao quando o Treinador abre no contexto de um Aluno (espelha `[VELA-2001]`) — Secao 3.1. Mockup atualizado |

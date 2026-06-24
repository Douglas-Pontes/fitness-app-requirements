# Visão Geral do Produto — Vela

> Identidade completa da marca em [`04-identidade-de-marca.md`](04-identidade-de-marca.md).

## Resumo
**Vela** é um app de musculação (mobile + web) cuja proposta é ser *o ponto onde a evolução começa* — **direção aplicada ao treino**. Em vez de ser apenas um catálogo de treinos, o Vela é uma **plataforma de evolução física** estruturada em duas trilhas: **`.track`** (evolução física, estética e consistência) e **`.performance`** (desempenho atlético para esportes).

---

## Proposta de Valor
> Qual dor este app resolve? Por que um aluno usaria este app e não outro?

Muita gente treina sem saber para onde está indo. O Vela resolve isso oferecendo **direção e acompanhamento estruturados**, transformando esforço em **progresso real**. O usuário escolhe o caminho que combina com seu objetivo — `.track` para evoluir no físico/estética ou `.performance` para melhorar o desempenho na sua modalidade — e acompanha sua evolução de forma clara e contínua.

---

## Diferenciais
- **Duas trilhas claras de evolução** — `.track` (físico/estética/consistência) e `.performance` (desempenho atlético), em vez de um único formato genérico.
- **Posicionamento entre genérico e atleta** — treino personalizado e estruturado, sem a limitação dos apps focados só em alto rendimento nem a superficialidade dos catálogos prontos.
- **Foco em direção e acompanhamento** — não só "o que treinar", mas para onde se está evoluindo.
- **Identidade forte e memorável** — marca minimalista, ciência aplicada ao treino, evolução contínua.

---

## Plataformas
- [x] Mobile iOS
- [x] Mobile Android
- [x] Web (browser)
- [ ] Desktop app

---

## Modelo de Negócio
> Como o app gera receita? Freemium? Assinatura? B2B (venda para academias)?

⚠️ PENDENTE: Definir com o cliente

---

## Perfil dos Usuários

| Tipo | Descrição | Acesso |
|---|---|---|
| Aluno | Praticante de musculação | App completo |
| ⚠️ | Definir demais perfis (Personal Trainer, Nutricionista, Admin/Academia?) | ⚠️ |

---

## Documentos do Projeto

| Documento | Descrição |
|---|---|
| `00-template-tela.md` | Template padrão para documentar telas |
| `01-visao-geral.md` | Este arquivo — índice mestre |
| `02-personas.md` | Personas e jornadas do usuário |
| `03-fluxos-de-navegacao.md` | Mapa de navegação entre telas |
| `04-identidade-de-marca.md` | Marca Vela: conceito, paleta, logo, categorias |
| `05-mvp.md` | Definição do MVP vs futuro |

---

## Índice de Telas e Status

### 🔐 Autenticação
| Tela | Arquivo | Status |
|---|---|---|
| Splash Screen | `screens/auth/splash.md` | 🔴 NÃO INICIADO |
| Login | `screens/auth/login.md` | 🔴 NÃO INICIADO |
| Cadastro | `screens/auth/cadastro.md` | 🔴 NÃO INICIADO |
| Recuperar Senha | `screens/auth/recuperar-senha.md` | 🔴 NÃO INICIADO |
| Redefinir Senha | `screens/auth/redefinir-senha.md` | 🔴 NÃO INICIADO |

### 🎯 Onboarding
| Tela | Arquivo | Status |
|---|---|---|
| Boas-vindas | `screens/onboarding/boas-vindas.md` | 🔴 NÃO INICIADO |
| Dados Pessoais | `screens/onboarding/dados-pessoais.md` | 🔴 NÃO INICIADO |
| Objetivo / Meta | `screens/onboarding/objetivo.md` | 🔴 NÃO INICIADO |
| Nível de Experiência | `screens/onboarding/nivel-experiencia.md` | 🔴 NÃO INICIADO |

### 🏠 Dashboard
| Tela | Arquivo | Status |
|---|---|---|
| Home / Dashboard | `screens/dashboard/home.md` | 🔴 NÃO INICIADO |

### 💪 Treinos

**Base de Treinos (visão do Treinador)**
| Tela | Arquivo | Status |
|---|---|---|
| Lista de Treinos `[VELA-4001]` | `screens/treinos/treinador/lista-treinos.md` | 🟢 CONCLUIDO |
| Visualizar Treino `[VELA-4002]` | `screens/treinos/treinador/visualizar-treino.md` | 🟢 CONCLUIDO |
| Cadastro / Edição de Treino `[VELA-4003]` | `screens/treinos/treinador/cadastro-treino.md` | 🟢 CONCLUIDO |

**Fluxo do Aluno (treinar)**
| Tela | Arquivo | Status |
|---|---|---|
| Visualizar / Executar Treino (Aluno) `[VELA-6003]` | `screens/treinos/aluno/visualizar-treino.md` | 🟢 CONCLUIDO |
| Lista de Treinos (Aluno) | `screens/treinos/aluno/lista-treinos.md` | 🔴 NÃO INICIADO |
| Histórico de Treinos | `screens/treinos/aluno/historico.md` | 🔴 NÃO INICIADO |

> **Nota (consolidação):** as telas antes previstas **Iniciar Treino**, **Treino em Andamento** e **Finalizar Treino** foram **consolidadas** numa única tela com estados — **Visualizar / Executar Treino (Aluno) `[VELA-6003]`** (ticket cliente `VELA-5002`, série 6xxx = Aluno): consulta → em execução (iniciar/marcar séries/timer de descanso) → resumo compartilhável (finalizar). É o **par de execução** da Visualizar do Treinador `[VELA-4002]` e o destino de toque do Detalhe da Rotina `[VELA-6002]` (RN08). Aqui se define o **modelo de execução (sessão)** — data, início/fim, duração, exercícios e séries/reps/carga realizados (RN04) — que **destrava** os KPIs e o "último treino executado" adiados em `[VELA-6002]`/`[VELA-6001]` (decisões #41 e #45). A antiga "Detalhe do Treino (histórico)" será reaproveitada pelo Histórico de Treinos (a mapear).

> **Nota:** o trio **VELA-4001/4002/4003** é a **base reutilizável de treinos do Treinador** (cadastro, listagem e visualização), espelhando o padrão de Exercícios e Avaliações. Cada treino agrupa exercícios em **grupos numerados (1, 2, 3…)** com tipo (Normal/Bi-set/Tri-set/Superset/Drop-set) — as **letras (A, B, C…)** ficam reservadas para a **Rotina**; séries/reps/descanso são **obrigatórios** já no treino e a descrição de execução é opcional (a prescrição é feita no próprio treino). Coexiste com o **fluxo do Aluno** (Iniciar/Andamento/Finalizar). A colisão de nome "Lista de Treinos" (Treinador vs Aluno) é resolvida pela **separação em subpastas por público** (`treinos/treinador/` vs `treinos/aluno/`).

### 📋 Rotinas

**Base de Rotinas (visão do Treinador)**
| Tela | Arquivo | Status |
|---|---|---|
| Lista de Rotinas `[VELA-5001]` | `screens/rotinas/treinador/lista-rotinas.md` | 🟢 CONCLUIDO |
| Visualizar Rotina `[VELA-5002]` | `screens/rotinas/treinador/visualizar-rotina.md` | 🟢 CONCLUIDO |
| Cadastro / Edição de Rotina `[VELA-5003]` | `screens/rotinas/treinador/cadastro-rotina.md` | 🟢 CONCLUIDO |

**Atribuição ao Aluno** *(ação do Treinador)*
| Tela | Arquivo | Status |
|---|---|---|
| Atrelar Rotina ao Aluno `[VELA-3004]` | `screens/rotinas/treinador/atrelar-rotina-aluno.md` | 🟢 CONCLUIDO |

**Fluxo do Aluno (consumir rotinas)**
| Tela | Arquivo | Status |
|---|---|---|
| Minhas Rotinas `[VELA-6001]` | `screens/rotinas/aluno/minhas-rotinas.md` | 🟢 CONCLUIDO |
| Detalhe da Rotina (Aluno) `[VELA-6002]` | `screens/rotinas/aluno/detalhe-rotina-aluno.md` | 🟢 CONCLUIDO |

> **Nota:** o trio **VELA-5001/5002/5003** é a **base reutilizável de rotinas do Treinador** (cadastro, listagem e visualização), espelhando o padrão de Treinos e Exercícios. Uma rotina é um **agrupamento ordenado de treinos** (`[VELA-4001]`) identificados por **letras A, B, C…** (a numeração 1, 2, 3… fica para os grupos dentro de cada treino). Por treino na rotina há **dia da semana** e **descrição curta** opcionais (dia pode repetir; sem visão de semana por ora). A **prescrição** (séries/reps/descanso) já vem do treino (`[VELA-4003]`, decisão #31) — a rotina não a reabre. As telas antigas "Criar/Editar/Detalhe da Rotina" foram **consolidadas** neste trio (Criar+Editar numa só tela `[VELA-5003]`; Detalhe → Visualizar `[VELA-5002]`).
>
> **Atrelar Rotina ao Aluno `[VELA-3004]`** (🔵 MVP) materializa o fluxo antes "futuro" (decisão #38): o Treinador atribui uma rotina a um aluno definindo **vigência** (início obrigatório; fim opcional/sem prazo), **objetivo** e **mensagem**. A rotina vem da **base** (`[VELA-5001]`) ou é **criada na hora** (`[VELA-5003]`, sempre salva na base) e é vinculada como **cópia/snapshot** (edições na base não afetam o que já foi entregue). Prescrição herdada é **ajustável, não obrigatória** (aviso não bloqueia). Rotinas **coexistem** (sem substituição automática).
>
> **Fluxo do Aluno — Minhas Rotinas `[VELA-6001]`** (🔵 MVP) é a **visão do Aluno** (nova série **6xxx**), distinta da Lista do Treinador `[VELA-5001]`: lista somente leitura das rotinas **atribuídas ao aluno**, em seções **Ativas · Agendadas · Anteriores** (cada uma some se vazia). O **status é calculado** das datas + data atual (Ativa/Agendada/Encerrada); o aluno **pode ter mais de uma rotina ativa**. Sem data de fim → "Ativa · sem prazo" + tempo decorrido. A **visibilidade de prazo** ao aluno é **controlada pelo Treinador** na atribuição (padrão visível — decisão #40). Card **enxuto**: **sem barra de progresso** e **sem contagem de exercícios** (ambas vivem no Detalhe `[VELA-6002]`); exibe **"X treinos realizados"** (registro de sessão do `[VELA-6003]`, decisões #41/#49). Tocar no card abre o **Detalhe da Rotina (Aluno) `[VELA-6002]`**. Ponto de entrada depende do **dashboard/menu do Aluno** (decisão #39).

### 🏋️ Exercícios
| Tela | Arquivo | Status |
|---|---|---|
| Lista de Exercícios `[VELA-3001]` | `screens/exercicios/lista-exercicios.md` | 🟢 CONCLUIDO |
| Visualizar Exercício `[VELA-3002]` | `screens/exercicios/visualizar-exercicio.md` | 🟢 CONCLUIDO |
| Cadastro / Edição de Exercício `[VELA-3003]` | `screens/exercicios/cadastro-exercicio.md` | 🟢 CONCLUIDO |

> **Nota:** as telas previstas "Catálogo de Exercícios", "Detalhe do Exercício" e "Busca de Exercícios" (pensadas para o Aluno montar rotina) foram **substituídas** pelo trio na **visão do Treinador**: Lista `[VELA-3001]`, Visualizar `[VELA-3002]` e Cadastro/Edição `[VELA-3003]`. **Não há acervo global de exercícios** — todo exercício é **criado pelo Treinador** (que edita/exclui os seus). A única base global do app é a **base de vídeos** (usada no campo Vídeo do cadastro: escolher da base ou colar link do YouTube). A busca da Lista é normalizada (sem acentos/minúsculas). A consulta do **Aluno** reaproveitará Lista/Visualização e será detalhada depois. **Hierarquia:** Exercício → **Treino** → Rotina — o exercício é incluído em **Treinos** (nunca direto na Rotina; a Rotina agrupa Treinos). Séries/repetições/descanso **não** ficam no exercício — são prescritos no **Treino** (`[VELA-4003]`, decisão #31).

### 📊 Avaliações
| Tela | Arquivo | Status |
|---|---|---|
| Lista de Avaliações `[VELA-2001]` | `screens/avaliacoes/lista-avaliacoes.md` | 🟢 CONCLUIDO |
| Visualizar Avaliação `[VELA-2002]` | `screens/avaliacoes/visualizar-avaliacao.md` | 🟢 CONCLUIDO |
| Cadastro / Edição de Avaliação `[VELA-2003]` | `screens/avaliacoes/cadastro-avaliacao.md` | 🟢 CONCLUIDO |
| Análise das Avaliações `[VELA-2004]` | `screens/avaliacoes/analise-avaliacoes.md` | 🟢 CONCLUIDO |

> **Nota:** as telas previstas "Nova Avaliação Completa", "Nova Anamnese" e "Detalhe da Avaliação" foram **consolidadas**: o cadastro/edição de todos os tipos passou a ser um **formulário único e dinâmico** `[VELA-2003]` (renderiza os campos conforme o tipo), e a visualização é a tela única `[VELA-2002]`. A lista `[VELA-2001]` reúne todos os tipos. Tipos com formulário completo já documentado: **Anamnese, Antropométrica, Dobras Cutâneas, Bioimpedância**.
>
> **Nota:** as telas previstas "Comparar Avaliações" e "Evolução / Gráficos" foram **consolidadas** em **Análise das Avaliações `[VELA-2004]`**, que reúne duas visões: **Gráficos** (uma métrica por vez, linha + resumo) e **Comparar** (avaliações do mesmo tipo lado a lado). Não há mais `comparar-avaliacoes.md` nem `evolucao.md` separados.

### 👤 Perfil
| Tela | Arquivo | Status |
|---|---|---|
| Meu Perfil | `screens/perfil/aluno/meu-perfil.md` | 🟢 CONCLUÍDO |
| Editar Perfil | `screens/perfil/aluno/editar-perfil.md` | 🟢 CONCLUÍDO |
| Minhas Metas | `screens/perfil/aluno/minhas-metas.md` | 🔴 NÃO INICIADO |
| Perfil do Aluno (visão do Treinador) | `screens/perfil/treinador/perfil-aluno-visao-treinador.md` | 🔴 NÃO INICIADO |

### 🥗 Dieta *(Pós-MVP)*
| Tela | Arquivo | Status |
|---|---|---|
| Minha Dieta | `screens/dieta/minha-dieta.md` | 🔴 NÃO INICIADO |
| Histórico de Dietas | `screens/dieta/historico-dietas.md` | 🔴 NÃO INICIADO |

### ⚙️ Configurações
| Tela | Arquivo | Status |
|---|---|---|
| Configurações | `screens/configuracoes/configuracoes.md` | 🔴 NÃO INICIADO |
| Notificações | `screens/configuracoes/notificacoes.md` | 🔴 NÃO INICIADO |

---

## Progresso Geral

- Total de telas: 37
- Concluídas: 19
- Em andamento: 0
- Pendente revisão: 0
- Não iniciadas: 18

---

## Decisões em Aberto

| # | Decisão | Impacto | Responsável | Prazo |
|---|---|---|---|---|
| 1 | Filtro de palavras ofensivas no @ interno (RN07): lista própria, biblioteca ou serviço externo? | Validação de username no cadastro/edição de perfil | ⚠️ A definir (adiado) | ⚠️ |
| 2 | Tela **Editar Perfil**: componente do seletor de **País** (ex: dropdown com busca, bandeira + nome). Exibição no Meu Perfil já definida: apenas a bandeira ao lado do @ no cabeçalho | Definição de UI/componente do campo País | ⚠️ A definir (ao mapear Editar Perfil) | ⚠️ |
| 3 | Tela **Configurações**: adicionar opção de **Idioma** (seleção de idioma do app) | Internacionalização / suporte a alunos de outras nacionalidades | ⚠️ A definir (ao mapear Configurações) | ⚠️ |
| 4 | Tela **Configurações**: adicionar opção **Alterar senha** (fluxo com código por e-mail) | Movido de Meu Perfil para Configurações | ⚠️ A definir (ao mapear Configurações) | ⚠️ |
| 5 | Tela **Configurações**: adicionar opção de **Tema/Aparência** com escolha entre **Escuro**, **Claro** ou **Seguir configuração do celular** | Suporte a dark/light mode + preferência do sistema | ⚠️ A definir (ao mapear Configurações) | ⚠️ |
| 18 | ✅ **RESOLVIDO** — **Pontos de entrada da Análise das Avaliações `[VELA-2004]`**: acesso pelo **toggle Lista/Análise** no topo da aba "Avaliações/Evolução" (entrada principal) + atalho **"Ver evolução"** no `[VELA-2002]`. **Descartados** o botão na Lista `[VELA-2001]` e o card no Perfil | Navegação de entrada do hub de análise | Cliente | 2026-06-16 |
| 6 | Tela **Configurações**: adicionar **Alterar e-mail** (com confirmação por e-mail). E-mail é somente leitura na Editar Perfil | Fluxo de alteração de e-mail | ⚠️ A definir (ao mapear Configurações) | ⚠️ |
| 7 | Onde posicionar o atalho **"Minhas Avaliações"** [VELA-2001+] — removido do Meu Perfil; definir nova localização (Dashboard? Aba própria? Outro) | Acesso ao módulo de Avaliações | ⚠️ A definir | ⚠️ |
| 8 | Tela **Cadastro**: **foto de perfil é obrigatória já no cadastro** (o perfil nunca fica sem foto; não há fallback de iniciais). Lembrar de incluir o campo foto obrigatório ao mapear o Cadastro | Fluxo de cadastro / regra de foto obrigatória | ⚠️ A capturar (ao mapear Cadastro) | ⚠️ |
| 9 | Nova tela **Perfil do Aluno (visão do Treinador)** — ainda não existe no projeto. O Treinador acessa o perfil de um aluno e clica no ícone **"+"** → é redirecionado para o **cadastro de avaliação** desse aluno. Permissões do Treinador: **apenas visualizar** + criar avaliação (+ enviar mensagem, a definir no futuro). **Somente o aluno** pode criar/editar o próprio perfil. **Abordagem decidida:** tela/documento próprio reaproveitando a base visual do Meu Perfil | Depende da role de Treinador; mapear nova tela do módulo Perfil/Avaliações | 🟢 Abordagem definida; falta mapear (depende de #10) | ⚠️ |
| 10 | **Como e onde o Treinador enxerga os perfis dos alunos** (lista de alunos? busca? a partir do cadastro de avaliação?) — ponto de entrada para o Perfil do Aluno (visão do Treinador) | Navegação do painel/visão do Treinador | ⚠️ A definir | ⚠️ |
| 11 | **Relação aluno ↔ treinador** — Opção 1: no cadastro o aluno seleciona o treinador (sistema sugere nomes, como no cadastro de avaliações). Opção 2: o treinador envia um **link/convite de cadastro pré-preenchido** com a info do treinador (exige feature "enviar link/convite" no perfil do Treinador) | Vínculo aluno-treinador + fluxo de cadastro/convite | ⚠️ A definir (futuro) | ⚠️ |
| 9 | ✅ **RESOLVIDO** — **Avaliações, permissões:** somente o **Treinador** cria/edita/exclui; pode **liberar/solicitar** avaliação ao Aluno. O **Aluno** apenas **visualiza** e **preenche** as liberadas (status Solicitada). **Atualizado em 2026-06-12 (decisão #14):** após a avaliação virar **Concluída**, ela fica **travada para o Aluno**, mas o **Treinador** pode corrigi-la via **"Revisar"** (edita no lugar, continua Concluída, sem versionamento) ou **excluir + recriar**. A ação de alterar chama-se "Editar" em Solicitada/Em andamento e "Revisar" em Concluída. Sem termos "membro/professor" | Permissões em Avaliações (`[VELA-2001]`/`[VELA-2002]`/`[VELA-2003]`) | Cliente | 2026-06-09 |
| 10 | ✅ **RESOLVIDO** — **Avaliações, exclusão:** **definitiva** (app **sem lixeira**), exclusiva do Treinador, sempre com **modal de confirmação** | UX de exclusão de avaliações | Cliente | 2026-06-09 |
| 11 | **Avaliações — tipos futuros:** por ora **apenas** Anamnese, Antropométrica, Dobras Cutâneas e Bioimpedância (cliente confirmou em 2026-06-09 que não há outros agora). A lista `[VELA-2001]` e o form `[VELA-2003]` já ficam preparados para novos tipos no futuro | Escopo dos tipos de avaliação | ⚠️ Reavaliar no futuro | ⚠️ |
| 12 | ✅ **RESOLVIDO** — **Avaliações, liberar/notificar:** ao liberar (status Solicitada), o Aluno recebe **notificação (push + in-app)** e a avaliação aparece **em destaque no topo da aba Avaliações** ("Para preencher (N)") com **badge** na Tab Bar. A liberação ocorre dentro do form `[VELA-2003]` (ação "Liberar para o aluno preencher") | Fluxo de solicitação/preenchimento de avaliação | Cliente | 2026-06-09 |
| 13 | ✅ **RESOLVIDO (notificação de avaliação)** — definido em `[VELA-2001]` RN11: **deep link** → abre a **lista `[VELA-2001]`** com o item no topo (não abre o formulário direto); **opt-out** → **in-app sempre**, só o **push** é desativável; **copy** proposto para os eventos liberada/reaberta/prazo-vencido (ajustável). ⚠️ **Resta** mapear a **tela Notificações** completa (`screens/configuracoes/notificacoes.md`): central in-app, agrupamento e demais tipos de notificação do app | Tela de Notificações / preferências de push | Cliente | 2026-06-12 |
| 17 | ✅ **RESOLVIDO** — **Reabertura de avaliação Expirada (versão leve):** o Aluno ganha o botão **"Solicitar reabertura"** em avaliações Expiradas (`[VELA-2001]` RN16 + `[VELA-2002]`), que **só notifica o Treinador** — sem novo status; quem reabre continua sendo só o Treinador (RN14) | Fluxo de reabertura de avaliação expirada | Cliente | 2026-06-12 |
| 16 | ✅ **RESOLVIDO (parcial)** — **Pontos de entrada da criação de avaliação (só Treinador, ícone "+"):** (a) **entrada global** = **FAB "+"** da **Lista de Avaliações** `[VELA-2001]` → `[VELA-2003]` com **seleção do aluno por busca**; (b) **por aluno** = **"+"** na tela de **Perfil do Aluno** → `[VELA-2003]` com **aluno travado**. ⚠️ **Pendente:** a tela **Perfil do Aluno (visão do Treinador)** ainda **não está mapeada** (`meu-perfil.md` é o perfil do próprio Aluno) — incluir o "+" do Treinador ao mapeá-la | Pontos de entrada de criação de avaliação | Cliente | 2026-06-12 |
| 15 | **Avaliações — fotos (regras técnicas):** definir quantidade (1 por slot vs. várias livres), formatos aceitos (JPG/PNG/HEIC), tamanho máximo e se há compressão automática. Hoje o `[VELA-2003]` só define os slots por ângulo (Frente/Costas/Perfis) e o anexo de laudo da Bioimpedância | Upload de fotos/laudo em avaliações | ⚠️ A definir (cliente decidir depois) | ⚠️ |
| 19 | ✅ **RESOLVIDO** — **Exercícios — ponto de entrada `[VELA-3001]`:** o Treinador acessa a Lista por (1) **aba/menu do Treinador** (modo gestão) e (2) **montagem/edição de Rotina** (modo seleção). ⚠️ Dependência: o **painel/menu do Treinador** ainda não está mapeado — confirmar o item de navegação ao mapeá-lo | Navegação de entrada do módulo Exercícios | Cliente | 2026-06-18 |
| 20 | ✅ **RESOLVIDO** — **Exercícios, atalho de vídeo na Lista `[VELA-3001]`:** abre em **modal/lightbox** com o player do YouTube **por cima da lista**, fechando e voltando à mesma posição | UX do atalho de vídeo | Cliente | 2026-06-17 |
| 21 | ✅ **RESOLVIDO** (atualizado em 2026-06-23 p/ hierarquia Exercício→Treino) — **Exercícios, exclusão e ciclo de vida:** **excluir só é permitido se o exercício não estiver em nenhum treino**; para "aposentar" um exercício em uso existe o toggle **Ativar/Desativar** — **inativo** permanece nos treinos atuais mas **não pode ser adicionado a novos** (com mensagem ao desativar). Propagado para `[VELA-3001]` (RN07/RN08), `[VELA-3002]` (RN05/RN07) e `[VELA-3003]` (RN07/RN11) | Integridade entre Exercícios e Treinos | Cliente | 2026-06-17 |
| 22 | ✅ **RESOLVIDO** — **Áudio removido do exercício:** não há campo de áudio no cadastro de exercício. A gravação de áudio passa para a **aba de Treino** — o Treinador grava no app uma instrução sobre o **treino** (não sobre um exercício específico). Detalhar ao mapear Treino | Áudio de instrução (movido para Treino) | Cliente | 2026-06-17 |
| 24 | ✅ **RESOLVIDO/OBSOLETO** — **Exercícios, equipamento:** o modelo "principal + adicionais" foi descartado. Agora é um **campo único** "Equipamentos/materiais necessários" (só o que não é óbvio no vídeo). Não há filtro por equipamento na Lista (filtros = grupo muscular + categoria) | Modelo do campo equipamento | Cliente | 2026-06-17 |
| 25 | ✅ **RESOLVIDO (`[VELA-4001]`)** — **Treinos, ordenação da Lista:** a lista segue **ordem alfabética por nome do treino** (RN02) | Ordenação da Lista de Treinos | Cliente | 2026-06-18 |
| 27 | **Exercícios — base de vídeos global:** definir origem/curadoria/gestão dessa base (quem cadastra os vídeos, busca/categorização, licenciamento) usada no campo Vídeo do `[VELA-3003]` | Conteúdo da base global de vídeos | ⚠️ A definir | ⚠️ |
| 26 | ✅ **RESOLVIDO (Treinos `[VELA-4003]`)** — **ordem dos exercícios dentro do treino:** sem campo de número manual; o Treinador **reordena por arraste (handle ⠿)** e a **numeração de execução é automática** pela posição (grupo + ordem dentro do grupo). Os grupos são **numerados (1, 2, 3…)** — as **letras A, B, C…** ficam reservadas para a **Rotina**. Revisitar só se a tela de Rotina exigir comportamento diferente | Ordenação de exercícios no treino | Cliente | 2026-06-18 |
| 23 | **Exercícios — consulta do Aluno:** detalhar a visão do Aluno (consulta/busca de exercícios, sem edição), reaproveitando Lista/Visualização | Escopo da visão do Aluno em Exercícios | ⚠️ A definir | ⚠️ |
| 28 | ✅ **RESOLVIDO** — **Exercícios, atalho "Incluir em rotina" → "Incluir em treino" `[VELA-3001]`:** firmada a hierarquia **Exercício → Treino → Rotina** (exercício nunca vai direto à Rotina; a Rotina agrupa Treinos). O atalho foi **renomeado para "Incluir em treino"**: adiciona o exercício a **um ou mais treinos em rascunho**, com **prescrição vazia** (séries/reps/descanso preenchidos depois no Treino, `[VELA-4003]`). Bottom-sheet passa a listar **treinos** ("Já no treino", "Entre no treino para finalizar"); **modo seleção** da Lista agora vem da **montagem de Treino**. Aplicado em `[VELA-3001]` (Seção 3/4, ações, RN11/RN13–RN16, fluxo) e propagado a `[VELA-3002]`/`[VELA-3003]`. `[VELA-3001]` → 🟢 CONCLUIDO | Atalho "Incluir em treino" (hierarquia Exercício→Treino) | Maria Isabela | 2026-06-23 |
| 29 | ✅ **RESOLVIDO** — **Aviso de exercícios com prescrição vazia → migra para o Treino:** com a hierarquia Exercício→Treino→Rotina, exercícios entram via atalho "Incluir em treino" **sem prescrição**. O aviso de "completar antes de salvar" deixa de pertencer à Rotina (que só agrupa treinos com prescrição já feita, `[VELA-4003]`) e passa ao **Cadastro de Treino**: ao salvar um treino com exercício sem séries/repetições/descanso, **bloquear/avisar** (espelha RN04 de `[VELA-4003]`). Substitui #28 antigo | Aviso de prescrição pendente (agora no Treino) | Maria Isabela | 2026-06-23 |
| 36 | ✅ **RESOLVIDO** — **Rotinas, estrutura do trio `[VELA-5001/5002/5003]`:** rotina = **agrupamento ordenado de treinos** (`[VELA-4001]`) por **letras A, B, C…** (arraste, letra automática); campos gerais Título + Objetivo (obrigatórios); por treino, Dia da semana + Descrição curta (opcionais). **Dia pode repetir** entre treinos; **sem visão de semana** por ora. **Mesmo treino não duplica** na rotina. Card da Lista = título + objetivo + nº de treinos + letras/nomes dos treinos. Criar+Editar consolidados em `[VELA-5003]`; Detalhe → Visualizar `[VELA-5002]` | Estrutura e regras do módulo Rotinas | Maria Isabela | 2026-06-18 |
| 37 | ✅ **RESOLVIDO (abordagem)** — **Rotinas, ponto de entrada `[VELA-5001]`:** acesso pela **aba/menu do Treinador**, espelhando #19 (Exercícios) e #30 (Treinos). ⚠️ Dependência: o **painel/menu do Treinador** ainda não está mapeado — confirmar o item de navegação ao mapeá-lo | Navegação de entrada do módulo Rotinas | Maria Isabela | 2026-06-18 |
| 38 | ✅ **RESOLVIDO (mapeado em `[VELA-3004]`)** — **Rotinas — atrelar rotina a aluno:** mapeada a tela **Atrelar Rotina ao Aluno `[VELA-3004]`** (🔵 MVP). Entrada por **ambos os caminhos** (pré-selecionado pela tela do aluno / entrada geral com busca; + "Atribuir a aluno" da **Visualizar `[VELA-5002]`**, mantendo o Cadastro `[VELA-5003]` em "modo construção"). Origem: rotina da **base** (`[VELA-5001]`) ou **criada na hora** (`[VELA-5003]`, **sempre salva na base**). Vínculo = **cópia/snapshot** (edições na base não afetam entregas). **Vigência:** início obrigatório, fim **opcional/sem prazo**. Prescrição herdada **ajustável, não obrigatória** (aviso não bloqueia). Rotinas **coexistem** (sem substituição). Pós-salvar volta à **tela do aluno**. **Atualizado em 2026-06-24:** **trava de exclusão por vínculo encerrada** — como a atribuição é **cópia/snapshot** (RN04), excluir a rotina-base **não afeta** a entrega; **não há trava** e o `[VELA-5003]` **não foi reaberto** (RN11 do `[VELA-3004]`). **Notificação ao aluno** (push + in-app) ao atribuir vira **nota de escopo** no `[VELA-3004]`, dependente da tela **Notificações** ainda não mapeada (decisão #13). Tela `[VELA-3004]` → 🟢 CONCLUIDO | Atrelamento de rotina a aluno | Maria Isabela | 2026-06-24 |
| 14 | ✅ **RESOLVIDO** — **Avaliação Concluída:** travada para o **Aluno**; o **Treinador** corrige via **"Revisar"** (edita **no lugar**, continua Concluída, **sem versionamento/histórico** — Q1=A) **ou** **excluir + recriar** (ambas convivem — Q2=B). Ação de alterar = "Editar" (Solicitada/Em andamento) / "Revisar" (Concluída). Propagado para `[VELA-2001]` (RN04/RN06/RN09), `[VELA-2002]` (RN04 + ações) e `[VELA-2003]` (Seção 1/2/3.1, RN05/RN13). Atualiza a decisão #9 | Edição/trava de avaliações Concluídas | Cliente | 2026-06-12 |
| 30 | ✅ **RESOLVIDO (abordagem)** — **Treinos `[VELA-400x]`, ponto de entrada:** a Lista de Treinos (`[VELA-4001]`) é acessada pela **aba/menu do Treinador** (gestão). A escolha de treinos para uma Rotina **não** abre esta tela — é feita pelo **seletor de treinos** próprio da montagem de Rotina (`[VELA-5003]`). ⚠️ Dependência: o **painel/menu do Treinador** ainda não está mapeado — confirmar o item de navegação ao mapeá-lo | Navegação de entrada do módulo Treinos (Treinador) | Cliente | 2026-06-18 |
| 31 | ✅ **RESOLVIDO** — **Treinos, salvar/ciclo de vida `[VELA-4003]`:** salvar exige **Nome + Categoria + ≥1 exercício**, e cada exercício deve ter **Séries + Repetições + Descanso** (obrigatórios; descrição de execução opcional) — **a prescrição é feita já no treino** (atualização: antes ficava para a Rotina). Exclusão **definitiva** (sem lixeira, com modal) **só se o treino não estiver em nenhuma rotina**; para aposentar em uso, toggle **Ativar/Desativar** (espelha #21). **Interino:** enquanto **Rotinas** não existir, não há vínculo a checar → exclusão **sempre liberada** (com modal); a trava por rotina passa a valer quando o módulo existir | Regras de salvar e exclusão de treinos | Cliente | 2026-06-18 |
| 32 | ✅ **RESOLVIDO** — **Treinos, agrupamento de exercícios `[VELA-4003]`:** **grupos numerados** (número automático 1, 2, 3…) com **tipo opcional**. Ordem por grupo e por exercício dentro do grupo (arrastar). **Lista de tipos:** Normal, Bi-set, Tri-set, Superset, Drop-set (Circuito **removido**). **Limite por tipo:** Normal/Drop-set = 1, Bi-set/Superset = 2, Tri-set = 3; **sem tipo = Normal (1)** | Modelo de agrupamento de exercícios no treino | Cliente | 2026-06-18 |
| 33 | ✅ **RESOLVIDO (`[VELA-4001]`)** — **Treinos, card da Lista:** nome + **categoria e quantidade de exercícios lado a lado** (ex: "Hipertrofia · 6 exercícios") + selo Ativo/Inativo. **Sem chips de grupos musculares** (removidos a pedido do cliente) | Formato do card da Lista de Treinos | Cliente | 2026-06-18 |
| 34 | ✅ **RESOLVIDO** — **Treinos, colisão de nome "Lista de Treinos":** resolvida pela **separação por público em subpastas** (decisão #42): `treinos/treinador/lista-treinos.md` (`[VELA-4001]`) vs `treinos/aluno/lista-treinos.md` (fluxo treinar). Sem necessidade de renomear | Nomenclatura/colisão de telas no módulo Treinos | Maria Isabela | 2026-06-22 |
| 35 | ✅ **RESOLVIDO (`[VELA-4001]`)** — **Treinos, revisão da Lista após Rotinas:** com Rotinas concluído (`[VELA-5003]`), fechados a **trava de exclusão por vínculo com rotina** (RN04, removida a cláusula interina → treino em rotina não exclui, oferece Desativar) e o atalho **"Incluir em rotina"** (RN07–RN10). O **"modo seleção" foi removido** desta tela — a escolha de treinos para a Rotina é descrita como **seletor de treinos** próprio de `[VELA-5003]` (sem duplicar a tela). Tela → 🟢 CONCLUIDO | Revisão da Lista de Treinos pós-Rotinas | Maria Isabela | 2026-06-24 |
| 39 | ✅ **RESOLVIDO (abordagem)** — **Rotinas, visão do Aluno `[VELA-6001]`:** mapeada **Minhas Rotinas** (🔵 MVP, nova série **6xxx**), leitura das rotinas atribuídas em seções Ativas/Agendadas/Anteriores; status calculado das datas; múltiplas ativas possíveis. ⚠️ **Pendente:** (a) o **ponto de entrada** depende do **dashboard/menu do Aluno**, ainda não mapeado (espelha #37/#30/#19). **(b) ✅ mapeado:** o **Detalhe da Rotina (Aluno) `[VELA-6002]`** (destino ao tocar no card) — tela própria do Aluno, **não** reusa a Visualizar do Treinador `[VELA-5002]` — está 🟡 EM ANDAMENTO. **Novo:** o destino de toque no treino é a **tela de treino do Aluno** (`treinos/aluno/`, ainda sem código), nova dependência rastreada em #44 | Navegação e detalhe da visão do Aluno em Rotinas | Maria Isabela | 2026-06-22 |
| 40 | ✅ **RESOLVIDO** — **Rotinas — visibilidade de prazo/progresso ao aluno (`[VELA-3004]` + `[VELA-6001]`):** adicionado o toggle **"Mostrar prazo e progresso ao aluno"** no `[VELA-3004]` (Bloco C, campo #6, RN10), **ligado por padrão** — quando desligado, o Aluno vê só o selo de status. Não afeta o contador de treinos realizados (#41). Reflexo de leitura já em `[VELA-6001]` RN05 e `[VELA-6002]` Bloco B. Mockup sincronizado | Controle de visibilidade da vigência para o aluno | Maria Isabela | 2026-06-24 |
| 41 | ✅ **RESOLVIDO (reincorporado ao MVP)** — **Rotinas — contador na visão do Aluno (`[VELA-6001]`):** o card exibe **"X treinos realizados"** (RN06), alimentado pelo **registro de execução (sessão)** do `[VELA-6003]` (decisão #49). A pedido da cliente, o card é **enxuto**: **sem barra de progresso** (RN04) e **sem contagem de exercícios** — ambas ficam no Detalhe `[VELA-6002]`. Agendadas não exibem contador; independe do toggle de visibilidade (#40/RN05) | Contador de execução no card de rotina do aluno | Maria Isabela | 2026-06-22 |
| 43 | ✅ **RESOLVIDO (aplicado em `[VELA-6002]`)** — **Rotinas — tag de categoria do treino na visão do Aluno:** o **Detalhe da Rotina (Aluno) `[VELA-6002]`** inclui uma **tag de categoria** (core, fortalecimento, hipertrofia…) **em cada card de treino** (ex.: "A · Peito · hipertrofia"), espelhando a Visualizar do Treinador `[VELA-5002]` (RN07). **Não** vai no card da lista `[VELA-6001]` — categoria é atributo do treino (1 treino = 1 categoria); rotina tem treinos de categorias possivelmente distintas, e o card da lista segue o padrão enxuto do `[VELA-5001]` (RN04) | Exibição de categoria do treino na visão do Aluno | Maria Isabela | 2026-06-22 |
| 44 | **Rotinas — destino do treino na visão do Aluno (`[VELA-6002]`):** ao tocar num card de treino no Detalhe da Rotina, o Aluno vai para a **tela de treino do Aluno** (`treinos/aluno/`, ticket cliente `VELA-5002`), responsável por consulta/execução. Essa tela ainda **não foi mapeada/codificada** — dependência; confirmar qual tela do fluxo do Aluno (visualizar/iniciar) é o destino ao mapeá-la (RN08 do `[VELA-6002]`) | Destino de navegação treino na visão do Aluno | ⚠️ A definir (ao mapear o fluxo de treino do Aluno) | ⚠️ |
| 45 | **Rotinas — conteúdo de execução no Detalhe (`[VELA-6002]`):** **Treinos executados / Exercícios executados**, o bloco **"último treino executado"** e o **nº de execuções por treino** (no card, ao lado do contador de exercícios — RN09) ficam **fora do MVP** desta tela; dependem do **registro de execução do Aluno** (Treino em Andamento / Histórico), ainda não mapeado. No MVP o topo exibe só **KPIs de data** (dias percorridos/restantes) + barra de vigência. Reavaliar quando a fonte existir (relacionado a #41) | Conteúdo de execução no detalhe da rotina do aluno | ⚠️ A reavaliar (depende do fluxo de execução) | ⚠️ |
| 46 | ✅ **RESOLVIDO (composição)** — **Treino do Aluno — card-resumo compartilhável (`[VELA-6003]`):** card estilo story com **primeiro nome do aluno** + nome do treino + **selo de trilha** (`.track`/`.performance`) + **duração, exercícios, treinos na semana** + data + marca `vela.` (sem foto; recado fora da imagem — RN11). Tocar em Compartilhar mostra **pré-visualização no app + folha de destinos do sistema**. ⚠️ Resta só: **formatos/resolução de export** da imagem (story 9:16, feed, etc.) | Compartilhamento social pós-treino | Maria Isabela | 2026-06-22 |
| 47 | ✅ **RESOLVIDO** — **Treino do Aluno — formato de execução (`[VELA-6003]`):** **lista vertical estilo MFit** (rolagem com cards por grupo numerado), reaproveitando a estrutura da Visualizar do Treinador `[VELA-4002]`. O **feed vertical / reels** (ideia ZeroUm) foi **descartado** para o MVP por custo de UX/dev | Formato de apresentação dos exercícios na execução | Maria Isabela | 2026-06-22 |
| 48 | **Treino do Aluno — som de repetição (`[VELA-6003]`):** som configurável estilo box de CrossFit como auxílio durante o exercício — **fora do MVP** (RN09); reavaliar em iteração futura | Recurso de áudio de cadência na execução | ⚠️ A reavaliar (pós-MVP) | Maria Isabela |
| 49 | ✅ **RESOLVIDO (destrava #41/#45)** — **Modelo de execução (sessão) do Aluno definido em `[VELA-6003]` (RN04):** registro com data, hora início/fim, duração, exercícios concluídos e séries/reps/carga realizadas, gerado ao **Finalizar treino** (Iniciar/Finalizar explícitos + persistência parcial retomável, RN03). É a **fonte** dos KPIs "treinos/exercícios executados", do bloco "último treino executado" e do "nº de execuções por treino" antes adiados em `[VELA-6002]` (#45) e `[VELA-6001]` (#41) — que podem ser **reincorporados ao MVP** dessas telas agora que a fonte existe (revisitar `[VELA-6001]`/`[VELA-6002]`) | Modelo de registro de execução do Aluno | Maria Isabela | 2026-06-22 |
| 50 | **Carga prescrita no treino (impacto em `[VELA-4003]`/`[VELA-4002]`):** decidido na entrevista da `[VELA-6003]` que o **treinador informa a carga sugerida** por exercício (o aluno sobrescreve na execução se usar diferente — RN06/RN10). Hoje o Cadastro de Treino prescreve **Séries/Reps/Descanso**, **sem carga** — precisa **adicionar campo de carga** ao `[VELA-4003]` (e exibir em leitura no `[VELA-4002]`). ⚠️ A definir: carga por série ou única por exercício, unidade (kg), e se é obrigatória ou opcional na prescrição | Campo de carga na prescrição do treino | ⚠️ A incluir ao revisar `[VELA-4003]`/`[VELA-4002]` | Maria Isabela |
| 51 | ✅ **RESOLVIDO** — **Feedback do aluno em dois níveis:** (a) **recado por treino** ao finalizar a execução — campo opcional, **máx. 300 caracteres**, **privado** ao treinador, fora do card compartilhável (`[VELA-6003]` RN11); (b) **considerações por rotina** quando a rotina fica **Encerrada** (vigência terminou) — campo opcional, **máx. 500 caracteres**, privado ao treinador (`[VELA-6002]` Bloco E / RN10). Gatilho do (b) = **vigência encerrada** (rotinas sem data de fim não disparam). ⚠️ Dependência (ambos): a **leitura pelo treinador** ocorre na visão do treinador sobre o aluno (ainda a mapear, junto dos KPIs de execução) | Canais de feedback do aluno (treino e rotina) | Maria Isabela | 2026-06-22 |
| 52 | ✅ **RESOLVIDO** — **Treino do Aluno — KPI "treinos na semana" no resumo (`[VELA-6003]` RN12):** o resumo troca "total de séries" por **treinos executados na semana / total de treinos da base do aluno** (ex.: 1/5). **"Semana" = segunda a sexta** da semana corrente (sáb/dom não contam; zera toda segunda). **Base (denominador) = soma dos treinos de todas as rotinas ativas** do aluno. Depende do registro de execução (RN04/#49) | Métrica semanal no resumo do treino | Maria Isabela | 2026-06-23 |
| 53 | ✅ **RESOLVIDO (atualizado — bloco único)** — **Editor do card de compartilhamento (`[VELA-6003]` RN13):** card estilo "stats sobre foto" (ref. Strava). **Fundo** = padrão do app ou **foto da câmera** (galeria = MVP futuro, não exibida). **Único fixo:** marca **`vela.` em destaque, centralizada no rodapé** — **selo de trilha removido** (foco em divulgação). **Bloco único** (nome do aluno, nome do treino, métricas, data/hora) que o aluno **move e redimensiona junto**; itens internos **ocultáveis/readicionáveis** via bandeja (substitui o modelo anterior de zonas/snap e blocos independentes). Card inclui **data + hora**. **Ícones de linha (não emoji), brancos**; destaque só na marca; fonte/cores **não editáveis**. ⚠️ Resta: **câmera no app** (captura) e **formatos de export** (#46) | Editor/UX do card de compartilhamento | Maria Isabela | 2026-06-23 |
| 54 | ✅ **RESOLVIDO** — **Treino do Aluno — fluxo de compartilhamento consolidado (`[VELA-6003]`):** o sub-fluxo passou de **3 telas** (escolher fundo + pré-visualização + modo edição) para **1 só** — **Editor único** com **fundo + texto na mesma tela** (card editável no topo; faixa de fundo "Tirar foto" + fundos do app na base; botão Compartilhar). Os **destinos** (Story Instagram/WhatsApp/Salvar) viram **folha do sistema em overlay** sobre o editor, não uma tela nova. O **Resumo** segue como porta de entrada (celebração + recado + Compartilhar/Concluir) | Fluxo de compartilhamento pós-treino | Maria Isabela | 2026-06-23 |
| 42 | ✅ **RESOLVIDO** — **Estrutura, separação Aluno × Treinador:** nos módulos que misturam os dois públicos, as telas ficam em **subpastas por público** (`<modulo>/treinador/` e `<modulo>/aluno/`), espelhado em `mockups/`. Aplicado a **rotinas, treinos e perfil**. Módulos de público único ficam sem subpasta até ganharem telas do outro público. Convenção registrada no `CLAUDE.md` | Organização de pastas por público (Aluno/Treinador) | Maria Isabela | 2026-06-22 |

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
| Tela | Arquivo | Status |
|---|---|---|
| Lista de Treinos | `screens/treinos/lista-treinos.md` | 🔴 NÃO INICIADO |
| Iniciar Treino | `screens/treinos/iniciar-treino.md` | 🔴 NÃO INICIADO |
| Treino em Andamento | `screens/treinos/treino-andamento.md` | 🔴 NÃO INICIADO |
| Finalizar Treino | `screens/treinos/finalizar-treino.md` | 🔴 NÃO INICIADO |
| Histórico de Treinos | `screens/treinos/historico.md` | 🔴 NÃO INICIADO |
| Detalhe do Treino | `screens/treinos/detalhe-treino.md` | 🔴 NÃO INICIADO |

### 📋 Rotinas
| Tela | Arquivo | Status |
|---|---|---|
| Lista de Rotinas | `screens/rotinas/lista-rotinas.md` | 🔴 NÃO INICIADO |
| Criar Rotina | `screens/rotinas/criar-rotina.md` | 🔴 NÃO INICIADO |
| Editar Rotina | `screens/rotinas/editar-rotina.md` | 🔴 NÃO INICIADO |
| Detalhe da Rotina | `screens/rotinas/detalhe-rotina.md` | 🔴 NÃO INICIADO |

### 🏋️ Exercícios
| Tela | Arquivo | Status |
|---|---|---|
| Lista de Exercícios `[VELA-3001]` | `screens/exercicios/lista-exercicios.md` | 🟡 EM ANDAMENTO |
| Visualizar Exercício `[VELA-3002]` | `screens/exercicios/visualizar-exercicio.md` | 🟡 EM ANDAMENTO |
| Cadastro / Edição de Exercício `[VELA-3003]` | `screens/exercicios/cadastro-exercicio.md` | 🟢 CONCLUIDO |

> **Nota:** as telas previstas "Catálogo de Exercícios", "Detalhe do Exercício" e "Busca de Exercícios" (pensadas para o Aluno montar rotina) foram **substituídas** pelo trio na **visão do Treinador**: Lista `[VELA-3001]`, Visualizar `[VELA-3002]` e Cadastro/Edição `[VELA-3003]`. **Não há acervo global de exercícios** — todo exercício é **criado pelo Treinador** (que edita/exclui os seus). A única base global do app é a **base de vídeos** (usada no campo Vídeo do cadastro: escolher da base ou colar link do YouTube). A busca da Lista é normalizada (sem acentos/minúsculas). A consulta do **Aluno** reaproveitará Lista/Visualização e será detalhada depois. Séries/reps/carga **não** ficam no exercício — são prescritas na Rotina.

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
| Meu Perfil | `screens/perfil/meu-perfil.md` | 🟢 CONCLUÍDO |
| Editar Perfil | `screens/perfil/editar-perfil.md` | 🟢 CONCLUÍDO |
| Perfil do Aluno (visão do Treinador) | `screens/perfil/perfil-aluno-visao-treinador.md` | 🔴 NÃO INICIADO |
| Minhas Metas | `screens/perfil/minhas-metas.md` | 🔴 NÃO INICIADO |

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

- Total de telas: 32
- Concluídas: 4
- Em andamento: 4
- Pendente revisão: 0
- Não iniciadas: 24

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
| 19 | **Exercícios — ponto de entrada `[VELA-3001]`:** onde o Treinador acessa a Lista de Exercícios. Acessos previstos: (1) ao montar/editar uma Rotina (seleção de exercícios); (2) aba/menu do Treinador (depende do painel do Treinador, ainda não mapeado) | Navegação de entrada do módulo Exercícios | ⚠️ A definir | ⚠️ |
| 20 | ✅ **RESOLVIDO** — **Exercícios, atalho de vídeo na Lista `[VELA-3001]`:** abre em **modal/lightbox** com o player do YouTube **por cima da lista**, fechando e voltando à mesma posição | UX do atalho de vídeo | Cliente | 2026-06-17 |
| 21 | ✅ **RESOLVIDO** — **Exercícios, exclusão e ciclo de vida:** **excluir só é permitido se o exercício não estiver em nenhuma rotina**; para "aposentar" um exercício em uso existe o toggle **Ativar/Desativar** — **inativo** permanece nas rotinas atuais mas **não pode ser adicionado a novas** (com mensagem ao desativar). Propagado para `[VELA-3001]` (RN10/RN11), `[VELA-3002]` (RN05/RN07) e `[VELA-3003]` (RN07/RN11) | Integridade entre Exercícios e Rotinas | Cliente | 2026-06-17 |
| 22 | ✅ **RESOLVIDO** — **Áudio removido do exercício:** não há campo de áudio no cadastro de exercício. A gravação de áudio passa para a **aba de Treino** — o Treinador grava no app uma instrução sobre o **treino** (não sobre um exercício específico). Detalhar ao mapear Treino | Áudio de instrução (movido para Treino) | Cliente | 2026-06-17 |
| 24 | ✅ **RESOLVIDO/OBSOLETO** — **Exercícios, equipamento:** o modelo "principal + adicionais" foi descartado. Agora é um **campo único** "Equipamentos/materiais necessários" (só o que não é óbvio no vídeo). Não há filtro por equipamento na Lista (filtros = grupo muscular + categoria) | Modelo do campo equipamento | Cliente | 2026-06-17 |
| 25 | **Treinos — ordenação da Lista de Treinos:** o Treinador define a sequência (Treino A, B, C...) ao criar; a lista segue **ordem alfabética considerando a sequência definida**. Detalhar ao mapear a Lista de Treinos | Ordenação da Lista de Treinos | ⚠️ A definir (ao mapear Treinos) | ⚠️ |
| 27 | **Exercícios — base de vídeos global:** definir origem/curadoria/gestão dessa base (quem cadastra os vídeos, busca/categorização, licenciamento) usada no campo Vídeo do `[VELA-3003]` | Conteúdo da base global de vídeos | ⚠️ A definir | ⚠️ |
| 26 | **Rotinas/Treinos — ordem dos exercícios dentro do treino:** ao montar o treino/rotina, o Treinador **numera cada linha de cards** na ordem que o Aluno deve seguir. Detalhar ao mapear Criar/Editar Rotina | Ordenação de exercícios no treino | ⚠️ A definir (ao mapear Rotinas) | ⚠️ |
| 23 | **Exercícios — consulta do Aluno:** detalhar a visão do Aluno (consulta/busca de exercícios, sem edição), reaproveitando Lista/Visualização | Escopo da visão do Aluno em Exercícios | ⚠️ A definir | ⚠️ |
| 14 | ✅ **RESOLVIDO** — **Avaliação Concluída:** travada para o **Aluno**; o **Treinador** corrige via **"Revisar"** (edita **no lugar**, continua Concluída, **sem versionamento/histórico** — Q1=A) **ou** **excluir + recriar** (ambas convivem — Q2=B). Ação de alterar = "Editar" (Solicitada/Em andamento) / "Revisar" (Concluída). Propagado para `[VELA-2001]` (RN04/RN06/RN09), `[VELA-2002]` (RN04 + ações) e `[VELA-2003]` (Seção 1/2/3.1, RN05/RN13). Atualiza a decisão #9 | Edição/trava de avaliações Concluídas | Cliente | 2026-06-12 |

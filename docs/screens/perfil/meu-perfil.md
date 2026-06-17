# Tela: Meu Perfil

---

## Metadados
| Campo | Valor |
|---|---|
| **Nome da tela** | Meu Perfil |
| **Modulo** | Perfil |
| **Prioridade** | 🔵 MVP |
| **Status** | 🟢 CONCLUIDO |
| **Ultima atualizacao** | 2026-06-17 |

---

## 1. Objetivo da Tela
> O que o usuario consegue fazer nesta tela? Qual problema ela resolve?

Esta tela e o hub do perfil do Aluno. Permite que o Aluno **visualize seus dados pessoais e a foto de perfil**, acesse a **edicao do perfil** e **saia da conta** (logout). Esta e uma tela de visualizacao: a edicao de dados e da foto acontece em tela separada (Editar Perfil).

---

## 2. Quem Acessa / Pre-condicoes
> Quem pode ver esta tela? Quais condicoes precisam ser verdadeiras?

- **Usuario:** Aluno autenticado (visualiza apenas o proprio perfil; nao acessa perfil de terceiros)
- **Pre-condicoes:**
  - Usuario deve estar logado
  - Nenhuma outra pre-condicao
- **Permissoes especiais:** Nenhuma

---

## 3. Layout e Componentes Visuais
> Descreva a estrutura visual da tela de cima para baixo.

### 3.1 Header / Cabecalho
- Conteudo: Titulo "Meu Perfil" + botao **"Editar perfil"** (acesso a tela Editar Perfil) + icone de **engrenagem** (acesso a Configuracoes)
- Comportamento: Fixo no topo

### 3.2 Corpo Principal
> Descrever secoes da tela, na ordem que aparecem

**Secao 1 — Foto e Identificacao (Cabecalho do perfil)**
- Componente: Avatar (foto de perfil) + bloco de identificacao
- Conteudo:
  - Foto de perfil
  - Nome completo
  - Linha com **@ aluno.vela + bandeira do pais** ao lado do @ (apenas a bandeira, sem o nome do pais)
  - Objetivo (somente leitura — proveniente da Anamnese) — exibido **abaixo** do @/bandeira
- Comportamento: Apenas exibicao. A foto nao e editavel nesta tela (gerenciamento da foto ocorre na tela Editar Perfil).

**Secao 2 — Dados Pessoais**
- Componente: Lista de campos (somente leitura)
- Conteudo:
  - E-mail
  - WhatsApp
  - Data de nascimento
  - Sexo
  - @ instagram
  - @ treinador.vela (somente leitura — referencia ao treinador vinculado)
- Comportamento: Apenas exibicao; a alteracao ocorre na tela Editar Perfil

**Secao 3 — Sair**
- Componente: Botao de acao
- Conteudo: Botao **"Sair"** (logout), centralizado
- Comportamento: Acao de logout com confirmacao

### 3.3 Footer / Rodape
- Conteudo: Barra de navegacao inferior com a aba "Perfil" ativa
- Comportamento: Fixo na parte inferior

---

## 4. Campos e Formularios

> Preencher apenas se a tela tiver campos de entrada (inputs, selects, etc.)

N/A — Tela sem formularios. Todos os campos sao exibidos em modo somente leitura. A entrada/edicao de dados ocorre na tela **Editar Perfil**.

### Regras de Preenchimento
- N/A nesta tela (visualizacao). As regras de preenchimento dos dados pessoais e do @ aluno.vela serao documentadas na tela Editar Perfil (ver RN nesta tela para o @ aluno.vela).
- O campo **Sexo** sera editavel na tela Editar Perfil com as opcoes: **Feminino**, **Masculino** e **Nao Informar**.
- O campo **Pais** sera editavel na tela Editar Perfil (selecao de pais — suporte a alunos de diferentes nacionalidades).

---

## 5. Botoes e Acoes

| # | Componente | Label / Icone | Posicao | Estado Inicial | Acao ao Clicar |
|---|---|---|---|---|---|
| 1 | Botao | "Editar perfil" | Header (direita) | Ativo | Navega para a tela Editar Perfil |
| 2 | Icone | Engrenagem (⚙) | Header (direita) | Ativo | Navega para a tela Configuracoes |
| 3 | Botao | "Sair" | Secao 3 (centralizado, ao final) | Ativo | Abre modal de confirmacao "Deseja sair?" → ao confirmar ("Sim, quero sair"), efetua logout → navega para a tela de Login |

---

## 6. Estados da Tela

### 6.1 Estado Inicial / Vazio
- Tela exibe os dados do Aluno carregados do backend.
- Nao ha estado vazio de dados (perfil sempre possui dados minimos do cadastro/onboarding).

### 6.2 Estado de Carregamento (Loading)
- **Carregar a tela:** skeleton loader nas secoes de foto e dados pessoais enquanto os dados sao buscados.

### 6.3 Estado de Erro
- **Erro ao carregar dados:** mensagem de erro com botao "Tentar novamente" (retry).
- **Erro de rede:** toast na parte superior "Sem conexao. Tente novamente."

### 6.4 Estado de Sucesso
- N/A — Esta tela e apenas de visualizacao; nao ha acoes que gerem estado de sucesso (alteracoes ocorrem na tela Editar Perfil).

### 6.5 Estado Desabilitado / Bloqueado *(se aplicavel)*
- N/A — Nao ha acoes editaveis nesta tela.

---

## 7. Fluxo de Navegacao

### De onde o usuario chega nesta tela
| Origem | Gatilho |
|---|---|
| Barra de navegacao inferior | Toca na aba "Perfil" |
| Dashboard / Home | Atalho/avatar de perfil (quando disponivel) |

### Para onde o usuario pode ir desta tela
| Destino | Gatilho |
|---|---|
| Editar Perfil | Clica em "Editar perfil" no header |
| Configuracoes | Clica no icone de engrenagem |
| Login | Clica em "Sair" e confirma no modal ("Sim, quero sair") |

---

## 8. Regras de Negocio
> Regras especificas que impactam o comportamento desta tela.

- **RN01:** O Aluno visualiza apenas o proprio perfil; nao tem acesso ao perfil de outros usuarios.
- **RN02:** A foto de perfil e apenas exibida nesta tela; sua edicao ocorre na tela **Editar Perfil**. A foto definida na Editar Perfil e exibida aqui. Como a foto e obrigatoria desde o cadastro, o perfil sempre tem foto.
- **RN03:** O **@ aluno.vela** e **unico** em todo o sistema. Nao podem existir dois usuarios com o mesmo @.
- **RN04:** O **@ aluno.vela** pode ser alterado pelo Aluno (na tela Editar Perfil). Ao ser alterado, a mudanca deve refletir **automaticamente em todos os lugares do app** que fazem mencao ao @.
- **RN05:** Antes de salvar uma alteracao do **@ aluno.vela**, o sistema deve **validar a unicidade** — se ja existir outro usuario com aquele @, bloquear o salvamento e informar o Aluno.
- **RN06:** Padrao do **@ aluno.vela**: apenas **letras minusculas e numeros**, **sem espacos** e **sem outros caracteres especiais**. Nao pode conter **palavras ofensivas**. Recomenda-se que seja o nome, apelido ou similar do Aluno.
- **RN07:** O **@ treinador.vela** e exibido em modo somente leitura (referencia ao treinador vinculado ao Aluno).
- **RN08:** O **Objetivo** exibido provem da **Anamnese** do Aluno (somente leitura nesta tela).
- **RN09:** O campo **Sexo** possui as opcoes **Feminino**, **Masculino** e **Nao Informar** (selecionaveis na tela Editar Perfil).
- **RN10:** A acao "Sair" (logout) exige **confirmacao** do Aluno: exibir modal com opcao "Sim, quero sair" e opcao de cancelar. O logout so ocorre apos a confirmacao.

---

## 9. Responsividade (Mobile vs Web)
> Diferencas de comportamento ou layout entre plataformas.

| Aspecto | Mobile | Web |
|---|---|---|
| Regras e comportamento | Identico | Identico |
| Layout | Tela cheia, secoes empilhadas | Conteudo centralizado com largura maxima; secoes podem usar colunas |

> As regras e o padrao de comportamento sao os mesmos em ambas as plataformas; apenas ajustes visuais e de layout sao aplicados.

---

## 10. Acessibilidade
> Consideracoes de acessibilidade para esta tela.

- Labels acessiveis em todos os itens e botoes.
- Texto alternativo na foto de perfil (ex: "Foto de perfil de [Nome]").
- Contraste de cores conforme WCAG 2.1 AA.
- Navegacao por teclado (tab order logica) no web.
- Area de toque adequada para os botoes no mobile.
- Mensagens de erro (toasts) tambem anunciadas por leitores de tela.

---

## 11. Historico de Alteracoes

| Data | Autor | Descricao |
|---|---|---|
| 2026-06-08 | Equipe FitnessApp | Criacao inicial do documento (entrevista de mapeamento) |
| 2026-06-08 | Equipe FitnessApp | Revisao: objetivo movido para o cabecalho do perfil; removidos peso/altura, @ aluno.vela e objetivo dos Dados Pessoais; renomeados campos (@ aluno.vela, @ instagram, @ treinador.vela, WhatsApp, Sexo); "Alterar senha" removido (ira para Configuracoes); secao "Conta" removida, restando apenas botao "Sair" centralizado |
| 2026-06-08 | Equipe FitnessApp | Adicionado campo "Pais" aos Dados Pessoais (suporte a alunos de diferentes nacionalidades) |
| 2026-06-08 | Equipe FitnessApp | Pais passa a ser exibido como bandeira no cabecalho ao lado do @ aluno.vela; objetivo movido para baixo do @/bandeira; removido item "Pais" da lista de Dados Pessoais (evitar duplicidade) |
| 2026-06-08 | Equipe FitnessApp | Removido o atalho "Minhas Avaliacoes" (local sera decidido depois); objetivo da tela atualizado; tela marcada como CONCLUIDA |
| 2026-06-08 | Equipe FitnessApp | Gerenciamento da foto (alterar/remover) movido exclusivamente para a tela Editar Perfil; nesta tela a foto passa a ser apenas exibida. Ajustados: objetivo, Secao 1, tabela de botoes, estados (6.2-6.5), RN01/RN02, responsividade e acessibilidade |
| 2026-06-08 | Equipe FitnessApp | Removida a regra de "avatar com iniciais quando nao ha foto" (RN antiga + mencoes na Secao 1 e estado inicial); RNs renumeradas |
| 2026-06-08 | Equipe FitnessApp | Reintroduzida a regra de iniciais do nome quando nao ha foto, agora como regra global RG01 (sem placeholder/foto generica); referenciada na Secao 1 e RN03 |
| 2026-06-08 | Equipe FitnessApp | Limpeza: removidas as mencoes/referencias repetidas a iniciais (Secao 1 e RN proprio); comportamento mantido apenas na regra global RG01; RNs renumeradas |
| 2026-06-08 | Equipe FitnessApp | Removida definitivamente a opcao de perfil sem foto/iniciais: foto e obrigatoria desde o cadastro, perfil sempre tem foto. Excluida a regra global RG01 |
| 2026-06-17 | Equipe Vela | Revisao final: status -> CONCLUIDO; data de atualizacao atualizada; acessibilidade limpa (removidas mencoes a "menu" e a feedback de "sucesso" inexistentes nesta tela) |
| 2026-06-17 | Equipe Vela | Removido o "Nome completo" duplicado dos Dados Pessoais (mantido apenas no cabecalho), seguindo o padrao de evitar duplicidade |

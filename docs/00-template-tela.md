# Template de Tela — [NOME DA TELA]

> **Instruções:** Copie este arquivo para a pasta correspondente, renomeie e preencha todos os campos.
> Campos marcados com ⚠️ PENDENTE precisam ser resolvidos antes de considerar a tela como concluída.

---

## Metadados
| Campo | Valor |
|---|---|
| **Nome da tela** | |
| **Módulo** | ex: Autenticação, Treinos |
| **Status** | 🔴 NÃO INICIADO |
| **Última atualização** | |

---

## 1. Objetivo da Tela
> O que o usuário consegue fazer nesta tela? Qual problema ela resolve?

_Descrever em 2-3 frases o propósito desta tela._

---

## 2. Quem Acessa / Pré-condições
> Quem pode ver esta tela? Quais condições precisam ser verdadeiras?

- **Usuário:** ex: Aluno autenticado / Visitante / Qualquer usuário
- **Pré-condições:**
  - ex: Usuário deve estar logado
  - ex: Deve ter ao menos uma rotina cadastrada
- **Permissões especiais:** ex: Nenhuma / Plano Premium

---

## 3. Layout e Componentes Visuais
> Descreva a estrutura visual da tela de cima para baixo.

### 3.1 Header / Cabeçalho
- Conteúdo: ex: Botão voltar + Título "Login" + ícone de ajuda
- Comportamento: ex: Fixo no topo / Scroll junto com conteúdo

### 3.2 Corpo Principal
> Descrever seções da tela, na ordem que aparecem

**Seção 1 — [Nome]**
- Componente: ex: Card, Lista, Formulário, Carrossel
- Conteúdo: ex: Lista de exercícios com nome, grupo muscular e imagem
- Comportamento: ex: Scroll vertical infinito

**Seção 2 — [Nome]**
- ...

### 3.3 Footer / Rodapé
- Conteúdo: ex: Barra de navegação inferior / Botão de ação flutuante (FAB)
- Comportamento: ex: Fixo na parte inferior

---

## 4. Campos e Formulários

> Preencher apenas se a tela tiver campos de entrada (inputs, selects, etc.)

| # | Nome do Campo | Tipo | Obrigatório | Placeholder | Validação | Mensagem de Erro |
|---|---|---|---|---|---|---|
| 1 | ex: E-mail | Text / Email | Sim | "seu@email.com" | Formato de e-mail válido | "Digite um e-mail válido" |
| 2 | ex: Senha | Password | Sim | "Sua senha" | Mínimo 8 caracteres | "Senha deve ter ao menos 8 caracteres" |
| 3 | | | | | | |

### Regras de Preenchimento
- ex: O campo "Peso" deve aceitar apenas números decimais com vírgula
- ex: O campo "Data" deve bloquear datas futuras

---

## 5. Botões e Ações

| # | Componente | Label / Ícone | Posição | Estado Inicial | Ação ao Clicar |
|---|---|---|---|---|---|
| 1 | Botão primário | "Entrar" | Centro inferior | Desabilitado até formulário válido | Chama API de login → navega para Dashboard |
| 2 | Link | "Esqueci minha senha" | Abaixo do campo senha | Ativo | Navega para tela Recuperar Senha |
| 3 | Botão secundário | "Criar conta" | Rodapé | Ativo | Navega para tela Cadastro |

---

## 6. Estados da Tela

### 6.1 Estado Inicial / Vazio
> O que o usuário vê quando abre a tela pela primeira vez ou não há dados?
- ex: Campos em branco, botão "Entrar" desabilitado
- ex: Ilustração + mensagem "Você ainda não tem treinos. Crie o primeiro!"

### 6.2 Estado de Carregamento (Loading)
> O que aparece enquanto uma ação está sendo processada?
- ex: Spinner sobre o botão "Entrar", botão desabilitado durante a requisição
- ex: Skeleton loader nas seções de conteúdo

### 6.3 Estado de Erro
> Como os erros são exibidos?
- **Erro de campo:** ex: Borda vermelha + mensagem abaixo do campo
- **Erro de rede:** ex: Toast na parte superior "Sem conexão. Tente novamente."
- **Erro da API:** ex: Toast "E-mail ou senha incorretos"

### 6.4 Estado de Sucesso
> O que acontece após uma ação bem-sucedida?
- ex: Toast "Login realizado com sucesso!" + redirect automático em 1s

### 6.5 Estado Desabilitado / Bloqueado *(se aplicável)*
- ex: Tela bloqueada para usuários do plano gratuito com banner de upgrade

---

## 7. Fluxo de Navegação

### De onde o usuário chega nesta tela
| Origem | Gatilho |
|---|---|
| ex: Tela de Splash | Usuário não está autenticado |
| ex: Tela de Cadastro | Clica em "Já tenho conta" |

### Para onde o usuário pode ir desta tela
| Destino | Gatilho |
|---|---|
| ex: Dashboard | Login bem-sucedido |
| ex: Recuperar Senha | Clica em "Esqueci minha senha" |
| ex: Cadastro | Clica em "Criar conta" |

---

## 8. Regras de Negócio
> Regras específicas que impactam o comportamento desta tela.

- RN01: ex: Após 3 tentativas de login incorretas, exibir captcha
- RN02: ex: Token de sessão expira em 30 dias
- RN03: ...

---

## 9. Histórico de Alterações

| Data | Autor | Descrição |
|---|---|---|
| | | Criação inicial do documento |

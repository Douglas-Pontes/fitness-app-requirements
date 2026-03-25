# Tela: [NOME DA TELA]

> **Instrucoes:** Copie este arquivo para a pasta correspondente, renomeie e preencha todos os campos.
> Campos marcados com ⚠️ PENDENTE precisam ser resolvidos antes de considerar a tela como concluida.
> Se uma secao nao se aplica a esta tela, escreva "N/A" — nao deixe vazio.

---

## Metadados
| Campo | Valor |
|---|---|
| **Nome da tela** | |
| **Modulo** | ex: Autenticacao, Treinos |
| **Prioridade** | 🔵 MVP / 🟣 Pos-MVP / ⚪ Futuro |
| **Status** | 🔴 NAO INICIADO |
| **Ultima atualizacao** | |

---

## 1. Objetivo da Tela
> O que o usuario consegue fazer nesta tela? Qual problema ela resolve?

_Descrever em 2-3 frases o proposito desta tela._

---

## 2. Quem Acessa / Pre-condicoes
> Quem pode ver esta tela? Quais condicoes precisam ser verdadeiras?

- **Usuario:** ex: Aluno autenticado / Visitante / Qualquer usuario
- **Pre-condicoes:**
  - ex: Usuario deve estar logado
  - ex: Deve ter ao menos uma rotina cadastrada
- **Permissoes especiais:** ex: Nenhuma / Plano Premium

---

## 3. Layout e Componentes Visuais
> Descreva a estrutura visual da tela de cima para baixo.

### 3.1 Header / Cabecalho
- Conteudo: ex: Botao voltar + Titulo "Login" + icone de ajuda
- Comportamento: ex: Fixo no topo / Scroll junto com conteudo

### 3.2 Corpo Principal
> Descrever secoes da tela, na ordem que aparecem

**Secao 1 — [Nome]**
- Componente: ex: Card, Lista, Formulario, Carrossel
- Conteudo: ex: Lista de exercicios com nome, grupo muscular e imagem
- Comportamento: ex: Scroll vertical infinito

**Secao 2 — [Nome]**
- ...

### 3.3 Footer / Rodape
- Conteudo: ex: Barra de navegacao inferior / Botao de acao flutuante (FAB)
- Comportamento: ex: Fixo na parte inferior

---

## 4. Campos e Formularios

> Preencher apenas se a tela tiver campos de entrada (inputs, selects, etc.)
> Se nao houver formularios, escreva "N/A — Tela sem formularios"

| # | Nome do Campo | Tipo | Obrigatorio | Placeholder | Validacao | Mensagem de Erro |
|---|---|---|---|---|---|---|
| 1 | ex: E-mail | Text / Email | Sim | "seu@email.com" | Formato de e-mail valido | "Digite um e-mail valido" |
| 2 | ex: Senha | Password | Sim | "Sua senha" | Minimo 8 caracteres | "Senha deve ter ao menos 8 caracteres" |

### Regras de Preenchimento
- ex: O campo "Peso" deve aceitar apenas numeros decimais com virgula
- ex: O campo "Data" deve bloquear datas futuras

---

## 5. Botoes e Acoes

| # | Componente | Label / Icone | Posicao | Estado Inicial | Acao ao Clicar |
|---|---|---|---|---|---|
| 1 | Botao primario | "Entrar" | Centro inferior | Desabilitado ate formulario valido | Chama API de login → navega para Dashboard |
| 2 | Link | "Esqueci minha senha" | Abaixo do campo senha | Ativo | Navega para tela Recuperar Senha |

---

## 6. Estados da Tela

### 6.1 Estado Inicial / Vazio
> O que o usuario ve quando abre a tela pela primeira vez ou nao ha dados?
- ex: Campos em branco, botao "Entrar" desabilitado
- ex: Ilustracao + mensagem "Voce ainda nao tem treinos. Crie o primeiro!"

### 6.2 Estado de Carregamento (Loading)
> O que aparece enquanto uma acao esta sendo processada?
- ex: Spinner sobre o botao "Entrar", botao desabilitado durante a requisicao
- ex: Skeleton loader nas secoes de conteudo

### 6.3 Estado de Erro
> Como os erros sao exibidos?
- **Erro de campo:** ex: Borda vermelha + mensagem abaixo do campo
- **Erro de rede:** ex: Toast na parte superior "Sem conexao. Tente novamente."
- **Erro da API:** ex: Toast "E-mail ou senha incorretos"

### 6.4 Estado de Sucesso
> O que acontece apos uma acao bem-sucedida?
- ex: Toast "Login realizado com sucesso!" + redirect automatico em 1s

### 6.5 Estado Desabilitado / Bloqueado *(se aplicavel)*
- ex: Tela bloqueada para usuarios do plano gratuito com banner de upgrade

---

## 7. Fluxo de Navegacao

### De onde o usuario chega nesta tela
| Origem | Gatilho |
|---|---|
| ex: Tela de Splash | Usuario nao esta autenticado |
| ex: Tela de Cadastro | Clica em "Ja tenho conta" |

### Para onde o usuario pode ir desta tela
| Destino | Gatilho |
|---|---|
| ex: Dashboard | Login bem-sucedido |
| ex: Recuperar Senha | Clica em "Esqueci minha senha" |

---

## 8. Regras de Negocio
> Regras especificas que impactam o comportamento desta tela.

- RN01: ex: Apos 3 tentativas de login incorretas, exibir captcha
- RN02: ex: Token de sessao expira em 30 dias

---

## 9. Responsividade (Mobile vs Web)
> Diferencas de comportamento ou layout entre plataformas.

| Aspecto | Mobile | Web |
|---|---|---|
| ex: Login social | Google + Apple | Apenas Google |
| ex: Layout | Tela cheia | Card centralizado max-width 480px |
| ex: Teclado | Formulario sobe ao abrir teclado | N/A |

> Se nao houver diferencas, escreva "Comportamento identico em ambas as plataformas"

---

## 10. Acessibilidade
> Consideracoes de acessibilidade para esta tela.

- Labels acessiveis em todos os campos de formulario
- Contraste de cores conforme WCAG 2.1 AA
- Navegacao por teclado (tab order logica)
- Textos alternativos em imagens e icones decorativos
- _(Adicionar consideracoes especificas da tela)_

---

## 11. Historico de Alteracoes

| Data | Autor | Descricao |
|---|---|---|
| | | Criacao inicial do documento |

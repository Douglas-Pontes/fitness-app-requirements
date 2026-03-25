# Tela: Login

> **Exemplo de tela preenchida** para servir de referencia de qualidade.
> Use esta tela como modelo de nivel de detalhe esperado.

---

## Metadados
| Campo | Valor |
|---|---|
| **Nome da tela** | Login |
| **Modulo** | Autenticacao |
| **Prioridade** | 🔵 MVP |
| **Status** | 🟠 PENDENTE REVISAO |
| **Ultima atualizacao** | — |

---

## 1. Objetivo da Tela
Permitir que um usuario ja cadastrado acesse sua conta no app. E a tela de entrada para usuarios que ja realizaram o cadastro anteriormente.

---

## 2. Quem Acessa / Pre-condicoes
- **Usuario:** Qualquer visitante (nao autenticado)
- **Pre-condicoes:**
  - Usuario deve ter uma conta cadastrada
  - App aberto pela primeira vez ou sessao expirada
- **Permissoes especiais:** Nenhuma

---

## 3. Layout e Componentes Visuais

### 3.1 Header / Cabecalho
- Sem botao de voltar (tela raiz do fluxo de auth)
- Logo do app centralizada no topo
- Sem titulo de pagina

### 3.2 Corpo Principal

**Secao 1 — Boas-vindas**
- Texto: "Bem-vindo de volta!"
- Subtexto: "Entre na sua conta para continuar"

**Secao 2 — Formulario**
- Campo: E-mail
- Campo: Senha
- Link: "Esqueci minha senha" (alinhado a direita, abaixo do campo de senha)

**Secao 3 — Acao Principal**
- Botao primario: "Entrar"

**Secao 4 — Divisor**
- Linha divisoria com texto "ou" centralizado

**Secao 5 — Login Social** *(⚠️ PENDENTE: confirmar se havera)*
- Botao "Continuar com Google"
- Botao "Continuar com Apple" *(apenas iOS)*

### 3.3 Footer / Rodape
- Texto: "Nao tem uma conta?"
- Link: "Cadastre-se" → navega para tela de Cadastro
- Fixo na parte inferior da tela, acima do teclado

---

## 4. Campos e Formularios

| # | Nome do Campo | Tipo | Obrigatorio | Placeholder | Validacao | Mensagem de Erro |
|---|---|---|---|---|---|---|
| 1 | E-mail | Email | Sim | "seu@email.com" | Formato de e-mail valido | "Digite um e-mail valido" |
| 2 | Senha | Password | Sim | "Sua senha" | Minimo 8 caracteres | "A senha deve ter ao menos 8 caracteres" |

### Regras de Preenchimento
- Campo de senha com botao de mostrar/ocultar (icone de olho)
- E-mail deve ser convertido para lowercase antes de enviar
- Ambos os campos perdem o foco ao clicar fora (dismiss keyboard no mobile)

---

## 5. Botoes e Acoes

| # | Componente | Label / Icone | Posicao | Estado Inicial | Acao ao Clicar |
|---|---|---|---|---|---|
| 1 | Botao primario | "Entrar" | Abaixo do formulario | Habilitado | Valida campos → autentica → navega para Dashboard |
| 2 | Link texto | "Esqueci minha senha" | Abaixo do campo senha | Ativo | Navega para Recuperar Senha |
| 3 | Botao secundario | "Continuar com Google" | Secao social | Ativo | Inicia OAuth Google |
| 4 | Botao secundario | "Continuar com Apple" | Secao social (iOS only) | Ativo | Inicia Sign In with Apple |
| 5 | Link texto | "Cadastre-se" | Footer | Ativo | Navega para Cadastro |

---

## 6. Estados da Tela

### 6.1 Estado Inicial / Vazio
- Campos em branco
- Botao "Entrar" habilitado (validacao acontece ao submeter, nao em tempo real)
- ⚠️ PENDENTE: Discutir se o botao deve ficar desabilitado ate o formulario ser preenchido

### 6.2 Estado de Carregamento (Loading)
- Ao clicar "Entrar": spinner substitui o texto do botao + botao desabilitado
- Campos ficam desabilitados durante o loading
- Duracao: ate resposta da API

### 6.3 Estado de Erro
- **Campos invalidos:** Borda vermelha + mensagem abaixo do campo especifico
- **Credenciais incorretas:** Toast vermelho no topo "E-mail ou senha incorretos"
- **Sem conexao:** Toast "Sem conexao com a internet. Verifique sua rede."
- **Erro do servidor (5xx):** Toast "Erro no servidor. Tente novamente em instantes."

### 6.4 Estado de Sucesso
- Toast verde discreto: "Login realizado com sucesso!"
- Redirect imediato para o Dashboard

### 6.5 Estado Desabilitado / Bloqueado
- N/A — Tela de login nao tem estado bloqueado

---

## 7. Fluxo de Navegacao

### De onde o usuario chega nesta tela
| Origem | Gatilho |
|---|---|
| Splash Screen | Usuario nao possui sessao ativa |
| Tela de Cadastro | Clica em "Ja tenho conta" |
| Tela Recuperar Senha | Apos redefinir senha com sucesso |

### Para onde o usuario pode ir desta tela
| Destino | Gatilho |
|---|---|
| Dashboard | Login bem-sucedido |
| Recuperar Senha | Clica em "Esqueci minha senha" |
| Cadastro | Clica em "Cadastre-se" |

---

## 8. Regras de Negocio
- RN01: ⚠️ PENDENTE — Definir politica de tentativas falhas (bloqueio temporario? captcha?)
- RN02: Opcao de login com Apple so aparece em dispositivos iOS
- RN03: Token JWT expira em ⚠️ PENDENTE (sugestao: 7 dias com refresh token de 30 dias)
- RN04: ⚠️ PENDENTE — "Manter conectado" (remember me) sera uma opcao?

---

## 9. Responsividade (Mobile vs Web)

| Aspecto | Mobile | Web |
|---|---|---|
| Layout | Tela cheia, formulario centralizado verticalmente | Card centralizado, max-width 480px, fundo com cor/pattern |
| Login social | Google + Apple (iOS) | Apenas Google |
| Teclado | Formulario sobe ao abrir teclado virtual | N/A |
| Logo | Menor, acima do titulo | Maior, com mais espaco |

---

## 10. Acessibilidade

- Labels acessiveis nos campos de e-mail e senha (`aria-label` / `accessibilityLabel`)
- Botao de mostrar/ocultar senha com label descritivo ("Mostrar senha" / "Ocultar senha")
- Contraste minimo WCAG 2.1 AA para textos e botoes
- Tab order: E-mail → Senha → Entrar → Esqueci senha → Login social → Cadastre-se
- Toast de erro anunciado por screen reader (`aria-live="assertive"`)

---

## 11. Historico de Alteracoes

| Data | Autor | Descricao |
|---|---|---|
| — | — | Criacao inicial como exemplo de referencia |
| — | Opus 4.6 | Adicionadas secoes: Dados/Entidades, Responsividade, Acessibilidade, Prioridade MVP |

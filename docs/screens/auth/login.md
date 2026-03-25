# Tela: Login

> **Exemplo de tela preenchida** para servir de referência de qualidade.
> Use esta tela como modelo de nível de detalhe esperado.

---

## Metadados
| Campo | Valor |
|---|---|
| **Nome da tela** | Login |
| **Módulo** | Autenticação |
| **Status** | 🟠 PENDENTE REVISÃO |
| **Última atualização** | — |

---

## 1. Objetivo da Tela
Permitir que um usuário já cadastrado acesse sua conta no app. É a tela de entrada para usuários que já realizaram o cadastro anteriormente.

---

## 2. Quem Acessa / Pré-condições
- **Usuário:** Qualquer visitante (não autenticado)
- **Pré-condições:**
  - Usuário deve ter uma conta cadastrada
  - App aberto pela primeira vez ou sessão expirada
- **Permissões especiais:** Nenhuma

---

## 3. Layout e Componentes Visuais

### 3.1 Header / Cabeçalho
- Sem botão de voltar (tela raiz do fluxo de auth)
- Logo do app centralizada no topo
- Sem título de página

### 3.2 Corpo Principal

**Seção 1 — Boas-vindas**
- Texto: "Bem-vindo de volta!"
- Subtexto: "Entre na sua conta para continuar"

**Seção 2 — Formulário**
- Campo: E-mail
- Campo: Senha
- Link: "Esqueci minha senha" (alinhado à direita, abaixo do campo de senha)

**Seção 3 — Ação Principal**
- Botão primário: "Entrar"

**Seção 4 — Divisor**
- Linha divisória com texto "ou" centralizado

**Seção 5 — Login Social** *(⚠️ PENDENTE: confirmar se haverá)*
- Botão "Continuar com Google"
- Botão "Continuar com Apple" *(apenas iOS)*

### 3.3 Footer / Rodapé
- Texto: "Não tem uma conta?"
- Link: "Cadastre-se" → navega para tela de Cadastro
- Fixo na parte inferior da tela, acima do teclado

---

## 4. Campos e Formulários

| # | Nome do Campo | Tipo | Obrigatório | Placeholder | Validação | Mensagem de Erro |
|---|---|---|---|---|---|---|
| 1 | E-mail | Email | Sim | "seu@email.com" | Formato de e-mail válido | "Digite um e-mail válido" |
| 2 | Senha | Password | Sim | "Sua senha" | Mínimo 8 caracteres | "A senha deve ter ao menos 8 caracteres" |

### Regras de Preenchimento
- Campo de senha com botão de mostrar/ocultar (ícone de olho)
- E-mail deve ser convertido para lowercase antes de enviar
- Ambos os campos perdem o foco ao clicar fora (dismiss keyboard no mobile)

---

## 5. Botões e Ações

| # | Componente | Label / Ícone | Posição | Estado Inicial | Ação ao Clicar |
|---|---|---|---|---|---|
| 1 | Botão primário | "Entrar" | Abaixo do formulário | Habilitado | Valida campos → chama API → navega para Dashboard |
| 2 | Link texto | "Esqueci minha senha" | Abaixo do campo senha | Ativo | Navega para Recuperar Senha |
| 3 | Botão secundario | "Continuar com Google" | Seção social | Ativo | Inicia OAuth Google |
| 4 | Botão secundario | "Continuar com Apple" | Seção social (iOS only) | Ativo | Inicia Sign In with Apple |
| 5 | Link texto | "Cadastre-se" | Footer | Ativo | Navega para Cadastro |

---

## 6. Estados da Tela

### 6.1 Estado Inicial / Vazio
- Campos em branco
- Botão "Entrar" habilitado (validação acontece ao submeter, não em tempo real)
- ⚠️ PENDENTE: Discutir se o botão deve ficar desabilitado até o formulário ser preenchido

### 6.2 Estado de Carregamento (Loading)
- Ao clicar "Entrar": spinner substitui o texto do botão + botão desabilitado
- Campos ficam desabilitados durante o loading
- Duração: até resposta da API

### 6.3 Estado de Erro
- **Campos inválidos:** Borda vermelha + mensagem abaixo do campo específico
- **Credenciais incorretas:** Toast vermelho no topo "E-mail ou senha incorretos"
- **Sem conexão:** Toast "Sem conexão com a internet. Verifique sua rede."
- **Erro do servidor (5xx):** Toast "Erro no servidor. Tente novamente em instantes."

### 6.4 Estado de Sucesso
- Toast verde discreto: "Login realizado com sucesso!"
- Redirect imediato para o Dashboard

---

## 7. Fluxo de Navegação

### De onde o usuário chega nesta tela
| Origem | Gatilho |
|---|---|
| Splash Screen | Usuário não possui sessão ativa |
| Tela de Cadastro | Clica em "Já tenho conta" |
| Tela Recuperar Senha | Após redefinir senha com sucesso |

### Para onde o usuário pode ir desta tela
| Destino | Gatilho |
|---|---|
| Dashboard | Login bem-sucedido |
| Recuperar Senha | Clica em "Esqueci minha senha" |
| Cadastro | Clica em "Cadastre-se" |

---

## 8. Regras de Negócio 
- RN01: Definir política de tentativas falhas (bloqueio temporário?)
- RN02: Opção de login com Apple só aparece em dispositivos iOS

---

## 9. Histórico de Alterações

| Data | Autor | Descrição |
|---|---|---|
| — | — | Criação inicial como exemplo de referência |
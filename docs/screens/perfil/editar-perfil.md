# Tela: Editar Perfil

---

## Metadados
| Campo | Valor |
|---|---|
| **Nome da tela** | Editar Perfil |
| **Modulo** | Perfil |
| **Prioridade** | 🔵 MVP |
| **Status** | 🟡 EM ANDAMENTO |
| **Ultima atualizacao** | 2026-03-27 |

---

## 1. Objetivo da Tela
> Permite ao aluno preencher ou editar todos os dados pessoais e físicos do seu perfil. Mesma tela usada tanto para inclusão inicial de dados quanto para edição posterior — o rótulo do botão principal muda conforme o contexto.

---

## 2. Quem Acessa / Pré-condições

- **Usuário:** Aluno autenticado
- **Pré-condições:**
  - Usuário deve estar logado
- **Permissões especiais:** Nenhuma. Personal Trainer NÃO pode editar o perfil do aluno.

---

## 3. Layout e Componentes Visuais

### 3.1 Header / Cabeçalho
- Conteúdo: Botão voltar (←) + Título "Meus Dados"
- Comportamento: Fixo no topo. Botão voltar retorna para Meu Perfil sem salvar alterações (exibe alerta de confirmação se houver mudanças não salvas).

### 3.2 Corpo Principal

**Seção 1 — Foto de Perfil**
- Componente: Avatar circular centralizado com botão "Alterar foto" abaixo
- Conteúdo: Foto atual (ou avatar genérico se não houver)
- Comportamento: Toque abre seletor (câmera ou galeria). Tamanho máximo: 2 MB. Se exceder, exibe erro.

**Seção 2 — Dados Pessoais**
- Componente: Formulário com campos em lista vertical
- Campos: Nome, E-mail, Telefone, Data de Nascimento, Sexo, Idioma, Instagram
- Ver seção 4 para validações detalhadas

**Seção 3 — Dados Físicos**
- Componente: Formulário com campos numéricos
- Campos: Peso, Altura, IMC (read-only, calculado automaticamente)
- Ver seção 4 para validações detalhadas

### 3.3 Footer / Rodapé
- Conteúdo: Botão primário "Salvar" (fixo no fundo, acima do tab bar)
- Comportamento: Fixo na parte inferior; teclado empurra o botão para cima

---

## 4. Campos e Formulários

### Dados Pessoais

| # | Nome do Campo | Tipo | Obrigatório | Placeholder | Validação | Mensagem de Erro |
|---|---|---|---|---|---|---|
| 1 | Nome | Text | Sim | "Seu nome completo" | Apenas letras e espaços; mín. 2 caracteres | "Nome deve conter apenas letras" |
| 2 | E-mail | Email | Sim | "seu@email.com" | Formato de e-mail válido (RFC 5322) | "Digite um e-mail válido" |
| 3 | Telefone | Tel | Não | "+55(11)91234-5678" | Máscara: +55(XX)9XXXXXXXX; apenas números | "Digite um telefone válido com DDD" |
| 4 | Data de Nascimento | Date | Sim | "dd/mm/aaaa" | Máscara dd/mm/aaaa; data válida; não pode ser futura; idade mín. 10 anos | "Digite uma data de nascimento válida" |
| 5 | Sexo | Select | Sim | — | Deve selecionar uma das 3 opções | "Selecione uma opção" |
| 6 | Idioma | Text | Não | "Ex: Português" | Apenas letras e espaços | "Idioma deve conter apenas letras" |
| 7 | Instagram | Text | Não | "@seuperfil" | Aceita apenas o @ handle (sem URL); caracteres válidos: letras, números, `.` e `_` | "Digite apenas o @ do Instagram (ex: @nome)" |

### Dados Físicos

| # | Nome do Campo | Tipo | Obrigatório | Placeholder | Validação | Mensagem de Erro |
|---|---|---|---|---|---|---|
| 8 | Peso | Number | Não | "Ex: 75" | Número inteiro ou decimal; entre 20 e 300; unidade: kg | "Digite um peso válido em kg" |
| 9 | Altura | Number | Não | "Ex: 175" | Número inteiro; entre 50 e 250; unidade: cm | "Digite uma altura válida em cm" |
| 10 | IMC | Text (read-only) | — | — | Calculado automaticamente: Peso(kg) / Altura(m)² | — |

### Opções do campo Sexo
- Feminino
- Masculino
- Prefiro não informar

### Regras de Preenchimento
- Todos os campos de Dados Pessoais são obrigatórios (exceto Telefone, Idioma e Instagram)
- IMC é exibido somente quando Peso e Altura estão preenchidos
- Instagram: remover automaticamente o "https://instagram.com/" se o usuário colar a URL completa, mantendo apenas o handle
- Telefone: aplicar máscara automaticamente ao digitar
- Data de Nascimento: aplicar máscara automaticamente ao digitar

---

## 5. Botões e Ações

| # | Componente | Label / Ícone | Posição | Estado Inicial | Ação ao Clicar |
|---|---|---|---|---|---|
| 1 | Botão primário | "Salvar" (modo edição) / "Incluir dados" (primeiro preenchimento) | Footer fixo | Habilitado sempre | Valida formulário → salva via API → volta para Meu Perfil |
| 2 | Avatar clicável | "Alterar foto" | Seção 1 | Ativo | Abre action sheet: "Câmera" / "Galeria" / "Remover foto" |
| 3 | Botão voltar | ← | Header | Ativo | Se há mudanças não salvas: exibe alerta "Deseja descartar as alterações?" → Sim: volta sem salvar / Não: permanece na tela |

---

## 6. Estados da Tela

### 6.1 Estado Inicial / Vazio (primeiro preenchimento)
- Campos em branco
- Avatar placeholder genérico
- Botão principal com label "Incluir dados"
- IMC vazio (aguardando Peso e Altura)

### 6.2 Estado de Edição (dados já existentes)
- Campos pré-preenchidos com dados atuais
- Botão principal com label "Salvar"

### 6.3 Estado de Carregamento (Loading)
- Spinner sobre o botão "Salvar", botão desabilitado durante a requisição
- Campos bloqueados para edição durante o salvamento

### 6.4 Estado de Erro
- **Erro de campo:** Borda vermelha + mensagem de erro abaixo do campo específico
- **Erro de rede:** Toast "Sem conexão. Tente novamente."
- **Erro na foto:** Toast "A foto deve ter no máximo 2 MB"
- **Erro da API:** Toast "Não foi possível salvar. Tente novamente."

### 6.5 Estado de Sucesso
- Toast "Dados salvos com sucesso!" + retorna para Meu Perfil automaticamente

---

## 7. Fluxo de Navegação

### De onde o usuário chega nesta tela
| Origem | Gatilho |
|---|---|
| Meu Perfil | Toque no card "Dados Pessoais" |
| Onboarding — Dados Pessoais | Fluxo pós-cadastro (se compartilhar a mesma tela) |

### Para onde o usuário pode ir desta tela
| Destino | Gatilho |
|---|---|
| Meu Perfil | Salvar com sucesso |
| Meu Perfil | Toque em voltar (← ) sem mudanças |
| Meu Perfil | Confirmar "Descartar alterações" |

---

## 8. Regras de Negócio

- RN01: E-mail não pode ser alterado para um e-mail já cadastrado por outro usuário
- RN02: Foto de perfil: tamanho máximo 2 MB; formatos aceitos: JPG, PNG, WEBP
- RN03: IMC = Peso(kg) / (Altura(m))² — recalculado em tempo real ao alterar Peso ou Altura
- RN04: Instagram — armazenar apenas o handle sem o "@" no banco; exibir com "@" na UI
- RN05: Telefone — armazenar apenas os dígitos (sem máscara) no banco
- RN06: Personal Trainer não tem acesso a esta tela — não pode editar dados do aluno

---

## 9. Responsividade (Mobile vs Web)

| Aspecto | Mobile | Web |
|---|---|---|
| Layout geral | Scroll vertical, full width | Coluna centralizada, max-width 480px |
| Teclado | Formulário sobe ao abrir teclado; botão "Salvar" permanece visível | N/A |
| Seletor de foto | Câmera ou galeria nativa | Upload de arquivo (input file) |
| Campo Sexo | Picker nativo (iOS/Android) | Select dropdown |
| Campo Data | Picker de data nativo | Input date com máscara |

---

## 10. Acessibilidade

- Labels acessíveis em todos os campos de formulário
- Contraste de cores conforme WCAG 2.1 AA
- Navegação por teclado (tab order lógica: topo → baixo)
- "Next" no teclado move para o próximo campo; último campo fecha o teclado
- Textos alternativos na foto de perfil
- Mensagens de erro anunciadas por leitores de tela via `aria-live`

---

## 11. Histórico de Alterações

| Data | Autor | Descrição |
|---|---|---|
| 2026-03-27 | Douglas | Criação inicial do documento |

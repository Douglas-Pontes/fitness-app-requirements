# Tela: Meu Perfil

---

## Metadados
| Campo | Valor |
|---|---|
| **Nome da tela** | Meu Perfil |
| **Modulo** | Perfil |
| **Prioridade** | 🔵 MVP |
| **Status** | 🟡 EM ANDAMENTO |
| **Ultima atualizacao** | 2026-03-27 |

---

## 1. Objetivo da Tela
> Tela hub do perfil do aluno. Centraliza acesso aos dados pessoais, dados físicos, avaliações e dieta. Permite visualização rápida das informações principais sem precisar editar.

---

## 2. Quem Acessa / Pré-condições

- **Usuário:** Aluno autenticado / Personal Trainer (visualização do aluno vinculado)
- **Pré-condições:**
  - Usuário deve estar logado
- **Permissões especiais:** Nenhuma

---

## 3. Layout e Componentes Visuais

### 3.1 Header / Cabeçalho
- Conteúdo: Título "Perfil"
- Comportamento: Fixo no topo

### 3.2 Corpo Principal

**Seção 1 — Foto e Identificação**
- Componente: Avatar circular + informações básicas
- Conteúdo:
  - Foto de perfil (circular, com ícone de câmera para editar)
  - Nome completo
  - @instagram (se preenchido)
- Comportamento: Toque na foto abre modal de "Atualizar Foto"

**Seção 2 — Dados Físicos (resumo)**
- Componente: Card com 3 métricas em linha
- Conteúdo:
  - Peso: `XX kg`
  - Altura: `XXX cm`
  - IMC: `XX,X — [Classificação]`
- Comportamento: Somente leitura. Valores vêm dos Dados Físicos preenchidos no Editar Perfil.
- Estado vazio: Exibe `—` com texto "Adicionar" em cada métrica

**Seção 3 — Card: Dados Pessoais**
- Componente: Card clicável com ícone + label + seta
- Conteúdo: Ícone de pessoa + "Dados Pessoais" + indicador de completude (ex: "7/7 campos preenchidos")
- Comportamento: Toque navega para tela Editar Perfil

**Seção 4 — Card: Avaliações**
- Componente: Card clicável com ícone + label + seta + último registro
- Conteúdo: Ícone de gráfico + "Avaliações" + data da última avaliação (se houver)
- Comportamento: Toque navega para Lista de Avaliações

**Seção 5 — Card: Dieta** *(Pós-MVP)*
- Componente: Card clicável com ícone + label + seta
- Conteúdo: Ícone de prato + "Minha Dieta" + status (ex: "Dieta atual: Cutting")
- Comportamento: Toque navega para Minha Dieta
- Estado sem dieta cadastrada: Exibe "Nenhuma dieta cadastrada"

### 3.3 Footer / Rodapé
- Conteúdo: Tab bar de navegação inferior
- Comportamento: Fixo na parte inferior

---

## 4. Campos e Formulários

N/A — Tela sem formulários (apenas visualização e navegação)

---

## 5. Botões e Ações

| # | Componente | Label / Ícone | Posição | Estado Inicial | Ação ao Clicar |
|---|---|---|---|---|---|
| 1 | Avatar clicável | Ícone de câmera sobre a foto | Seção 1 | Ativo | Abre modal "Atualizar Foto" |
| 2 | Card | "Dados Pessoais" | Seção 3 | Ativo | Navega para Editar Perfil |
| 3 | Card | "Avaliações" | Seção 4 | Ativo | Navega para Lista de Avaliações |
| 4 | Card | "Minha Dieta" *(Pós-MVP)* | Seção 5 | Ativo | Navega para Minha Dieta |

---

## 6. Estados da Tela

### 6.1 Estado Inicial / Vazio
- Foto de perfil: avatar genérico (placeholder)
- Dados físicos: `—` em Peso, Altura e IMC, com texto "Adicionar"
- Cards de Dados Pessoais, Avaliações e Dieta: visíveis mas indicando "sem dados"

### 6.2 Estado de Carregamento (Loading)
- Skeleton loader nas seções 1, 2 e nos cards

### 6.3 Estado de Erro
- **Erro de rede:** Toast "Não foi possível carregar seu perfil. Tente novamente."

### 6.4 Estado de Sucesso
- Após atualizar foto: toast "Foto atualizada com sucesso!"

### 6.5 Estado Desabilitado / Bloqueado
- N/A

---

## 7. Fluxo de Navegação

### De onde o usuário chega nesta tela
| Origem | Gatilho |
|---|---|
| Tab Bar | Toque no ícone "Perfil" |
| Qualquer tela | Toque no avatar do usuário (se disponível no header) |

### Para onde o usuário pode ir desta tela
| Destino | Gatilho |
|---|---|
| Editar Perfil | Toque no card "Dados Pessoais" |
| Lista de Avaliações | Toque no card "Avaliações" |
| Minha Dieta *(Pós-MVP)* | Toque no card "Dieta" |
| Modal Atualizar Foto | Toque no ícone de câmera sobre a foto |

---

## 8. Regras de Negócio

- RN01: IMC é calculado automaticamente com base em Peso (kg) e Altura (cm): `IMC = peso / (altura_m²)`
- RN02: Classificação do IMC exibida junto ao valor:
  - < 18,5 → Abaixo do peso
  - 18,5–24,9 → Peso normal
  - 25,0–29,9 → Sobrepeso
  - 30,0–34,9 → Obesidade grau I
  - 35,0–39,9 → Obesidade grau II
  - ≥ 40,0 → Obesidade grau III
- RN03: IMC só é exibido se Peso E Altura estiverem preenchidos
- RN04: Personal Trainer vinculado ao aluno pode visualizar esta tela (somente leitura)

---

## 9. Responsividade (Mobile vs Web)

| Aspecto | Mobile | Web |
|---|---|---|
| Layout geral | Scroll vertical, full width | Coluna centralizada, max-width 480px |
| Cards de módulo | Empilhados verticalmente | Grid 2 colunas |
| Foto de perfil | Avatar 96x96px | Avatar 128x128px |

---

## 10. Acessibilidade

- Labels acessíveis em todos os cards e botões
- Contraste de cores conforme WCAG 2.1 AA
- Navegação por teclado (tab order lógica)
- Textos alternativos na foto de perfil e ícones decorativos
- Classificação do IMC acessível por leitores de tela (não só por cor)

---

## 11. Histórico de Alterações

| Data | Autor | Descrição |
|---|---|---|
| 2026-03-27 | Douglas | Criação inicial do documento |

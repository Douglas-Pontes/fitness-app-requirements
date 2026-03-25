# Design System — Referências Base

> Define os padrões visuais e de componentes que todos os documentos de tela devem referenciar.
> ⚠️ Preencher junto com o designer antes de iniciar a documentação de telas.

---

## Paleta de Cores

| Token | Hex | Uso |
|---|---|---|
| `primary` | ⚠️ PENDENTE | Botões principais, destaques |
| `primary-dark` | ⚠️ PENDENTE | Hover/press de botão primário |
| `secondary` | ⚠️ PENDENTE | Ações secundárias |
| `background` | ⚠️ PENDENTE | Fundo das telas |
| `surface` | ⚠️ PENDENTE | Cards, modais |
| `text-primary` | ⚠️ PENDENTE | Texto principal |
| `text-secondary` | ⚠️ PENDENTE | Texto de apoio, labels |
| `error` | ⚠️ PENDENTE | Erros, validações |
| `success` | ⚠️ PENDENTE | Confirmações, concluído |
| `warning` | ⚠️ PENDENTE | Alertas |
| `border` | ⚠️ PENDENTE | Divisores, bordas de input |

---

## Tipografia

| Estilo | Fonte | Tamanho | Peso | Uso |
|---|---|---|---|---|
| `heading-1` | ⚠️ | 28px | Bold | Títulos de tela |
| `heading-2` | ⚠️ | 22px | SemiBold | Seções |
| `heading-3` | ⚠️ | 18px | SemiBold | Sub-seções |
| `body-1` | ⚠️ | 16px | Regular | Texto corrido |
| `body-2` | ⚠️ | 14px | Regular | Texto secundário |
| `caption` | ⚠️ | 12px | Regular | Labels, legendas |
| `button` | ⚠️ | 16px | SemiBold | Labels de botão |

---

## Espaçamento

| Token | Valor | Uso |
|---|---|---|
| `spacing-xs` | 4px | Espaços internos mínimos |
| `spacing-sm` | 8px | Entre elementos próximos |
| `spacing-md` | 16px | Padding padrão de tela |
| `spacing-lg` | 24px | Entre seções |
| `spacing-xl` | 32px | Margens maiores |
| `spacing-2xl` | 48px | Separações de bloco |

---

## Componentes Padrão

### Botão Primário
- Altura: 52px
- Border-radius: ⚠️ PENDENTE
- Cor de fundo: `primary`
- Cor do texto: Branco
- Estado desabilitado: opacity 0.4
- Estado loading: spinner substitui label + desabilitado

### Botão Secundário (Outline)
- Mesmas dimensões do primário
- Fundo transparente + borda `primary`
- Texto: `primary`

### Input de Texto
- Altura: 52px
- Border: 1px `border`
- Border-radius: ⚠️ PENDENTE
- Estado focus: borda `primary`
- Estado erro: borda `error` + mensagem abaixo em `error`
- Label: acima do campo

### Card
- Background: `surface`
- Padding: `spacing-md`
- Border-radius: ⚠️ PENDENTE
- Shadow: ⚠️ PENDENTE

### Toast / Snackbar
- Posição: topo da tela (sob a status bar)
- Duração: 3 segundos
- Tipos: success (verde), error (vermelho), info (azul)

### Loading / Skeleton
- Usar skeleton loader para listas e cards
- Usar spinner centralizado para ações de tela cheia

---

## Ícones

- Biblioteca: ⚠️ PENDENTE (sugestão: Phosphor Icons ou Lucide)
- Tamanho padrão: 24px
- Tamanho em tab bar: 26px

---

## Grids e Layout

### Mobile
- Padding lateral de tela: 16px
- Colunas de grid: 4
- Gutter: 8px

### Web
- Largura máxima do container: 1200px
- Padding lateral: 24px
- Colunas de grid: 12

---

## Animações e Transições

| Tipo | Duração | Easing | Uso |
|---|---|---|---|
| Fade | 200ms | ease-out | Modais, toasts |
| Slide | 300ms | ease-in-out | Navegação entre telas |
| Spring | 400ms | spring | FAB, cards expansíveis |

---

## ⚠️ Decisões Pendentes de Design

- Tema claro / escuro? Só claro inicialmente?
- Fonte escolhida para o app?
- Estilo visual geral: minimalista, vibrante, dark mode focused?
- Biblioteca de componentes de referência: Material, iOS HIG, customizado?

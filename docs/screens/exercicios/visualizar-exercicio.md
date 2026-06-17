# Tela: Visualizar Exercício `[VELA-3002]`

---

## Metadados
| Campo | Valor |
|---|---|
| **Nome da tela** | Visualizar Exercício |
| **Modulo** | Exercícios |
| **Codigo** | VELA-3002 |
| **Prioridade** | 🔵 MVP |
| **Status** | 🟡 EM ANDAMENTO |
| **Ultima atualizacao** | 2026-06-17 |

---

## 1. Objetivo da Tela
> O que o usuario consegue fazer nesta tela? Qual problema ela resolve?

Tela de **leitura** que mostra todas as informações de um exercício de forma clara e prática, para o **Treinador** ter total clareza do que cadastrou (e, futuramente, para o **Aluno** entender como executar). Reúne vídeo, classificação, instruções e observações em uma visão organizada. A partir daqui o Treinador pode **editar** o exercício.

---

## 2. Quem Acessa / Pre-condicoes
> Quem pode ver esta tela? Quais condicoes precisam ser verdadeiras?

- **Usuario:**
  - **Treinador** — visualiza um exercício do seu acervo; vê ações de editar/ativar-desativar/excluir.
  - **Aluno** — (consulta futura) visualiza o exercício em modo leitura, sem ações de edição.
- **Pre-condicoes:**
  - Usuário deve estar logado.
  - Deve existir um exercício selecionado (do acervo do Treinador).
- **Permissoes especiais:** Editar/excluir exigem ser o **Treinador** que criou o exercício (ver Seção 8).

---

## 3. Layout e Componentes Visuais
> Descreva a estrutura visual da tela de cima para baixo.

### 3.1 Header / Cabecalho
- Conteudo: Botão voltar (←) + Nome do exercício (com etiqueta **"Inativo"** quando aplicável) + menu de ações (Editar / Ativar-Desativar / Excluir).
- Comportamento: Fixo no topo.

### 3.2 Corpo Principal
> Scroll vertical, com a mídia no topo e as informações em seções.

**Secao 1 — Mídia**
- Componente: Player de vídeo (da base do app ou do YouTube).
- Conteudo: Vídeo de execução (sempre presente — obrigatório no cadastro).
- Comportamento: Player embutido; toque inicia a reprodução.

**Secao 2 — Classificação**
- Componente: Chips/etiquetas e lista de atributos.
- Conteudo: Grupo muscular primário, grupos secundários, categoria, equipamentos complementares (quando houver), nível e trilha Vela.

**Secao 3 — Instruções de execução**
- Componente: Texto.
- Conteudo: Passo a passo da execução. Se vazio, a seção é omitida.

**Secao 4 — Observações gerais**
- Componente: Texto.
- Conteudo: Observações gerais sobre o exercício. Se vazio, omitida.

### 3.3 Footer / Rodape
- Conteudo: Botão "Editar". Para o Aluno (futuro): N/A.
- Comportamento: Fixo na parte inferior em mobile.

---

## 4. Campos e Formularios

N/A — Tela sem formularios (somente leitura).

---

## 5. Botoes e Acoes

| # | Componente | Label / Icone | Posicao | Estado Inicial | Acao ao Clicar |
|---|---|---|---|---|---|
| 1 | Botão voltar | ← | Header (esq.) | Ativo | Volta para a Lista `[VELA-3001]` |
| 2 | Player de vídeo | ▶ | Seção de mídia | Ativo (se houver vídeo) | Reproduz o vídeo embutido |
| 3 | Botão / menu | "Editar" | Header / Rodapé | Visível só p/ Treinador dono | Abre Cadastro `[VELA-3003]` em modo edição |
| 4 | Menu | "Ativar / Desativar" | Header (⋯) | Visível só p/ Treinador dono | Alterna disponibilidade; ao desativar, exibe aviso ("continua nas rotinas atuais, mas não pode ser adicionado a novas") |
| 5 | Menu | "Excluir" | Header (⋯) | Visível só p/ Treinador dono; **desabilitado se estiver em uso** | Abre modal de confirmação → exclui definitivamente (só se não estiver em nenhuma rotina) → volta à Lista |

---

## 6. Estados da Tela

### 6.1 Estado Inicial / Vazio
- Tela carregada com os dados do exercício. Seções de texto vazias são **omitidas** (não mostram rótulo sem conteúdo).

### 6.2 Estado de Carregamento (Loading)
- Skeleton loader na área de mídia e nas seções enquanto os dados carregam.

### 6.3 Estado de Erro
- **Erro de rede/API:** toast "Não foi possível carregar o exercício." + botão recarregar.
- **Vídeo indisponível:** mensagem na área de mídia "Vídeo indisponível" (mantém o restante das informações).

### 6.4 Estado de Sucesso
- Após editar, retorno a esta tela com os dados atualizados e toast "Exercício atualizado".

### 6.5 Estado Desabilitado / Bloqueado
- Para o **Aluno** (futuro), nenhuma ação de edição aparece.

---

## 7. Fluxo de Navegacao

### De onde o usuario chega nesta tela
| Origem | Gatilho |
|---|---|
| Lista de Exercícios `[VELA-3001]` | Toca no card do exercício |
| Cadastro de Exercício `[VELA-3003]` | (Opcional) após salvar, abre a visualização |

### Para onde o usuario pode ir desta tela
| Destino | Gatilho |
|---|---|
| Lista de Exercícios `[VELA-3001]` | Botão voltar ou após excluir |
| Cadastro de Exercício `[VELA-3003]` | "Editar" |

---

## 8. Regras de Negocio
> Regras especificas que impactam o comportamento desta tela.

- RN01: A visualização é a tela **única de leitura** para um exercício do acervo do Treinador.
- RN02: Seções de texto **vazias são omitidas** — a tela mostra só o que foi preenchido.
- RN03: Todo exercício é do próprio Treinador, que vê **"Editar"/"Excluir"**. Não há acervo global nem ação "Duplicar".
- RN04: Séries/repetições/carga **não** aparecem aqui (são da Rotina); a tela mostra apenas a definição do exercício.
- RN05: Exclusão é **definitiva**, sempre confirmada por modal e **só permitida se o exercício não estiver em uso por nenhuma rotina**; caso contrário, usar **Desativar** (ver `[VELA-3003]` RN07/RN11).
- RN07: Exercício **inativo** é sinalizado com etiqueta "Inativo"; permanece visível e abrível, mas não pode ser adicionado a novas rotinas. **Os dados são preservados** ao desativar e voltam ao reativar. Ao **reativar**, exibir alerta pedindo para **revisar o exercício**.
- RN06: O **vídeo de execução** está sempre presente (obrigatório no cadastro). Não há áudio no exercício.

---

## 9. Responsividade (Mobile vs Web)

| Aspecto | Mobile | Web |
|---|---|---|
| Layout | Coluna única; mídia no topo, seções empilhadas; ação fixa no rodapé | Mídia à esquerda e informações à direita (2 colunas), ou centralizado max-width ~960px |
| Player de vídeo | Largura total, responsivo | Player em destaque na coluna de mídia |
| Ações | Botão fixo no rodapé + menu ⋯ | Botões no topo/lateral |

---

## 10. Acessibilidade
- Player de vídeo com controles acessíveis e legenda quando disponível.
- Hierarquia de títulos (headings) clara entre as seções.
- Contraste conforme WCAG 2.1 AA (paleta Vela).
- Navegação por teclado entre seções e ações.
- Imagem de capa com texto alternativo (nome do exercício).

---

## 11. Historico de Alteracoes

| Data | Autor | Descricao |
|---|---|---|
| 2026-06-17 | Equipe Vela | Criação inicial do documento (visualização de exercício — visão do Treinador); substitui o antigo "Detalhe do Exercício" |

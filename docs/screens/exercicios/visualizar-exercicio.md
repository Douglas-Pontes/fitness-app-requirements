# Tela: Visualizar Exercício `[VELA-3002]`

---

## Metadados
| Campo | Valor |
|---|---|
| **Nome da tela** | Visualizar Exercício |
| **Modulo** | Exercícios |
| **Codigo** | VELA-3002 |
| **Prioridade** | 🔵 MVP |
| **Status** | 🟢 CONCLUIDO |
| **Ultima atualizacao** | 2026-06-18 |

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
- Conteudo: Botão voltar (←) + Nome do exercício (com **badge "Inativo"** ao lado do nome quando aplicável) + menu de ações ⋯ (Ativar-Desativar / Excluir). No web, "Editar" também aparece no topo/lateral.
- Comportamento: Fixo no topo. Nome longo é truncado com reticências.
- **Faixa de estado inativo:** quando o exercício está inativo, exibir uma faixa/banner discreta logo abaixo do header: "Exercício inativo — não pode ser adicionado a novas rotinas."

### 3.2 Corpo Principal
> Scroll vertical, com a mídia no topo e as informações em seções.

**Secao 1 — Mídia**
- Componente: Player de vídeo (da base do app ou do YouTube), formato 16:9.
- Conteudo: Vídeo de execução (sempre presente — obrigatório no cadastro).
- Comportamento: Exibe **thumbnail/capa com botão ▶**; a reprodução só começa ao tocar (sem autoplay).

**Secao 2 — Classificação**
- Componente: Lista **híbrida** — cada atributo numa linha com **rótulo à esquerda e valor(es) como chips à direita**.
- Conteudo (ordem): Trilha Vela, Grupo muscular primário, Grupos secundários, Categoria, Equipamentos complementares (quando houver), Nível.
- Comportamento:
  - Atributos **sem valor são omitidos** (não mostram rótulo vazio), mesma lógica das seções de texto.
  - **Trilha Vela** (`.track`/`.performance`) e **Grupo muscular primário** usam chip na **cor-assinatura (verde-limão neon)**; demais atributos em chip neutro.
  - **Nível** é exibido como chip de texto simples (sem indicador gráfico).

**Secao 3 — Instruções de execução**
- Componente: Texto.
- Conteudo: Passo a passo da execução. Se vazio, a seção é omitida.

**Secao 4 — Observações gerais**
- Componente: Texto.
- Conteudo: Observações gerais sobre o exercício. Se vazio, omitida.

### 3.3 Footer / Rodape
- Conteudo: Botão "Editar" (mobile). No web, "Editar" fica no topo/lateral. Para o Aluno (futuro): N/A.
- Comportamento: Fixo na parte inferior em mobile. O menu ⋯ do header contém apenas **Ativar/Desativar** e **Excluir** (sem "Editar", para evitar duplicação).

---

## 4. Campos e Formularios

N/A — Tela sem formularios (somente leitura).

---

## 5. Botoes e Acoes

| # | Componente | Label / Icone | Posicao | Estado Inicial | Acao ao Clicar |
|---|---|---|---|---|---|
| 1 | Botão voltar | ← | Header (esq.) | Ativo | Volta para a Lista `[VELA-3001]` |
| 2 | Player de vídeo | ▶ | Seção de mídia | Ativo (se houver vídeo) | Reproduz o vídeo embutido |
| 3 | Botão | "Editar" | Rodapé (mobile) / topo-lateral (web) | Visível só p/ Treinador dono | Abre Cadastro `[VELA-3003]` em modo edição |
| 4 | Menu | "Ativar / Desativar" | Header (⋯) | Visível só p/ Treinador dono | Abre **modal de confirmação** explicando o efeito ("continua nas rotinas atuais, mas não pode ser adicionado a novas") → confirma → alterna disponibilidade |
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
- **Exercício inativo:** badge "Inativo" ao lado do nome + faixa/banner abaixo do header ("Exercício inativo — não pode ser adicionado a novas rotinas"). As ações de Editar/Excluir continuam disponíveis ao Treinador dono; "Ativar/Desativar" passa a oferecer **Reativar**.

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
- RN02: Seções de texto **e atributos de classificação vazios são omitidos** — a tela mostra só o que foi preenchido.
- RN08: **Desativar exige modal de confirmação** (assim como Excluir), explicando que o exercício continua nas rotinas atuais mas não pode ser adicionado a novas.
- RN03: Todo exercício é do próprio Treinador, que vê **"Editar"/"Excluir"**. Não há acervo global nem ação "Duplicar".
- RN04: Séries/repetições/carga **não** aparecem aqui (são da Rotina); a tela mostra apenas a definição do exercício.
- RN05: Exclusão é **definitiva**, sempre confirmada por modal e **só permitida se o exercício não estiver em uso por nenhuma rotina**; caso contrário, usar **Desativar** (ver `[VELA-3003]` RN07/RN11).
- RN06: O **vídeo de execução** está sempre presente (obrigatório no cadastro). Não há áudio no exercício.
- RN07: Exercício **inativo** é sinalizado com etiqueta "Inativo"; permanece visível e abrível, mas não pode ser adicionado a novas rotinas. **Os dados são preservados** ao desativar e voltam ao reativar. Ao **reativar**, exibir alerta pedindo para **revisar o exercício**.

---

## 9. Responsividade (Mobile vs Web)

| Aspecto | Mobile | Web |
|---|---|---|
| Layout | Coluna única; mídia no topo, seções empilhadas; ação fixa no rodapé | **2 colunas** centralizado em max-width ~960px: vídeo à esquerda (~55%), informações roláveis à direita |
| Player de vídeo | Largura total, responsivo (16:9) | Vídeo fixo/destaque na coluna esquerda |
| Ações | Barra fixa no rodapé com **apenas "Editar"** + menu ⋯ no header (Ativar-Desativar / Excluir) | "Editar" no topo/lateral + menu ⋯ |

---

## 10. Acessibilidade
- Player de vídeo com controles acessíveis, rótulo/título do vídeo (nome do exercício) e legenda quando disponível.
- Hierarquia de títulos (headings) clara entre as seções.
- Contraste conforme WCAG 2.1 AA (paleta Vela).
- Navegação por teclado entre seções e ações.

---

## 11. Historico de Alteracoes

| Data | Autor | Descricao |
|---|---|---|
| 2026-06-17 | Equipe Vela | Criação inicial do documento (visualização de exercício — visão do Treinador); substitui o antigo "Detalhe do Exercício" |
| 2026-06-18 | Equipe Vela | Revisão: classificação omite atributos vazios; "Desativar" exige modal de confirmação (RN08); "Editar" único por plataforma (sai do menu ⋯); acessibilidade do vídeo corrigida. Status → CONCLUIDO |
| 2026-06-18 | Equipe Vela | Decisões de layout (pré-mockup): classificação híbrida (rótulo + chips); trilha e grupo primário na cor-assinatura; vídeo em thumbnail+play 16:9 (sem autoplay); estado inativo com badge + faixa explicativa; web em 2 colunas (vídeo esq./infos dir., max-width ~960px); nível como chip de texto; rodapé mobile só "Editar" |

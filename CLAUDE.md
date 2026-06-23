# Vela — Contexto do Projeto

## O Que Este Repositorio E

Este repositorio contem o **documento de requisitos completo** do **Vela**, um app de musculacao (mobile + web). Aqui nao tem codigo — apenas documentacao de requisitos em Markdown. O objetivo e mapear **todas as telas, campos, comportamentos, fluxos e regras de negocio** antes de iniciar o desenvolvimento.

O documento sera usado como entrada para:
1. **Lovable** — gerar a base do projeto (arquitetura, layout, rotas)
2. **Claude Code** — construir as features do app a partir dos requisitos detalhados

## Identidade da Marca

O produto se chama **Vela** — *o ponto onde a evolucao comeca*. A marca representa **direcao aplicada ao treino**: transformar esforco em progresso real. O logotipo termina em ponto (`vela.`), simbolo do inicio da jornada.

O produto tem duas categorias (trilhas), ambas usando o ponto como elemento da marca:
- **`.track`** — evolucao fisica, estetica e consistencia (hipertrofia, emagrecimento, estilo de vida).
- **`.performance`** — atletas/esportes: forca, potencia, resistencia, velocidade, prevencao de lesao.

Paleta-assinatura: **verde-limao neon** (`#CCF24D` aprox.) + **azuis** (marinho/claro/ardosia), estilo minimalista de alto contraste, tipografia geometrica em caixa baixa.

> Detalhes completos em `docs/04-identidade-de-marca.md`. Logos em `assets/identidade/`.

## Idioma e Estilo

- Todos os documentos sao escritos em **portugues brasileiro**
- Usar linguagem **clara e direta**, sem jargoes desnecessarios
- Campos pendentes sao marcados com `⚠️ PENDENTE` — isso e um padrao, nao remover esse marcador ate o campo ser preenchido
- Status de telas usam emojis padrao: 🔴 NAO INICIADO | 🟡 EM ANDAMENTO | 🟠 PENDENTE REVISAO | 🟢 CONCLUIDO

## Estrutura do Projeto

```
docs/
  00-template-tela.md      ← Template padrao (SEMPRE seguir ao criar telas)
  01-visao-geral.md        ← Indice mestre com status de todas as telas
  02-personas.md           ← Personas e jornadas do usuario
  03-fluxos-de-navegacao.md ← Mapa de navegacao entre telas
  04-identidade-de-marca.md ← Marca Vela: conceito, paleta, logo, categorias
  05-mvp.md                ← Definicao do que entra no MVP vs futuro
  guia-de-uso.md           ← Guia de uso dos comandos do projeto
  screens/                 ← Uma pasta por modulo, um .md por tela
    auth/
    onboarding/
    dashboard/
    treinos/               ← modulo misto: subpastas por publico
      treinador/           ← telas do Treinador (ex: lista-treinos, cadastro-treino)
      aluno/               ← telas do Aluno (ex: treino-andamento, historico)
    rotinas/
      treinador/           ← base de rotinas + atribuicao (ex: lista-rotinas, atrelar-rotina-aluno)
      aluno/               ← consumo de rotinas (ex: minhas-rotinas)
    exercicios/
    avaliacoes/
    perfil/
      aluno/               ← meu-perfil, editar-perfil, minhas-metas
      treinador/           ← perfil-aluno-visao-treinador
    configuracoes/
```

> **Separacao por publico:** quando um modulo tem telas de **Aluno** e de **Treinador**, separa-las em subpastas `<modulo>/treinador/` e `<modulo>/aluno/` (espelhado em `mockups/`). O `mockups/` segue a mesma estrutura de `docs/screens/`. Modulos de publico unico nao precisam de subpasta ate ganharem telas do outro publico.

## Como Trabalhar Neste Projeto

### Ao criar uma nova tela:
1. Copiar o template de `docs/00-template-tela.md`
2. Salvar em `docs/screens/[modulo]/[nome-da-tela].md` — em modulos mistos, dentro da subpasta do publico: `docs/screens/[modulo]/[treinador|aluno]/[nome-da-tela].md`
3. Preencher TODAS as secoes do template — se algo nao se aplica, escrever "N/A" em vez de deixar vazio
4. Atualizar o status no indice em `docs/01-visao-geral.md`

### Ao revisar uma tela:
1. Buscar todos os `⚠️ PENDENTE` no arquivo
2. Para cada pendencia, fazer perguntas objetivas ao usuario (com opcoes quando possivel)
3. Atualizar o status da tela apos a revisao

### Ao criar um novo fluxo:
1. Usar diagramas ASCII no estilo dos existentes em `docs/03-fluxos-de-navegacao.md`
2. Sempre listar: entrada, telas, decisoes, modais, saidas

## Convencoes de Nomenclatura

- Nomes de arquivo: `kebab-case.md` (ex: `treino-andamento.md`)
- Nomes de pasta: `kebab-case` sem acentos (ex: `avaliacoes`, nao `avaliações`)
- **Publico em modulo misto:** usar subpasta `treinador/` ou `aluno/` em vez de sufixo no nome do arquivo (a subpasta ja indica o publico e resolve colisoes de nome — ex: `treinos/treinador/lista-treinos.md` vs `treinos/aluno/lista-treinos.md`)
- Regras de negocio: prefixo `RN` + numero sequencial (ex: RN01, RN02)
- Campos de formulario: usar o nome que aparecera na UI como label

## Regras Importantes

- **Nunca** gerar conteudo de tela sem seguir o template em `00-template-tela.md`
- **Sempre** respeitar a identidade da marca **Vela** (paleta, tom, conceito do ponto e nomenclatura das categorias `.track`/`.performance`) definida em `04-identidade-de-marca.md` ao gerar/mapear telas, fluxos e resumos
- **Sempre** atualizar o indice em `01-visao-geral.md` ao criar/modificar telas
- **Sempre** verificar se o fluxo de navegacao e bidirecional (se A vai pra B, B deve listar A como origem)
- **Separar copy de UI de nota interna** — Toda informacao **necessaria ao usuario** aparece **na tela** (ex: alerta do PAR-Q, "ultima medicao" da avaliacao anterior, mensagens de erro/validacao, textos de ajuda que orientam a acao). Ja explicacoes/justificativas **internas** (regras de comportamento, decisoes de design, racional do tipo "o treinador pode deixar em branco...", referencias a RNs) ficam **somente nos documentos** (`docs/`) e **nunca** sao renderizadas na tela nem nos mockups. Em caso de duvida se um texto e copy de UI ou nota interna, **perguntar**.
- Quando o usuario disser algo ambiguo, **perguntar antes de assumir** — requisitos errados custam caro
- Priorizar perguntas **objetivas com opcoes** (ex: "O botao deve ficar desabilitado ate preencher? Sim/Nao")
- **Sempre marcar a opcao recomendada:** em **toda** pergunta com opcoes (em qualquer processo ou tela, inclusive na ferramenta de perguntas), adicionar **`(recomendado)`** ao final do rotulo da opcao que voce julgar ser a melhor e coloca-la **como a primeira** da lista. Sempre existe uma recomendada.
- **Manter o mockup em sincronia com o doc:** sempre que alterar o **comportamento visivel** de uma tela que **ja possui** mockup em `mockups/...` (layout, campos, copy de UI, botoes, estados), **atualizar o `.html` correspondente na MESMA tarefa**, espelhando o documento — sem precisar o usuario pedir. Mudancas **puramente internas** (notas, RNs sem reflexo visual) **nao** exigem atualizar o mockup. Para telas **sem** mockup, **nao** gerar automaticamente — isso so via `/visualizar-tela` quando solicitado. Ao final, avisar que o mockup foi atualizado e lembrar do hard refresh (Cmd+Shift+R).
- Ao identificar uma decisao em aberto, adicionar na tabela "Decisoes em Aberto" do `01-visao-geral.md`

## Custom Commands Disponiveis

Use `/` seguido do nome do comando no Claude Code:

- `/mapear-tela` — Documentar uma nova tela do zero (interativo)
- `/revisar-tela` — Revisar tela existente e completar pendencias
- `/mapear-fluxo` — Mapear fluxo de navegacao de um modulo
- `/entrevistar-cliente` — Processar respostas/anotacoes do cliente
- `/validar-consistencia` — Checar inconsistencias entre documentos
- `/gerar-resumo` — Gerar resumo executivo ou briefing tecnico
- `/estimar-complexidade` — Estimar complexidade e planejar implementacao
- `/mapear-modulo` — Mapear um modulo inteiro (fluxo + todas as telas)
- `/visualizar-tela` — Gerar um mockup HTML+CSS (Tailwind) de uma tela para conferencia visual
- `/status` — Ver progresso atual do documento de requisitos

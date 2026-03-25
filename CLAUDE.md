# FitnessApp — Contexto do Projeto

## O Que Este Repositorio E

Este repositorio contem o **documento de requisitos completo** de um app de musculacao (mobile + web). Aqui nao tem codigo — apenas documentacao de requisitos em Markdown. O objetivo e mapear **todas as telas, campos, comportamentos, fluxos e regras de negocio** antes de iniciar o desenvolvimento.

O documento sera usado como entrada para:
1. **Lovable** — gerar a base do projeto (arquitetura, layout, rotas)
2. **Claude Code** — construir as features do app a partir dos requisitos detalhados

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
  04-design-system.md      ← Cores, fontes, componentes base
  06-mvp.md                ← Definicao do que entra no MVP vs futuro
  screens/                 ← Uma pasta por modulo, um .md por tela
    auth/
    onboarding/
    dashboard/
    treinos/
    rotinas/
    exercicios/
    avaliacoes/
    perfil/
    configuracoes/
```

## Como Trabalhar Neste Projeto

### Ao criar uma nova tela:
1. Copiar o template de `docs/00-template-tela.md`
2. Salvar em `docs/screens/[modulo]/[nome-da-tela].md`
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
- Regras de negocio: prefixo `RN` + numero sequencial (ex: RN01, RN02)
- Campos de formulario: usar o nome que aparecera na UI como label

## Regras Importantes

- **Nunca** gerar conteudo de tela sem seguir o template em `00-template-tela.md`
- **Sempre** atualizar o indice em `01-visao-geral.md` ao criar/modificar telas
- **Sempre** verificar se o fluxo de navegacao e bidirecional (se A vai pra B, B deve listar A como origem)
- Quando o usuario disser algo ambiguo, **perguntar antes de assumir** — requisitos errados custam caro
- Priorizar perguntas **objetivas com opcoes** (ex: "O botao deve ficar desabilitado ate preencher? Sim/Nao")
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
- `/status` — Ver progresso atual do documento de requisitos

# Vela — Documento de Requisitos

Repositorio de especificacao completa do Vela: app mobile e web para alunos de musculacao.

---

## Como Usar Este Repositorio

### Pre-requisitos
- VS Code
- Extensao recomendada: **Markdown All in One** (para preview dos `.md`)
- **Claude Code** (plano Pro recomendado)

### Setup

1. Abra esta pasta no VS Code
2. Abra o Claude Code — ele lera automaticamente o `CLAUDE.md` e ja entendera o contexto
3. Use os **custom commands** (descritos abaixo) para conduzir o trabalho

---

## Custom Commands (Slash Commands)

Estes comandos sao invocados diretamente no Claude Code digitando `/` + nome:

| Comando | O que faz | Exemplo de uso |
|---|---|---|
| `/mapear-tela` | Documenta uma nova tela do zero (entrevista interativa) | `/mapear-tela Cadastro` |
| `/revisar-tela` | Revisa tela existente e completa pendencias | `/revisar-tela docs/screens/auth/login.md` |
| `/mapear-fluxo` | Mapeia fluxo de navegacao de um modulo | `/mapear-fluxo Treinos` |
| `/mapear-modulo` | Mapeia modulo completo (fluxo + todas as telas) | `/mapear-modulo Avaliacoes` |
| `/entrevistar-cliente` | Processa respostas/anotacoes do cliente | `/entrevistar-cliente reuniao sobre treinos` |
| `/validar-consistencia` | Checa inconsistencias entre documentos | `/validar-consistencia` ou `/validar-consistencia Treinos` |
| `/gerar-resumo` | Gera resumo executivo ou briefing | `/gerar-resumo cliente` ou `/gerar-resumo lovable` |
| `/estimar-complexidade` | Estima complexidade de desenvolvimento | `/estimar-complexidade` |
| `/visualizar-tela` | Gera mockup HTML (Tailwind) de uma tela para conferencia visual | `/visualizar-tela docs/screens/perfil/meu-perfil.md` |
| `/status` | Ve progresso atual do documento | `/status` |

> Os prompts manuais em `prompts/` continuam disponiveis como referencia, mas os custom commands acima sao a forma recomendada de trabalhar.

---

## Fluxo de Trabalho Recomendado

```
1. Entrevista/reuniao com o cliente
        ↓ usar: /entrevistar-cliente

2. Definir o que entra no MVP
        ↓ editar: docs/05-mvp.md

3. Mapear fluxo de navegacao do modulo
        ↓ usar: /mapear-fluxo [modulo]

4. Documentar cada tela do modulo
        ↓ usar: /mapear-tela [tela]
        ↓ (ou /mapear-modulo para fazer tudo de uma vez)

5. Revisar e completar telas com pendencias
        ↓ usar: /revisar-tela [arquivo]

6. Validar consistencia entre as telas
        ↓ usar: /validar-consistencia

7. Checar progresso
        ↓ usar: /status

8. Gerar entregaveis
        ↓ usar: /gerar-resumo cliente  (para o cliente)
        ↓ usar: /gerar-resumo dev      (para o time)
        ↓ usar: /gerar-resumo lovable  (para iniciar o dev)
```

---

## Estrutura de Arquivos

```
fitness-app-requirements/
├── CLAUDE.md                           ← Contexto lido automaticamente pelo Claude Code
├── .claude/
│   └── commands/                       ← Custom commands (slash commands)
│       ├── mapear-tela.md
│       ├── revisar-tela.md
│       ├── mapear-fluxo.md
│       ├── mapear-modulo.md
│       ├── entrevistar-cliente.md
│       ├── validar-consistencia.md
│       ├── gerar-resumo.md
│       ├── estimar-complexidade.md
│       ├── status.md
│       └── visualizar-tela.md
├── prompts/                            ← Prompts manuais (referencia)
├── mockups/                            ← Mockups HTML (Tailwind) gerados por /visualizar-tela
├── docs/
│   ├── 00-template-tela.md             ← Template padrao para novas telas
│   ├── 01-visao-geral.md              ← Indice mestre + status de cada tela
│   ├── 02-personas.md                 ← Personas e jornadas do usuario
│   ├── 03-fluxos-de-navegacao.md      ← Mapa de navegacao entre telas
│   ├── 04-identidade-de-marca.md      ← Marca Vela: conceito, paleta, logo, categorias
│   ├── 05-mvp.md                      ← Definicao do MVP vs futuro
│   ├── guia-de-uso.md                 ← Guia de uso dos comandos do projeto
│   └── screens/                       ← Uma pasta por modulo, um .md por tela
│       ├── auth/
│       ├── onboarding/
│       ├── dashboard/
│       ├── treinos/
│       ├── rotinas/
│       ├── exercicios/
│       ├── avaliacoes/
│       ├── perfil/
│       └── configuracoes/
└── assets/
    └── identidade/                     ← Logos da marca (vela. / .track / .performance)
```

---

## Status do Projeto

Consulte `docs/01-visao-geral.md` para o indice completo e status de cada tela.
Ou use `/status` no Claude Code para um resumo rapido.

**Legenda:**
- 🔴 NAO INICIADO
- 🟡 EM ANDAMENTO
- 🟠 PENDENTE REVISAO
- 🟢 CONCLUIDO

> O nivel de detalhe esperado para cada tela esta definido no template `docs/00-template-tela.md`.

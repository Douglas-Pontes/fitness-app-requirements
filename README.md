# FitnessApp — Documento de Requisitos

Repositório de especificação completa do FitnessApp: app mobile e web para alunos de musculação.

---

## Como Usar Este Repositório

### Pré-requisitos
- VS Code
- Extensão recomendada: **Markdown All in One** (para preview dos `.md`)
- Claude Code (plano Pro recomendado para usar Projects com contexto persistente)

### Setup no Claude Code

1. Abra esta pasta no VS Code
2. Abra o Claude Code e crie um **novo Project**
3. Adicione este repositório como contexto do projeto
4. O Claude vai ler automaticamente o `CLAUDE.md` e já entenderá o contexto completo

---

## Fluxo de Trabalho

```
1. Reunião/entrevista com o cliente
        ↓ usar: prompts/entrevistar-cliente.md
        
2. Mapear fluxo de navegação do módulo
        ↓ usar: prompts/mapear-fluxo.md
        
3. Documentar cada tela do módulo
        ↓ usar: prompts/mapear-tela.md
        
4. Revisar e completar telas com pendências
        ↓ usar: prompts/revisar-tela.md
        
5. Validar consistência entre as telas
        ↓ usar: prompts/validar-consistencia.md
        
6. Gerar resumo para apresentação ou próxima etapa
        ↓ usar: prompts/gerar-resumo.md
        
7. Estimar complexidade / planejar implementação
        ↓ usar: prompts/estimar-complexidade.md
```

---

## Estrutura de Arquivos

```
fitness-app-requirements/
├── .claude/
│   └── CLAUDE.md                    ← Contexto lido automaticamente pelo Claude Code
├── prompts/
│   ├── mapear-tela.md               ← Documentar nova tela do zero
│   ├── revisar-tela.md              ← Completar tela com pendências
│   ├── mapear-fluxo.md              ← Mapear fluxo de navegação
│   ├── entrevistar-cliente.md       ← Conduzir/processar entrevista
│   ├── gerar-resumo.md              ← Gerar resumo executivo
│   ├── validar-consistencia.md      ← Checar inconsistências
│   └── estimar-complexidade.md      ← Estimar complexidade e planejar dev
├── docs/
│   ├── 00-template-tela.md          ← Template padrão para novas telas
│   ├── 01-visao-geral.md            ← Visão geral + índice de progresso
│   ├── 02-personas.md               ← Personas e jornadas do usuário
│   ├── 03-fluxos-de-navegacao.md    ← Mapa de navegação entre telas
│   ├── 04-design-system.md          ← Cores, fontes, componentes base
│   └── screens/
│       ├── auth/
│       │   └── login.md             ← Exemplo de tela preenchida ✅
│       ├── onboarding/
│       ├── dashboard/
│       ├── treinos/
│       ├── rotinas/
│       ├── exercicios/
│       ├── avaliacoes/
│       ├── perfil/
│       └── configuracoes/
└── assets/
    └── wireframes/                  ← Rascunhos e imagens de referência
```

---

## Status do Projeto

Consulte `docs/01-visao-geral.md` para o índice completo e status de cada tela.

**Legenda:**
- 🔴 NÃO INICIADO
- 🟡 EM ANDAMENTO  
- 🟠 PENDENTE REVISÃO
- 🟢 CONCLUÍDO

---

## Tela de Exemplo

O arquivo `docs/screens/auth/login.md` está preenchido como **exemplo de referência** do nível de detalhe esperado para todas as telas.

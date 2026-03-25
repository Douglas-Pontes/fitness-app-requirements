Gere um resumo do documento de requisitos do FitnessApp.

**Tipo de resumo:** $ARGUMENTS
(Opcoes: "cliente", "dev", "status", "lovable")

Leia todos os documentos do projeto e gere conforme o tipo:

---

**Se "cliente"** — Resumo executivo para apresentar ao cliente:
- Maximo 2 paginas, linguagem nao tecnica
- Visao geral, modulos, principais fluxos
- Tabela de decisoes pendentes do cliente
- Proximos passos
- Salvar em `docs/resumos/resumo-cliente.md`

**Se "dev"** — Briefing tecnico para desenvolvedor:
- Arquitetura de telas com rotas sugeridas
- Pontos de atencao tecnica
- O que esta confirmado vs pendente
- Salvar em `docs/resumos/briefing-dev.md`

**Se "status"** — Status report de progresso:
- Total de telas documentadas vs total
- Status por modulo (tabela)
- Pendencias criticas
- Proximos 3 arquivos sugeridos para documentar
- NAO salvar, apenas exibir

**Se "lovable"** — Prompt otimizado para o Lovable:
- Em INGLES (Lovable performa melhor)
- Arquitetura de navegacao, telas do MVP, design system
- Prompt pronto para colar no Lovable
- Salvar em `docs/resumos/prompt-lovable.md`

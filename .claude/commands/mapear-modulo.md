Vamos mapear um modulo COMPLETO do FitnessApp — fluxo + todas as telas.

**Modulo:** $ARGUMENTS

Este comando conduz o mapeamento completo de um modulo em uma unica sessao. O processo e:

## Fase 1 — Visao Geral do Modulo
Me pergunte:
- Qual o proposito deste modulo?
- Quais acoes o usuario realiza aqui?
- Este modulo faz parte do MVP? (consulte `docs/06-mvp.md`)

## Fase 2 — Fluxo de Navegacao
Me pergunte sobre:
- Como o usuario chega no modulo
- Quais telas existem
- Como as telas se conectam
- Modais e sheets
Depois gere o diagrama ASCII e atualize `docs/03-fluxos-de-navegacao.md`

## Fase 3 — Documentar Cada Tela (uma por vez)
Para cada tela identificada no fluxo:
1. Me faca as perguntas do template (em blocos, nao tudo de uma vez)
2. Gere o arquivo `.md` seguindo `docs/00-template-tela.md`
3. Salve em `docs/screens/[modulo]/`
4. Atualize o indice em `docs/01-visao-geral.md`

## Fase 4 — Validacao Cruzada
Ao terminar todas as telas:
1. Verifique navegacao bidirecional entre as telas do modulo
2. Verifique consistencia de campos e nomenclatura
3. Reporte o que foi criado e se ha pendencias

Conduza a conversa fase por fase, aguardando minhas respostas antes de avancar.

# Prompt: Estimar Complexidade

> **Como usar:** Use após documentar um conjunto de telas para ter uma estimativa
> de complexidade de desenvolvimento. Útil para planejar sprints no Lovable/Claude.

---

## Variante A — Estimativa por Tela

```
Analise o documento de requisitos da tela [NOME DA TELA / ARQUIVO] e estime sua complexidade de desenvolvimento.

Para cada tela, avalie e classifique em: 🟢 Simples | 🟡 Média | 🔴 Complexa

Critérios:
- Número de campos e validações
- Quantidade de estados diferentes
- Integrações com APIs
- Lógica de negócio envolvida
- Componentes visuais especiais (gráficos, câmera, timer, etc.)
- Diferença de comportamento mobile vs. web

Gere uma tabela com:
| Tela | Complexidade | Principais razões | Atenções especiais para o dev |
```

---

## Variante B — Estimativa do Projeto Completo

```
Com base em todos os documentos de requisitos do FitnessApp, gere uma estimativa de complexidade para o projeto completo.

Organize por módulo:
1. Classifique cada tela: 🟢 Simples | 🟡 Média | 🔴 Complexa
2. Identifique os 5 componentes/features mais complexos do projeto
3. Identifique dependências críticas (o que precisa ser feito antes de outra coisa)
4. Sugira uma ordem de implementação fazendo sentido técnico:
   - O que deve ser feito primeiro (fundação)
   - O que pode ser feito em paralelo
   - O que depende de outras partes prontas

Formato de saída: lista ordenada de módulos com justificativa, não uma estimativa de horas.
```

---

## Variante C — Plano de Implementação para Lovable

```
Com base no documento de requisitos do FitnessApp, me ajude a criar o melhor prompt inicial para o Lovable.

O prompt do Lovable deve:
1. Descrever a arquitetura de navegação principal (tab bar + stacks)
2. Listar as telas do MVP (mínimo para funcionar)
3. Definir as entidades de dados principais
4. Especificar o design system base (cores, fontes, estilo)
5. Ser claro o suficiente para o Lovable gerar uma estrutura de projeto sólida

Baseie-se nos documentos:
- `docs/01-visao-geral.md`
- `docs/03-fluxos-de-navegacao.md`
- `docs/04-design-system.md`

Gere o prompt pronto para colar no Lovable, em inglês (o Lovable performa melhor em inglês).
```

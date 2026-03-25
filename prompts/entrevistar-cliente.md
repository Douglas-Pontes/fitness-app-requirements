# Prompt: Entrevistar Cliente

> **Como usar:** Use no início do projeto ou ao iniciar um novo módulo para extrair requisitos do cliente.
> Ideal para sessões de descoberta. Você pode adaptar o foco para um módulo específico.

---

## Variante A — Entrevista Geral (início de projeto)

```
Vou te passar as respostas do meu cliente sobre o FitnessApp. Me ajude a:
1. Identificar os requisitos claros a partir das respostas
2. Identificar ambiguidades e o que ainda precisa ser esclarecido
3. Sugerir as próximas perguntas para aprofundar o entendimento
4. Ao final, gerar um resumo dos requisitos descobertos e atualizar os documentos relevantes

Aqui estão as respostas do cliente:
---
[COLE AQUI AS RESPOSTAS DO CLIENTE]
---
```

---

## Variante B — Roteiro de Entrevista por Módulo

```
Preciso preparar uma entrevista com meu cliente sobre o módulo de [NOME DO MÓDULO] do FitnessApp.

Me gere um roteiro de perguntas para a entrevista cobrindo:

1. **Propósito:** O que o usuário precisa conseguir neste módulo?
2. **Regras de negócio:** Quais são as regras e restrições mais importantes?
3. **Dados:** Quais informações precisam ser armazenadas e exibidas?
4. **Fluxo:** Como o usuário interage com este módulo passo a passo?
5. **Casos extremos:** O que acontece em situações excepcionais?
6. **Diferenciais:** O que deve ser diferente do que existe no mercado?

Organize as perguntas do mais geral para o mais específico, em linguagem acessível para um cliente não técnico.
Máximo de 15 perguntas para não cansar.
```

---

## Variante C — Processar Anotações de Reunião

```
Tive uma reunião com o cliente sobre [ASSUNTO]. Aqui estão minhas anotações brutas:

---
[COLE SUAS ANOTAÇÕES AQUI]
---

Por favor:
1. Organize as informações em requisitos claros
2. Separe o que é CONFIRMADO do que é INCERTO ou PENDENTE
3. Identifique contradições ou pontos que precisam de esclarecimento
4. Gere as atualizações necessárias nos documentos do projeto:
   - Se houver novos requisitos de tela → identifique quais arquivos de tela precisam ser criados ou atualizados
   - Se houver decisões sobre fluxo → sinalize atualização no `03-fluxos-de-navegacao.md`
   - Se houver decisões em aberto resolvidas → atualize a tabela em `01-visao-geral.md`
```

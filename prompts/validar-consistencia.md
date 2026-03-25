# Prompt: Validar Consistência

> **Como usar:** Use periodicamente para encontrar contradições, lacunas ou inconsistências
> entre os documentos de tela. Essencial antes de entregar o documento ao time de dev.

---

## Variante A — Validação Completa

```
Analise todos os documentos de requisitos do FitnessApp e identifique inconsistências.

Verifique especificamente:

1. **Navegação quebrada:** Existe alguma tela que é mencionada como destino de navegação em outro documento, mas que ainda não foi documentada?

2. **Campos inconsistentes:** O mesmo dado é nomeado de forma diferente em telas diferentes? (ex: "nome completo" em uma tela e "nome do usuário" em outra para o mesmo campo)

3. **Fluxos contraditórios:** Alguma tela A diz que navega para B, mas B não lista A como origem?

4. **Regras de negócio conflitantes:** Alguma regra em uma tela contradiz uma regra em outra?

5. **Estados faltando:** Alguma tela documenta a ação de "criar/editar/deletar" mas não documenta o estado de loading ou erro dessa ação?

6. **APIs indefinidas:** Alguma tela usa dados que nunca são definidos (não tem endpoint mapeado)?

Gere um relatório organizado por tipo de problema, com referência ao arquivo e sugestão de correção.
```

---

## Variante B — Validação de um Módulo Específico

```
Valide a consistência interna do módulo [NOME DO MÓDULO] do FitnessApp.

Leia todos os arquivos em `docs/screens/[modulo]/` e verifique:
1. Todas as telas do módulo estão documentadas conforme o índice em `01-visao-geral.md`?
2. Os fluxos de navegação batem entre as telas (origem e destino)
3. Campos que aparecem em múltiplas telas são consistentes
4. Todos os estados obrigatórios estão documentados em cada tela
5. Não há ⚠️ PENDENTE em campos críticos (campos, validações, regras de negócio principais)

Liste os problemas encontrados com: [Tela] → [Problema] → [Sugestão]
```

---

## Variante C — Checklist de Qualidade por Tela

```
Aplique o seguinte checklist de qualidade na tela: [ARQUIVO DA TELA]

Checklist:
- [ ] Objetivo da tela está claro e em 1-3 frases?
- [ ] Pré-condições de acesso definidas?
- [ ] Todos os elementos visuais descritos (header, corpo, footer)?
- [ ] Todos os campos têm: tipo, obrigatoriedade, validação, mensagem de erro?
- [ ] Todos os botões têm: posição, estado inicial, ação ao clicar?
- [ ] Estado vazio documentado?
- [ ] Estado de loading documentado?
- [ ] Estado de erro documentado?
- [ ] Estado de sucesso documentado?
- [ ] Origens de navegação definidas?
- [ ] Destinos de navegação definidos?
- [ ] Regras de negócio listadas?
- [ ] Sem campos ⚠️ PENDENTE em itens críticos?

Para cada item reprovado, indique o que precisa ser preenchido.
```

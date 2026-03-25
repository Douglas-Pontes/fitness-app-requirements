Analise todos os documentos de requisitos do FitnessApp e identifique inconsistencias.

**Escopo:** $ARGUMENTS
(Se vazio, validar TUDO. Se informado um modulo, validar apenas ele.)

Leia todos os documentos relevantes e verifique:

1. **Navegacao quebrada:** Tela mencionada como destino mas que nao existe como arquivo
2. **Navegacao unidirecional:** Tela A diz que vai pra B, mas B nao lista A como origem
3. **Campos inconsistentes:** Mesmo dado com nomes diferentes em telas diferentes
4. **Regras conflitantes:** Regra em uma tela contradiz outra
5. **Estados faltando:** Tela tem acao de criar/editar/deletar mas nao documenta loading/erro
6. **Template desatualizado:** Tela nao tem todas as secoes do template atual (`docs/00-template-tela.md`)
7. **Indice desatualizado:** Status no `docs/01-visao-geral.md` nao bate com o status real do arquivo

Gere um relatorio organizado:
```
## Problemas Criticos (bloqueiam desenvolvimento)
## Problemas Medios (causam retrabalho)
## Melhorias Sugeridas (qualidade do documento)
```

Para cada problema: [Arquivo] → [Problema] → [Sugestao de correcao]

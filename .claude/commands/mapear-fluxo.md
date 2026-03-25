Vamos mapear o fluxo de navegacao de um modulo do FitnessApp.

**Modulo:** $ARGUMENTS

Conduza a conversa me fazendo perguntas sobre:

1. **Entrada:** Como o usuario chega neste modulo? (tab bar, botao, notificacao, deep link)
2. **Telas:** Quais telas existem dentro deste modulo? Me ajude a pensar se esta faltando alguma
3. **Tela principal:** Qual e a tela "hub" de onde o usuario navega para as demais?
4. **Criacao/edicao:** Se o modulo permite criar ou editar algo, como e o fluxo? (tela unica, wizard, modal)
5. **Detalhe:** Como o usuario acessa detalhes de um item?
6. **Saida:** De quais formas o usuario sai do modulo?
7. **Modais/sheets:** Quais acoes abrem modais ou bottom sheets?
8. **Casos especiais:** Estados que redirecionam (sem dados, nao logado, plano gratuito)

Apos coletar as respostas:
1. Gere um diagrama ASCII no estilo dos existentes em `docs/03-fluxos-de-navegacao.md`
2. Liste as telas a documentar com sugestao de nome de arquivo
3. Atualize `docs/03-fluxos-de-navegacao.md` com o novo fluxo
4. Atualize `docs/01-visao-geral.md` se novas telas forem identificadas

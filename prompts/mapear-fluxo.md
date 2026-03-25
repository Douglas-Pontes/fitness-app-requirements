# Prompt: Mapear Fluxo de Navegação

> **Como usar:** Use para mapear ou revisar o fluxo de navegação entre telas de um módulo específico.
> Ótimo para usar no início de um módulo antes de documentar as telas individualmente.

---

```
Vamos mapear o fluxo de navegação do módulo [NOME DO MÓDULO] do FitnessApp.

Contexto do módulo: [DESCREVA BREVEMENTE O QUE O MÓDULO FAZ]

Me ajude a responder as seguintes perguntas para construir o fluxo completo:

1. **Entrada no módulo:** Como o usuário chega neste módulo? (Tab bar, botão em outra tela, notificação, deep link?)

2. **Telas do módulo:** Quais são todas as telas que existem dentro deste módulo?

3. **Tela principal:** Qual é a tela "hub" do módulo, ou seja, a tela inicial de onde o usuário navega para as demais?

4. **Fluxos de criação/edição:** Se o módulo permite criar ou editar algo, como é esse fluxo? (tela única? wizard em etapas? modal?)

5. **Fluxos de detalhe:** Como o usuário acessa o detalhe de um item? (clique na lista → detalhe)

6. **Pontos de saída:** De quais formas o usuário sai do módulo? (botão voltar, concluir ação, cancelar)

7. **Modais e sheets:** Quais ações abrem modais ou bottom sheets em vez de novas telas?

8. **Casos especiais:** Existe algum estado que redireciona o usuário? (ex: sem dados → tela vazia com CTA, não logado → login)

Após nossa conversa, gere:
- Um diagrama de fluxo em texto (ASCII) no estilo dos outros fluxos em `docs/03-fluxos-de-navegacao.md`
- A lista de telas a serem documentadas, com sugestão de nome de arquivo
- Atualize o arquivo `docs/03-fluxos-de-navegacao.md` com o novo fluxo
```

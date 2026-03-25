# Prompt: Mapear Nova Tela

> **Como usar:** Cole este prompt no Claude Code, substitua os campos em [COLCHETES] e envie.
> O Claude vai conduzir você pelas perguntas e ao final gerar o arquivo `.md` da tela preenchido.

---

```
Vamos documentar uma nova tela do FitnessApp seguindo nosso padrão de requisitos.

**Tela a documentar:** [NOME DA TELA]
**Módulo:** [ex: Autenticação / Treinos / Rotinas / Avaliações / Perfil]

Antes de gerar o documento, me faça as perguntas necessárias para preencher corretamente todos os campos do template. Cubra obrigatoriamente:

1. **Objetivo:** O que o usuário faz nesta tela? Qual problema resolve?
2. **Acesso:** Quem pode ver esta tela? Precisa estar logado? Tem permissões especiais?
3. **Layout:** Quais elementos visuais aparecem na tela? (header, seções, cards, listas, formulários, botões flutuantes)
4. **Campos:** Se tiver formulário — quais campos, tipos, são obrigatórios, quais validações, mensagens de erro
5. **Botões e ações:** Quais botões existem, onde ficam, o que fazem ao clicar
6. **Estados:** Como fica a tela quando está vazia? Carregando? Com erro? Com sucesso? Sem conexão?
7. **Navegação:** De onde o usuário chega nesta tela? Para onde pode ir a partir dela?
8. **Regras de negócio:** Tem alguma regra especial? Limites, condições, restrições?
9. **APIs/integrações:** Quais dados a tela busca ou envia? Tem algum endpoint específico?
10. **Notas técnicas:** Alguma atenção especial para o desenvolvedor?

Faça as perguntas em blocos, não todas de uma vez. Após coletar as respostas, gere o arquivo `.md` completo seguindo exatamente o template em `docs/00-template-tela.md`.

O arquivo deve ser salvo em: `docs/screens/[MODULO]/[nome-da-tela].md`
```

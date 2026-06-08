Gere um mockup de UI (HTML + CSS com Tailwind) de uma tela do Vela, apenas para conferencia visual.

**Arquivo da tela:** $ARGUMENTS

> Este mockup e **avulso**: serve so para visualizar se a tela documentada esta fazendo sentido. **Nao** e codigo de producao e **nao** entra no app.

Faca o seguinte, em modo direto (sem entrevista):

1. Leia o documento da tela indicado em `$ARGUMENTS`.
2. Leia `docs/04-identidade-de-marca.md` para aplicar paleta, tipografia e tom da marca.
3. Extraia do doc: layout (secao 3 — header / corpo / footer), campos (secao 4), botoes e acoes (secao 5), estados (secao 6) e responsividade (secao 9).
4. Gere **um unico arquivo HTML standalone** com Tailwind via CDN (`<script src="https://cdn.tailwindcss.com"></script>`) — sem build, abre direto no navegador com duplo clique.
5. Salve em `mockups/[modulo]/[nome-da-tela].html`, espelhando o caminho do arquivo em `docs/screens/`. Crie a pasta do modulo se nao existir.
6. Ao final, informe o caminho do arquivo gerado e instrua a abrir no navegador.

## Fidelidade ao documento (obrigatorio)

- Renderize **exatamente** os campos, botoes e secoes descritos no doc — use os textos e labels que aparecem nele.
- **Nao invente** funcionalidade, campos ou conteudo que nao esteja no documento.
- Campos marcados com `⚠️ PENDENTE` viram um placeholder visivel com aviso (ex: borda tracejada + texto "⚠️ pendente"), nunca conteudo fabricado.

## Identidade visual Vela (obrigatorio)

- **Mobile-first:** cada tela e renderizada dentro de um **frame de celular** (~390px de largura, cantos arredondados, fundo neutro ao redor, simulando o device).
- **Paleta** via config inline do Tailwind:
  ```html
  <script>
    tailwind.config = {
      theme: { extend: { colors: {
        lime: '#CCF24D',        // verde-limao neon — cor-assinatura / destaque
        navy: '#0E4C86',        // azul-marinho — texto sobre o verde
        track: '#A8DAEC',       // azul-claro — categoria .track
        performance: '#4B5F79', // azul-ardosia — categoria .performance
      } } }
    }
  </script>
  ```
- **Tipografia:** sans-serif geometrica do Google Fonts (ex: Poppins ou Sora), pesos leve/regular. Textos de marca em **caixa baixa**, alto contraste, layout minimalista com bastante respiro.
- **Marca:** quando fizer sentido (header, splash, topo), use o logotipo `vela.` **preservando o ponto**. Para telas de categoria, respeite `.track` (fundo azul-claro) e `.performance` (fundo azul-ardosia).

## Estados a renderizar

- Renderize o **estado principal** da tela e, ao lado, os **estados-chave** descritos na secao 6 do doc — apenas os que existirem (vazio, loading, erro, sucesso, bloqueado).
- Disponha os frames **lado a lado** num layout que quebra para coluna em telas estreitas (ex: `flex flex-wrap`), cada frame **rotulado** com o nome do estado (ex: "principal", "vazio", "erro").

## Banner de aviso

No topo do HTML, inclua um banner fixo deixando claro que e um mockup:

> "Mockup visual — nao e codigo de producao. Gerado a partir de `docs/screens/.../arquivo.md`."

(substitua pelo caminho real do doc usado)

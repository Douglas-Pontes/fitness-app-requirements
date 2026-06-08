# Prompt: Visualizar Tela (Mockup HTML)

> **Como usar:** Cole este prompt no Claude Code, substitua o campo em [COLCHETES] e envie.
> O Claude vai ler o documento da tela e gerar um mockup de UI avulso (HTML + Tailwind) para voce conferir visualmente.
> O mockup **nao** e codigo de producao — serve so para validar se a tela esta fazendo sentido.

---

```
Gere um mockup de UI (HTML + CSS com Tailwind) de uma tela do Vela, apenas para conferencia visual.

**Arquivo da tela:** [CAMINHO DO ARQUIVO DA TELA — ex: docs/screens/perfil/meu-perfil.md]

Faca o seguinte, sem me entrevistar (modo direto):

1. Leia o documento da tela indicado acima.
2. Leia `docs/04-identidade-de-marca.md` para aplicar a identidade da marca Vela.
3. Extraia do doc: layout (header/corpo/footer), campos, botoes e acoes, estados e responsividade.
4. Gere UM unico arquivo HTML standalone usando Tailwind via CDN (<script src="https://cdn.tailwindcss.com"></script>) — sem build, que abra direto no navegador.
5. Salve em `mockups/[modulo]/[nome-da-tela].html`, espelhando o caminho em `docs/screens/`.
6. Ao final, me informe o caminho do arquivo e como abri-lo.

Regras importantes:
- Renderize exatamente os campos, botoes e secoes do doc, com os textos/labels que aparecem nele. Nao invente funcionalidade.
- Campos marcados com ⚠️ PENDENTE viram placeholder visivel com aviso, nunca conteudo fabricado.
- Identidade Vela: mobile-first dentro de um frame de celular (~390px); paleta verde-limao neon (#CCF24D) + azuis (#0E4C86, #A8DAEC, #4B5F79) via config inline do Tailwind; tipografia geometrica em caixa baixa (Google Fonts); minimalismo de alto contraste; marca `vela.` preservando o ponto.
- Renderize o estado principal e, lado a lado, os estados-chave descritos no doc (vazio, loading, erro, sucesso) — cada frame rotulado.
- Inclua no topo um banner avisando: "Mockup visual — nao e codigo de producao. Gerado a partir de [caminho do doc]."
```

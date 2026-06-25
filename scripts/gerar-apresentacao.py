#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera um unico arquivo HTML de apresentacao das telas do Vela para o cliente.
- Embute cada mockup via <iframe srcdoc> (arquivo autocontido / portatil).
- Descricoes e campos sao escritos a mao a partir dos docs de requisitos.
Saida: apresentacao-telas-vela.html (na raiz do projeto)
"""

import html
import os
import re
import subprocess
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOCK = os.path.join(ROOT, "mockups")

# Chrome usado para medir a altura real de cada mockup em tempo de build.
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
# Largura do conteudo do iframe (= largura da coluna do mockup, menos a borda).
IFRAME_W = 878
ALTURA_FALLBACK = 1500  # usado se a medicao com o Chrome falhar

# ---------------------------------------------------------------------------
# Conteudo: categorias -> telas. Cada tela:
#   titulo, publico ("Treinador" | "Aluno" | "Aluno e Treinador"),
#   arquivo (relativo a mockups/), o_que_faz (str),
#   campos: lista de (nome, explicacao) — foco em campos com logica/fonte de dados.
# ---------------------------------------------------------------------------

CATEGORIAS = [
    {
        "id": "exercicios",
        "nome": "Exercícios",
        "intro": "O exercício é a peça reutilizável do app: o treinador cadastra cada movimento uma vez "
                 "(com vídeo, classificação e instruções) e depois o reaproveita em vários treinos. "
                 "Importante: o exercício <strong>não</strong> guarda séries/repetições — esses números são definidos no Treino.",
        "telas": [
            {
                "titulo": "Lista de Exercícios",
                "publico": "Treinador",
                "arquivo": "exercicios/lista-exercicios.html",
                "o_que_faz": "Acervo de exercícios do treinador. Tela inicial do módulo: busca, filtra, "
                             "cria, abre e gerencia os exercícios. Cada card tem um atalho de vídeo que "
                             "abre a execução sem sair da tela.",
                "campos": [
                    ("Busca", "Filtra a lista enquanto digita. É \"normalizada\": ignora acentos e maiúsculas/minúsculas "
                              "(digitar \"triceps\" ou \"Tríceps\" dá o mesmo resultado)."),
                    ("Filtros (Grupo muscular / Categoria / Nível)", "Tocar em cada botão abre uma folha inferior com as opções. "
                              "São combináveis entre si e com a busca; o botão fica destacado quando há filtro ativo."),
                    ("Contador de resultados", "Mostra o total atual da lista (ex.: \"12 exercícios\") e acompanha os filtros aplicados."),
                    ("Card do exercício (ao tocar)", "Abre a tela nº 03 (Visualizar Exercício), com vídeo, classificação e instruções."),
                    ("Linha de metadados do card", "Mostra grupo muscular primário · categoria · nível. Categoria e nível "
                              "só aparecem quando preenchidos. Equipamento e trilha não entram no card."),
                    ("Atalho de vídeo (▶)", "Abre o vídeo de execução num modal por cima da lista, sem perder a posição; ao fechar, volta ao mesmo ponto."),
                    ("Menu ⋮ → Incluir em treino", "Abre uma folha inferior com os treinos em rascunho do treinador. Marca um ou vários e o exercício "
                              "entra em cada um sem séries/reps — a prescrição é completada depois, dentro do treino. Não aparece para exercícios inativos."),
                    ("Menu ⋮ → Editar", "Abre o Cadastro (nº 02) já preenchido com os dados do exercício."),
                    ("Menu ⋮ → Ativar/Desativar", "Alterna a disponibilidade. Desativado, o exercício continua nos treinos atuais, mas não entra em novos."),
                    ("Menu ⋮ → Excluir", "Pede confirmação e exclui em definitivo — só é permitido se o exercício não estiver em nenhum treino."),
                    ("Botão \"+\" (novo exercício)", "Botão flutuante no rodapé que abre o Cadastro (nº 02) em branco."),
                    ("Etiqueta \"Inativo\"", "Marca exercícios desativados; eles continuam visíveis e abríveis, só não entram em novos treinos."),
                ],
            },
            {
                "titulo": "Cadastro / Edição de Exercício",
                "publico": "Treinador",
                "arquivo": "exercicios/cadastro-exercicio.html",
                "o_que_faz": "Formulário para criar ou editar um exercício. A mesma tela serve para os dois casos "
                             "(vem em branco ou pré-preenchida). Define o exercício de forma reutilizável — sem séries/repetições.",
                "campos": [
                    ("Nome do exercício", "Obrigatório. Precisa ser único por nível dentro do acervo do treinador "
                              "(pode repetir o nome se o nível for diferente)."),
                    ("Grupo muscular primário", "Obrigatório, seleção única. É o que aparece em destaque no card da lista."),
                    ("Grupos musculares secundários", "Opcional, múltipla escolha — músculos auxiliares trabalhados."),
                    ("Categoria", "Opcional, mas recomendada: alimenta o filtro da lista (hipertrofia, força, alongamento etc.)."),
                    ("Equipamentos complementares", "Opcional. Registra só o que não fica óbvio no vídeo (ex.: band, step). "
                              "Ao adicionar, o app sugere os materiais que o treinador já usou antes e permite digitar um novo."),
                    ("Nível", "Obrigatório (iniciante / intermediário / avançado). Opções fixas — sustentam o filtro e a regra de nome único por nível."),
                    ("Trilha Vela", "Opcional. Marca o exercício como .track e/ou .performance (pode pertencer às duas)."),
                    ("Vídeo de execução", "Opcional. Duas fontes: escolher entre os vídeos do próprio treinador ou colar um link do YouTube. "
                              "Ao informar, mostra uma pré-visualização do player."),
                    ("Imagem de capa", "Opcional. Se ficar vazia, o app usa a miniatura do vídeo como capa."),
                    ("Instruções de execução / Observações", "Campos de texto longo, opcionais — passo a passo e notas que aparecem na visualização do exercício."),
                    ("Ativo / Inativo (só na edição)", "Desativar não apaga nada — todos os dados ficam salvos. Ao reativar, o app pede para revisar o exercício."),
                    ("Salvar exercício", "Fica desabilitado até preencher os obrigatórios. Ao salvar, volta para a Lista (nº 01) com o exercício em destaque."),
                ],
            },
            {
                "titulo": "Visualizar Exercício",
                "publico": "Treinador",
                "arquivo": "exercicios/visualizar-exercicio.html",
                "o_que_faz": "Tela de leitura com tudo do exercício organizado: vídeo, classificação, instruções e observações. "
                             "A partir daqui o treinador edita, ativa/desativa ou exclui.",
                "campos": [
                    ("Player de vídeo", "Mostra capa com botão ▶; só reproduz ao clicar (sem autoplay)."),
                    ("Bloco de classificação", "Lista cada atributo com o(s) valor(es) em \"chips\". "
                              "Atributos vazios são omitidos — a tela mostra só o que foi preenchido."),
                    ("Faixa \"Exercício inativo\"", "Aparece quando o exercício está desativado, avisando que ele não pode entrar em novos treinos."),
                    ("Editar", "Abre o Cadastro (nº 02) já preenchido para alterar o exercício."),
                    ("Menu ⋯ → Ativar/Desativar", "Abre um modal de confirmação explicando o efeito antes de alternar a disponibilidade."),
                    ("Excluir", "Só é permitido se o exercício não estiver em uso em nenhum treino. Se estiver, o caminho é desativar."),
                ],
            },
        ],
    },
    {
        "id": "treinos",
        "nome": "Treinos",
        "intro": "O treino agrupa exercícios em <strong>grupos numerados (1, 2, 3…)</strong> e é onde a prescrição vive: "
                 "cada exercício recebe séries, repetições e descanso. O treino é um bloco reutilizável que depois compõe as Rotinas. "
                 "O aluno tem uma versão própria desta tela, voltada para <strong>executar</strong> o treino.",
        "telas": [
            {
                "titulo": "Lista de Treinos",
                "publico": "Treinador",
                "arquivo": "treinos/treinador/lista-treinos.html",
                "o_que_faz": "Base de treinos reutilizáveis do treinador. Cria, abre, duplica, ativa/desativa e exclui treinos.",
                "campos": [
                    ("Busca", "Filtra por nome, normalizada (ignora acento e maiúsculas/minúsculas)."),
                    ("Filtros (Categoria / Status)", "Status filtra entre Ativos / Inativos / Todos; combinam com a busca."),
                    ("Card do treino (ao tocar)", "Abre a tela nº 06 (Visualizar Treino), com os grupos, exercícios e a prescrição."),
                    ("Conteúdo do card", "Nome, categoria e quantidade de exercícios (ex.: \"Hipertrofia · 6 exercícios\") + selo de status (Ativo/Inativo)."),
                    ("Menu ⋮ → Incluir em rotina", "Abre uma folha inferior com as rotinas em rascunho; adiciona o treino a uma ou mais. "
                              "A ordem (letras A, B, C…) é definida depois, dentro da rotina. Não aparece para treinos inativos."),
                    ("Menu ⋮ → Duplicar", "Cria uma cópia editável do treino na própria lista, independente do original (\"Treino duplicado\")."),
                    ("Menu ⋮ → Ativar/Desativar", "Alterna o status ali mesmo; inativo continua nas rotinas atuais, mas não entra em novas."),
                    ("Menu ⋮ → Excluir", "Pede confirmação e exclui em definitivo — só se o treino não estiver em nenhuma rotina; senão, o caminho é desativar."),
                    ("Botão \"+\" (novo treino)", "Botão flutuante que abre o Cadastro de Treino (nº 05) em branco."),
                ],
            },
            {
                "titulo": "Cadastro / Edição de Treino",
                "publico": "Treinador",
                "arquivo": "treinos/treinador/cadastro-treino.html",
                "o_que_faz": "Monta o treino: dados gerais + lista de exercícios em grupos numerados, cada exercício com sua prescrição. "
                             "Mesma tela para criar e editar.",
                "campos": [
                    ("Nome do treino", "Obrigatório, único na base do treinador."),
                    ("Categoria", "Obrigatória, seleção única (Aeróbico, Força e Potência, Resistência, Funcional, Mobilidade, Abdômen/Core)."),
                    ("Áudio do treino", "Opcional. Gravação feita no app com uma instrução sobre o treino como um todo (máx. 2 minutos). Não há áudio por exercício."),
                    ("Grupos numerados (1, 2, 3…)", "A numeração é automática pela ordem. As letras A, B, C… ficam reservadas para a Rotina."),
                    ("Tipo do grupo", "Opcional: Normal, Bi-set, Tri-set, Superset ou Drop-set. O tipo define quantos exercícios o grupo aceita "
                              "(Normal/Drop-set = 1; Bi-set/Superset = 2; Tri-set = 3). Sem tipo = Normal. Ao atingir o limite, o botão de adicionar fica indisponível."),
                    ("Adicionar exercício", "Abre o seletor sobre o acervo do treinador (só exercícios ativos). No seletor, o ícone de vídeo abre a execução num modal "
                              "e tocar no exercício abre a tela nº 03 (Visualizar Exercício)."),
                    ("Séries", "Obrigatório por exercício — número inteiro."),
                    ("Repetições", "Obrigatório por exercício — aceita faixa (ex.: \"10-12\")."),
                    ("Descanso", "Obrigatório por exercício, em segundos. Aceita 0 (exercícios emendados), mas não pode ficar em branco."),
                    ("Descrição de execução", "Opcional, por exercício (ex.: cadência, observação de técnica)."),
                    ("Arrastar (⠿) para reordenar", "Reordena exercícios dentro do grupo; a ordem de execução segue os grupos e a posição."),
                    ("Salvar treino", "Desabilitado até ter nome, categoria e ao menos 1 exercício com séries/reps/descanso. Ao salvar, volta para a Lista (nº 04)."),
                ],
            },
            {
                "titulo": "Visualizar Treino",
                "publico": "Treinador",
                "arquivo": "treinos/treinador/visualizar-treino.html",
                "o_que_faz": "Leitura do treino sem risco de alterar por acidente: dados gerais + grupos e exercícios com a prescrição. "
                             "Daqui o treinador edita, duplica ou exclui.",
                "campos": [
                    ("Cards de exercício (ao tocar)", "Mostram a prescrição em leitura (séries, repetições, descanso). Tocar no card abre a tela nº 03 "
                              "(Visualizar Exercício), com vídeo e execução completa."),
                    ("Editar", "Botão no rodapé que abre o Cadastro de Treino (nº 05) já preenchido."),
                    ("Menu ⋮ → Duplicar", "Cria a cópia \"Nome (cópia)\" e já abre a edição (nº 05) para ajustar."),
                    ("Menu ⋮ → Excluir", "Pede confirmação; bloqueado se o treino estiver em uso em alguma rotina (mostra aviso)."),
                ],
            },
            {
                "titulo": "Visualizar / Executar Treino (Aluno)",
                "publico": "Aluno",
                "arquivo": "treinos/aluno/visualizar-treino.html",
                "o_que_faz": "Tela onde o aluno consulta e executa o treino: assiste aos vídeos, inicia a sessão, marca séries com timer de "
                             "descanso e finaliza. Ao finalizar, gera o registro de execução e mostra um resumo compartilhável (estilo story).",
                "campos": [
                    ("Play/Pause + cronômetro geral (topo)", "O cronômetro começa em 00:00 e só conta depois que o aluno toca em Play; pode pausar e retomar. "
                              "É ele que mede a duração do treino e habilita os controles de execução nos cards."),
                    ("Vídeo / thumbnail do exercício", "Ao tocar, abre o player do exercício num modal por cima da lista."),
                    ("Contador de séries", "Por exercício (ex.: \"3 / 4\"); o exercício fica concluído quando todas as séries são marcadas."),
                    ("Reps realizadas / Carga realizada", "Pré-preenchidos com o que o treinador sugeriu; o aluno só ajusta se fez diferente. Não é obrigatório editar para concluir."),
                    ("Botão \"⏱ Descanso\"", "Abre um timer regressivo iniciando no descanso prescrito (ex.: 0:45→0:00), com +15s e Play. Não dispara sozinho; "
                              "ao zerar, re-arma para a próxima série."),
                    ("Check (✓) / \"Marcar como concluído\"", "Marca o exercício como feito (card fica verde). Exercícios sem séries usam só o botão \"Marcar como concluído\"."),
                    ("Sair (←) no meio do treino", "Não descarta nada: a sessão fica salva como \"em andamento\" e pode ser retomada de onde parou."),
                    ("Finalizar treino", "Encerra a sessão, grava o registro de execução (alimenta os contadores das telas 12 e 13) e abre o resumo."),
                    ("Resumo / card compartilhável", "Mostra duração, exercícios concluídos e \"treinos na semana\" (execuções de seg–sex ÷ total de treinos das rotinas ativas). "
                              "Pode editar (mover/ocultar itens, trocar o fundo) e compartilhar no story, com a marca vela. em destaque."),
                    ("Compartilhar", "Abre o editor do card e, em seguida, a folha do sistema com os destinos: Story do Instagram, WhatsApp e Salvar."),
                    ("Recado para o treinador", "Opcional (máx. 300 caracteres). É privado — vai junto do registro de execução e nunca entra na imagem compartilhada."),
                ],
            },
        ],
    },
    {
        "id": "rotinas",
        "nome": "Rotinas",
        "intro": "A rotina é um conjunto ordenado de <strong>treinos</strong>, identificados por <strong>letras A, B, C…</strong> "
                 "É o que o treinador monta na sua base e depois <strong>atribui a um aluno</strong>. O aluno tem suas próprias telas "
                 "para ver as rotinas que recebeu. Lembrando a hierarquia: exercício → treino → rotina.",
        "telas": [
            {
                "titulo": "Lista de Rotinas",
                "publico": "Treinador",
                "arquivo": "rotinas/treinador/lista-rotinas.html",
                "o_que_faz": "Base de rotinas reutilizáveis do treinador. Cria, abre, duplica, ativa/desativa e exclui rotinas.",
                "campos": [
                    ("Busca", "Filtra por título, normalizada (ignora acento e caixa)."),
                    ("Filtros (treino / categoria do treino / status)", "Permitem achar rotinas que contêm um determinado treino ou categoria, e filtrar por Ativas/Inativas/Todas."),
                    ("Card da rotina (ao tocar)", "Abre a tela nº 10 (Visualizar Rotina), com a lista ordenada de treinos."),
                    ("Conteúdo do card", "Título, objetivo resumido e os treinos de forma compacta (ex.: \"4 treinos · A Peito · B Costas…\") + selo de status."),
                    ("Menu ⋮ → Duplicar", "Cria uma cópia da rotina ali mesmo na lista (\"Rotina duplicada\")."),
                    ("Menu ⋮ → Ativar/Desativar", "Alterna o status (abre confirmação ao desativar); inativar não apaga os dados."),
                    ("Menu ⋮ → Excluir", "Pede confirmação e exclui em definitivo."),
                    ("Botão \"+\" (nova rotina)", "Botão flutuante que abre o Cadastro de Rotina (nº 09) em branco."),
                ],
            },
            {
                "titulo": "Cadastro / Edição de Rotina",
                "publico": "Treinador",
                "arquivo": "rotinas/treinador/cadastro-rotina.html",
                "o_que_faz": "Monta a rotina: título, objetivo e uma lista ordenada de treinos. Mesma tela para criar e editar.",
                "campos": [
                    ("Título", "Obrigatório, único na base do treinador."),
                    ("Objetivo", "Obrigatório — descreve a finalidade da rotina."),
                    ("Letras A, B, C…", "Geradas automaticamente pela ordem dos treinos; reordenar por arrastar (⠿) atualiza as letras. Não são editáveis."),
                    ("Adicionar treino", "Abre um seletor sobre a base de treinos do treinador (só treinos ativos). O mesmo treino não pode entrar duas vezes na mesma rotina."),
                    ("Dia da semana (por treino)", "Opcional. O mesmo dia pode se repetir em mais de um treino (ex.: A e B na segunda)."),
                    ("Descrição curta (por treino)", "Opcional — uma nota daquele treino específica desta rotina (ex.: \"foco em carga\")."),
                    ("Ver treino (▶)", "Atalho no card que abre a tela nº 06 (Visualizar Treino) para conferir o conteúdo sem sair da montagem."),
                    ("Excluir rotina (só edição)", "Botão de texto vermelho ao fim do formulário; pede confirmação e exclui em definitivo."),
                    ("Salvar rotina", "Desabilitado até ter título, objetivo e ao menos 1 treino. Ao salvar, volta para a Lista (nº 08)."),
                ],
            },
            {
                "titulo": "Visualizar Rotina",
                "publico": "Treinador",
                "arquivo": "rotinas/treinador/visualizar-rotina.html",
                "o_que_faz": "Leitura da rotina: título, objetivo e a lista ordenada de treinos (A, B, C…). Daqui o treinador edita, "
                             "duplica, ativa/desativa ou exclui.",
                "campos": [
                    ("Cards de treino (ao tocar)", "Mostram letra + nome + categoria e um resumo (qtd de exercícios e grupos musculares). Tocar abre a tela nº 06 "
                              "(Visualizar Treino), com o conteúdo completo."),
                    ("Editar", "Botão no rodapé que abre o Cadastro de Rotina (nº 09) já preenchido."),
                    ("Menu ⋮ → Duplicar / Ativar-Desativar / Excluir", "Duplicar abre a edição da cópia; Ativar/Desativar alterna o status na hora; Excluir pede confirmação. "
                              "(É também o lugar reservado para o \"Atribuir a aluno\" — ver tela nº 11.)"),
                ],
            },
            {
                "titulo": "Atrelar Rotina ao Aluno",
                "publico": "Treinador",
                "arquivo": "rotinas/treinador/atrelar-rotina-aluno.html",
                "o_que_faz": "Atribui uma rotina a um aluno, definindo período de vigência, objetivo e uma mensagem. A rotina pode vir da base "
                             "ou ser criada na hora. O vínculo é uma cópia (snapshot) — independente da base.",
                "campos": [
                    ("Aluno", "Obrigatório. Vem travado quando o treinador chega pela tela do aluno; ou é escolhido por busca na entrada geral."),
                    ("Usar rotina da base", "Abre a Lista de Rotinas (nº 08) em modo seleção; o treinador escolhe uma rotina existente, que volta selecionada aqui."),
                    ("Criar nova rotina", "Abre o Cadastro de Rotina (nº 09); ao concluir, a rotina é salva na base e o fluxo volta a esta tela já com ela selecionada."),
                    ("Card-resumo da rotina", "Depois de escolhida, mostra título, objetivo e treinos. Tem atalhos \"Ver detalhes\" (abre a nº 10) e \"Trocar rotina\"."),
                    ("Aviso de prescrição incompleta", "Se algum exercício estiver sem séries/repetições, mostra um aviso com atalho \"Revisar prescrição\". É aviso, não bloqueio — pode entregar e completar depois."),
                    ("Data de início", "Obrigatória; não pode ser anterior a hoje."),
                    ("Data de fim", "Opcional. Em branco = rotina sem prazo (vale até ser trocada/encerrada). Se preenchida, tem que ser depois do início."),
                    ("Objetivo da rotina para este aluno", "Obrigatório — o objetivo específico desta atribuição."),
                    ("Mostrar prazo e progresso ao aluno", "Liga/desliga (ligado por padrão). Controla se o aluno vê as datas, a barra de progresso e o tempo decorrido nas telas 12 e 13. "
                              "Desligado, ele vê só o status (Ativa/Agendada/Encerrada). Não afeta a contagem de treinos realizados."),
                    ("Mensagem ao aluno", "Opcional — texto livre que o aluno vê ao receber a rotina."),
                    ("Atribuir rotina", "Cria a cópia (snapshot) vinculada ao aluno e volta para a tela do aluno. O aluno recebe uma notificação da nova rotina."),
                ],
            },
            {
                "titulo": "Minhas Rotinas (Aluno)",
                "publico": "Aluno",
                "arquivo": "rotinas/aluno/minhas-rotinas.html",
                "o_que_faz": "Lista, na visão do aluno, as rotinas atribuídas a ele, separadas em Ativas, Agendadas e Anteriores. Só leitura — o aluno não cria rotinas.",
                "campos": [
                    ("Seções Ativas / Agendadas / Anteriores", "Cada seção só aparece se tiver pelo menos uma rotina. O status é calculado automaticamente pelas datas + dia de hoje."),
                    ("Card da rotina (ao tocar)", "Abre a tela nº 13 (Detalhe da Rotina), com o progresso e a lista de treinos para executar."),
                    ("Selo de status", "Ativa / Agendada / Encerrada — derivado das datas, não é definido manualmente."),
                    ("Faixa de datas", "Só aparece se o treinador permitiu na atribuição; senão, o card mostra apenas título, objetivo e status."),
                    ("Contador \"X treinos realizados\"", "Total acumulado de execuções daquela rotina. Independe do controle de visibilidade. Rotinas agendadas (sem execução) não exibem contador."),
                ],
            },
            {
                "titulo": "Detalhe da Rotina (Aluno)",
                "publico": "Aluno",
                "arquivo": "rotinas/aluno/detalhe-rotina-aluno.html",
                "o_que_faz": "Detalhe de uma rotina atribuída: progresso de vigência, indicadores no topo e a lista de treinos (A, B, C…). "
                             "Daqui o aluno abre cada treino para executar.",
                "campos": [
                    ("KPIs / progresso de vigência", "Dias percorridos, dias restantes (quando há data de fim) e barra de % do período decorrido. "
                              "Respeitam o controle de visibilidade do treinador (somem se ele desligou)."),
                    ("Cards de treino (ao tocar)", "Letra + nome + categoria, com contador de exercícios. Tocar abre a tela nº 07 (Visualizar/Executar Treino) para executar."),
                    ("Tag \"recomendado do dia\"", "Aparece no treino cujo dia sugerido pelo treinador é o dia de hoje. É a única forma como o dia sugerido aparece no card."),
                    ("Considerações da rotina", "Aparece só quando a rotina está Encerrada: campo opcional (máx. 500 caracteres) para o aluno comentar como foi. É privado, vai ao treinador."),
                ],
            },
        ],
    },
    {
        "id": "avaliacoes",
        "nome": "Avaliações",
        "intro": "Módulo que responde \"estou evoluindo?\". O treinador cria avaliações (Anamnese, Antropométrica, Dobras Cutâneas, "
                 "Bioimpedância), preenche ou <strong>libera para o aluno preencher</strong>, e acompanha a evolução em gráficos. "
                 "Tudo gira em torno de quatro status: <strong>Solicitada → Em andamento → Concluída</strong> (ou <strong>Expirada</strong>).",
        "telas": [
            {
                "titulo": "Lista de Avaliações",
                "publico": "Aluno e Treinador",
                "arquivo": "avaliacoes/lista-avaliacoes.html",
                "o_que_faz": "Lista única de todos os tipos de avaliação, agrupada em Pendentes, Expiradas e Anteriores. O treinador cria/edita/exclui/libera; "
                             "o aluno visualiza e preenche o que foi liberado para ele.",
                "campos": [
                    ("Card (tipo, data, quem fez, status)", "Card enxuto e neutro: tipo e status são reconhecidos pelo ícone colorido. Não mostra métricas (peso, % de gordura) — isso fica ao abrir a avaliação."),
                    ("Visualizar (no card)", "Disponível para os dois papéis; abre a tela nº 16 (Visualizar Avaliação)."),
                    ("Preencher / Continuar (aluno)", "Aparece para o aluno nas pendentes (Solicitada ou Em andamento iniciada por ele); abre o formulário nº 15 em modo preenchimento."),
                    ("Editar / Revisar (treinador)", "Abre o formulário nº 15 já preenchido. \"Editar\" em Solicitada/Em andamento; \"Revisar\" em Concluída (edita no lugar)."),
                    ("Reabrir / Solicitar reabertura (expirada)", "Treinador vê \"Reabrir\" (volta a Solicitada com novo prazo). Aluno vê \"Solicitar reabertura\", que só avisa o treinador."),
                    ("Filtros (Período / Status / Tipo)", "Cada botão abre um painel; combinam entre si (E). A tela abre sem filtro aplicado."),
                    ("Status", "Solicitada (liberada, aguardando) · Em andamento (começou, não enviou) · Concluída (enviada) · Expirada (passou do prazo sem concluir)."),
                    ("Badge na aba (aluno)", "Contador de pendências do aluno (Solicitadas + Em andamento). Não conta Expiradas nem Concluídas."),
                    ("Menu ⋮ (treinador)", "Reúne \"Excluir\" (confirmação, definitivo) e, quando aplicável, \"Liberar para o aluno preencher\"."),
                    ("FAB \"Nova avaliação\"", "Só para o treinador. Abre o seletor de tipo e leva ao formulário nº 15, onde ele escolhe o aluno por busca."),
                    ("Toggle Lista | Análise", "Alterna entre esta lista e a tela nº 17 (Análise: gráficos e comparação)."),
                ],
            },
            {
                "titulo": "Cadastro / Edição / Preenchimento de Avaliação",
                "publico": "Aluno e Treinador",
                "arquivo": "avaliacoes/cadastro-avaliacao.html",
                "o_que_faz": "Formulário único e dinâmico que muda os campos conforme o tipo. Serve para o treinador criar/editar e para o aluno preencher "
                             "uma avaliação liberada. Abaixo de cada campo numérico mostra a última medição registrada.",
                "campos": [
                    ("Aluno (na criação)", "Travado quando aberto pelo perfil do aluno; campo de busca quando aberto pela entrada global (busca entre os alunos vinculados)."),
                    ("Tipo da avaliação", "Definido na criação e não muda depois. É o que decide quais campos o formulário mostra (Anamnese, Antropométrica, Dobras, Bioimpedância)."),
                    ("Quem vai preencher (Treinador / Aluno)", "Define a ação final: Treinador → \"Concluir\"; Aluno → \"Liberar para o aluno preencher\". "
                              "Se for o aluno, pergunta se haverá prazo."),
                    ("Prazo (data limite)", "Opcional, só quando o aluno vai preencher. Vencido sem envio, a avaliação fica Expirada. Sem prazo, nunca expira."),
                    ("Data da avaliação", "Obrigatória; não pode ser futura."),
                    ("\"Última: XXXXX\" sob cada campo", "Mostra só o último valor registrado daquele campo, do mesmo tipo de avaliação. Sem data nem variação. "
                              "Se não houver histórico, mostra \"Sem dados anterior\"."),
                    ("Campos calculados (IMC, RCQ, Soma das dobras)", "Preenchidos automaticamente e somente leitura; recalculam em tempo real conforme o preenchimento."),
                    ("Campos manuais de composição (% gordura, densidade, massa gorda/magra)", "O app não calcula — o treinador digita (calcula por fora ou registra de outra fonte). Em Dobras Cutâneas não há seletor de protocolo."),
                    ("PAR-Q (Anamnese)", "Sete perguntas Sim/Não. Qualquer \"Sim\" mostra um alerta recomendando liberação médica (informativo, não bloqueia)."),
                    ("Fotos / laudo", "Slots de foto por ângulo (frente, costas, perfis) e, na Bioimpedância, anexo do laudo. Todos opcionais."),
                    ("Aviso de faixa fora do esperado", "Valores muito fora do plausível mostram um aviso suave, mas não bloqueiam salvar (caso real/raro pode ser confirmado)."),
                    ("Salvar rascunho / Concluir / Enviar / Liberar", "Rascunho = Em andamento (retoma depois). Concluir/Enviar = Concluída. Liberar = Solicitada (notifica o aluno). "
                              "Em todos, ao salvar volta para a Lista (nº 14)."),
                ],
            },
            {
                "titulo": "Visualizar Avaliação",
                "publico": "Aluno e Treinador",
                "arquivo": "avaliacoes/visualizar-avaliacao.html",
                "o_que_faz": "Leitura completa de uma avaliação, adaptada ao tipo. Para cada campo numérico, mostra o valor e a variação vs. a avaliação anterior.",
                "campos": [
                    ("Variação vs. avaliação anterior", "Para campos numéricos, mostra ▲/▼/= com o delta — não depende só de cor (tem seta + texto)."),
                    ("Resumo-chave", "Quando concluída, destaca as métricas principais (ex.: % de gordura, peso)."),
                    ("Fotos / laudo", "Quando existirem, aparecem em galeria; tocar abre a visualização ampliada."),
                    ("Editar / Revisar (treinador)", "Abre o formulário nº 15 já preenchido."),
                    ("Preencher / Solicitar reabertura (aluno)", "\"Preencher\" se a avaliação está Solicitada (abre a nº 15); \"Solicitar reabertura\" se Expirada (avisa o treinador)."),
                    ("Menu ⋮ → Excluir (treinador)", "Pede confirmação e exclui em definitivo; ao concluir, volta para a Lista (nº 14)."),
                    ("Ver evolução", "Atalho para a tela nº 17 (Análise), abrindo na métrica/tipo correspondente."),
                ],
            },
            {
                "titulo": "Análise das Avaliações",
                "publico": "Aluno e Treinador",
                "arquivo": "avaliacoes/analise-avaliacoes.html",
                "o_que_faz": "Hub de análise (somente leitura) com duas visões: Gráficos (evolução de uma métrica ao longo do tempo) e "
                             "Comparar (avaliações do mesmo tipo lado a lado).",
                "campos": [
                    ("Toggle Gráficos | Comparar", "Alterna entre as duas visões. Gráficos abre por padrão."),
                    ("Seletor de métrica (Gráficos)", "Lista só métricas que têm ao menos uma medição (Peso, % gordura, IMC, Cintura etc.). Uma por vez."),
                    ("Resumo da métrica", "Valor mais recente + variação total no período exibido."),
                    ("Gráfico de linha", "Eixo X = datas, eixo Y = valor. Tocar num ponto mostra valor + data e leva à tela nº 16 (Visualizar Avaliação) daquela medição."),
                    ("Seletor de período", "3 meses / 6 meses / 1 ano / Tudo / Personalizado (intervalo de datas) — ajusta a janela do gráfico."),
                    ("Comparar (tipo + avaliações)", "Botão \"Selecionar avaliações\" abre um painel; só compara avaliações do mesmo tipo, no máximo as 5 mais recentes, exigindo pelo menos 2."),
                    ("Tabela comparativa", "Cada avaliação vira uma coluna; cada campo, uma linha, com a variação entre colunas. Tocar no cabeçalho (data) abre a avaliação (nº 16)."),
                ],
            },
        ],
    },
    {
        "id": "perfil",
        "nome": "Perfil",
        "intro": "Telas do perfil do aluno: consulta dos dados pessoais e edição. Alguns campos são apenas leitura porque vêm de "
                 "outros fluxos (ex.: o objetivo vem da Anamnese; o treinador vinculado é preenchido automaticamente).",
        "telas": [
            {
                "titulo": "Meu Perfil",
                "publico": "Aluno",
                "arquivo": "perfil/aluno/meu-perfil.html",
                "o_que_faz": "Hub do perfil: o aluno vê seus dados e a foto, acessa a edição, abre as configurações e sai da conta. Só visualização.",
                "campos": [
                    ("@ aluno.vela", "Identificador único do aluno em todo o sistema. Exibido ao lado da bandeira do país."),
                    ("Objetivo", "Somente leitura — vem da Anamnese do aluno."),
                    ("@ treinador.vela", "Somente leitura — referência ao treinador vinculado."),
                    ("Bandeira do país", "Mostra só a bandeira ao lado do @ (sem o nome do país)."),
                    ("Editar perfil", "Botão no topo que abre a tela nº 19 (Editar Perfil)."),
                    ("Engrenagem (⚙)", "Abre as Configurações (onde fica, por ex., a alteração de e-mail)."),
                    ("Sair", "Logout com confirmação (\"Deseja sair?\"); ao confirmar, volta para a tela de login."),
                ],
            },
            {
                "titulo": "Editar Perfil",
                "publico": "Aluno",
                "arquivo": "perfil/aluno/editar-perfil.html",
                "o_que_faz": "Edição dos dados pessoais e da foto. O aluno altera os campos editáveis e confirma em Salvar.",
                "campos": [
                    ("Foto de perfil", "Obrigatória. É o único lugar onde a foto é gerenciada — o ícone de lápis abre as opções Tirar foto / Escolher foto."),
                    ("@ aluno.vela", "Obrigatório e único no sistema: só letras minúsculas e números, sem espaços/caracteres especiais e sem palavras ofensivas. "
                              "Validado ao sair do campo e ao salvar; ao mudar, reflete em todo o app."),
                    ("Data de nascimento", "Digitável com máscara DD/MM/AAAA (sem date picker); não pode ser futura; sem idade mínima."),
                    ("WhatsApp", "Obrigatório, com DDI (suporta alunos de várias nacionalidades) e máscara."),
                    ("País", "Obrigatório — seletor com busca (bandeira + nome)."),
                    ("Sexo", "Obrigatório — Feminino / Masculino / Não Informar."),
                    ("@ instagram", "Único campo opcional do formulário."),
                    ("Somente leitura (E-mail, @ treinador.vela, Objetivo)", "E-mail muda só nas Configurações (com confirmação por e-mail); o treinador é automático; o objetivo vem da Anamnese."),
                    ("Salvar", "Fica desabilitado até haver alguma alteração válida. Ao salvar, mostra confirmação e volta para o Meu Perfil (nº 18). "
                              "Ao voltar sem salvar com mudanças pendentes, pergunta se quer descartar."),
                ],
            },
        ],
    },
]

# ---------------------------------------------------------------------------
# Montagem do HTML
# ---------------------------------------------------------------------------

BADGE_CLASS = {
    "Treinador": "badge-treinador",
    "Aluno": "badge-aluno",
    "Aluno e Treinador": "badge-ambos",
}


# CSS injetado em cada mockup para esconder notas internas de conferencia
# (banner de aviso no topo + bloco de notas/legenda no rodape, fora do device).
OCULTAR_NOTAS = """<style>
  /* 1. Faixa de aviso "mockup visual" — sempre um div bg-navy no topo do body
        (em alguns mockups e sticky, em outros w-full; bg-navy cobre os dois). */
  body > div.bg-navy { display: none !important; }

  /* 2. Padrao com <header>/<main>: esconde o cabecalho interno (marca + codigo
        [VELA-xxxx]) e qualquer nota de rodape que venha depois do <main>. */
  body > header { display: none !important; }
  body > main ~ footer, body > main ~ section,
  body > main ~ p, body > main ~ div { display: none !important; }

  /* 3. Mockups sem <main> (device .frame): o titulo/subtitulo e a nota ficam
        como <h1>/<p> dentro do wrapper unico — o grid de frames e um <div>. */
  body > div:not(.bg-navy) > h1,
  body > div:not(.bg-navy) > p { display: none !important; }

  /* 4. Rotulos/anotacoes internas que acompanham cada frame (irmaos do device):
        so atingem irmaos da moldura — nunca o conteudo dentro da tela. */
  *:has(> .phone)  > :not(.phone),
  *:has(> .device) > :not(.device),
  *:has(> .frame)  > :not(.frame) { display: none !important; }
</style>
"""

# Script temporario (so na medicao) que escreve a altura do mockup no <title>,
# para ser lido via Chrome headless --dump-dom.
_REPORTER = (
    "<script>function up(){document.title='VELAH:'+Math.max("
    "document.body.scrollHeight,document.documentElement.scrollHeight)}"
    "window.addEventListener('load',up);var n=0,t=setInterval(function(){"
    "up();if(++n>15)clearInterval(t)},200);</script>"
)


def ler_mockup(rel_path):
    full = os.path.join(MOCK, rel_path)
    with open(full, "r", encoding="utf-8") as f:
        conteudo = f.read()
    # injeta apenas o CSS de ocultacao logo antes de </head>
    if "</head>" in conteudo:
        conteudo = conteudo.replace("</head>", OCULTAR_NOTAS + "</head>", 1)
    return conteudo


def medir_altura(conteudo_mockup):
    """Renderiza o mockup no Chrome headless (na largura real da coluna) e
    devolve a altura em px. Garante alturas exatas sem JS em runtime."""
    if not os.path.exists(CHROME):
        return None
    html_meas = conteudo_mockup.replace("</head>", _REPORTER + "</head>", 1)
    tf = tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8")
    try:
        tf.write(html_meas)
        tf.close()
        # Janela BAIXA de proposito: varios mockups tem body com min-height:100vh,
        # entao a scrollHeight nunca fica menor que o viewport. Com a janela baixa,
        # o conteudo sempre excede o viewport e a scrollHeight = altura real.
        out = subprocess.run(
            [CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
             f"--window-size={IFRAME_W},200", "--virtual-time-budget=7000",
             "--dump-dom", f"file://{tf.name}"],
            capture_output=True, text=True, timeout=45,
        ).stdout
        m = re.search(r"VELAH:(\d+)", out)
        return int(m.group(1)) if m else None
    except Exception:
        return None
    finally:
        try:
            os.unlink(tf.name)
        except OSError:
            pass


def bloco_tela(tela, num):
    mockup = ler_mockup(tela["arquivo"])
    altura = medir_altura(mockup) or ALTURA_FALLBACK
    print(f"  tela {num:02d}: altura medida = {altura}px  ({tela['titulo']})")
    srcdoc = html.escape(mockup, quote=True)
    badge = BADGE_CLASS.get(tela["publico"], "badge-ambos")
    nn = f"{num:02d}"

    campos_html = "\n".join(
        f"""          <div class="campo-item">
            <div class="campo-nome">{html.escape(nome)}</div>
            <div class="campo-logica">{exp}</div>
          </div>"""
        for nome, exp in tela["campos"]
    )

    return f"""
    <section class="tela" id="tela-{num}">
      <div class="tela-head">
        <span class="num">{nn}</span>
        <h3>{html.escape(tela['titulo'])}</h3>
        <span class="badge {badge}">{html.escape(tela['publico'])}</span>
      </div>
      <p class="o-que-faz">{tela['o_que_faz']}</p>

      <div class="tela-body">
        <div class="mockup-wrap">
          <iframe class="mockup" srcdoc="{srcdoc}" scrolling="no"
                  style="height: {altura + 12}px"
                  title="Mockup — {html.escape(tela['titulo'])}"></iframe>
        </div>
        <div class="campos-col">
          <h4 class="campos-titulo">Campos e lógica</h4>
{campos_html}
        </div>
      </div>
    </section>
"""


def bloco_categoria(cat, num_inicial):
    partes = []
    n = num_inicial
    for t in cat["telas"]:
        partes.append(bloco_tela(t, n))
        n += 1
    num_final = n - 1
    faixa = f"{num_inicial:02d}" if num_inicial == num_final else f"{num_inicial:02d}–{num_final:02d}"
    telas_html = "\n".join(partes)
    return f"""
  <div class="categoria" id="cat-{cat['id']}">
    <div class="cat-head">
      <div class="cat-faixa">Telas {faixa}</div>
      <h2>{html.escape(cat['nome'])}</h2>
      <p class="cat-intro">{cat['intro']}</p>
    </div>
    {telas_html}
  </div>
""", n


def indice():
    blocos = []
    n = 1
    for cat in CATEGORIAS:
        linhas = []
        for t in cat["telas"]:
            linhas.append(
                f'<li><a href="#tela-{n}"><span class="idx-num">{n:02d}</span>'
                f'{html.escape(t["titulo"])}</a></li>'
            )
            n += 1
        blocos.append(
            f'<div class="idx-cat">'
            f'<a class="idx-cat-link" href="#cat-{cat["id"]}">{html.escape(cat["nome"])}</a>'
            f'<ul>{"".join(linhas)}</ul></div>'
        )
    return "\n".join(blocos)


total_telas = sum(len(c["telas"]) for c in CATEGORIAS)

# monta as categorias com numeracao sequencial continua (1..N)
_cat_html_parts = []
_n = 1
for _c in CATEGORIAS:
    _html, _n = bloco_categoria(_c, _n)
    _cat_html_parts.append(_html)
categorias_html = "".join(_cat_html_parts)

HTML = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Vela — Apresentação das Telas</title>
<style>
  :root {{
    --tinta: #1e293b;
    --suave: #64748b;
    --linha: #e2e8f0;
    --fundo: #f8fafc;
    --lime: #b7d72e;
    --navy: #0E4C86;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: var(--tinta);
    background: #fff;
    line-height: 1.55;
  }}
  .container {{ max-width: 1320px; margin: 0 auto; padding: 0 24px; }}

  /* Capa */
  header.capa {{
    background: var(--navy);
    color: #fff;
    padding: 56px 0 48px;
  }}
  header.capa .container {{ }}
  .marca {{ font-size: 40px; font-weight: 700; letter-spacing: -1px; }}
  .marca b {{ color: var(--lime); }}
  header.capa h1 {{ font-size: 26px; margin: 18px 0 6px; font-weight: 600; }}
  header.capa p {{ color: #cbd5e1; margin: 4px 0; max-width: 640px; }}
  .meta-capa {{ margin-top: 22px; font-size: 13px; color: #94a3b8; }}

  /* Indice — limpo e simples */
  nav.indice {{ border-bottom: 1px solid var(--linha); padding: 30px 0 34px; }}
  nav.indice h2 {{ font-size: 12px; text-transform: uppercase; letter-spacing: 1.5px; color: var(--suave); margin: 0 0 22px; }}
  .idx-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 26px 40px; }}
  .idx-cat {{ break-inside: avoid; }}
  .idx-cat-link {{
    display: block; font-weight: 600; color: var(--navy); text-decoration: none;
    font-size: 14px; margin-bottom: 10px;
  }}
  .idx-cat ul {{ list-style: none; margin: 0; padding: 0; }}
  .idx-cat li a {{
    display: flex; align-items: baseline; gap: 10px;
    color: #475569; text-decoration: none; font-size: 13px; padding: 3px 0;
  }}
  .idx-cat li a:hover {{ color: var(--navy); }}
  .idx-num {{ color: #94a3b8; font-variant-numeric: tabular-nums; font-size: 12px; min-width: 18px; }}

  /* Categoria — inicio de bloco bem evidente */
  .categoria {{ padding: 8px 0 0; }}
  .cat-head {{
    background: var(--navy); color: #fff; border-radius: 12px;
    padding: 20px 24px; margin: 46px 0 26px;
  }}
  .cat-faixa {{
    font-size: 11px; font-weight: 700; letter-spacing: 1px; text-transform: uppercase;
    color: var(--lime); margin-bottom: 4px;
  }}
  .cat-head h2 {{ font-size: 26px; margin: 0 0 8px; color: #fff; }}
  .cat-intro {{ margin: 0; color: #cbd5e1; font-size: 14px; max-width: 880px; }}

  /* Tela */
  .tela {{ padding: 8px 0 30px; border-bottom: 1px solid var(--linha); }}
  .tela-head {{ display: flex; align-items: center; gap: 12px; flex-wrap: wrap; }}
  .num {{
    background: var(--lime); color: var(--navy); font-weight: 700;
    font-size: 13px; font-variant-numeric: tabular-nums;
    width: 30px; height: 30px; border-radius: 8px;
    display: inline-flex; align-items: center; justify-content: center; flex: none;
  }}
  .tela-head h3 {{ font-size: 19px; margin: 0; }}
  .badge {{ font-size: 11.5px; font-weight: 600; padding: 3px 10px; border-radius: 999px; white-space: nowrap; }}
  .badge-treinador {{ background: #e0ecf9; color: #0E4C86; }}
  .badge-aluno {{ background: #eef6d6; color: #5b6b15; }}
  .badge-ambos {{ background: #ede9fe; color: #5b21b6; }}
  .o-que-faz {{ margin: 10px 0 18px; font-size: 14.5px; color: #334155; }}

  /* Corpo: mockup + campos lado a lado */
  .tela-body {{ display: flex; gap: 30px; align-items: flex-start; flex-wrap: wrap; }}
  .mockup-wrap {{
    flex: none;
    width: 880px;          /* largura fixa: a altura do iframe e medida nessa largura */
    background: var(--fundo);
    border: 1px solid var(--linha);
    border-radius: 12px;
    overflow: hidden;
  }}
  iframe.mockup {{
    width: 100%;
    border: 0;
    display: block;
    height: 1500px;        /* fallback; a altura real vem inline (medida no build) */
  }}

  /* Coluna de campos — fixa ao rolar (acompanha mockups altos) */
  .campos-col {{
    flex: 1 1 320px;
    min-width: 300px;
    position: sticky;
    top: 18px;
    align-self: flex-start;
  }}
  .campos-titulo {{
    font-size: 11px; text-transform: uppercase; letter-spacing: 1px; color: var(--suave);
    margin: 2px 0 14px; padding-bottom: 9px; border-bottom: 2px solid var(--lime);
  }}
  .campo-item {{ margin-bottom: 15px; }}
  .campo-nome {{ font-weight: 600; color: var(--navy); font-size: 13.5px; margin-bottom: 2px; }}
  .campo-logica {{ color: #334155; font-size: 12.8px; line-height: 1.52; }}

  @media (max-width: 900px) {{
    .tela-body {{ flex-direction: column; }}
    .campos-col {{ flex: 1 1 auto; width: 100%; position: static; }}
  }}

  footer.rodape {{ padding: 36px 0 60px; color: var(--suave); font-size: 12.5px; text-align: center; }}

  /* Impressao */
  @media print {{
    @page {{ size: A4 landscape; margin: 12mm; }}
    body {{ -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
    nav.indice {{ page-break-after: always; }}
    .categoria {{ page-break-before: always; }}
    .cat-head {{ margin-top: 0; }}
    .campos-col {{ position: static; }}
    .tela-head {{ break-after: avoid; }}
    /* mockups altos podem ocupar mais de uma pagina — nao forcamos avoid neles */
  }}
</style>
</head>
<body>

<header class="capa">
  <div class="container">
    <div class="marca">vela<b>.</b></div>
    <h1>Apresentação das Telas do App</h1>
    <p>Este documento mostra as telas já desenhadas do Vela, explicando o que cada uma faz e a lógica
       dos principais campos. As telas aparecem exatamente como nos protótipos visuais (mockups).</p>
    <div class="meta-capa">{total_telas} telas · 5 módulos · documento para leitura e impressão (PDF)</div>
  </div>
</header>

<nav class="indice">
  <div class="container">
    <h2>Índice</h2>
    <div class="idx-grid">
      {indice()}
    </div>
  </div>
</nav>

<main class="container">
  {categorias_html}
</main>

<footer class="rodape">
  <div class="container">
    vela. — o ponto onde a evolução começa · Documento de apresentação gerado a partir dos requisitos do projeto.
  </div>
</footer>


</body>
</html>
"""

out = os.path.join(ROOT, "apresentacao-telas-vela.html")
with open(out, "w", encoding="utf-8") as f:
    f.write(HTML)

print("Gerado:", out)
print("Tamanho: %.1f KB" % (os.path.getsize(out) / 1024))
print("Telas:", total_telas)

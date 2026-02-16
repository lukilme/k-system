# Regras Práticas para Nomeação de Arquivos

Este guia apresenta recomendações para nomear arquivos de forma consistente, independentemente do tipo (imagem, texto, áudio ou vídeo). O objetivo é facilitar a organização, a busca e a identificação do conteúdo, evitando ambiguidades e problemas técnicos.

---

## Use nomes descritivos e consistentes
Escolha um padrão e mantenha‑o para todos os arquivos semelhantes. O nome deve permitir entender o conteúdo sem abrir o arquivo.

## Prefira letras minúsculas
Evite misturar maiúsculas e minúsculas para não gerar confusão em sistemas que diferenciam caixa (ex.: Linux).

*Exemplo correto:* `relatorio-final.docx`  
*Exemplo incorreto:* `Relatorio_Final.docx`

## Substitua espaços por underscores (_) ou hífens (-)
Espaços podem causar problemas em links, linhas de comando e alguns sistemas.

*Exemplo correto:* `entrevista_joao_silva.mp3` ou `entrevista-joao-silva.mp3`  
*Exemplo incorreto:* `entrevista joão silva.mp3`

## Evite caracteres especiais e acentos
Acentos, cedilhas e símbolos como ?, !, @, #, $, %, &, * podem gerar erros em diferentes plataformas.

*Exemplo correto:* `capa_livro_aquarela.png`  
*Exemplo incorreto:* `çapa_livro_aquarela!.png`

## Use o formato de data ISO 8601 (YYYY-MM-DD)
Colocar a data no início facilita a ordenação cronológica automática.

*Exemplo correto:* `2025-03-15_reuniao_equipe.mp4`  
*Exemplo incorreto:* `15-03-2025_reuniao_equipe.mp4` ou `reuniao_15_mar.mp4`

## Inclua uma breve descrição do conteúdo
Seja sucinto, mas claro: indique o assunto, local, evento, pessoa ou projeto.

*Exemplo correto:* `2025-03-10_contrato_servicos_xyz_v1.pdf`  
*Exemplo incorreto:* `documento.pdf`

## Adicione versão ou número de revisão (quando aplicável)
Use `v1`, `v2`, `v1.2`, `rascunho`, `final`, mas seja consistente. Evite apenas “final” porque pode haver mais de um final.

*Exemplo correto:* `proposta_projeto_alpha_v2.3.docx`  
*Exemplo incorreto:* `proposta_final_final.docx`

## Indique o tipo de arquivo ou resolução (imagens/vídeos)
- Para imagens: incluir resolução (ex.: `1920x1080`) ou uso (thumb, banner).  
- Para vídeos: indicar qualidade ou formato (ex.: `1080p`, `HD`).

*Exemplo correto:* `paisagem_serra_capa_1920x1080.jpg`  
*Exemplo correto:* `entrevista_especialista_1080p.mp4`

## Evite nomes genéricos ou ambíguos
Palavras como “novo”, “cópia”, “meu arquivo” não ajudam na busca.

*Exemplo correto:* `2025-03-12_backup_banco_dados.sql`  
*Exemplo incorreto:* `copia_backup.sql`

## Limite o tamanho do nome, mas sem perder clareza
Nomes muito longos podem ser truncados em alguns sistemas. Procure um equilíbrio.

*Exemplo correto:* `relatorio_vendas_2024_q4.xlsx`  
*Exemplo incorreto:* `relatorio_de_vendas_do_quarto_trimestre_de_2024_para_a_diretoria_com_analises_e_graficos.xlsx`

## Exemplos práticos por tipo de mídia

### Imagens
`[data]_[assunto]_[local]_[resolução].[extensão]`  
`2025-02-20_show_banda_rio_1024x768.jpg`

### Documentos de texto
`[data]_[tipo documento]_[projeto/cliente]_v[versão].[extensão]`  
`2025-03-01_contrato_servicos_silva_v2.docx`

### Áudio
`[data]_[evento]_[entrevistado]_[episódio].[extensão]`  
`2025-01-10_podcast_tecnologia_entrevista_ana_ep5.mp3`

### Vídeo
`[data]_[evento]_[descrição]_[qualidade].[extensão]`  
`2024-12-20_formatura_turma_engenharia_1080p.mp4`

## 12. Combine com uma boa estrutura de pastas
Use pastas para separar por ano, projeto, cliente ou tipo de mídia, e dentro delas mantenha a nomeação padronizada.

Exemplo de estrutura: